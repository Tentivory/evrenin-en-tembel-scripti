#!/usr/bin/env python3
# Evrenin En Tembel Scripti
# Bu script hiçbir şey yapmaz. Yapmaması için elinden geleni yapar.

import time
import random

mazaretler = [
    "Yarın yaparım abi, bugün yorgunum.",
    "Çay içiyorum, biraz bekle.",
    "Bilgisayar açılıyor... (yalan)",
    "Kedi klavyenin üstüne oturdu.",
    "İnternet yok, kuşkonmaz çekiyorum.",
    "Bu görev bana göre değil, daha tembel biri lazım.",
    "Uyuyorum, uyanınca bakarım.",
    "Yemek yiyorum, midem boşken çalışmam."
]

def tembel_calis():
    print("Script başlatılıyor... (asla başlamaz)")
    while True:
        print(random.choice(mazaretler))
        time.sleep(random.uniform(2, 5))
        print("...devam ediyor... (devam etmiyor)")

if __name__ == "__main__":
    try:
        tembel_calis()
    except KeyboardInterrupt:
        print("\nDurduruldum. Teşekkürler, dinlenmeye devam.")
