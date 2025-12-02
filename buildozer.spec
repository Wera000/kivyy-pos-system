[app]
title = My Kivy 8-Screen App
package.name = myapp
package.domain = org.myapp.github
source.dir = .
requirements = python3.9,kivy
source.include_dirs = screens
source.include_exts = py,kv,png,jpg,atlas,zip,wav,mp3,ogg
version = 0.1
orientation = landscape
fullscreen = 0
android.api = 30
android.minapi = 21
android.ndk = 21b
android.accept_licenses = True
# CRITICAL FIX: Disable the problematic Aidl recipe to bypass "Aidl not found" error
p4a.broken_recipes = aidl

[buildozer]
log_level = 2
warn_on_error = 0
