[app]

# --- Proqram Haqqında Məlumat ---
title = Akif Admin Tool
package.name = akifkeygen
package.domain = org.akif
version = 0.3

# --- Fayllar ---
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# --- Kitabxanalar (ƏN VACİB HİSSƏ) ---
# 1. Kivy 2.3.0 -> Android 15 dəstəyi üçün
# 2. KivyMD (Link ilə) -> Ən son xətaların düzəldilmiş versiyası (Master branch)
# 3. Pillow -> Şəkil və ikonlar üçün vacibdir
requirements = python3,kivy==2.3.0,https://github.com/kivymd/KivyMD/archive/master.zip,pillow

# --- Ekran Ayarları ---
orientation = portrait
fullscreen = 0

# --- Android Ayarları ---
# İnternet icazəsi
android.permissions = INTERNET

# API Səviyyələri (Android 14/15 standartı)
android.api = 34
android.minapi = 24

# Arxitektura (Həm köhnə, həm təzə telefonlar)
android.archs = arm64-v8a, armeabi-v7a

# Yeni sistemlər üçün vacib (Kivy 2.3.0 tələb edir)
android.enable_androidx = True

# Başlanğıc ekranı rəngi (Qara - Gözü yormasın)
android.presplash_color = #121212

# Python-for-Android master versiyası
p4a.branch = master

[buildozer]

# --- Build Ayarları ---
log_level = 2
warn_on_root = 1