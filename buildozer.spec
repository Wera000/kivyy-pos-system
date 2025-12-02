[app]
title = My Kivy B-Screen App
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

[buildozer]
log_level = 2
warn_on_error = 0
