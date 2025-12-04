[app]
title = MyApp
package.name = myapp
package.domain = org.myapp

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3==3.9,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a,armeabi-v7a
android.api = 30
android.minapi = 21

android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = /home/runner/android-sdk
android.sdkmanager_path = /home/runner/android-sdk/tools/bin/sdkmanager

android.bootstrap = sdl2
android.ndk_api = 25
android.copy_libs = 1

version = 0.1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_error = 0
