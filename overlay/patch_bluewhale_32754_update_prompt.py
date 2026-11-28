#!/usr/bin/env python3
"""32754: KSU 式启动更新提示（进 App 弹一次对话框）。

官方 KernelSU 管理器的行为是「进面具时，有更新就提示一次」——一个对话框，
看完关掉就结束。蓝鱼此前只有系统通知栏 + 首页常驻横幅，缺少这一步的弹窗。
本补丁补上：首页读一次版本号，发现更高版本且该版本没提示过，就弹一次
Material3 AlertDialog，带版本名、更新说明、「更新 / 以后再说」两个按钮。

同一个 versionCode 只弹一次（SharedPreferences 记 prompted_version），
与 ManagerUpdateNotifier 的通知去重互不影响。
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()

PROMPT_KT = "manager/src/main/java/com/maplesu/core/ui/util/ManagerUpdatePrompt.kt"
HOME_SCREEN = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeScreen.kt"
ZH = "manager/src/main/res/values-zh-rCN/strings.xml"
EN = "manager/src/main/res/values/strings.xml"
GRADLE = "manager/build.gradle.kts"

failures = []

PROMPT_SOURCE = '''package com.maplesu.core.ui.util

import android.content.Context
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import com.maplesu.core.R
import com.maplesu.core.ui.screen.home.HomeUiState

/**
 * KSU 式启动更新提示：进 App 拉到新版本就弹一次对话框。
 *
 * 与 [ManagerUpdateNotifier]（系统通知栏）互补：通知栏负责「App 不在前台时提醒」，
 * 这里负责「一进 App 就看到」。同一个 versionCode 只弹一次，「以后再说」也算看过。
 * 隐身模式下 [HomeUiState.checkUpdateEnabled] 为 false，这里整段跳过，不联网也不弹。
 */
@Composable
internal fun ManagerUpdatePrompt(
    state: HomeUiState,
    onOpenUrl: (String) -> Unit,
) {
    val context = LocalContext.current
    val info = state.latestVersionInfo
    var visible by remember { mutableStateOf(false) }

    LaunchedEffect(info.versionCode, state.checkUpdateEnabled) {
        if (!state.checkUpdateEnabled) return@LaunchedEffect
        if (info.versionCode <= 0 || info.downloadUrl.isBlank()) return@LaunchedEffect
        val prefs = context.getSharedPreferences(UPDATE_PROMPT_PREFS, Context.MODE_PRIVATE)
        if (prefs.getInt(UPDATE_PROMPT_KEY, 0) >= info.versionCode) return@LaunchedEffect
        prefs.edit().putInt(UPDATE_PROMPT_KEY, info.versionCode).apply()
        visible = true
    }

    if (!visible) return

    val label = info.versionName.ifBlank { info.versionCode.toString() }
    val body = info.changelog.ifBlank { stringResource(R.string.update_prompt_no_changelog) }

    AlertDialog(
        onDismissRequest = { visible = false },
        title = { Text(stringResource(R.string.new_version_available, label)) },
        text = { Text(body) },
        confirmButton = {
            TextButton(onClick = {
                visible = false
                onOpenUrl(info.downloadUrl)
            }) { Text(stringResource(R.string.module_update)) }
        },
        dismissButton = {
            TextButton(onClick = { visible = false }) {
                Text(stringResource(R.string.update_prompt_later))
            }
        },
    )
}

private const val UPDATE_PROMPT_PREFS = "manager_update_prompt"
private const val UPDATE_PROMPT_KEY = "prompted_version"
'''


def create_file(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        print(f"unchanged: {rel}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"created: {rel} ({len(content)} B)")


def swap(rel: str, pairs, label: str) -> None:
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"missing {rel}")
        return
    text = path.read_text(encoding="utf-8")
    hits = 0
    for old, new in pairs:
        if old not in text:
            print(f"MISS {rel}: {old[:60]!r}")
            continue
        text = text.replace(old, new, 1)
        hits += 1
    path.write_text(text, encoding="utf-8")
    print(f"patched: {label} ({hits})")


def bump() -> None:
    path = ROOT / GRADLE
    if not path.is_file():
        failures.append("missing gradle")
        return
    text = path.read_text(encoding="utf-8")
    if "32753" not in text or "3.22.14-bw" not in text:
        print("SKIP bump: 32753/3.22.14-bw not found")
        return
    text = text.replace("32753", "32754", 1).replace("3.22.14-bw", "3.22.15-bw", 1)
    path.write_text(text, encoding="utf-8")
    print("bumped manager version -> 32754/3.22.15-bw")


def main() -> int:
    create_file(PROMPT_KT, PROMPT_SOURCE)

    # 首页路由：两套皮肤走同一个入口，在 CompositionLocalProvider 之前插入弹窗调用。
    swap(HOME_SCREEN, [
        (
            "    CompositionLocalProvider(\n"
            "        com.maplesu.core.theme.LocalThemeHomeForeground provides isCurrentPage,",
            "    // KSU 式启动更新提示：一进 App 拉到更高版本就弹一次，同版本只弹一次。\n"
            "    com.maplesu.core.ui.util.ManagerUpdatePrompt(\n"
            "        state = statusState,\n"
            "        onOpenUrl = actions.onOpenUrl,\n"
            "    )\n\n"
            "    CompositionLocalProvider(\n"
            "        com.maplesu.core.theme.LocalThemeHomeForeground provides isCurrentPage,",
        ),
    ], "HomeScreen 调用点")

    # 中英文案
    swap(ZH, [
        (
            '    <string name="module_update">更新</string>',
            '    <string name="module_update">更新</string>\n'
            '    <string name="update_prompt_later">以后再说</string>\n'
            '    <string name="update_prompt_no_changelog">新版本已发布，建议更新到最新版本。</string>',
        ),
    ], "zh 文案")

    swap(EN, [
        (
            '    <string name="module_update">Update</string>',
            '    <string name="module_update">Update</string>\n'
            '    <string name="update_prompt_later">Later</string>\n'
            '    <string name="update_prompt_no_changelog">A new version is available. Updating is recommended.</string>',
        ),
    ], "en 文案")

    bump()

    if failures:
        print("FAIL:", failures)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
