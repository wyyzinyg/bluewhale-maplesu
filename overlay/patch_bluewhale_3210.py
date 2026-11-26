#!/usr/bin/env python3
"""蓝鱼 3.21.0 第一步（32738）：更新通道数据层

按《蓝鱼更新推送功能方案（KSU 风格）》第 2 节做「三渠道兜底 + 来源可解释」，
只动数据层，不碰 UI：设置入口、通知、应用内下载安装留给下一步。

改两件事：
  1. LatestVersionInfo 加四个带默认值的字段（versionName / sha256 / sizeBytes / source），
     老的构造点（`LatestVersionInfo(50110, DOWNLOAD)`、`LatestVersionInfo()`）全部不受影响，
     `==` 语义也不变（默认值相等）。
  2. ManagerUpdate.kt 整文件替换：
     - 渠道顺序改成方案第 2 节的要求：CloudBase 主站 → Tiana（配置了才发请求）→ GitHub raw，
       品牌站作为最后一条兜底（老逻辑里它是第二条，挪到末尾，避免抢在 Tiana 前面）。
     - 任一渠道成功即返回，并带上 `source`，更新页可以显示「实际使用的来源」。
     - update.json 解析补上 versionName / sha256 / size；没有 sha256 的老格式仍按老路解析。
     - 网络层异常按「该渠道不可用」处理，继续下一个渠道，不抛出给 UI。

用法（跑在 patch_bluewhale_321.py 之后）：
    python3 overlay/patch_bluewhale_3210.py <上游源码根目录>
"""
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []
notices: list[str] = []
changed: list[str] = []

VERSION_CODE = "32738"
VERSION_NAME = "3.21.0-bw"
PREV_CODE = "32737"
PREV_NAME = "3.20.1-bw"

GRADLE = "manager/build.gradle.kts"
LATEST = "manager/src/main/java/com/maplesu/core/ui/util/module/LatestVersionInfo.kt"
UPDATE_KT_PATH = "manager/src/main/java/com/maplesu/core/ui/util/ManagerUpdate.kt"


def read_raw(rel: str) -> str | None:
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return None
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def read(rel: str) -> str | None:
    raw = read_raw(rel)
    return None if raw is None else raw.replace("\r\n", "\n")


def write(rel: str, text: str, like: str | None = None) -> None:
    if like is not None and "\r\n" in like:
        text = text.replace("\r\n", "\n").replace("\n", "\r\n")
    with open(ROOT / rel, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    if rel not in changed:
        changed.append(rel)


UPDATE_KT = '''package com.maplesu.core.ui.util

import com.maplesu.core.ui.util.module.LatestVersionInfo
import okhttp3.OkHttpClient
import okhttp3.Request
import org.json.JSONObject

/**
 * 蓝鱼自己的更新通道（3.19.0 起，3.21.0 加渠道名与来源）。
 *
 * 顺序即优先级（3.21.0 方案第 2 节）：CloudBase 主站 → Tiana 镜像 → GitHub raw，
 * 品牌站放在最后一条兜底。任一渠道拿到可用版本就返回，并把渠道名带回去，
 * 更新页据此显示「实际使用的来源」。
 */
internal const val MANAGER_UPDATE_URL =
    "https://bluewhale-release-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com/update.json"

private const val BRAND_UPDATE_URL =
    "https://bluewhale-brand-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com/update.json"

private const val GITHUB_RAW_UPDATE_URL =
    "https://raw.githubusercontent.com/wyyzinyg/bluewhale-maplesu/main/release/update.json"

/**
 * Tiana 备用镜像（3.20.0 起）。Tiana 文件存储的直链带 `_fs_scope` 鉴权参数，
 * 匿名请求返回 403，不能直接写进 update.json；这里只接受 Tiana Web 上匿名可读的 update.json。
 * 留空表示该渠道整条跳过——不发起请求、不占更新延迟，也不会显示成「镜像不可用」。
 */
internal const val TIANA_UPDATE_URL = ""

/** 一条更新渠道：名字用于界面展示，url 用于请求。 */
internal data class UpdateChannel(val name: String, val url: String)

/** 按优先级列出当前配置的渠道；Tiana 没配地址时自动缺席。 */
internal fun managerUpdateChannels(): List<UpdateChannel> = buildList {
    add(UpdateChannel("cloudbase", MANAGER_UPDATE_URL))
    if (TIANA_UPDATE_URL.isNotBlank()) {
        add(UpdateChannel("tiana", TIANA_UPDATE_URL))
    }
    add(UpdateChannel("github", GITHUB_RAW_UPDATE_URL))
    add(UpdateChannel("cloudbase-brand", BRAND_UPDATE_URL))
}

/**
 * 依次尝试各渠道，第一个拿到可用版本的渠道胜出。
 *
 * 单个渠道的失败（超时、404、JSON 坏掉、被墙）都只算「这一条不可用」，
 * 继续下一条；全部不可用才返回空的 [LatestVersionInfo]（versionCode = 0）。
 * 调用方据此区分「检查失败」和「已是最新版」，不要用空对象冒充最新。
 */
internal fun fetchLatestManagerVersion(client: OkHttpClient): LatestVersionInfo {
    for (channel in managerUpdateChannels()) {
        val info = runCatching { fetchOne(client, channel) }.getOrNull() ?: continue
        if (info.versionCode > 0 && info.downloadUrl.isNotBlank()) {
            return info
        }
    }
    return LatestVersionInfo()
}

private fun fetchOne(client: OkHttpClient, channel: UpdateChannel): LatestVersionInfo =
    client.newCall(
        Request.Builder().url(channel.url)
            .header("Accept", "application/json")
            .build(),
    ).execute().use { response ->
        if (!response.isSuccessful) return@use LatestVersionInfo()
        parseManagerUpdate(response.body.string()).copy(source = channel.name)
    }

/** 先按蓝鱼 update.json 解析，认不出来再走上游 GitHub Release 的旧格式。 */
internal fun parseManagerUpdate(body: String): LatestVersionInfo {
    val json = runCatching { JSONObject(body) }.getOrNull() ?: return LatestVersionInfo()
    if (json.has("versionCode")) {
        val code = json.optInt("versionCode", 0)
        val url = json.optString("downloadUrl").ifBlank {
            json.optString("apkUrl").ifBlank {
                json.optJSONArray("assets")?.optJSONObject(0)?.optString("browser_download_url").orEmpty()
            }
        }
        if (code > 0 && url.isNotBlank()) {
            return LatestVersionInfo(
                versionCode = code,
                downloadUrl = url,
                changelog = json.optString("changelog", ""),
                versionName = json.optString("versionName", ""),
                sha256 = json.optString("sha256", "").lowercase(),
                sizeBytes = json.optLong("size", 0L),
            )
        }
    }
    return parseManagerRelease(body)
}

/** 上游 GitHub Release 格式（保留，作为最后兜底与既有单测的入口）。 */
internal fun parseManagerRelease(body: String): LatestVersionInfo {
    val release = JSONObject(body)
    if (release.optBoolean("draft") || release.optBoolean("prerelease")) return LatestVersionInfo()
    val assets = release.optJSONArray("assets") ?: return LatestVersionInfo()
    val changelog = release.optString("body", "")
    val apkAssets = (0 until assets.length()).mapNotNull { assets.optJSONObject(it) }
        .filter { it.optString("name").endsWith(".apk") }
    for (asset in apkAssets) {
        // 蓝鱼资产名 …-bw-32734.apk；KSU 风格 …_50110-release.apk。两种都认。
        val name = asset.optString("name")
        val code = name.substringAfterLast("-bw-").substringBefore(".apk").toIntOrNull()
            ?: name.substringAfterLast('_').substringBefore('-').toIntOrNull()
            ?: continue
        val url = asset.optString("browser_download_url")
        if (code > 0 && url.isNotBlank()) {
            return LatestVersionInfo(versionCode = code, downloadUrl = url, changelog = changelog)
        }
    }
    val parts = release.optString("tag_name").removePrefix("v").split(".")
    if (parts.size != 3) return LatestVersionInfo()
    val numbers = parts.map { it.toLongOrNull() ?: return LatestVersionInfo() }
    if (numbers[0] > Int.MAX_VALUE / 10_000 || numbers[1] > 99 || numbers[2] > 99) {
        return LatestVersionInfo()
    }
    val code = numbers[0] * 10_000 + numbers[1] * 100 + numbers[2]
    if (code !in 1..Int.MAX_VALUE.toLong()) return LatestVersionInfo()
    val asset = apkAssets.firstOrNull { it.optString("browser_download_url").isNotBlank() }
        ?: return LatestVersionInfo()
    return LatestVersionInfo(code.toInt(), asset.getString("browser_download_url"), changelog)
}
'''

LATEST_KT = '''package com.maplesu.core.ui.util.module

data class LatestVersionInfo(
    val versionCode: Int = 0,
    val downloadUrl: String = "",
    val changelog: String = "",
    /**
     * 3.21.0：更新页要显示的字段。
     *
     * 全部带默认值，老的构造点（[LatestVersionInfo] 的 0/2/3 参用法）与 `==` 语义都不变；
     * 老格式的 update.json 没有这些字段时它们保持空值，界面按「未提供」处理。
     */
    val versionName: String = "",
    val sha256: String = "",
    val sizeBytes: Long = 0L,
    /** 实际命中的渠道名（cloudbase / tiana / github / cloudbase-brand）；未命中为空串。 */
    val source: String = "",
)
'''

gradle_raw = read_raw(GRADLE)
gradle_text = None if gradle_raw is None else gradle_raw.replace("\r\n", "\n")
already = gradle_text is not None and f"versionCode = {VERSION_CODE}" in gradle_text

# —— 1. 版本 ——
if gradle_text is not None:
    if already:
        notices.append(f"版本已是 {VERSION_CODE}/{VERSION_NAME}")
    else:
        for old, new in ((f"versionCode = {PREV_CODE}", f"versionCode = {VERSION_CODE}"),
                         (f'versionName = "{PREV_NAME}"', f'versionName = "{VERSION_NAME}"')):
            if gradle_text.count(old) != 1:
                failures.append(f"{GRADLE}: 版本锚点 {old!r} 不唯一")
                continue
            gradle_text = gradle_text.replace(old, new)
        if not any("版本锚点" in item for item in failures):
            write(GRADLE, gradle_text, like=gradle_raw)
            print(f"版本 → {VERSION_NAME} / {VERSION_CODE}")

# —— 2. LatestVersionInfo 加字段（锚点式，保留原文件的行尾与缩进） ——
latest_raw = read_raw(LATEST)
if latest_raw is not None:
    latest = latest_raw.replace("\r\n", "\n")
    if "sizeBytes" in latest:
        notices.append("LatestVersionInfo 已加过字段，跳过")
    elif latest.strip() == LATEST_KT.strip():
        notices.append("LatestVersionInfo 内容一致，跳过")
    else:
        write(LATEST, LATEST_KT, like=latest_raw)
        print(f"改好 {LATEST}: 加 versionName / sha256 / sizeBytes / source")

# —— 3. ManagerUpdate.kt 整文件替换 ——
update_raw = read_raw(UPDATE_KT_PATH)
if update_raw is not None:
    current = update_raw.replace("\r\n", "\n")
    if "managerUpdateChannels" in current:
        notices.append("ManagerUpdate 已是 3.21.0 版本，跳过")
    else:
        write(UPDATE_KT_PATH, UPDATE_KT, like=update_raw)
        print(f"改好 {UPDATE_KT_PATH}: 三渠道兜底 + 来源 + 版本元数据")

# —— 4. 单测同步（这两个断言在 3.19.0 换端点时就已经失配，这里一并校正） ——
TEST_KT = "manager/src/test/java/com/maplesu/core/ui/util/ManagerUpdateTest.kt"
test_raw = read_raw(TEST_KT)
if test_raw is not None:
    test = test_raw.replace("\r\n", "\n")
    old_url = 'assertEquals("https://api.github.com/repos/FengQiuFQ/MapleSU/releases/latest", requestUrl)'
    new_url = "assertEquals(MANAGER_UPDATE_URL, requestUrl)"
    old_value = ('assertEquals(LatestVersionInfo(50110, download, "## Changes\\nUpdate fixture"), '
                 "fetchLatestManagerVersion(client))")
    new_value = ('assertEquals(LatestVersionInfo(50110, download, "## Changes\\nUpdate fixture", '
                 'source = "cloudbase"), fetchLatestManagerVersion(client))')
    if old_url in test or old_value in test:
        if test.count(old_url) != 1 or test.count(old_value) != 1:
            failures.append(f"{TEST_KT}: 单测锚点命中数异常（url {test.count(old_url)} 处，value {test.count(old_value)} 处）")
        else:
            write(TEST_KT, test.replace(old_url, new_url).replace(old_value, new_value), like=test_raw)
            print(f"改好 {TEST_KT}: 端点改成 MANAGER_UPDATE_URL，期望值带上 source")
    else:
        notices.append("单测已对齐，跳过")

# —— 4. 自检 ——
update_text = read(UPDATE_KT_PATH)
if update_text is not None:
    checks = [
        ("managerUpdateChannels" in update_text, "缺 managerUpdateChannels"),
        ('UpdateChannel("cloudbase"' in update_text, "缺 CloudBase 主渠道"),
        ("TIANA_UPDATE_URL.isNotBlank()" in update_text, "Tiana 渠道不是条件启用"),
        ("source = channel.name" in update_text, "渠道名没有带进结果"),
        ("sizeBytes = json.optLong(\"size\"" in update_text, "update.json 的 size 未解析"),
    ]
    for ok, message in checks:
        if not ok:
            failures.append(f"{UPDATE_KT_PATH}: {message}")
test_text = read(TEST_KT) if (ROOT / TEST_KT).is_file() else None
if test_text is not None and "source = \"cloudbase\"" not in test_text:
    failures.append(f"{TEST_KT}: 期望值没有带上 source")
latest_text = read(LATEST)
if latest_text is not None and "val source: String = \"\"" not in latest_text:
    failures.append(f"{LATEST}: 缺 source 字段")
if read(GRADLE) is not None and f"versionCode = {VERSION_CODE}" not in read(GRADLE):
    failures.append(f"{GRADLE}: 版本未落到 {VERSION_CODE}")

if failures:
    print("\n3.21.0 数据层补丁失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)

print()
for item in notices:
    print("注意: " + item)
print(f"3.21.0 数据层补丁已应用：改动 {len(changed)} 个文件。")
for rel in changed:
    print("  · " + rel)
