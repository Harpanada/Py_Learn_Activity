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

import unittest








#Super Usage
class Mobil:
    def __init__(self, warna, merek, kecepatan,hambatan_udara):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        self.hambatan_udara = hambatan_udara

    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10
    
    def info(self):
        print(f"Kondisi Jalan: Licin. Kecepatan Mobil: {self.kecepatan} km/h. Kecepatan Disarankan: 60 km/h. ")


def aeroDynamicStatus(AeroAct):
    if AeroAct:
        print("[Aerodynamic Actived]")
    else:
        print("[Aerodynamic Deactived]")

def turboStatus(TurboAct):
    if TurboAct:
        print("[Turbo Actived]")
    else:
        print("[Turbo Deactived]")




class MobilSport(Mobil):


    def turbo(self):
        self.kecepatan += 50
        
     #tambah_kecepatan
    def tambah(self):  
        print("Kecepatan ditingkatkan, hati-hati!")
        #Super, for call a method from parent class
        super().tambah_kecepatan()  #Memanggil metode dari kelas induk

    def aeroDynamic(self):
        efect=self.hambatan_udara - 5
        return efect
        



class TestMobilSport(unittest.TestCase):
    #Test case 1
    def test_turbo(self):
        carTester=MobilSport("Merah","AstonMartin",250,10)
        carTester.turbo()
        self.assertEqual(carTester.kecepatan,300)

    def test_aeroDynamic(self):
        carTester=MobilSport("Merah","AstonMartin",250,10)
        self.assertNotEqual(carTester.aeroDynamic(),carTester.hambatan_udara)
        



if __name__ == "__main__":
    # Test Runner
    unittest.main()