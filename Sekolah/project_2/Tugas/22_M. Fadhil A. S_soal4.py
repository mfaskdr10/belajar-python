def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

print(is_prima(5))

def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []

  for y in range(awal, akhir + 1):
    if is_prima(y):
      list_bilangan_prima.append(y)

  return list_bilangan_prima

print(cari_bilangan_prima(2, 12))