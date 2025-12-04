[app]

# App info
title = MyApp
package.name = myapp
package.domain = org.myapp

# Main app folder
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Python + Kivy
requirements = python3==3.9, kivy==2.3.2

# Screen
orientation = portrait
fullscreen = 0

# Android settings
android.api = 30
android.minapi = 21
android.ndk = 25b
android.ndk_api = 25
android.archs = arm64-v8a, armeabi-v7a
android.bootstrap = sdl2
android.build_tools = 30.0.3

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Fix for libs
android.copy_libs = 1

# Do not set manual paths; workflow handles SDK/NDK
# android.ndk_path = 
# android.sdk_path = 

# Versioning
version = 0.1
