#!/usr/bin/env python3
"""32741: no-root limited navigation (Home + Settings) and diagnostics moved to Settings."""
from pathlib import Path


def _replace(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"FATAL: {label}: marker not found in {path}")
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {path.name}: {label}")


def patch_navigation_policy(root: Path) -> None:
    path = root / "manager/src/main/java/com/maplesu/core/ui/viewmodel/MainNavigationPolicy.kt"
    text = path.read_text(encoding="utf-8")
    if "resolveInitialPage" in text:
        print("skip: navigation policy already patched")
        return
    old = """    fun resolvePage(page: Int, homeOnly: Boolean): Int =
        if (homeOnly) 0 else MainPagerConfig.coercePage(page)
"""
    new = """    fun resolvePage(page: Int, homeOnly: Boolean): Int =
        if (homeOnly) page.coerceIn(0, 1) else MainPagerConfig.coercePage(page)

    /** Entering limited mode must not turn a previously-open Superuser tab into Settings. */
    fun resolveInitialPage(page: Int, homeOnly: Boolean): Int =
        if (homeOnly) {
            if (page == 3) 1 else 0
        } else {
            MainPagerConfig.coercePage(page)
        }
"""
    if old not in text:
        raise SystemExit("FATAL: navigation policy marker not found")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched MainNavigationPolicy.kt: limited Home + Settings")


def patch_navigation_test(root: Path) -> None:
    path = root / "manager/src/test/java/com/maplesu/core/ui/viewmodel/MainNavigationPolicyTest.kt"
    if not path.is_file():
        print("skip: navigation policy test not present")
        return
    text = path.read_text(encoding="utf-8")
    old = """    @Test fun restoringOtherPagesReturnsToHomeWhenUninstalled() {
        (0 until MainPagerConfig.PAGE_COUNT).forEach { page ->
            assertEquals(0, MainNavigationPolicy.resolvePage(page, homeOnly = true))
        }
    }
"""
    new = """    @Test fun restoringOtherPagesBoundsToLimitedHomeAndSettings() {
        (0 until MainPagerConfig.PAGE_COUNT).forEach { page ->
            assertEquals(page.coerceIn(0, 1), MainNavigationPolicy.resolvePage(page, homeOnly = true))
        }
    }
"""
    if old not in text:
        print("skip: navigation policy test already updated")
        return
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("patched MainNavigationPolicyTest.kt: limited page bounds")


def patch_main_screen(root: Path) -> None:
    path = root / "manager/src/main/java/com/maplesu/core/ui/MainActivity.kt"
    text = path.read_text(encoding="utf-8")
    if "LimitedBottomBar" in text:
        print("skip: MainActivity already patched")
        return
    if "import com.maplesu.core.ui.component.bottombar.BottomBar\n" not in text:
        raise SystemExit("FATAL: BottomBar import not found")
    text = text.replace(
        "import com.maplesu.core.ui.component.bottombar.BottomBar\n",
        "import com.maplesu.core.ui.component.bottombar.BottomBar\n"
        "import com.maplesu.core.ui.component.bottombar.LimitedBottomBar\n",
        1,
    )
    text = text.replace(
        "    val homeOnly = MainNavigationPolicy.isHomeOnly(\n",
        "    val homeOnly = !homeUiState.isRootAvailable || MainNavigationPolicy.isHomeOnly(\n",
        1,
    )
    text = text.replace(
        "    val pageCount = if (homeOnly) 1 else MainPagerConfig.PAGE_COUNT\n",
        "    val pageCount = if (homeOnly) 2 else MainPagerConfig.PAGE_COUNT\n",
        1,
    )
    text = text.replace(
        "        initialPage = MainNavigationPolicy.resolvePage(initialPage, homeOnly),\n",
        "        initialPage = MainNavigationPolicy.resolveInitialPage(initialPage, homeOnly),\n",
        1,
    )
    old_when = """                    when (page) {
                        0 -> HomePager(homeViewModel, navController, bottomInnerPadding, isCurrentPage,
                            authorizedCount = superuserCount.takeIf { themeCountsEnabled },
                            moduleEnabledCount = enabledModuleCount.takeIf { themeCountsEnabled })
                        1 -> SuperUserPager(navController, bottomInnerPadding, isCurrentPage)
                        2 -> ModulePager(bottomInnerPadding, isCurrentPage)
                        3 -> SettingPager(navController, bottomInnerPadding, isCurrentPage)
                    }
"""
    new_when = """                    when (page) {
                         0 -> HomePager(homeViewModel, navController, bottomInnerPadding, isCurrentPage,
                            authorizedCount = superuserCount.takeIf { themeCountsEnabled },
                            moduleEnabledCount = enabledModuleCount.takeIf { themeCountsEnabled })
                        1 -> if (homeOnly) {
                            SettingPager(
                                navigator = navController,
                                bottomInnerPadding = bottomInnerPadding,
                                isCurrentPage = isCurrentPage,
                                diagnosticsState = homeUiState,
                                onDiagnosticsRetry = { homeViewModel.refresh() },
                            )
                        } else {
                            SuperUserPager(navController, bottomInnerPadding, isCurrentPage)
                        }
                        2 -> if (!homeOnly) ModulePager(bottomInnerPadding, isCurrentPage)
                        3 -> if (!homeOnly) {
                            SettingPager(
                                navigator = navController,
                                bottomInnerPadding = bottomInnerPadding,
                                isCurrentPage = isCurrentPage,
                                diagnosticsState = homeUiState,
                                onDiagnosticsRetry = { homeViewModel.refresh() },
                            )
                        }
                    }
"""
    if old_when not in text:
        raise SystemExit("FATAL: pager page switch not found")
    text = text.replace(old_when, new_when, 1)
    old_bottom = """            val bottomBar = @Composable {
                if (!homeOnly) Box(
                    modifier = Modifier.fillMaxWidth()
                ) {
                    BottomBar(
                        blurBackdrop = blurBackdrop,
                        backdrop = backdrop,
                        navigationBadge = navigationBadge,
                        modifier = Modifier.align(Alignment.BottomCenter),
                    )
                }
            }
"""
    new_bottom = """            val bottomBar = @Composable {
                if (homeOnly) {
                    Box(modifier = Modifier.fillMaxWidth()) {
                        LimitedBottomBar(
                            blurBackdrop = blurBackdrop,
                            modifier = Modifier.align(Alignment.BottomCenter),
                        )
                    }
                } else {
                    Box(modifier = Modifier.fillMaxWidth()) {
                        BottomBar(
                            blurBackdrop = blurBackdrop,
                            backdrop = backdrop,
                            navigationBadge = navigationBadge,
                            modifier = Modifier.align(Alignment.BottomCenter),
                        )
                    }
                }
            }
"""
    if old_bottom not in text:
        raise SystemExit("FATAL: bottom bar block not found")
    text = text.replace(old_bottom, new_bottom, 1)
    path.write_text(text, encoding="utf-8")
    print("patched MainActivity.kt: two-page limited navigation")


def remove_home_diagnostics(root: Path) -> None:
    miuix = root / "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
    material = root / "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMaterial.kt"
    block_miuix = """                        // 3.22.0：状态卡下方的紧凑 Root 诊断入口，双皮肤一致；无 root 也可用。
                        Column(modifier = sideInset) {
                            RootDiagnosticsSection(
                                state = state,
                                onRetry = actions.onEnvironmentRetry,
                                flat = flatHome,
                            )
                        }
"""
    block_material = """            // 3.22.0：状态卡下方的紧凑 Root 诊断入口，双皮肤一致；无 root 也可用。
            RootDiagnosticsSection(
                state = state,
                onRetry = actions.onEnvironmentRetry,
            )
"""
    for path, block, label in (
        (miuix, block_miuix, "HomeMiuix"),
        (material, block_material, "HomeMaterial"),
    ):
        text = path.read_text(encoding="utf-8")
        if block not in text:
            print(f"skip: {label} diagnostics already moved")
            continue
        path.write_text(text.replace(block, "", 1), encoding="utf-8")
        print(f"patched {label}: removed Root diagnostics card")


def patch_settings(root: Path) -> None:
    screen = root / "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsScreen.kt"
    miuix = root / "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMiuix.kt"
    material = root / "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMaterial.kt"

    # SettingsScreen: add optional diagnostics inputs and pass them through.
    text = screen.read_text(encoding="utf-8")
    if "diagnosticsState" in text:
        print("skip: SettingsScreen already patched")
    else:
        text = text.replace(
            "import com.maplesu.core.ui.navigation3.Route\n",
            "import com.maplesu.core.ui.navigation3.Route\n"
            "import com.maplesu.core.ui.screen.home.HomeUiState\n",
            1,
        )
        old_sig = """    appearanceOnly: Boolean = false,
    onBack: (() -> Unit)? = null,
) {
"""
        new_sig = """    appearanceOnly: Boolean = false,
    onBack: (() -> Unit)? = null,
    diagnosticsState: HomeUiState? = null,
    onDiagnosticsRetry: () -> Unit = {},
) {
"""
        if old_sig not in text:
            raise SystemExit("FATAL: SettingPager signature not found")
        text = text.replace(old_sig, new_sig, 1)
        text = text.replace(
            "        UiMode.Miuix -> SettingPagerMiuix(uiState, actions, bottomInnerPadding, appearanceOnly, onBack, miuixListState, miuixTopBarState)\n"
            "        UiMode.Material -> SettingPagerMaterial(uiState, actions, bottomInnerPadding, appearanceOnly, onBack, materialScrollState, materialTopBarState)\n",
            "        UiMode.Miuix -> SettingPagerMiuix(uiState, actions, bottomInnerPadding, appearanceOnly, onBack, miuixListState, miuixTopBarState, diagnosticsState, onDiagnosticsRetry)\n"
            "        UiMode.Material -> SettingPagerMaterial(uiState, actions, bottomInnerPadding, appearanceOnly, onBack, materialScrollState, materialTopBarState, diagnosticsState, onDiagnosticsRetry)\n",
            1,
        )
        screen.write_text(text, encoding="utf-8")
        print("patched SettingsScreen.kt: diagnostics parameters")

    # Miuix settings list: import and insert the diagnostics card above Appearance.
    text = miuix.read_text(encoding="utf-8")
    if "RootDiagnosticsSection" not in text:
        for line in (
            "import com.maplesu.core.ui.screen.home.HomeUiState\n",
            "import com.maplesu.core.ui.screen.home.RootDiagnosticsSection\n",
            "import com.maplesu.core.ui.theme.LocalFlatUi\n",
        ):
            if line not in text:
                text = text.replace(
                    "import com.maplesu.core.ui.theme.LocalEnableBlur\n",
                    "import com.maplesu.core.ui.theme.LocalEnableBlur\n" + line,
                    1,
                )
        old_sig = """    onBack: (() -> Unit)? = null,
    listState: LazyListState,
    topBarState: TopAppBarState,
) {
"""
        new_sig = """    onBack: (() -> Unit)? = null,
    listState: LazyListState,
    topBarState: TopAppBarState,
    diagnosticsState: HomeUiState? = null,
    onDiagnosticsRetry: () -> Unit = {},
) {
"""
        if old_sig not in text:
            raise SystemExit("FATAL: SettingPagerMiuix signature not found")
        text = text.replace(old_sig, new_sig, 1)
        old_item = """                if (appearanceOnly) {
                    item(key = "appearance") {
"""
        new_item = """                if (!appearanceOnly && diagnosticsState != null) {
                    item(key = "root-diagnostics") {
                        RootDiagnosticsSection(
                            state = diagnosticsState,
                            onRetry = onDiagnosticsRetry,
                            flat = LocalFlatUi.current,
                        )
                        Spacer(Modifier.height(12.dp))
                    }
                }
                if (appearanceOnly) {
                    item(key = "appearance") {
"""
        if old_item not in text:
            raise SystemExit("FATAL: Miuix settings list marker not found")
        text = text.replace(old_item, new_item, 1)
        miuix.write_text(text, encoding="utf-8")
        print("patched SettingsMiuix.kt: Root diagnostics at top")

    # Material settings: same optional parameters and card insertion.
    text = material.read_text(encoding="utf-8")
    if "RootDiagnosticsSection" not in text:
        for line in (
            "import com.maplesu.core.ui.screen.home.HomeUiState\n",
            "import com.maplesu.core.ui.screen.home.RootDiagnosticsSection\n",
        ):
            if line not in text:
                text = text.replace(
                    "import com.maplesu.core.ui.theme.LocalEnableBlur\n",
                    "import com.maplesu.core.ui.theme.LocalEnableBlur\n" + line,
                    1,
                )
        old_sig = """    onBack: (() -> Unit)? = null,
    scrollState: ScrollState,
    topBarState: TopAppBarState,
) {
"""
        new_sig = """    onBack: (() -> Unit)? = null,
    scrollState: ScrollState,
    topBarState: TopAppBarState,
    diagnosticsState: HomeUiState? = null,
    onDiagnosticsRetry: () -> Unit = {},
) {
"""
        if old_sig not in text:
            raise SystemExit("FATAL: SettingPagerMaterial signature not found")
        text = text.replace(old_sig, new_sig, 1)
        old_body = """            if (appearanceOnly) {
                AppearanceBodyMaterial(uiState, actions)
            } else {
                SegmentedColumn(
"""
        new_body = """            if (appearanceOnly) {
                AppearanceBodyMaterial(uiState, actions)
            } else {
                if (diagnosticsState != null) {
                    Column(modifier = GroupPadding) {
                        RootDiagnosticsSection(
                            state = diagnosticsState,
                            onRetry = onDiagnosticsRetry,
                        )
                        Spacer(Modifier.height(12.dp))
                    }
                }
                SegmentedColumn(
"""
        if old_body not in text:
            raise SystemExit("FATAL: Material settings body marker not found")
        text = text.replace(old_body, new_body, 1)
        material.write_text(text, encoding="utf-8")
        print("patched SettingsMaterial.kt: Root diagnostics at top")


def add_limited_bottom_bar(root: Path) -> None:
    path = root / "manager/src/main/java/com/maplesu/core/ui/component/bottombar/LimitedBottomBar.kt"
    if path.is_file():
        print("skip: LimitedBottomBar already exists")
        return
    path.write_text(
        """package com.maplesu.core.ui.component.bottombar

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Cottage
import androidx.compose.material.icons.rounded.Settings
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ShortNavigationBar
import androidx.compose.material3.ShortNavigationBarItem
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import com.maplesu.core.R
import com.maplesu.core.ui.LocalMainPagerState
import com.maplesu.core.ui.LocalUiMode
import com.maplesu.core.ui.UiMode
import com.maplesu.core.ui.util.BlurredBar
import top.yukonga.miuix.kmp.basic.NavigationBar
import top.yukonga.miuix.kmp.basic.NavigationBarItem
import top.yukonga.miuix.kmp.blur.LayerBackdrop
import top.yukonga.miuix.kmp.theme.MiuixTheme

/**
 * No-root mode: only Home and Settings exist, so the regular four-tab bar must not pretend
 * that unavailable pages can be opened. This bar intentionally uses the stock icons.
 */
@Composable
fun LimitedBottomBar(
    blurBackdrop: LayerBackdrop?,
    modifier: Modifier = Modifier,
) {
    val mainState = LocalMainPagerState.current
    when (LocalUiMode.current) {
        UiMode.Miuix -> {
            BlurredBar(blurBackdrop) {
                NavigationBar(
                    modifier = modifier,
                    color = MiuixTheme.colorScheme.surface,
                ) {
                    NavigationBarItem(
                        modifier = Modifier.weight(1f),
                        icon = Icons.Rounded.Cottage,
                        label = stringResource(R.string.home),
                        selected = mainState.selectedPage == 0,
                        onClick = { mainState.animateToPage(0) },
                    )
                    NavigationBarItem(
                        modifier = Modifier.weight(1f),
                        icon = Icons.Rounded.Settings,
                        label = stringResource(R.string.settings),
                        selected = mainState.selectedPage == 1,
                        onClick = { mainState.animateToPage(1) },
                    )
                }
            }
        }

        UiMode.Material -> {
            ShortNavigationBar(
                containerColor = MaterialTheme.colorScheme.surfaceContainer,
            ) {
                ShortNavigationBarItem(
                    selected = mainState.selectedPage == 0,
                    onClick = { mainState.animateToPage(0) },
                    icon = { Icon(Icons.Rounded.Cottage, contentDescription = stringResource(R.string.home)) },
                    label = { Text(stringResource(R.string.home)) },
                )
                ShortNavigationBarItem(
                    selected = mainState.selectedPage == 1,
                    onClick = { mainState.animateToPage(1) },
                    icon = { Icon(Icons.Rounded.Settings, contentDescription = stringResource(R.string.settings)) },
                    label = { Text(stringResource(R.string.settings)) },
                )
            }
        }
    }
}
"""
    , encoding="utf-8")
    print("added LimitedBottomBar.kt")


def patch_32741(root: Path) -> None:
    patch_navigation_policy(root)
    patch_navigation_test(root)
    patch_main_screen(root)
    remove_home_diagnostics(root)
    patch_settings(root)
    add_limited_bottom_bar(root)
    print("32739-r4: limited Home + Settings, diagnostics moved to Settings")
