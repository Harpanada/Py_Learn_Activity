import math 

print("Cari Luas Dan Keliling Lingkaran")

pi=math.pi

def Keliling(r):
    result= 2*pi*r
    return result

def Luas(r):
    result = pi*r**2
    return result

resKeliling=Keliling(10)
print(resKeliling)

resLuas=Luas(10)
print(resLuas)

