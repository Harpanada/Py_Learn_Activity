
from fractions import Fraction

var_mat = [
    [1, 2, 2],
    [2, 4, 3],
    [4, 7, 8]
]


#FIND DETERMINANT 3x3 MATRIX
def determinant_3x3(mat):
    tambah = (
        mat[0][0]*mat[1][1]*mat[2][2]
        + mat[0][1]*mat[1][2]*mat[2][0]
        + mat[0][2]*mat[1][0]*mat[2][1]
    )
    kurang = (
        mat[0][2]*mat[1][1]*mat[2][0]
        + mat[0][0]*mat[1][2]*mat[2][1]
        + mat[0][1]*mat[1][0]*mat[2][2]
    )
    return tambah - kurang

#FIND COFACTOR MATRIX
def minor(mat, row, col):
    return [
        [mat[i][j] for j in range(3) if j != col]
        for i in range(3) if i != row
    ]
def det2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]


rules= [[1,-1,1],
        [-1,1,-1],
        [1,-1,1]]

kof=[[0 for i in range(len(var_mat))] for j in range(len(var_mat))]
for row in range(len(var_mat)):
    for col in range(len(var_mat)):
       minor_matrix = minor(var_mat, row, col)
       kof[row][col]=det2x2(minor_matrix)*rules[row][col]
       

#ADJOIN MATRIX
adjoin=[[0 for i in range(len(var_mat))] for j in range(len(var_mat))]

for i in range(len(var_mat)):
    for j in range(len(var_mat)):
       
        adjoin[i][j]= kof[j][i]



# INVERS MATRIX
var_inv=[[0 for i in range(len(var_mat))] for j in range(len(var_mat))]
for i in range(len(var_mat)):
    for j in range(len(var_mat)):
        var_inv[i][j]= Fraction(1, determinant_3x3(var_mat)).limit_denominator() * adjoin[i][j]



print("Matriks awal:")
print(var_mat)
print("Matriks Adjoin:")
print(adjoin)
print("Matriks Inverse:")
print([[str(var_inv[i][j]) for j in range(len(var_mat))] for i in range(len(var_mat))])

