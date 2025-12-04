[app]

# App info
title = MyApp
package.name = myapp
package.domain = org.myapp

# Main app folder
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Python + Kivy
requirements = python3==3.9, kivy

# Screen
orientation = portrait
fullscreen = 0

# Android settings
android.api = 30
android.minapi = 21

# Android NDK
android.ndk = 25b
android.ndk_api = 25

# Architectures
android.archs = arm64-v8a, armeabi-v7a
android.bootstrap = sdl2

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Include libraries correctly
android.copy_libs = 1

# Versioning
version = 0.1

# Avoid setting android.ndk_path manually (GitHub Actions handles it)
# android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
