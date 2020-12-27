print("""
******************************


Telefon Rehberine Hoşgeldiniz


******************************
""")

a=3
i=0
j=1
k=2
l=3
rehber = []
while True:
# 5 fonksiyon (ekle,çıkar,görüntüle,değiştir,ara). Seçim için input al.
    islem  = int(input("""Yapmak istediğiniz işlemi seçiniz:
1. Yeni Kayıt Ekleme
2. Kayıt Silme
3. Kayıt Listesi Görüntüleme
4. Kaydı Değiştir
5. Kaydı Ara
6. Çıkış
"""))
#ilk fonksiyon kullanıcı eklemek.
    if islem == 1:
        rehber.append(input("İsim: "))
        rehber.append(input("Soyisim: "))
        rehber.append(input("Mail: "))
        rehber.append(input("Telefon Numarası: "))
        uzunluk=len(rehber)
#sağlama amaçlı her bloğa print ekledik
        print(rehber)
#ikinci fonksiyon kayıt silmek        
    elif islem == 2:
        print("Silmek istediğiniz kişinin bilgilerini giriniz.")
        rehber.remove(input("İsim: "))
        rehber.remove(input("Soyisim: "))
        rehber.remove(input("Mail: "))
        rehber.remove(input("Telefon Numarası: "))
        print(rehber)
#üçüncü fonksiyon kayıt listesi görüntülemek
    elif islem == 3:
        while l < (uzunluk):
            print("İsim            : ",rehber[i])
            print("Soyisim         : ",rehber[j])
            print("Mail            : ",rehber[k])
            print("Telefon Numarası: ",rehber[l])
            i=i+4
            j=j+4
            k=k+4
            l=l+4
#dördüncü fonksiyon kaydı değiştirmek
    elif islem == 4:
        print("Değiştirmek istediğiniz kişinin bilgilerini giriniz.")
        rehber.remove(input("İsim: "))
        rehber.remove(input("Soyisim: "))
        rehber.remove(input("Mail: "))
        rehber.remove(input("Telefon Numarası: "))
        print("Güncellenmek istediğiniz bilgileri giriniz.")
        rehber.append(input("İsim: "))
        rehber.append(input("Soyisim: "))
        rehber.append(input("Mail: "))
        rehber.append(input("Telefon Numarası: "))
        print(rehber)
#beşinci fonksiyon kaydı aramak
    elif islem == 5:
        metin = input("Aramak istediğiniz kullanıcının ismini giriniz: ")
        if metin in rehber:
            sayi = rehber.index(metin)
            sayi4=sayi+4
            print(rehber[sayi:sayi4])
        else:
            print("Böyle bir kullanıcı kaydı bulunmamaktadır.")
#altıncı fonksiyon çıkış
    elif islem == 6:
        break
    else:
        print("Yanlış sayı girdiniz.")
