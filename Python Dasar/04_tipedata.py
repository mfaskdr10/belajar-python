# a = 10, a adalah variabel dengan nilai 10

# tipe data: angka satuan (integer)
data_integer = 1
print("data:", data_integer, "bertipe data:", type(data_integer))

# tipe data: angka desimal (float)
data_float = 1.5
print("data:", data_float, "bertipe data:", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "otong dan ucup"
print("data:", data_string, "bertipe data:", type(data_string))

# tipe data: biner true/false (boolean)
data_boolean = True
print("data:", data_boolean, "bertipe data:", type(data_boolean))

## tipe data khusus
# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

from ctypes import c_double
data_c_doubles = c_double(6)
print("data:", data_c_doubles, "bertipe data:", type(data_c_doubles))