
# Program Daftar Belanja Menggunakan Dictionary

def tampilkan_daftar_belanja(daftar_belanja):
    if not daftar_belanja:
        print("\nDaftar belanja kosong.")
    else:
        print("\nDaftar belanja:")
        for item, jumlah in daftar_belanja.items():
            print(f"- {item}: {jumlah}")

def tambah_barang(daftar_belanja):
    barang = input("Masukkan nama barang: ").strip()
    jumlah = int(input(f"Masukkan jumlah untuk {barang}: "))
    
    if barang in daftar_belanja:
        daftar_belanja[barang] += jumlah
    else:
        daftar_belanja[barang] = jumlah
    
    print(f"{barang} berhasil ditambahkan dengan jumlah {jumlah}.")

def hapus_barang(daftar_belanja):
    barang = input("Masukkan nama barang yang akan dihapus: ").strip()
    
    if barang in daftar_belanja:
        del daftar_belanja[barang]
        print(f"{barang} berhasil dihapus dari daftar belanja.")
    else:
        print(f"{barang} tidak ada dalam daftar belanja.")

def main():
    daftar_belanja = {}
    
    while True:
        print("\n=== Menu Daftar Belanja ===")
        print("1. Tampilkan Daftar Belanja")
        print("2. Tambah Barang")
        print("3. Hapus Barang")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4): ").strip()
        
        if pilihan == '1':
            tampilkan_daftar_belanja(daftar_belanja)
        elif pilihan == '2':
            tambah_barang(daftar_belanja)
        elif pilihan == '3':
            hapus_barang(daftar_belanja)
        elif pilihan == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

main()

