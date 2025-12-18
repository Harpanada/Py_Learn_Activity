var_array = [i for i in range(101)]

for i in range(len(var_array)):
    jumlah=var_array[0]
    for j in range(i+1):
        jumlah += var_array[j]

rata_rata=jumlah/len(var_array)
print(f"Rata-rata dari 0 sampai 100 adalah: {rata_rata}")


var_arr= [0 for i in range(10)]
print(var_arr)


