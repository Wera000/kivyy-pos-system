[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (reverse DNS style)
package.domain = org.myapp

# (str) Source code entry point
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3==3.9,kivy

# (str) Python version
# (Already fixed by requirements above, no need to change)

# (str) Orientation of your app: landscape, portrait or all
orientation = portrait

# (bool) Indicate if the application should fullscreen
fullscreen = 0

# (str) Supported Android architectures
android.archs = arm64-v8a,armeabi-v7a

# (int) Target Android API
android.api = 30

# (int) Minimum Android API
android.minapi = 21

# (str) Path to Android NDK (GitHub Actions NDK location)
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

# (str) Android SDK version (not always necessary)
android.sdk = 30

# (bool) Copy libraries instead of linking
android.copy_libs = 1

# (str) Android bootstrap
# SDL2 is the most stable for Kivy
android.bootstrap = sdl2

# (int) NDK API (minimum API for NDK)
android.ndk_api = 21

# (str) Application version
version = 0.1

# (str) Icon file (optional)
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/presplash.png

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
