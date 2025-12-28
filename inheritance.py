# #Inheritence (Pewarisan)
# class dataStudent:
#     def __init__(self,name,clas,birth,idnum):
#         self.name=name
#         self.clas=clas
#         self.birth=birth
#         self.idnum=idnum
    


# class getStudent(dataStudent):
#     def showData(self):
#         print("--DATA STUDENT--")
#         print(f"Name         :   {self.name}") 
#         print(f"Class        :   {self.clas}") 
#         print(f"Birth        :   {self.birth}") 
#         print(f"Id Number    :   {self.idnum}") 

# christy=getStudent("Angelina Christy", "IX-2", "5 DEC 2005",123)
# nixie=getStudent("Cathleen Nixie", "IX-1", "28 MAY 2009",112)
# vans=getStudent("Liyovan Harpanada","IX-F2A","13 MAY 2009",221)
# christy.showData()
# nixie.showData()
# vans.showData()



#Super Usage
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10
    
    def info(self):
        print(f"Kondisi Jalan: Licin. Kecepatan Mobil: {self.kecepatan} km/h. Kecepatan Disarankan: 60 km/h. ")

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah(self):     # tambah_kecepatan
        print("Kecepatan ditingkatkan, hati-hati!")
        #Super, for call a method from parent class
        super().info()  # Memanggil metode info dari kelas induk
        super().tambah_kecepatan()  # Memanggil metode dari kelas induk

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

"""
Output:
160
180
"""