# import matplotlib.pyplot as plt
 
# # Data
# semester = [1, 2, 3, 4, 5]
# nilai = [80, 79, 81, 82, 85]
 
# # Membuat plot garis
# plt.plot(semester, nilai)
 
# # Menambahkan judul dan label sumbu
# plt.title("Rata-Rata Nilai Ujian Siswa Per Semester")
# plt.xlabel("Semester")
# plt.ylabel("Nilai Rata-Rata")
 
# # Menampilkan plot
# plt.show()


#Mathplotlib dan seabor
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Contoh data
# tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
datas={
    'nilai' :[80, 79, 81, 82, 85],
    'semester': [1,2,3,4,5]
}

df=pd.DataFrame(datas)
# Contoh plot histogram
sns.barplot(data=df, x='semester',y='nilai')
plt.title('Nilai Siswa')
plt.xlabel('Semester')
plt.ylabel('Nilai')
plt.show()

