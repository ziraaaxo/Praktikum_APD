# penginputan jenis kelamin
print('''Pilih jenis kelamin anda
1. Pria
2. Wanita''')
jenisKelamin = input('Pilihan (1/2): ')

# penginputan data
beratBadan = float(input('Masukkan berat badan anda (dalam kg): '))
tinggiBadan = float(input('Masukkan tinggi badan anda (dalam cm): '))
umur = int(input('Masukkan umur anda: '))

# perhitungan bmr
if jenisKelamin == '1':
    bmr = (10 * beratBadan) + (6.25 * tinggiBadan) - (5 * umur) + 5
    print('BMR anda adalah ' + str(bmr))
elif jenisKelamin == '2':
    bmr = (10 * beratBadan) + (6.25 * tinggiBadan) - (5 * umur) - 161
    print('BMR anda adalah ' + str(bmr))
else:
    print('Pemilihan jenis kelamin tidak valid')

# penginputan level aktivitas
print('''Pilih level aktivitas harian anda
1. Aktivitas Ringan (Jarang Bergerak)                             
2. Aktivitas Sedang (Olahraga 1-3 kali seminggu) 
3. Aktivitas Berat (Olahraga 4-7 kali seminggu)''')                             
level_aktivitas_harian = input('Pilihan (1/2/3): ')

# penentuan nilai level aktivitas
if level_aktivitas_harian == '1':
    nilai_aktivitas = 1.25
elif level_aktivitas_harian == '2':
    nilai_aktivitas = 1.36
elif level_aktivitas_harian == '3':
    nilai_aktivitas = 1.72
else:
    print('Pemilihan level aktivitas tidak valid')

# perhitungan tdee
tdee = bmr * nilai_aktivitas
print(f"\nKebutuhan Kalori Harian Anda (TDEE) adalah: {tdee:.2f} kalori")