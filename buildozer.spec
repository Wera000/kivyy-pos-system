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

# VERY important: match GitHub Actions setup
android.ndk = 25b
android.ndk_api = 25

android.archs = arm64-v8a, armeabi-v7a
android.bootstrap = sdl2

# Fix: do NOT set a manual ndk_path (GitHub Actions sets it)
# android.ndk_path = (removed)

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Required for including libs correctly
android.copy_libs = 1

# Versioning
version = 0.1
