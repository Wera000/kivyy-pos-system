[app]
title = MyApp
package.name = myapp
package.domain = org.myapp

source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 0.1
orientation = portrait
fullscreen = 0

requirements = python3==3.9,kivy

android.archs = arm64-v8a,armeabi-v7a

android.api = 30
android.minapi = 21

android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.ndk_api = 25

android.sdk = 30
android.bootstrap = sdl2
android.copy_libs = 1

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
