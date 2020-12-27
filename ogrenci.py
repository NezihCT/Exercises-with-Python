# class ogrenci:
#     """
#     Bu alan zorunlu alan değildir, sadece __document__ 
#     metodunu print ettiğinizde size bu sınıf hakkında bu alana
#     ne yazdıysanız onu teslim eder.
#     """


# print(ogrenci.__doc__)

import socket

hostname = socket.gethostname()
print(hostname)
ip = socket.gethostbyname(hostname)
print(ip)
from datetime import datetime

class coreEntity():
    def __init__(self):
        self.createddate = datetime.now()
        self.cratedcomputername = socket.gethostname()
        self.cratedip = socket.gethostbyname("")

class category():
    
    categoryname = ""
    description = ""

class Product(coreEntity):
    
    Productname = ""
    UnitPrice = 0
    UnitsInstock = 0

product = Product()
print(product.createddate)