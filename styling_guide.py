# class Kalkulator:
#     """kalkulator tambah kurang"""

#     def __init__(self, _i):
#         self.i = _i

#     #Anotasi Fungsi
#     def tambah(
#         self, _i: float
#     ) -> float:  #Menambahkan informasi tipe data di parameter dan return   
#         return self.i + _i

#     def kurang(
#         self, _i: float
#     ) -> float:  #Menambahkan informasi tipe data di parameter dan return   
#         return self.i - _i


# #Contoh Penggunaan
# hasil = Kalkulator(10.0).tambah(5.0)
# print(hasil)


# #Anotasi fungsi di gabung dengan nilai parameter
# def perkalian(a: int = None, b: int = None) -> int:
#     return a * b


# print(perkalian(3, 4))



class user:
        #Pricate Method
    def __password(self):
        print("User1_1234.")

        #Public Method
    def akses_password(self,namaUser):
        if namaUser == "user1":
            return self.__password()
        else:
            raise Exception("akses ditolak")

user1 = user()
pw=user1.akses_password("use1")  #Tidak disarankan mengakses method private secara langsung  
print(pw)