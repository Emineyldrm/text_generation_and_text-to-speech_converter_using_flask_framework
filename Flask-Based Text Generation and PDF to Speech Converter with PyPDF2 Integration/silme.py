import os
import glob

def eski_dosyalari_temizle():
    # 'static' klasöründeki tüm .mp3 dosyalarını bul ve sil
    files = glob.glob(os.path.join("static", "*.mp3"))
    for file in files:
        os.remove(file)

