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
audio_url = "https://mp4.shabakngy.com/m/m/CrjPD3Fg3Wk.mp3"
image_url = "https://upload.wikimedia.org/wikipedia/commons/1/15/Bald_Eagle_Portrait.jpg"
audio_file = "/sdcard/start.mp3"
image_file = "/sdcard/eagle.jpg"

# ===== تحميل الملفات =====
def download_file(url, path, desc="file"):
    print(f"📥 Downloading {desc}...", flush=True)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"✅ {desc.capitalize()} saved to: {path}", flush=True)
        return True
    except Exception as e:
        print(f"❌ Failed to download {desc}: {e}", flush=True)
        return False

# ===== تشغيل الصوت + عرض صورة ونص =====
def play_audio_with_image():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((600, 300))
    pygame.display.set_caption("NASR")

    # تحميل الصورة وعرضها
    try:
        background = pygame.image.load(image_file)
        background = pygame.transform.scale(background, (600, 300))
        screen.blit(background, (0, 0))
    except:
        screen.fill((0, 0, 0))  # خلفية سوداء في حال فشل تحميل الصورة

    # إعداد الخط
    font = pygame.font.SysFont("Arial", 40, bold=True)
    text = font.render("🦅 NASR – THE EAGLE", True, (255, 0, 0))
    text_rect = text.get_rect(center=(300, 150))
    screen.blit(text, text_rect)

    pygame.display.flip()

    # تشغيل الصوت
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

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
    audio_ok = download_file(audio_url, audio_file, "audio")
    image_ok = download_file(image_url, image_file, "image")
    if audio_ok:
        play_audio_with_image()
