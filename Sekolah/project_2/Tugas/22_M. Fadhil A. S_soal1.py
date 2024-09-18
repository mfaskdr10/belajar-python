inp_usia = int(input("Masukkan usia anda: "))

if inp_usia <= 12:
  print("Anak-Anak")
elif inp_usia >= 13 and inp_usia <= 19:
  print("Remaja") 
else:
  print("Dewasa")