# 构建结果

- run: 34  提交: 24a85b6e875e41eaee050d6fcf9a199523b3c56c
- 作业结论: failure

#### 补丁摘要（是否真应用）
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/src/main/res/values/maplesu_strings.xml
改好 manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt
插入 BLUEWHALE_KEY_COLOR 常量
改好 manager/src/main/res/values/colors.xml
改好 manager/build.gradle.kts
修好 build.py: cmake 可执行名跨平台
修好 build.py: ninja 可执行名跨平台
修好 build.py: ir spec 路径反斜杠归一（带 basename 回退）
改好 build.gradle.kts: policy bundle 固定 ultra
改好 build.gradle.kts: bundle 同源校验随自检开关跳过
修好 prepare_host_dependencies.py: 插入 _retry_urlopen
修好 prepare_host_dependencies.py: 下载走重试
蓝鱼品牌化补丁已全部应用。
3.16 APK 第 1/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 2/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 3/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 4/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 5/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 6/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
修补失败：
 - 品牌资产还原失败: 3.16 APK 下载失败（已试 6 次）: IncompleteRead(8682852 bytes read, 4649 more expected)
改好 build.gradle.kts: runtime 目标集按开关决定 bridge
改好 manager/build.gradle.kts: @get:InputFile abstract val ultraBridgeLibrary: 
改好 manager/build.gradle.kts: ultraBridgeLibrary.get().asFile.copyTo(jniDirect
改好 manager/build.gradle.kts: ultraBridgeLibrary.set(runtimeBuild.map { it.fil
改好 build.gradle.kts: bridge 不再作为硬性输出
改好 product.py: cached_jar 缺缓存时从 Maven 补拉
改好 build.gradle.kts: Ultra claim 门槛随跳过开关放行
改好 gradle.properties: 落 bluewhaleSkipUltraBridge
改好 manager/src/main/AndroidManifest.xml: android:authorities="dev.maplesu.manager.soter"
改好 manager/src/main/java/dev/maplesu/manager/soter/SoterTargetProvider.kt: const val AUTHORITY = "dev.maplesu.manager.soter

#### gradle 失败原因

#### CMake 错误日志

```
#### provider 子构建日志（CMake/cargo 报错常只写在这里）
#### 主构建日志尾
上游体积: 703M
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/src/main/res/values/maplesu_strings.xml
改好 manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt
插入 BLUEWHALE_KEY_COLOR 常量
改好 manager/src/main/res/values/colors.xml
移除位图 drawable-xxhdpi
移除位图 drawable-hdpi
移除位图 drawable-mdpi
移除位图 drawable-xxxhdpi
移除位图 drawable-xhdpi
放入矢量图标
改好 manager/build.gradle.kts
修好 build.py: cmake 可执行名跨平台
修好 build.py: ninja 可执行名跨平台
修好 build.py: ir spec 路径反斜杠归一（带 basename 回退）
改好 build.gradle.kts: policy bundle 固定 ultra
改好 build.gradle.kts: bundle 同源校验随自检开关跳过
policy bundle 自检：18 个源，缺 0，漂 0
修好 prepare_host_dependencies.py: 插入 _retry_urlopen
修好 prepare_host_dependencies.py: 下载走重试

蓝鱼品牌化补丁已全部应用。
3.16 APK 第 1/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 2/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 3/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 4/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 5/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)
3.16 APK 第 6/6 次下载失败: IncompleteRead(8682852 bytes read, 4649 more expected)

修补失败：
 - 品牌资产还原失败: 3.16 APK 下载失败（已试 6 次）: IncompleteRead(8682852 bytes read, 4649 more expected)
改好 build.gradle.kts: runtime 目标集按开关决定 bridge
改好 manager/build.gradle.kts: @get:InputFile abstract val ultraBridgeLibrary: 
改好 manager/build.gradle.kts: ultraBridgeLibrary.get().asFile.copyTo(jniDirect
改好 manager/build.gradle.kts: ultraBridgeLibrary.set(runtimeBuild.map { it.fil
改好 build.gradle.kts: bridge 不再作为硬性输出
改好 product.py: cached_jar 缺缓存时从 Maven 补拉
改好 build.gradle.kts: Ultra claim 门槛随跳过开关放行
改好 gradle.properties: 落 bluewhaleSkipUltraBridge
改好 manager/src/main/AndroidManifest.xml: android:authorities="dev.maplesu.manager.soter"
改好 manager/src/main/java/dev/maplesu/manager/soter/SoterTargetProvider.kt: const val AUTHORITY = "dev.maplesu.manager.soter
```
