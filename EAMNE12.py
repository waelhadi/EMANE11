import os
import time
import pygame
import requests

# ==== محاولة تثبيت تلقائي (يُستخدم في Pydroid عند الحاجة) ====
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

try:
    import pygame
except ImportError:
    os.system("pip install pygame")
    import pygame

# ===== إعداد =====
url = "https://mp4.shabakngy.com/m/m/CrjPD3Fg3Wk.mp3"
filename = "/sdcard/start.mp3"  # موقع الحفظ على الهاتف

# ===== تحميل الصوت =====
def download_audio():
    print("📥 Downloading audio file...", flush=True)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"✅ Saved to: {filename}", flush=True)
        return True
    except Exception as e:
        print(f"❌ Download failed: {e}", flush=True)
        return False

# ===== تشغيل الصوت + عرض كلمة NASR – THE EAGLE =====
def play_audio_with_text():
    pygame.init()
    pygame.mixer.init()

    # إعداد نافذة العرض
    screen = pygame.display.set_mode((600, 300))
    pygame.display.set_caption("NASR")
    screen.fill((0, 0, 0))  # خلفية سوداء

    # إعداد الخط والنص
    font = pygame.font.SysFont("Arial", 50, bold=True)
    text = font.render("🦅 NASR – THE EAGLE", True, (255, 0, 0))  # أحمر
    text_rect = text.get_rect(center=(300, 150))
    screen.blit(text, text_rect)

    pygame.display.flip()

    # تشغيل الصوت
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # الانتظار حتى ينتهي الصوت أو يُغلق المستخدم النافذة
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not pygame.mixer.music.get_busy():
            running = False
        time.sleep(0.1)

    pygame.quit()

# ===== التنفيذ =====
if name == "main":
    if download_audio():
        play_audio_with_text()
