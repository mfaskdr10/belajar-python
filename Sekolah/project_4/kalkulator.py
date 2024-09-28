# fungsi penjumlahan
def penjumlahan(a, b):
  return a + b
# fungsi pengurangan
def pengurangan(a, b):
  return a - b
# fungsi perkalian
def perkalian(a, b):
  return a * b
def pembagian(a, b):
  return a / b

while True:
  print(30*"=")
  print("Kalkulator Sederhana - mfaskdr10")
  print(30*"=")

  print("1. Penjumlahan")
  print("2. Pengurangan")
  print("3. Perkalian")
  print("4. Pembagian")
  print("5. Keluar")

  operator = ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]

  pilihan_user = int(input("Masukkan pilihan anda: "))

  if pilihan_user in (1, 2, 3, 4):
    angka_1 = float(input("Masukkan angka pertama: "))
    angka_2 = float(input("Masukkan angka kedua: "))
    print(10*"=")
    if(pilihan_user == 1):
      print("Jawabannya adalah:", penjumlahan(angka_1, angka_2))
      print("\n")
    elif(pilihan_user == 2):
      print("Jawabannya adalah:", pengurangan(angka_1, angka_2))
      print("\n")
    elif(pilihan_user == 3):
      print("Jawabannya adalah:", perkalian(angka_1, angka_2))
      print("\n")
    elif(pilihan_user == 4):
      print("Jawabannya adalah:", pembagian(angka_1, angka_2))
      print("\n")
  elif(pilihan_user == 5):
      break
  else:
    print("Pilihan tidak valid")
    print("\n")
    
  


