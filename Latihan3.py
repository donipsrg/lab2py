# masukan atau input nilai variabel a dan b
a = input("masukkan nilai a: ")
b = input("masukan nilai b: ")

# manampilkan isi variabel a dan b yang sudah di input sebelumnya
print("variabel a =",a)
print("variabel b =",b)

print("peggabungan {0} & {1} = ".format(a, b) + (a + b))

# mengkonversi nilai variabel ke integer dengan method int()
a = int(a)
b = int(b)

# menampilkan hasil pemjumlahan dari a + b
print("hasil penjumlahan {0} + {1} = %d".format(a, b ) % (a+b))

# menampilkan hasil pembagian dari a / b
print("hasil penbagian {0} / {1} = %d".format(a, b ) % (a/b))

# menampilkan hasil perkalian dari a * b
print("hasil perkalian {0} * {1} = %d".format(a, b ) % (a*b))
