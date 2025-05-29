import os
import requests
import shutil
import subprocess

# ===== إعداد =====
url = "https://mp4.shabakngy.com/m/m/CrjPD3Fg3Wk.mp3"
filename = "/sdcard/start.mp3"  # موقع الحفظ على الهاتف

# ===== تحقق من وجود Termux وأدواته =====
def install_termux_tools():
    print("📦 التحقق من وجود Termux ...", flush=True)
    if shutil.which("termux-media-player") is None:
        print("⚙️ جاري تثبيت termux-api و termux-media-player ...", flush=True)
        try:
            subprocess.run(["pkg", "update", "-y"])
            subprocess.run(["pkg", "install", "-y", "termux-api"])
            subprocess.run(["pkg", "install", "-y", "termux-media-player"])
            print("✅ تم تثبيت الأدوات بنجاح.", flush=True)
        except Exception as e:
            print(f"❌ فشل التثبيت التلقائي: {e}", flush=True)
    else:
        print("✅ termux-media-player مثبت مسبقًا.", flush=True)

# ===== تحميل الصوت =====
def download_audio():
    print("📥 جاري تحميل الملف الصوتي ...", flush=True)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print(f"✅ تم الحفظ: {filename}", flush=True)
        return True

    except Exception as e:
        print(f"❌ فشل التحميل: {e}", flush=True)
        return False

# ===== تشغيل الصوت =====
def play_audio():
    print("🔊 يتم تشغيل الصوت ...", flush=True)
    os.system(f"termux-media-player play {filename}")
    print("✅ تم التشغيل.", flush=True)

# ===== التنفيذ =====
if __name__ == "__main__":
    install_termux_tools()
    if download_audio():
        play_audio()
    input("📌 اضغط Enter للخروج ...")
