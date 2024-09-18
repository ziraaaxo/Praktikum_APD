jumlahBuku = int(input('Masukkan pembelian buku: '))
totalHarga = int(input('Masukkaan total belanja: '))
if jumlahBuku < 5:
    print('Pembelian minimal 5 buku.')
elif totalHarga >= 100000:
    print ('Mendapat diskon sebesar 20%')
else:
    print('Total belanja minimal 100000')

