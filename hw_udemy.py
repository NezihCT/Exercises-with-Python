def cift (sayi):
    if (sayi % 2 == 0):
        return sayi
    else:
        raise ValueError

print("İçinde tek ve çift sayıların bulunduğu bir liste oluşturalım.")
adet = int(input("Kaç adet sayı girmek istersin:"))
liste = []
i = 0
while i < adet :
    sayi1 = int(input(""))
    liste.append(sayi1)
    i += 1
print("")
j = 0
print("Listenin içindeki çift sayılar ise aşağıdaki gibidir.")
for j in liste:
    try:        
        print(cift(j))
    except ValueError:
        pass

