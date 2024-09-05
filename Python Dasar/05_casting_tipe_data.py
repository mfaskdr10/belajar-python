# Casting tipe data adalah merubah dari satu tipe data ke tipe data yang lain

data_int = 10
print("Data =", data_int,", tipe:", type(data_int))

data_float = float(data_int) # merubah tipe data integer menjadi float
print("Data =", data_float,", tipe:", type(data_float))

data_str = str(data_int) # merubah tipe data integer menjadi string
print("Data =", data_str,", tipe:", type(data_str))

# Jika integer bernilai 0 maka akan menghasilkan boolean false
# Jika integer bernilai selain 0 maka akan menghasilkan boolean true
data_bool = bool(data_int) # merubah tipe data integer menjadi boolean
print("Data =", data_bool,", tipe:", type(data_bool))

