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

# --- මෙන්න මේ කොටස අලුතින් හෝ නිවැරදිව දමන්න ---
android.api = 31
android.minapi = 21
android.sdk = 31
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
