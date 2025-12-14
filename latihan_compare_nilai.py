absen_siswa=[1,2,3,4,5]
nama_siswa=["Christy","Cynthia","Nixie","Cathleen","Diana"]
nilai_mtk = [80, 90, 75, 85, 60]
nilai_bindo = [70, 60, 65, 75, 80]
nilai_inggris = [85, 80, 90, 70, 75]
nilai_fisika = [90, 85, 80, 95, 70]
total_nilai_siswa = []

a=0

for i in range( len(absen_siswa)):
    total= (nilai_mtk[i] + nilai_bindo[i] + nilai_inggris[i] + nilai_fisika[i])
    total_nilai_siswa.append(total)

    nilai_terbesar = total_nilai_siswa[0]
    nilai_terkecil = total_nilai_siswa[0]

    absen_siswa_nilai_terbesar = absen_siswa[0]
    absen_siswa_nilai_terkecil = absen_siswa[0]

    
    nama_siswa_nilai_terbesar = nama_siswa[0]
    nama_siswa_nilai_terkecil = nama_siswa[0]
    


for i in range( len(total_nilai_siswa)):
    #Mencari nilai terbesar
    current= total_nilai_siswa[i]

    if current > nilai_terbesar:
     nilai_terbesar = current
     nama_siswa_nilai_terbesar = nama_siswa[i]
     absen_siswa_nilai_terbesar = absen_siswa[i]
             
    #Mencari nilai terkecil
    elif current < nilai_terkecil:
        nilai_terkecil = current
        nama_siswa_nilai_terkecil = nama_siswa[i]
        absen_siswa_nilai_terkecil = absen_siswa[i]

    
print(f"Total nilai terbesar adalah: {nilai_terbesar} milik absen nomor: {absen_siswa_nilai_terbesar} yaitu {nama_siswa_nilai_terbesar}" )
print(f"Total nilai terkecil adalah: {nilai_terkecil} milik absen nomor: {absen_siswa_nilai_terkecil} yaitu {nama_siswa_nilai_terkecil}" )


















