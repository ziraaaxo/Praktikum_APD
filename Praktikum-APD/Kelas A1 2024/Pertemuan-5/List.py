# A1 = ['Azira', 'Lian', 'Ayu']
# print(A1[2])

nama = ['Celio', 'shandy', 'farel', 'ghazali', 'vito']
print(type(nama))
print(nama[0:2])

# print(f'Sebelum = {nama}')

# menambahkan
# nama.append('azira')
# print(f'Sesudah = {nama}')
# nama.insert(2, 'afrizal')

# update
# nama[4] = 'fufufafa'

# hapus
# del nama[2]
# hapus = nama.pop(2)

# konsep step
print(nama[0:4:2])

# panggil index
print(nama[0:4])

# operasi dalam list ( + atau * )
matkul = ['APD', 'APL', 'BASDAT', 'STRUKDAT', 'WEB', 'JARKOM']
sesudah = nama + matkul
print(sesudah)

# nested list
data = ['farel', 'celio', [1,2,['halo', 23, 2.3, True]]]
print(data[2])
print(data[2][0])
print(data[2][2][0])
print(data[2][2][::-1])
print(data[-1])

# pakai perulangan
angka = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in angka:
    print(i)
    # print(i, end=' ')
    # for j in i:
    #     print(j)
    

