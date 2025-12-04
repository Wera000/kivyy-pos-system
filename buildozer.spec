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

# NDK / build
android.ndk = 25b
android.ndk_api = 25
android.bootstrap = sdl2
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Include libs
android.copy_libs = 1

# Versioning
version = 0.1

# -----------------------------------------
# Notes:
# 1. Do NOT set android.ndk_path → workflow handles it
# 2. Do NOT specify build-tools → workflow uses 30.0.3
