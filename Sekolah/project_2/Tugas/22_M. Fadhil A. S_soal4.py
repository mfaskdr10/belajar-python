r1 = int(input("Masukkan Rentang Angka Pertama = ")) # Memasukkan input rentang angka pertama
r2 = int(input("Masukkan Rentang Angka Terakhir = ")) + 1 # Memasukkan input rentang angka kedua, +1 ini berfungsi ketika kita ingin memanggil list_prima. Maka akan menampilkan bilangan sebelum inputan
list_prima = [] # Untuk memanggil bilangan prima nantinya

for p in range (r1, r2) : # p dalam range rentang 1 dan rentang 2
    if p > 2 : # 1 dan 2 bukan  bilangan prima, karena pasti habis dibagi 1 dan 2
        a = 1
        b = 0
        while p > a :
            if p % a == 0 : 
                b += 1
            a += 1
        if b == 1 :
            list_prima.append(p)
print(f"Susunan Bilangan Prima yang didapat berjumlah {len(list_prima)} bilangan")

while True:
    n = input("Apakah Anda Ingin Melihat Susunan Bilangan Primanya (y/n) = ")
    if n == "y":
        print(f"Bilangan Primanya Terdiri Dari {list_prima}")
        print("Program telah Selesai")
        break
    elif n == "n":
        print("Program telah Selesai")
        break
    else: 
        print("Piihan Anda Tidak Valid")