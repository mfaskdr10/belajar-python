def main():
    # Meminta pengguna memasukkan nilai mata pelajaran
    nilai_input = input("Masukkan nilai mata pelajaran (pisahkan dengan koma): ")
    
    # Mengubah string input menjadi list of float
    nilai_list = [float(nilai) for nilai in nilai_input.split(',')]
    
    # Menghitung rata-rata nilai
    rata_rata = sum(nilai_list) / len(nilai_list)
    
    # Menentukan kategori nilai berdasarkan rata-rata
    if rata_rata >= 90:
        kategori = "Sangat baik"
    elif rata_rata >= 75:
        kategori = "Baik"
    elif rata_rata >= 60:
        kategori = "Cukup"
    else:
        kategori = "Perlu perbaikan"
    
    # Menampilkan hasil
    print(f"Rata-rata nilai: {rata_rata}")
    print(f"Kategori nilai: {kategori}")

# Menjalankan program
main()
