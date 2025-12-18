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

