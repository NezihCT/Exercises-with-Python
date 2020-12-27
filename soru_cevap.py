import random
import time


def harf_alma(answer):
    # Harf almak isteyen kullanıcı 0'a bastığında çağıracağımız fonksiyon
    uzunluk = len(answer)
    x = random.randint(0,(uzunluk-1))
    i = 0
    while i<uzunluk:
        if i == x:
            print(answer[i], end=" ")
            i += 1
        else:
            print("-",end=" ")
            i += 1
def tebrik():
    # Doğru cevap sonrası çağıracağımız fonksiyon
    print( "Tebrikler doğru bildiniz.\n Diğer soru yükleniyor...")
    time.sleep(1.5)
def yanlis():
    # Yanlış cevap sonrası çağıracağımız fonksiyon
    print("Maalesef bilemediniz. Diğer soru yükleniyor...")
    time.sleep(1.5)
def cizgi(dogru_cevap):
    # her doğru cevabın kaç harften oluştuğunu göstermek amaçlı çağırdığımız fonksiyon
    i = 0
    j = len(dogru_cevap)
    while i < j:
        print("-",end=" ")
        i += 1

print(""""
*************************************

...Soru-Cevap Oyununa Hoşgeldiniz...

*************************************
""")

print("\n 3 soru sorulacaktır. Her soruda 1 harf alma hakkına sahipsiniz.\nHarf almak için 0'a basınız.\n")
print("1. Türkiye Cumhuriyeti devletinin ilk kadın pilotunun ismi nedir ?")
true_answer0 = 'sabiha'
cizgi(true_answer0)
cevap0 = input("\nCevabınız:")
kucuk_cevap0 = cevap0.lower() #burada aldığımız inputun karakterlerini küçülttük
if kucuk_cevap0 == true_answer0:
    tebrik()
else:
    if kucuk_cevap0 != true_answer0 or int(kucuk_cevap0) == 0:
        harf_alma(true_answer0)
        yeni_cevap0 = input("\nCevabınız:")
        if yeni_cevap0 == true_answer0:
            tebrik()
        else:
            yanlis()
        
        

print("\n\n2. İnsan DNA'sına en yakın hayvan hangisidir?")
true_answer1 = 'şempanze'
cizgi(true_answer1)
cevap1 = input("\nCevabınız:")
kucuk_cevap1 = cevap1.lower()
if kucuk_cevap1 == true_answer1:
    tebrik()
else:
    if kucuk_cevap1 != true_answer1 or int(kucuk_cevap1) == 0:
        harf_alma(true_answer1)
        yeni_cevap1 = input("\nCevabınız:")
        if yeni_cevap1 == true_answer1:
            tebrik()
        else:
            yanlis()


print("\n\n3. Pandas, matplotlib, opencv gibi kütüphaneleri bulunan yazılım dilinin adı nedir?")
true_answer2 = 'python'
cizgi(true_answer2)
cevap2 = input("\nCevabınız:")
kucuk_cevap2 = cevap2.lower()
if kucuk_cevap2 == true_answer2:
    tebrik()
else:
    if kucuk_cevap2 != true_answer2 or int(kucuk_cevap2) == 0:
        harf_alma(true_answer2)
        yeni_cevap2 = input("\nCevabınız:")
        if yeni_cevap2 == true_answer2:
            print("Tebrikler, doğru bildiniz. Yarışmamız burada sona ermiştir.")
        else:
            print("Maalesef bilemediniz. Yarışmamız burada sona ermiştir.")
            print("Katıldığınız için teşekkürler...")








# elif kucuk_cevap0 in (0 or true_answer0):
#     if kucuk_cevap0 in 0 :
#         harf_alma(true_answer0)
#         yeni_cevap0 = input("\nCevabınız:")
#         if yeni_cevap0 == true_answer0:
#             tebrik()
#         else:
#             yanlis()
#     elif kucuk_cevap0 not in true_answer0:
#         yanlis() 
