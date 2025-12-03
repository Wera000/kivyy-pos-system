[app]
title = My Kivy 8-Screen App
package.name = myapp
package.domain = org.myapp.github

source.dir = .
source.include_dirs = screens
source.include_exts = py,kv,png,jpg,atlas,zip,wav,mp3,ogg

version = 0.1
orientation = landscape
fullscreen = 0

requirements = python3==3.9.*,kivy

android.api = 30
android.minapi = 21
android.ndk = 21b
android.accept_licenses = True

# FORCE Buildozer to use our SDK + sdkmanager path
android.sdk_path = /home/runner/android-sdk
android.sdkmanager_path = /home/runner/android-sdk/cmdline-tools/latest/bin/sdkmanager

# COMMENT OUT broken recipes
# p4a.broken_recipes = aidl
