[app]

title = MyApp
package.name = myapp
package.domain = org.myapp

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3, kivy

orientation = portrait
fullscreen = 0

android.api = 30
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

android.archs = arm64-v8a, armeabi-v7a
android.bootstrap = sdl2

android.copy_libs = 1
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

version = 1.0
