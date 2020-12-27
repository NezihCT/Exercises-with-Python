import math as m
log = m.log10
ln = m.log
cos = m.cos
sin = m.sin
e = m.e
pi = m.pi
tan = m.tan
degree = m.radians
rad = m.degrees
faktor = m.factorial
karekok = m.sqrt
ebob = m.gcd
üs = m.pow
asin = m.asin
acos = m.acos
atan = m.atan
x=1
try:
    while x != 'exit':
        print("=> Çıkış için 'exit' yazınız.\n=> Komutları öğrenmek için 'help' yazınız.")
        x = eval(input(">> "))
        if x == 'help':
            print("""
            log     = Verilen sayının 10 tabanında logaritmasını hesaplar. ( log(10) = 1 )
            ln      = Birinci değerin ikinci değere göre logaritmasını hesaplar. ( ln(25,5) = 2 ) 
            cot     = cosinüs / sinüs
            sec     = 1 / cos
            cosec   = 1 / sin
            faktor  = Verilen sayının faktöriyelini hesaplar. ( faktor(5) = 120 )
            karekok = Verilen sayının karekökünü hesaplar. ( karekok(16) = 4 )
            ebob    = Verilen iki sayının en büyük ortak bölenini bulur. ( ebob(45,70) = 5 )
            üs      = Birinci sayının ikiye göre kuvvetini alır. ( üs(2,5) = 32 )
            pi      = pi sayısını tutan değişken. Değeri: 3.141592….
            e       = euler sabitini tutan bir değişken. Değeri: 2.718281… 
            
            *** Trigonometrik değerlerde doğru yazım şekli aşağıdaki gibidir:
            
            sin(degree(30)) = 0.5
            cos(degree(60)) = 0.5
            
            """)
        else:
            print(x)
            print("")
            print("")
except:
    print("Tanımsız.")
