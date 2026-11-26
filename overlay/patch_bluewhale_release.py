#!/usr/bin/env python3
"""3.19.0 收口：恢复蓝鱼自有的更新通道 + 把可见文案里剩下的 MapleSU/枫叶清干净。

做三件事：
  1. ManagerUpdate.kt 改成先读蓝鱼自己的 update.json（CloudBase 主站，GitHub raw 兜底），
     原有 GitHub Release 解析保留，作为最后兜底；不再指向 FengQiuFQ/MapleSU。
  2. 全量扫 res/values* 下的 <string>，把可见的 MapleSU / MapleSU_xxx / 枫叶 换成蓝鱼口径。
     署名类句子（关于页里“内核方案由 MapleSU 维护”等）按 key 白名单原样保留。
  3. 版本推到 32735 / 3.19.0-bw。

用法：python3 patch_bluewhale_release.py <上游源码根目录>
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []

UPDATE_KT = '''package com.maplesu.core.ui.util

import com.maplesu.core.ui.util.module.LatestVersionInfo
import okhttp3.OkHttpClient
import okhttp3.Request
import org.json.JSONObject

/**
 * 蓝鱼自己的更新通道（3.19.0 起）：
 * 主站是 CloudBase 静态托管上的 update.json，GitHub raw 里的同名文件作为兜底。
 * 两者都是蓝鱼自己的版本描述（versionCode / downloadUrl / changelog），不再指向上游 MapleSU。
 */
internal const val MANAGER_UPDATE_URL =
    "https://bluewhale-release-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com/update.json"

private val MANAGER_UPDATE_FALLBACKS = listOf(
    "https://bluewhale-brand-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com/update.json",
    "https://raw.githubusercontent.com/wyyzinyg/bluewhale-maplesu/main/release/update.json",
)

/** 依次尝试主站与兜底；任何一个解析出有效版本就返回。 */
internal fun fetchLatestManagerVersion(client: OkHttpClient): LatestVersionInfo {
    for (url in listOf(MANAGER_UPDATE_URL) + MANAGER_UPDATE_FALLBACKS) {
        val info = runCatching { fetchOne(client, url) }.getOrDefault(LatestVersionInfo())
        if (info.versionCode > 0 && info.downloadUrl.isNotBlank()) return info
    }
    return LatestVersionInfo()
}

private fun fetchOne(client: OkHttpClient, url: String): LatestVersionInfo =
    client.newCall(
        Request.Builder().url(url)
            .header("Accept", "application/json")
            .build(),
    ).execute().use { response ->
        if (!response.isSuccessful) return@use LatestVersionInfo()
        parseManagerUpdate(response.body.string())
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
            return LatestVersionInfo(code, url, json.optString("changelog", ""))
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
        val code = Regex("""v(.+?)_(\\d+)-""").find(asset.optString("name"))
            ?.groupValues?.get(2)?.toIntOrNull() ?: continue
        val url = asset.optString("browser_download_url")
        if (code > 0 && url.isNotBlank()) return LatestVersionInfo(code, url, changelog)
    }
    val version = Regex("""v?(\\d+)\\.(\\d+)\\.(\\d+)""").matchEntire(release.optString("tag_name"))
        ?: return LatestVersionInfo()
    val (major, minor, patch) = version.destructured
    val parts = listOf(major, minor, patch).map { it.toLongOrNull() ?: return LatestVersionInfo() }
    if (parts[0] > Int.MAX_VALUE / 10_000 || parts[1] > 99 || parts[2] > 99) return LatestVersionInfo()
    val code = parts[0] * 10_000 + parts[1] * 100 + parts[2]
    if (code !in 1..Int.MAX_VALUE.toLong()) return LatestVersionInfo()
    val asset = apkAssets.firstOrNull { it.optString("browser_download_url").isNotBlank() }
        ?: return LatestVersionInfo()
    return LatestVersionInfo(code.toInt(), asset.getString("browser_download_url"), changelog)
}
'''

# 署名句：这些 key 里出现 MapleSU 属于对上游的正当署名，原样保留。
KEEP_KEYS = {
    "about_maple_ultra_point_kernel",
    "about_maple_overview",
    "about_maple_overview_plain",
    "about_maple_developers",
    "about_maple_thanks",
    "about_maple_license",
}

STRING_RE = re.compile(r"(<string\b[^>]*>)(.*?)(</string>)", re.S)
TAG_RE = re.compile(r"<string\b[^>]*\bname=\"([^\"]+)\"")


def brand(locale_dir: str) -> str:
    name = locale_dir.name
    if name in {"values-zh-rTW", "values-zh-rHK", "values-zh-rMO"}:
        return "藍魚"
    if name.startswith("values-zh"):
        return "蓝鱼"
    return "BlueWhale"


def rewrite_text(text: str, b: str) -> str:
    # MapleSU 自带的后缀先整体吃掉，避免出现 “蓝鱼 _Ultra”。
    for token in ("MapleSU_98260", "MapleSU_93260", "MapleSU_Ultra", "MapleSU_Normal",
                  "MapleSU_Lite", "MapleSU_", "MapleSU"):
        text = text.replace(token, b if not token.endswith(("Ultra", "Normal", "Lite")) else b + " " + token.split("_")[-1])
    text = text.replace("枫叶", "粒子").replace("楓葉", "粒子")
    text = text.replace("FengQiuFQ/MapleSU", "wyyzinyg/bluewhale-maplesu")
    # 中文之间的空格去掉（"需要 蓝鱼 配对" → "需要蓝鱼配对"），
    # 中英相邻的地方补一个空格（"Ultra模式" → "Ultra 模式"）。
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", text)
    text = re.sub(r"([A-Za-z0-9])([\u4e00-\u9fff])", r"\1 \2", text)
    text = re.sub(r" {2,}", " ", text)
    return text


def patch_strings() -> None:
    res = ROOT / "manager/src/main/res"
    if not res.is_dir():
        failures.append("缺目录: manager/src/main/res")
        return
    changed = 0
    for values in sorted(res.glob("values*")):
        if not values.is_dir():
            continue
        for xml in sorted(values.glob("*.xml")):
            raw = xml.read_text(encoding="utf-8")
            b = brand(values)

            def repl(match: re.Match[str]) -> str:
                head, body, tail = match.group(1), match.group(2), match.group(3)
                key_match = TAG_RE.search(head)
                key = key_match.group(1) if key_match else ""
                if key in KEEP_KEYS:
                    return match.group(0)
                if "GPL" in body or "MapleAutumn" in body:
                    return match.group(0)
                new = rewrite_text(body, b)
                return head + new + tail if new != body else match.group(0)

            new_raw = STRING_RE.sub(repl, raw)
            if new_raw != raw:
                xml.write_text(new_raw, encoding="utf-8")
                changed += 1
    print(f"文案总清：改写 {changed} 个资源文件")


def bump_version() -> None:
    path = ROOT / "manager/build.gradle.kts"
    if not path.is_file():
        failures.append("缺文件: manager/build.gradle.kts")
        return
    text = path.read_text(encoding="utf-8")
    for old, new in (("versionCode = 32734", "versionCode = 32735"),
                     ('versionName = "3.18.2-bw"', 'versionName = "3.19.0-bw"')):
        if text.count(old) != 1:
            failures.append(f"版本锚点异常: {old}")
            return
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("版本 → 3.19.0-bw / 32735")


def write_update_kt() -> None:
    path = ROOT / "manager/src/main/java/com/maplesu/core/ui/util/ManagerUpdate.kt"
    if not path.is_file():
        failures.append("缺文件: ManagerUpdate.kt")
        return
    path.write_text(UPDATE_KT, encoding="utf-8")
    print("更新通道 → 蓝鱼 update.json（CloudBase 主站 + GitHub raw 兜底）")


write_update_kt()
patch_strings()
bump_version()

if failures:
    print("\n3.19.0 收口失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("3.19.0 收口已应用。")
