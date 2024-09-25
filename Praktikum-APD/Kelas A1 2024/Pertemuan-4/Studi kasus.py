# Buatlah program perulangan while yang menjumlahkan semua inputan integer positif,
# jika diinput negatif maka program berhenti! #

total = 0
while True:
    angka = int(input('Masukkan angka postif atau angka negatif: '))
    if angka < 0:
        break
    total += angka 
print(f'Total jumlah angka positif: {total}')

# ada variavbel i dimuali dari 1 sampai 20 lompatan 3
# kalau ada yang dimodulus 2 sama dengan 0, maka di cont

for i in range (1, 20, 3):
    if i % 2 == 0:
        continue
    print(i)
