biodata = {
    'Nama': 'Azira',
    'Umur': 18,
    'NIM': 2409106016,
    'Jurusan': 'Informatika',
    'Angkatan': 2024
} 

print("""
    1. Tampilkan
    2. Tambah
    """)
pilihan  = input('Pilih opsi (1/2): ')

if pilihan == '1':
    for i, j in biodata.items():
        print(f'{i}: {j}')
elif pilihan == '2':
    nama = input('Masukkan nama: ')
    umur = input('Masukkan umur: ')
    nim = input('Masukkan nim: ')
    jurusan = input('Masukkan jurusan: ')
    angkatan = input('Masukkan angkatan: ')
else:
    print('Pilihan tidak valid.')

biodata[nama] = {
    'Umur': umur,
    'NIM': nim,
    'Jurusan': jurusan,
    'Angkatan': angkatan
    }
print(biodata)
