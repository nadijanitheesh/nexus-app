[app]
title = NEXUS
package.name = nexus
package.domain = com.nexus.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# මෙන්න මෙතැනට kivy එකතු කර ඇත
requirements = python3,kivy,requests,openssl,certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
