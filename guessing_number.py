import time
import random

print("""
****************************************

Sayı Tahmin Etme Oyununa Hoşgeldiniz

****************************************
""")

print("")
print("Sayımız 0-100 aralığında olacaktır. Tahmin hakkınız = 10 (0 ve 100 dahil)")

tahmin_hakki = 10
sayi = random.randint(0,100)

while True:
    tahmin = int(input("Lütfen tahmininizi giriniz:"))
    if tahmin < sayi :
        print("Bilgiler doğrulanıyor...")
        time.sleep(1.5)
        tahmin_hakki -= 1
        print("Daha yüksek bir tahminde bulununuz. Kalan tahmin sayısı",tahmin_hakki)
    elif tahmin > sayi :
        print("Bilgiler doğrulanıyor...")
        time.sleep(1.5)
        tahmin_hakki -= 1
        print("Daha düşük bir tahminde bulununuz. Kalan tahmin sayısı",tahmin_hakki)
    else :
        print("Bilgiler doğrulanıyor...")
        time.sleep(1.5)
        print("Tebrikler doğru tahmin. Sayımız",sayi)
        break
    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitmiştir.")
        break
