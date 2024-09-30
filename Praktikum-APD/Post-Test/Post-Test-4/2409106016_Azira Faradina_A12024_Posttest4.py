# fitur login
percobaan = 0
login = False

while percobaan < 3:
    username = input('Masukkan username anda (huruf kecil): ')
    password = input('Masukkan password anda (tanpa 0): ')
    if username == 'azira' and password == '16':
        print(f'Berhasil login. Selamat datang, {username}')
        login = True
        break
    else:
        print('Username atau password anda salah. Silahkan coba lagi')
        percobaan += 1
if not login:
    print('Percobaan login gagal 3 kali. Program dihentikan.')
else:
    while True:
        # penginputan jenis kelamin
        print('''Pilih jenis kelamin anda
        1. Pria
        2. Wanita''')
        jenisKelamin = input('Pilihan (1/2): ')

        if jenisKelamin not in ['1', '2']:
            print('Pemilihan jenis kelamin tidak valid, silahkan coba lagi.')
            continue

        # penginputan data
        beratBadan = float(input('Masukkan berat badan anda (dalam kg): '))
        tinggiBadan = float(input('Masukkan tinggi badan anda (dalam cm): '))
        umur = int(input('Masukkan umur anda: '))

        # perhitungan bmr
        if jenisKelamin == '1':
            bmr = (10 * beratBadan) + (6.25 * tinggiBadan) - (5 * umur) + 5
            print('BMR anda adalah ' + str(bmr))
        else:
            bmr = (10 * beratBadan) + (6.25 * tinggiBadan) - (5 * umur) - 161
            print('BMR anda adalah ' + str(bmr))

        # penginputan level aktivitas
        print('''Pilih level aktivitas harian anda
        1. Aktivitas Ringan (Jarang Bergerak)
        2. Aktivitas Sedang (Olahraga 1-3 kali seminggu) 
        3. Aktivitas Berat (Olahraga 4-7 kali seminggu)''')                             
        level_aktivitas_harian = input('Pilihan (1/2/3): ')

        if level_aktivitas_harian not in ['1','2', '3']:
            print('Pemilihan level aktivitas harian tidak valid. Silahkan coba lagi.')
            continue

        # penentuan nilai level aktivitas
        if level_aktivitas_harian == '1':
            nilai_aktivitas = 1.25
        elif level_aktivitas_harian == '2':
            nilai_aktivitas = 1.36
        else: 
            nilai_aktivitas = 1.72

        # perhitungan tdee
        tdee = bmr * nilai_aktivitas
        print(f"\nKebutuhan Kalori Harian Anda (TDEE) adalah: {tdee:.2f} kalori")

        # User memilih berhenti atau tidak
        berhenti = input('Apakah anda ingin berhenti menghitung?: ')
        if berhenti == 'ya' or berhenti == 'Ya':
            print('Terima kasih telah menggunakan program ini. Have a nice day!')
            break