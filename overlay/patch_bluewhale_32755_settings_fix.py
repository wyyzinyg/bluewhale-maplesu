#!/usr/bin/env python3
"""32755: 修两处真机问题。

一、首页「设备型号」显示 `23013RK75C`（小米内部代号），不是「Redmi K60」。
   根因：HomeViewModel 里 deviceModel 初始值和探测兜底都直接取 Build.MODEL，
   绕过了 resolveDeviceName()；而 resolveDeviceName() 的小米分支只试了
   `ro.product.marketname`，某些机型这个属性本身就存代号，也会被原样返回。
   改法：DeviceNameHelper 加代号识别 + 多属性链 + 常见机型映射表；
   HomeViewModel 两处都走 resolveDeviceName()。

二、设置页少了「检查管理器更新」开关。
   根因：SettingsUiState.checkUpdate 和 onSetCheckUpdate 都在，ViewModel 读写也正常，
   但 UI 里从来没有渲染它，SettingsSection 枚举里也没有对应 section。
   用户想开关首页那张更新卡，进设置页找不到。
   改法：新增 SettingsSection.MANAGER_UPDATE + SettingsRow.MANAGER_UPDATE_CHECK，
   放进 COMMON_SECTIONS（不需要 root），两套皮肤各加一张卡，排在最前面。
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()

DEVICE_HELPER = "manager/src/main/java/com/maplesu/core/ui/util/DeviceNameHelper.kt"
HOME_VM = "manager/src/main/java/com/maplesu/core/ui/viewmodel/HomeViewModel.kt"
POLICY = "manager/src/main/java/dev/maplesu/manager/workmode/ui/SettingsModePolicy.kt"
MATERIAL = "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMaterial.kt"
MIUIX = "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMiuix.kt"
ZH = "manager/src/main/res/values-zh-rCN/strings.xml"
EN = "manager/src/main/res/values/strings.xml"
GRADLE = "manager/build.gradle.kts"

failures = []

DEVICE_SOURCE = '''package com.maplesu.core.ui.util

import android.annotation.SuppressLint
import android.os.Build
import java.io.File

private const val SAMSUNG_FLOATING_FEATURE_CLASS = "com.samsung.android.feature.SemFloatingFeature"
private const val KEY_SAMSUNG_PRODUCT_NAME = "SEC_FLOATING_FEATURE_SETTINGS_CONFIG_BRAND_NAME"

private val SAMSUNG_FLOATING_FEATURE_PATHS = listOf(
    "/vendor/etc/floating_feature.xml",
    "/system/etc/floating_feature.xml",
)

/**
 * 小米/红米/POCO 内部型号 → 市场名。
 *
 * 真机反馈：K60 首页「设备型号」显示成 `23013RK75C`。某些 HyperOS 版本上
 * `ro.product.marketname` 拿到的就是代号本身，读属性这条路不可靠，所以留一张表兜底。
 * 表里没有的机型走「厂商 + 型号」兜底，至少不是一串裸代码。
 */
private val MODEL_CODE_MAP = mapOf(
    // Redmi K 系列
    "23013RK75C" to "Redmi K60",
    "23013RK75" to "Redmi K60",
    "22127RK46C" to "Redmi K50",
    "22041211AC" to "Redmi K50",
    "22021211RC" to "Redmi K50 Pro",
    "21121210C" to "Redmi K50G",
    "22081212C" to "Redmi K50 Ultra",
    "23078RKD5C" to "Redmi K70",
    "23113RKC6C" to "Redmi K70 Pro",
    "23117RK66C" to "Redmi K70E",
    "24069PC21G" to "Redmi K70 Ultra",
    "24117RK2CC" to "Redmi K80",
    // Xiaomi 数字旗舰
    "23127PNY2C" to "Xiaomi 14",
    "23116PN5BC" to "Xiaomi 14 Pro",
    "2311DRK48C" to "Xiaomi 14 Ultra",
    "2211133C" to "Xiaomi 13",
    "2210132C" to "Xiaomi 13 Pro",
    "2304FPN6DC" to "Xiaomi 13 Ultra",
    "2201123C" to "Xiaomi 12",
    "2201122C" to "Xiaomi 12 Pro",
    "2203121C" to "Xiaomi 12S Ultra",
    "2112123AC" to "Xiaomi 12S",
    "2106118C" to "Xiaomi 11 Ultra",
    "M2101K9C" to "Xiaomi 11",
    "M2011K2C" to "Xiaomi 11",
    "24053PY09C" to "Xiaomi 15",
    // Redmi Note 系列
    "2312DRAABC" to "Redmi Note 13",
    "23090RA98C" to "Redmi Note 13 Pro",
    "22111317C" to "Redmi Note 12",
    "22101317C" to "Redmi Note 12 Pro",
    "22101316C" to "Redmi Note 12 Pro+",
    "2201117TG" to "Redmi Note 11",
    "21091116C" to "Redmi Note 11 Pro",
    "M2103K19C" to "Redmi Note 10",
    // POCO
    "23013PC75G" to "POCO F5",
    "22111317PG" to "POCO X5",
)

/**
 * Resolve the commercial device name.
 * 1. Dispatch by [Build.MANUFACTURER] — each vendor branch uses its own property
 *    or dedicated helper (e.g. Samsung).
 * 2. Xiaomi 系额外过滤「看起来像内部代号」的值，并查 [MODEL_CODE_MAP]。
 * 3. If the vendor branch returns nothing, Fallback to MANUFACTURER + BRAND + MODEL.
 */
fun resolveDeviceName(): String {
    val marketName = when (Build.MANUFACTURER.orEmpty().lowercase()) {
        "samsung" -> getSamsungProductName()
        "xiaomi", "redmi", "poco" -> resolveXiaomiMarketName()
        "oppo", "oneplus", "realme", "oplus" ->
            getSystemProperty("ro.vendor.oplus.market.name").takeIfValidDeviceName()

        "vivo" -> getSystemProperty("ro.vivo.market.name").takeIfValidDeviceName()
        "honor", "huawei" -> getSystemProperty("ro.config.marketing_name").takeIfValidDeviceName()
        "zte", "nubia" -> getSystemProperty("ro.vendor.product.ztename").takeIfValidDeviceName()

        else -> null
    }
    if (marketName != null) return marketName

    MODEL_CODE_MAP[Build.MODEL]?.let { return it }

    return buildString {
        append(Build.MANUFACTURER)
        if (!Build.BRAND.equals(Build.MANUFACTURER, ignoreCase = true)) append(" ").append(Build.BRAND)
        append(" ").append(Build.MODEL)
    }
}

/**
 * 小米系市场名：多个属性依次试，只收「像人念的名字」的那个。
 * `ro.product.marketname` 在部分 HyperOS 机型上返的是代号本身，所以要做代号过滤。
 */
private fun resolveXiaomiMarketName(): String? {
    val candidates = listOf(
        "ro.product.marketname",
        "ro.product.vendor.marketname",
        "ro.product.odm.marketname",
        "ro.config.marketing_name",
        "persist.sys.marketname",
    )
    for (key in candidates) {
        val raw = getSystemProperty(key).takeIfValidDeviceName() ?: continue
        if (!looksLikeModelCode(raw)) return raw
    }
    return null
}

/**
 * 判断一个值是不是内部型号代号：`23013RK75C`、`2211133C`、`M2101K9C`、`23127PNY2C`。
 * 特征：不含空格、只由字母数字组成、长度 8~15、以数字或 M 开头。
 * 市场名（`Redmi K60`、`Xiaomi 14 Ultra`）都含空格，不会被误判。
 */
private fun looksLikeModelCode(raw: String): Boolean {
    val compact = raw.trim()
    if (compact.contains(' ')) return false
    if (compact.length !in 8..15) return false
    if (!compact.all { it.isLetterOrDigit() }) return false
    return compact.first().isDigit() || compact.startsWith("M", ignoreCase = true)
}

private fun getSamsungProductName(): String? {
    val name = getSamsungProductNameFromFloatingFeature()
        ?: getSamsungProductNameFromFloatingFeatureFile()
    return name.withSamsungPrefix()
}

@SuppressLint("PrivateApi")
private fun getSamsungProductNameFromFloatingFeature(): String? = try {
    val clazz = Class.forName(SAMSUNG_FLOATING_FEATURE_CLASS)
    val instance = clazz.getMethod("getInstance").invoke(null)
    val value = clazz.getMethod("getString", String::class.java)
        .invoke(instance, KEY_SAMSUNG_PRODUCT_NAME) as? String
    value.takeIfValidDeviceName()
} catch (_: Throwable) {
    null
}

private fun getSamsungProductNameFromFloatingFeatureFile(): String? {
    val pattern = Regex(
        "<$KEY_SAMSUNG_PRODUCT_NAME>\\s*(.*?)\\s*</$KEY_SAMSUNG_PRODUCT_NAME>",
        RegexOption.DOT_MATCHES_ALL,
    )
    return SAMSUNG_FLOATING_FEATURE_PATHS.firstNotNullOfOrNull { path ->
        try {
            pattern.find(File(path).readText())?.groupValues?.getOrNull(1).takeIfValidDeviceName()
        } catch (_: Throwable) {
            null
        }
    }
}

private fun String?.takeIfValidDeviceName(): String? =
    this?.trim()?.takeIf {
        it.isNotEmpty() &&
                !it.equals(Build.UNKNOWN, ignoreCase = true) &&
                !it.equals("null", ignoreCase = true)
    }

private fun String?.withSamsungPrefix(): String? {
    val name = this.takeIfValidDeviceName() ?: return null
    return if (name.startsWith("Samsung", ignoreCase = true)) name else "Samsung $name"
}
'''


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def patch(path: str, old: str, new: str, label: str) -> None:
    p = ROOT / path
    if not p.exists():
        failures.append(f"{label}: 文件不存在 {path}")
        return
    text = p.read_text(encoding="utf-8")
    if new in text:
        print(f"  SKIP {label}（已应用）")
        return
    if old not in text:
        failures.append(f"{label}: 锚点未命中 {path}")
        return
    p.write_text(text.replace(old, new, 1), encoding="utf-8")
    print(f"  命中 {label}")


print("[1/7] DeviceNameHelper 重写")
write(DEVICE_HELPER, DEVICE_SOURCE)

print("[2/7] HomeViewModel：设备名初始值与兜底都走 resolveDeviceName()")
patch(
    HOME_VM,
    'val name = (result as? EnvironmentProbeResult.Completed)?.value ?: Build.MODEL',
    'val name = (result as? EnvironmentProbeResult.Completed)?.value\n'
    '            ?: runCatching { resolveDeviceName() }.getOrDefault(Build.MODEL)',
    "deviceName-fallback",
)
patch(
    HOME_VM,
    'deviceModel = Build.MODEL,',
    'deviceModel = runCatching { resolveDeviceName() }.getOrDefault(Build.MODEL),',
    "systemInfo-initial",
)

print("[3/7] SettingsModePolicy：新增 MANAGER_UPDATE")
patch(
    POLICY,
    '    /** 通用：界面与外观入口 + 外观子页。 */\n    APPEARANCE,',
    '    /** 通用：界面与外观入口 + 外观子页。 */\n    APPEARANCE,\n\n'
    '    /** 通用：检查管理器更新（纯客户端，不需要 root）。 */\n    MANAGER_UPDATE,',
    "section-enum",
)
patch(
    POLICY,
    '    APPEARANCE_ENTRY,\n    PERSONALIZATION_GROUP,',
    '    APPEARANCE_ENTRY,\n    PERSONALIZATION_GROUP,\n    MANAGER_UPDATE_CHECK,',
    "row-enum",
)
patch(
    POLICY,
    '    SettingsSection.APPEARANCE -> setOf(SettingsRow.APPEARANCE_ENTRY, SettingsRow.PERSONALIZATION_GROUP)',
    '    SettingsSection.APPEARANCE -> setOf(SettingsRow.APPEARANCE_ENTRY, SettingsRow.PERSONALIZATION_GROUP)\n'
    '    SettingsSection.MANAGER_UPDATE -> setOf(SettingsRow.MANAGER_UPDATE_CHECK)',
    "rows-of",
)
patch(
    POLICY,
    '    SettingsSection.APPEARANCE,\n    SettingsSection.MODULE_UPDATE,',
    '    SettingsSection.APPEARANCE,\n    SettingsSection.MANAGER_UPDATE,\n    SettingsSection.MODULE_UPDATE,',
    "data-sources-empty",
)
patch(
    POLICY,
    '            SettingsSection.APPEARANCE,\n            SettingsSection.MODULE_UPDATE,',
    '            SettingsSection.APPEARANCE,\n            SettingsSection.MANAGER_UPDATE,\n            SettingsSection.MODULE_UPDATE,',
    "common-sections",
)

print("[4/7] SettingsMaterial：加「检查管理器更新」卡（最前）")
patch(
    MATERIAL,
    '                SegmentedColumn(\n'
    '                    modifier = GroupPadding,\n'
    '                    content = listOf {\n'
    '                        ArrowRowMaterial(\n'
    '                            title = stringResource(R.string.ui_d_appearance_title),',
    '                SegmentedColumn(\n'
    '                    modifier = GroupPadding,\n'
    '                ) {\n'
    '                    item(key = "manager-update") {\n'
    '                        SegmentedSwitchItem(\n'
    '                            icon = Icons.Filled.SystemUpdateAlt,\n'
    '                            title = stringResource(R.string.settings_manager_check_update),\n'
    '                            summary = stringResource(R.string.settings_check_update_summary),\n'
    '                            checked = uiState.checkUpdate,\n'
    '                            onCheckedChange = actions.onSetCheckUpdate,\n'
    '                        )\n'
    '                    }\n'
    '                }\n'
    '\n'
    '                SegmentedColumn(\n'
    '                    modifier = GroupPadding,\n'
    '                    content = listOf {\n'
    '                        ArrowRowMaterial(\n'
    '                            title = stringResource(R.string.ui_d_appearance_title),',
    "material-manager-update",
)

print("[5/7] SettingsMiuix：加「检查管理器更新」卡（最前）")
patch(
    MIUIX,
    '                item(key = "appearance-entry") {',
    '                item(key = "manager-update") {\n'
    '                    SettingsCardMiuix(Modifier.animateItem(fadeInSpec = tween(120), placementSpec = tween(160), fadeOutSpec = null)) {\n'
    '                        SwitchRowMiuix(\n'
    '                            title = stringResource(R.string.settings_manager_check_update),\n'
    '                            summary = stringResource(R.string.settings_check_update_summary),\n'
    '                            icon = Icons.Rounded.SystemUpdateAlt,\n'
    '                            checked = uiState.checkUpdate,\n'
    '                            onCheckedChange = actions.onSetCheckUpdate,\n'
    '                        )\n'
    '                    }\n'
    '                }\n'
    '\n'
    '                item(key = "appearance-entry") {',
    "miuix-manager-update",
)

print("[6/7] 字符串")
patch(
    ZH,
    '    <string name="settings_module_check_update">检查模块更新</string>',
    '    <string name="settings_manager_check_update">检查管理器更新</string>\n'
    '    <string name="settings_module_check_update">检查模块更新</string>',
    "zh-string",
)
patch(
    EN,
    '    <string name="settings_module_check_update">Check for module updates</string>',
    '    <string name="settings_manager_check_update">Check for manager updates</string>\n'
    '    <string name="settings_module_check_update">Check for module updates</string>',
    "en-string",
)


print("[7/7] 版本 bump")
def bump(gradle_rel: str, old_code: int, old_name: str, new_code: int, new_name: str) -> None:
    p = ROOT / gradle_rel
    if not p.exists():
        print(f"  SKIP bump（找不到 {gradle_rel}）")
        return
    text = p.read_text(encoding="utf-8")
    if f"{new_code}" in text and new_name in text:
        print("  SKIP bump（已是目标版本）")
        return
    if f"versionCode = {old_code}" in text:
        text = text.replace(f"versionCode = {old_code}", f"versionCode = {new_code}", 1)
    if f'"{old_name}"' in text:
        text = text.replace(f'"{old_name}"', f'"{new_name}"', 1)
    p.write_text(text, encoding="utf-8")
    print(f"  bump {old_code}/{old_name} -> {new_code}/{new_name}")


bump(GRADLE, 32754, "3.22.15-bw", 32755, "3.22.16-bw")

if failures:
    print("\nFAILURES:")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("\nOK: 32755 补丁全部命中")
