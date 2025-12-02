[app]

# Application configuration
title = My Kivy 8-Screen App
package.name = myapp
package.domain = org.myapp.github
source.dir = .

# (Python 3.10 Fix for jnius compatibility)
requirements = python3.10,kivy

# (Include screens folder)
source.include_dirs = screens

# Other necessary settings
source.include_exts = py,kv,png,jpg,atlas,zip,wav,mp3,ogg
version = 0.1
orientation = landscape
fullscreen = 0
android.api = 31
android.minapi = 21
android.ndk = 25b
