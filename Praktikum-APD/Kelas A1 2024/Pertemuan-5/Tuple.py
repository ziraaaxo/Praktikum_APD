nama = ('farrel', 'vito', 'shandy', 'rijal')
print(nama[1])
# tupple tidak dinamis, tidak bisa ditambahkan/dikurangin

# tuple di dalam tuple
nama1 = ('azira', 'ayu', 'triya', 'nabila')
nama2 = nama + nama1
print(nama2)

# unpacking
mahasiswa = (69, 'infromatika', '2209106044', 'aldy septian')
absen, prodi, nim, nama = mahasiswa
print(nim)

print(
"""
=========================
|   DATA MAHASISWA A24  |
=========================
|    1. TAMBAH DATA     |
|    2. TAMPILKAN DATA  |
|    3. UBAH DATA       |
|    4. HAPUS DATA      |
|    5. KELUAR          |
=========================
"""
) 
data_mahasiswa = []
while True:
    pilih = int(input('Pilih: '))
    if pilih == 1:
        nama = input('Masukkan nama anda: ')
        nim = input('Masukkan NIM anda: ')
        kelas = input('Masukkan kelas anda: ')
        data_mahasiswa.append([nama, nim, kelas])
    elif pilih == 2:
        for data in data_mahasiswa:
            for i in range(len(data)):
                print(f'\n Data Mahasiswa ke-{i+1}\n nama: {data[i][0]}\n nim: {data[i][1]}\n kelas: {data[i][2]}')
    elif pilih == 3:
        nama_lama = input('Masukkan nama lama: ')
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input('Masukkan nama anda: ')
                nim_baru = input('Masukkan NIM anda: ')
                kelas_baru = input('Masukkan kelas anda: ')
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print('Terima kasih telah menggunakan program ini!')
        break
    else:
        print('Anda salah')