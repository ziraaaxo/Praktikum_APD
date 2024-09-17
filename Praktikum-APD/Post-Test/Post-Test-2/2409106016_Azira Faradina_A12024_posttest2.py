# penginputan data
print('Program Pengisian Biodata Mahasiswa')
namaLengkap = input('Masukkan nama lengkap anda: ')
namaPanggilan = input('Masukkan nama panggilan anda: ')
nim = input('Masukkan NIM anda: ')
prodi = input('Masukkan Program Studi anda: ')
umur = int(input('Masukkan umur anda: '))
bb = float(input('Masukkan berat badan anda (dalam kg): '))
tb = float(input ('Masukkan tinggi badan anda (dalam cm): '))
asalKota = input('Masukkan asal kota anda: ')
hobi = input('Masukkan hobi anda: ')
citaCita = input('Masukkan cita-cita anda: ')

# angka nim terakhir
a = int(nim[8:10])
modNim = a % 6

# inputan menjadi kalimat
print('Nama saya ' + namaLengkap + ', biasa dipanggil ' + namaPanggilan, end='', flush=True)
print('. NIM saya adalah ' + nim + '. Saya berasal dari Program Studi ' + prodi + '.')
print('Saya berumur ' + str(umur) + ' tahun. Berat badan saya adalah ' + str(bb) + ' kg dan tinggi badan saya ' + str(tb) + ' cm.')
print('Saya berasal dari ' + asalKota + '. Hobi saya adalah ' + hobi + '. Di masa depan saya ingin menjadi ' + citaCita + '. ' + str(modNim))