def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang



def minimal(a,b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return a
    

min=minimal(1,0)
print(min)


