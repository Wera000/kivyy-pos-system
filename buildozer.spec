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
android.ndk = 21b

android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r21b
android.sdkmanager_path = /home/runner/android-sdk/tools/bin/sdkmanager

[buildozer]
log_level = 2
warn_on_error = 0
