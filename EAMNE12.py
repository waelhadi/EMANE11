import os
import sys
import subprocess
import time

# تثبيت المكتبات تلقائيًا
required = ["requests", "pygame"]
for package in required:
    try:
        __import__(package)
    except ImportError:
        print(f"📦 جاري تثبيت المكتبة: {package}", flush=True)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ تم تثبيت {package}", flush=True)

import requests
import pygame

# رابط الصوت
url = "https://mp4.shabakngy.com/m/m/CrjPD3Fg3Wk.mp3"
filename = "start.mp3"

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


    while pygame.mixer.music.get_busy():
        time.sleep(0.5)


except requests.exceptions.RequestException as e:
    print(f"❌ فشل تحميل الملف: {e}", flush=True)
    input("📌 اضغط Enter للخروج ...")
except pygame.error as e:
    print(f"❌ خطأ في Pygame: {e}", flush=True)
    input("📌 اضغط Enter للخروج ...")
except Exception as e:
    print(f"❌ خطأ عام: {e}", flush=True)
    input("📌 اضغط Enter للخروج ...")
