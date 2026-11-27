#!/usr/bin/env python3
"""32740 (3.22.1-bw): KernelSU-style "notify once per new version" manager update push.

Adds on top of the 32739 chain:
  1. ManagerUpdateNotifier.kt — dedicated channel + one-shot policy: the same
     versionCode is announced at most once; a higher version announces again.
     Android 13+ without POST_NOTIFICATIONS stays silent (no permission nagging).
  2. HomeViewModel.refreshUpdate() calls the notifier after the existing check,
     so the once-per-launch check doubles as the push source. No extra requests.
  3. The home banner keeps its changelog / download behaviour; the notification
     lands on MainActivity, where the banner is already visible.
  4. Version bump 32739/3.22.0-bw -> 32740/3.22.1-bw so the published update.json
     is strictly newer than every APK already in the field.

Callable as a function (advisor step) or as a script:
    python3 overlay/patch_bluewhale_32740_update.py src
"""
import sys
from pathlib import Path

GRADLE = "manager/build.gradle.kts"
HOME_VM = "manager/src/main/java/com/maplesu/core/ui/viewmodel/HomeViewModel.kt"
NOTIFIER = "manager/src/main/java/com/maplesu/core/ui/util/ManagerUpdateNotifier.kt"

VERSION_CODE = "32740"
VERSION_NAME = "3.22.1-bw"
PREV_CODE = "32739"
PREV_NAME = "3.22.0-bw"

NOTIFIER_KT = '''package com.maplesu.core.ui.util

import android.Manifest
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import androidx.core.content.ContextCompat
import com.maplesu.core.R
import com.maplesu.core.ui.MainActivity
import com.maplesu.core.ui.util.module.LatestVersionInfo

/**
 * KernelSU 式管理器更新提醒。
 *
 * 规则和 KSU 面具一致：有新版本才推，同一版本只推一次。
 * 1. 只有 [LatestVersionInfo.versionCode] 严格高于本机当前版本时才提醒；
 * 2. 同一 versionCode 无论用户点没点、划没划，都不会二次提醒；
 * 3. 更高版本出现时才再次提醒 —— 记录里存的是"已提醒过的最高版本"；
 * 4. Android 13+ 未授予 POST_NOTIFICATIONS 时静默跳过，不反复弹权限框；
 * 5. 通知点击回到 [MainActivity]，首页更新横幅仍在，用户可在那里看更新说明。
 */
internal object ManagerUpdateNotifier {

    private const val CHANNEL_ID = "manager_update"
    private const val CHANNEL_NAME = "版本更新"
    private const val CHANNEL_DESCRIPTION = "发现蓝鱼新版本时提醒一次"
    private const val PREFS_NAME = "manager_update_notice"
    private const val KEY_LAST_NOTIFIED = "last_notified_version"
    private const val NOTIFICATION_ID = 0x0B1F

    const val EXTRA_FROM_UPDATE_NOTIFICATION = "com.blue.whale.mask.extra.FROM_UPDATE_NOTIFICATION"

    /**
     * 发现新版本时调用；返回 true 表示本次真的推了一条通知。
     * [currentVersionCode] 由调用方传 BuildConfig.VERSION_CODE，便于单元测试注入。
     */
    fun notifyIfNeeded(
        context: Context,
        info: LatestVersionInfo,
        currentVersionCode: Long,
    ): Boolean {
        if (info.versionCode <= 0) return false
        if (info.versionCode.toLong() <= currentVersionCode) return false

        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        if (prefs.getInt(KEY_LAST_NOTIFIED, 0) >= info.versionCode) return false

        if (!hasNotificationPermission(context)) return false
        val manager = context.getSystemService(NotificationManager::class.java) ?: return false
        ensureChannel(manager)

        val versionLabel = info.versionName.ifBlank { info.versionCode.toString() }
        val summary = info.changelog
            .lineSequence()
            .map { it.trim().trimStart('-', '*', '#').trim() }
            .firstOrNull { it.isNotBlank() }
            .orEmpty()
        val body = if (summary.isBlank()) {
            "新版本 $versionLabel 已发布，点此查看更新说明。"
        } else {
            "新版本 $versionLabel：$summary"
        }

        val intent = Intent(context, MainActivity::class.java).apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
            putExtra(EXTRA_FROM_UPDATE_NOTIFICATION, true)
        }
        val pendingIntent = PendingIntent.getActivity(
            context,
            NOTIFICATION_ID,
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
        )

        val notification = NotificationCompat.Builder(context, CHANNEL_ID)
            .setSmallIcon(R.drawable.ic_logo_vector)
            .setContentTitle("蓝鱼有新版本 $versionLabel")
            .setContentText(body)
            .setStyle(NotificationCompat.BigTextStyle().bigText(body))
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .setCategory(NotificationCompat.CATEGORY_RECOMMENDATION)
            .setAutoCancel(true)
            .setContentIntent(pendingIntent)
            .build()

        return runCatching {
            NotificationManagerCompat.from(context).notify(NOTIFICATION_ID, notification)
            // 先记"已提醒"，再返回；写失败也不会变成每次启动都推。
            prefs.edit().putInt(KEY_LAST_NOTIFIED, info.versionCode).apply()
            true
        }.getOrDefault(false)
    }

    /** 仅供调试/测试：清掉"已提醒"记录，下一次检查会重新推。 */
    fun resetNotificationHistory(context: Context) {
        context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE).edit().clear().apply()
    }

    private fun hasNotificationPermission(context: Context): Boolean =
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            ContextCompat.checkSelfPermission(
                context,
                Manifest.permission.POST_NOTIFICATIONS,
            ) == PackageManager.PERMISSION_GRANTED
        } else {
            true
        }

    private fun ensureChannel(manager: NotificationManager) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) return
        if (manager.getNotificationChannel(CHANNEL_ID) != null) return
        manager.createNotificationChannel(
            NotificationChannel(
                CHANNEL_ID,
                CHANNEL_NAME,
                NotificationManager.IMPORTANCE_DEFAULT,
            ).apply { description = CHANNEL_DESCRIPTION }
        )
    }
}
'''


def _read(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def _write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def bump_version(root: Path) -> None:
    text = _read(root, GRADLE)
    if f"versionCode = {VERSION_CODE}" in text:
        print(f"skip: version already {VERSION_CODE}/{VERSION_NAME}")
        return
    if f"versionCode = {PREV_CODE}" not in text:
        raise SystemExit(f"FATAL: expected versionCode = {PREV_CODE} in {GRADLE}, got none")
    text = text.replace(f"versionCode = {PREV_CODE}", f"versionCode = {VERSION_CODE}", 1)
    text = text.replace(f'versionName = "{PREV_NAME}"', f'versionName = "{VERSION_NAME}"', 1)
    _write(root, GRADLE, text)
    print(f"bumped version to {VERSION_CODE}/{VERSION_NAME}")


def add_notifier(root: Path) -> None:
    path = root / NOTIFIER
    if path.is_file() and "ManagerUpdateNotifier" in path.read_text(encoding="utf-8"):
        print(f"skip: {NOTIFIER} already present")
        return
    _write(root, NOTIFIER, NOTIFIER_KT)
    print(f"wrote {NOTIFIER}")


def wire_home_view_model(root: Path) -> None:
    text = _read(root, HOME_VM)
    if "ManagerUpdateNotifier.notifyIfNeeded" in text:
        print("skip: HomeViewModel already wired")
        return

    import_anchor = "import com.maplesu.core.ui.util.checkNewVersion\n"
    if import_anchor not in text:
        raise SystemExit("FATAL: HomeViewModel import anchor missing")
    text = text.replace(
        import_anchor,
        import_anchor + "import com.maplesu.core.ui.util.ManagerUpdateNotifier\n",
        1,
    )

    old = """    private fun refreshUpdate(enabled: Boolean) {
        if (!enabled) return
        viewModelScope.launch {
            val latest = withContext(Dispatchers.IO) {
                runCatching { checkNewVersion() }.getOrNull()
            } ?: return@launch
            _uiState.update { if (it.checkUpdateEnabled) it.copy(latestVersionInfo = latest) else it }
        }
    }
"""
    new = """    private fun refreshUpdate(enabled: Boolean) {
        if (!enabled) return
        viewModelScope.launch {
            val latest = withContext(Dispatchers.IO) {
                runCatching { checkNewVersion() }.getOrNull()
            } ?: return@launch
            _uiState.update { if (it.checkUpdateEnabled) it.copy(latestVersionInfo = latest) else it }
            // KSU 式更新推送：同一版本只提醒一次，更高版本才再提醒。
            if (latest.versionCode > BuildConfig.VERSION_CODE) {
                withContext(Dispatchers.IO) {
                    runCatching {
                        ManagerUpdateNotifier.notifyIfNeeded(
                            ksuApp,
                            latest,
                            BuildConfig.VERSION_CODE.toLong(),
                        )
                    }
                }
            }
        }
    }
"""
    if old not in text:
        raise SystemExit("FATAL: HomeViewModel refreshUpdate marker missing")
    _write(root, HOME_VM, text.replace(old, new, 1))
    print("patched HomeViewModel: refreshUpdate -> ManagerUpdateNotifier")


def patch_32740_update(root: Path) -> None:
    root = Path(root).resolve()
    if not root.is_dir():
        raise SystemExit(f"FATAL: source root not found: {root}")
    bump_version(root)
    add_notifier(root)
    wire_home_view_model(root)
    checks = [
        (f"versionCode = {VERSION_CODE}" in _read(root, GRADLE), "versionCode 未更新"),
        (VERSION_NAME in _read(root, GRADLE), "versionName 未更新"),
        ((root / NOTIFIER).is_file(), "ManagerUpdateNotifier.kt 缺失"),
        ("ManagerUpdateNotifier.notifyIfNeeded" in _read(root, HOME_VM), "HomeViewModel 未接入通知"),
    ]
    for ok, message in checks:
        if not ok:
            raise SystemExit(f"FATAL: {message}")
    print("32740 update-push patch done: 32740/3.22.1-bw, notify-once notifier wired")


if __name__ == "__main__":
    patch_32740_update(Path(sys.argv[1] if len(sys.argv) > 1 else "src"))
