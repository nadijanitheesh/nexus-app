[app]
title = NEXUS
package.name = nexus
package.domain = com.nexus.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,requests,gtts,openssl,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# ස්ථාවර SDK සහ NDK වර්ෂන් සැකසීම
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
