# 1 perulangan
ulang = 15
for i in range(ulang):
    print("Perulangan ke-" + str(i))

# 2 perulangan list
simpan = [12, "udin petot", 14.5, True, 'A']
for item in simpan:
    print(item, end='. ')
# kalau integer engga usah pakai range

# 3 for didalam for
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} : {j} = {i / j}")
    print()
# pakai f supaya variabel bisa dipanggil di string tanpa harus keluar dari string

# 4 perulangan lompat
for i in range (1, 10, 2):
    print(i)

# 5 perulangan tidak berjumlah
jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print(f"Total perulangan: {hitung}")

# break
hitung = 0
while True:
    hitung += 1
    ulang = input("Masih Ingin Mengulang? ")
    if ulang == "tidak" or ulang =="Tidak":
        break
print(f"Total Perulangan: {hitung}")

# continue
print('Daftar bilangan ganjil dari 1-10')
for i in range(20):
    if i % 2 == 0:
        continue
print(i)