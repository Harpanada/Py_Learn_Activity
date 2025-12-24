def fungsiPangkat(a,b):
    """
    This function used for exponentiation operations of a number.
    
    Args:
    a(int): Base number to be raised to the power of b.
    b(int): Exponent value for a .

    Returns:
    int: Result of base number (a) raised to the power of exponent value (b).
    """
    pangkat= a**b
    return pangkat


a=2
b=3
pangkatkan=fungsiPangkat(a=a,b=b)
print(f'Hasil dari {a} dipangkatkan {b} adalah {pangkatkan}')


#Postitional only parameter
def penjumlahan(a, b, /):
    return a+b

tambah=penjumlahan(2, 3)
print(tambah)

#Keyword only parameter
def pengurangan(*, a, b):
    return a-b

minus= pengurangan(a=10, b=5)
print(minus)


#Var Positional
def perkalian(*args):
    hasil = 1
    for num in args:
        hasil *= num
    return hasil

hasil_kali = perkalian(2, 3, 4,5,6,7,8,9)
print(hasil_kali)

#Var Key 
def InfoNya(**kwargs):
    info=""
    for key, value in kwargs.items():
        info += f"{key}: {value}\n"
    return info

siswa=["Christy","Cathleen","Nixie","Luna"]
hobi=["Bernyanyi","Menari","Berenang","Tidur"]
usia=[19,17,16,21]

print(f"\n")
for i in range(len(siswa)):
    print(InfoNya(Nama=siswa[i],Usia=usia[i],Hobbi=hobi[i]))

