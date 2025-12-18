# baris= input("Masukan besar baris matriks: ")
# kolom= input("Masukan besar kolom matriks: ")

# #Matriks dengan default value= 0
# matriks=[[0 for i in range(int(baris))] for j in range(int(kolom))]
# print(matriks)


# nilai_mtk =     [80, 90, 75, 85, 60]
# nilai_bindo =   [70, 60, 65, 75, 80]
# nilai_inggris = [85, 80, 90, 70, 75]
# nilai_fisika =  [90, 85, 80, 95, 70]

# nilai_siswa = [  nilai_mtk ,nilai_bindo ,nilai_inggris,nilai_fisika]

# print(nilai_siswa[3][1])


from fractions import Fraction

var_mat = [
    [1, 3, 5],
    [4, 9, -8],
    [3, 2, 7]
]


#FIND DETERMINANT 3x3 MATRIX
tambah= var_mat[0][0] * var_mat[1][1] * var_mat[2][2]+ var_mat[0][1] * var_mat[1][2] * var_mat[2][0]+ var_mat[0][2] * var_mat[1][0] * var_mat[2][1]
kurang= var_mat[0][2] * var_mat[1][1] * var_mat[2][0]+ var_mat[0][0] * var_mat[1][2] * var_mat[2][1]+ var_mat[0][1] * var_mat[1][0] * var_mat[2][2]
det= tambah - kurang
# print(det)



#TRANSPOSE MATRIX
var_t=[[0 for i in range(len(var_mat))] for j in range(len(var_mat))]

for i in range(len(var_mat)):
    # print(i)
    for j in range(len(var_mat)):
        # print(j)
        # print( var_mat[i])
        # print(var_mat[j])
        # print(var_mat[j][i], end=" ")
        var_t[i][j]= var_mat[j][i]
 


 #FIND ADJOIN MATRIX
rules= [[1,-1,1],
        [-1,1,-1],
        [1,-1,1]]

var_adjoin=[[0 for i in range(len(var_mat))] for j in range(len(var_mat))]
for i in range(len(var_mat)):
    for j in range(len(var_mat)):
        var_adjoin[i][j]= var_t[i][j] * rules[i][j]



#FIND INVERSE MATRIX
var_inv=[[0 for i in range(len(var_mat))] for j in range(len(var_mat))]
for i in range(len(var_mat)):
    for j in range(len(var_mat)):
        var_inv[i][j]= Fraction(1, det).limit_denominator() * var_adjoin[i][j]


print("Matriks awal:")
print(var_mat)
print("Matriks Transpose:")
print(var_t)
print("Matriks Adjoin:")
print(var_adjoin)
print("Matriks Inverse:")
print([[str(var_inv[i][j]) for j in range(len(var_mat))] for i in range(len(var_mat))])

