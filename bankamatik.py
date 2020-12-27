import time
Hesaplar = [
    {
    'indexNo'         : 0,
    'Ad'            : 'Nezih Can',
    'Soyad'         : 'Turgut',
    'Bakiye'        : 5000,
    'Kart Numarası' : 123458,
    'Sifre'         : 12345
    },
    {
    'indexNo'         : 1,
    'Ad'            : 'Ata',
    'Soyad'         : 'Güzeler',
    'Bakiye'        : 4500,
    'Kart Numarası' : 123456,
    'Sifre'         : 54321
    }
]
giris_no = int(input("Kart Numaranızı giriniz:"))
giris_sifre = int(input("Şifrenizi giriniz:"))
print("\n")

i=0
while giris_sifre != Hesaplar[i]['Sifre']:
    i += 1

def bakiye_goster(hesap) :
    print(f"Sevgili {(hesap['Ad']),(hesap['Soyad'])}, {hesap['Kart Numarası']} kart numaralı hesabınızda {hesap['Bakiye']} ₺ bulunmaktadır.")
ek_hesap_limiti = 5000
ek_hesap_limiti1 = 5000
try:    
    if (giris_no) == int(Hesaplar[i]['Kart Numarası']):
        if (giris_sifre) == int(Hesaplar[i]['Sifre']):
            print(f"Sevgili {Hesaplar[i]['Ad']} {Hesaplar[i]['Soyad']}, hoşgeldiniz...")
            time.sleep(1.3), print("\n")
            print("""Yapmak istediğiniz işlemi seçiniz:
            1-Bakiye Öğren
            2-Şifre Değiştir
            3-Para Yatırma
            4-Para Çekme
            5-Para Transferi
            """)
            while True:
                secim = input("""
                    Ana menüye dönmek için 9'a basınız.
                    İşlemi bitirmek için 0'a basınız. """)
                print("")
                if int(secim) == 1:
                    print("\n")
                    bakiye_goster(Hesaplar[i])
                    print('\n')
                    time.sleep(1.3)
                elif int(secim) == 2:
                    mevcut_sifre = int(input("Mevcut şifrenizi giriniz:"))
                    if  Hesaplar[i]['Sifre'] == mevcut_sifre :
                        yeni_sifre = int(input("Oluşturmak istediğiniz şifreyi giriniz:"))
                        del Hesaplar[i]['Sifre']
                        Hesaplar[i]['Sifre'] = yeni_sifre
                        time.sleep(1.3)
                        print("")
                        print(f"Şifreniz başarıyla değiştirildi. Yeni şifreniz {Hesaplar[i]['Sifre']}")
                    else:
                        time.sleep(1.3)
                        print("Bilgiler uyuşmuyor.")
                        print("")
                elif int(secim) == 3:
                    tutar = int(input("Yatırmak istediğiniz tutarı giriniz (₺):"))
                    bakiye = int(Hesaplar[i]['Bakiye'])
                    Hesaplar[i]['Bakiye'] = bakiye + tutar
                    print("İşleminiz gerçekleştiriliyor...")
                    time.sleep(1.3), print("\n")
                    print(f"Yeni bakiye {Hesaplar[i]['Bakiye']}₺")
                elif int(secim) == 4:
                    tutar = int(input("Çekmek istediğiniz tutarı giriniz (₺):"))
                    if ((-tutar) + int(Hesaplar[i]['Bakiye']) >= 0):
                        bakiye = int(Hesaplar[i]['Bakiye'])
                        Hesaplar[i]['Bakiye'] = bakiye - tutar
                        print("İşleminiz gerçekleştiriliyor...")
                        time.sleep(1.3), print("\n")
                        print(f"Yeni bakiye {Hesaplar[i]['Bakiye']} ₺")
                    else:
                        ek_hesap=int(input("Ek hesap kullanılsın mı? Ek hesap limitiniz 5000 ₺.İşlem için (1/0)"))
                        if ek_hesap == 1:
                            (toplam) = (ek_hesap_limiti) + (int(Hesaplar[i]['Bakiye']))
                            (ek_hesap_limiti) = (toplam - tutar)
                            print("İşleminiz gerçekleştiriliyor...")
                            time.sleep(1.3), print("\n")
                            print(f"Kalan bakiye 0 ₺, kalan ek hesap bakiyesi {ek_hesap_limiti}₺")
                        elif ek_hesap == 0:
                            print("Bakiye yetersiz...")
                elif int(secim) == 5:
                    transfer = int(input("Transfer etmek istediğiniz tutarı giriniz (₺):"))
                    hesapNo = int(input("Transfer etmek istediğiniz hesabın kart numarasını giriniz:"))
                    j=0
                    while hesapNo != (Hesaplar[j]['Kart Numarası']):
                        j += 1
                    if transfer > Hesaplar[i]['Bakiye']:
                        ek_hesap1=int(input("Ek hesap kullanılsın mı? Ek hesap limitiniz 5000 ₺.İşlem için (1/0)"))
                        if ek_hesap1 == 1:
                            if (transfer - int(Hesaplar[i]['Bakiye']) < 5000):
                                (toplam) = (ek_hesap_limiti1) + (int(Hesaplar[i]['Bakiye']))
                                Hesaplar[j]['Bakiye'] += transfer
                                Hesaplar[i]['Bakiye'] -= transfer
                                print("")
                                print("İşleminiz gerçekleştiriliyor...")
                                time.sleep(1.3)
                                print("\n")
                                print(f"Transfer başarıyla gerçekleşti. Transfer edilen hesabın yeni bakiyesi {Hesaplar[j]['Bakiye']} ₺")
                                print("\n")                                
                                (ek_hesap_limiti1) = (toplam - transfer)
                                time.sleep(1.3), print("\n")
                                print(f"Kalan bakiye 0 ₺, kalan ek hesap bakiyesi {ek_hesap_limiti1}₺")
                            else:
                                print("Yetersiz bakiye...")
                        else:
                            print("Başka bir işlem seçiniz.")
                    elif transfer <= Hesaplar[i]['Bakiye']:
                        Hesaplar[j]['Bakiye'] += transfer
                        Hesaplar[i]['Bakiye'] -= transfer
                        print("")
                        print("İşleminiz gerçekleştiriliyor...")
                        time.sleep(1.3)
                        print("\n")
                        print(f"Transfer başarıyla gerçekleşti. Transfer edilen hesabın yeni bakiyesi {Hesaplar[j]['Bakiye']} ₺")
                        print("\n")
                        print(f"Transfer başarıyla gerçekleşti. Hesabın yeni bakiyesi {Hesaplar[i]['Bakiye']} ₺")                                                        
                elif int(secim) == 0:
                    break
                elif int(secim) == 9:
                    print("""Yapmak istediğiniz işlemi seçiniz:
            1-Bakiye Öğren
            2-Şifre Değiştir
            3-Para Yatırma
            4-Para Çekme
            5-Para Transferi
            """)
                    time.sleep(1.3), print("\n")
                    continue
                else:
                    print("Geçersiz işlem.")
    else:
        print("Bilgilerinizi doğru giriniz.") 
except: 
    print("Yanlış girdi. Yeniden deneyiniz.")




# print(f"Sevgili {Hesaplar[i]['Ad']} {Hesaplar[i]['Soyad']}, hoşgeldiniz...")

# print("""

# """)
# print(Hesaplar[i])

# mevcut_sifre = int(input("Mevcut şifrenizi giriniz:"))
# if giris_sifre == mevcut_sifre :
#     yeni_sifre = int(input("Oluşturmak istediğiniz şifreyi giriniz:"))
#     del Hesaplar[i]['Sifre']
#     Hesaplar[i]['Sifre'] = yeni_sifre
#     print(f"Şifreniz başarıyla değiştirildi. Yeni şifreniz {Hesaplar[i]['Sifre']}")
# else:
#     print("Bilgiler uyuşmuyor.")

