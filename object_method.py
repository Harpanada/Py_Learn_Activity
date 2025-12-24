#Object Method
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
    
    def rem(self):
        self.kecepatan -=20
    
    def stop(self):
        self.kecepatan=0

mobil_1=Mobil("Hitam","BMW M4",120)
print(f"{mobil_1.merek} {mobil_1.warna} {mobil_1.kecepatan} km/h")
mobil_1.tambah_kecepatan()
print(f"{mobil_1.merek} {mobil_1.warna} {mobil_1.kecepatan} km/h")
mobil_1.rem()
print(f"{mobil_1.merek} {mobil_1.warna} {mobil_1.kecepatan} km/h")
mobil_1.stop()
print(f"{mobil_1.merek} {mobil_1.warna} {mobil_1.kecepatan} km/h")