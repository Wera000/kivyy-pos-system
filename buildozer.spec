[app]
title = My Kivy App
package.name = myapp
package.domain = org.myapp.github

source.dir = .
source.include_exts = py,kv,png,jpg,atlas,zip,wav,mp3,ogg

version = 0.1
orientation = landscape
fullscreen = 0

requirements = python3==3.9,kivy

android.api = 30
android.minapi = 21
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b


# ✅ DO NOT FORCE OLD NDK
# ❌ android.ndk = 21b  (REMOVED)

android.sdk_path = /home/runner/android-sdk

[buildozer]
log_level = 2
warn_on_error = 0
