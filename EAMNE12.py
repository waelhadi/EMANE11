import os
import sys
import subprocess
import time

# تثبيت تلقائي للمكتبات إذا لم تكن موجودة
required = ["requests", "playsound"]

for package in required:
    try:
        __import__(package)
    except ImportError:
        print(f"📦 تثبيت المكتبة: {package}", flush=True)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ تم التثبيت: {package}", flush=True)

import requests
from playsound import playsound

url = "https://mp4.shabakngy.com/m/m/CrjPD3Fg3Wk.mp3"
filename = "start.mp3"

try:
    print("📥 جاري تحميل الملف الصوتي ...", flush=True)
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print("✅ تم التحميل: start.mp3", flush=True)

    print("🔊 يتم تشغيل الصوت ...", flush=True)
    playsound(filename)

    print("✅ تم التشغيل.", flush=True)
    input("📌 اضغط Enter للخروج ...")

except requests.exceptions.RequestException as e:
    print(f"❌ فشل تحميل الملف: {e}", flush=True)
    input("📌 اضغط Enter للخروج ...")
except Exception as e:
    print(f"❌ خطأ: {e}", flush=True)
    input("📌 اضغط Enter للخروج ...")
