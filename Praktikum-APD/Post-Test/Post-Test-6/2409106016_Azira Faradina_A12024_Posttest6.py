# penyimpanan password
dict_password = {}
# penyimpanan akun untuk login
data_akun = {
     'admin': 'admin2024',
     'user1': 'user2024'
}
# menu utama
while True:
    print("""
    =======================
    |     MENU UTAMA      |
    =======================
    |    1. Login         |
    |    2. Registrasi    |
    |    3. Keluar        |
    =======================
    """)
    # sistem login
    pilihan = input('Pilih opsi (1/2/3): ')
    if pilihan == '1':
        print('\n=== Sistem Login ===')
        username = input('Masukkan username anda: ')
        password = input('Masukkan password anda: ')
        if username not in data_akun or data_akun[username] != password:
            print('Username atau password anda salah. Silahkan coba lagi.')
            continue
        peran = 'admin' if username == 'admin' else 'user'
        print(f'Berhasil Login. Anda masuk sebagai {peran}.')
            
        while True:
            if peran == 'admin':
                print("""
                ===============================
                |  Sistem Manajemen Password  |
                ===============================
                |    1. Tambah Password       |
                |    2. Lihat Password        |
                |    3. Update Password       |
                |    4. Hapus Password        |
                |    5. Logout                |
                ===============================
                """)
            else:
                print("""
                ===============================
                |  Sistem Manajemen Password  |
                ===============================
                |    1. Tambah Password       |
                |    2. Lihat Password        |
                |    3. Logout                |
                ===============================
                """)
            pilihan_user = input('Pilih opsi: ')
            # program jika pengguna adalah admin
            if peran == 'admin':
                # tambah password
                if pilihan_user == '1':
                    website = input('Masukkan nama website/platform: ')
                    username = input('Masukkan username: ')
                    password = input('Masukkan password: ')
                    dict_password[website] = {'username': username, 'password': password}
                    print(f'Password untuk {website} berhasil ditambahkan.')
                # lihat daftar password
                elif pilihan_user == '2':
                    if not dict_password:
                        print('Tidak ada password yang terdaftar.')
                    else:
                        print('Daftar password:')
                        for website, data in dict_password.items():
                            print(f'- {website}: {data['username']}: {data['password']}') 
                # update password
                elif pilihan_user == '3':
                    if not dict_password:
                        print('Tidak ada password yang terdaftar.')
                    else:
                        print('Daftar password: ')
                        for i, website in enumerate(dict_password.keys()):
                            print(f'{i + 1}. {website}')
                        website = input('Masukkan nama website atau platform yang ingin di-update: ')
                        if website in dict_password:
                            update_website = input('Apakah anda ingin mengupdate website/platform? (y/n): ')
                            if update_website == 'y':                
                                website_baru = input('Masukkan website atau platform baru: ')
                                dict_password[website_baru] = dict_password.pop(website)
                                website = website_baru
                            username_baru = input('Masukkan username baru: ')
                            password_baru = input('Masukkan password baru: ')
                            dict_password[website] = {'username': username_baru, 'password': password_baru}
                            print('Password berhasil diperbarui!')
                        else:
                            print('Website tidak ditemukan.')
                # hapus password 
                elif pilihan_user == '4':
                    if not dict_password:
                        print('Tidak ada password yang terdaftar.')
                    else:
                        for i, website in enumerate(dict_password.keys()):
                            print(f'{i + 1}. {website}')
                        website = input('Masukkan website/platform yang inigin dihapus: ')
                        if website in dict_password:
                            del dict_password[website]
                            print(f'Password untuk {website} berhasil dihapus.')
                        else:
                            print('Website tidak ditemukan.')
                # logout dari akun
                elif pilihan_user == '5':
                    print ('Berhasil Logout.')
                    break
                else: 
                    print('Pilihan anda tidak valid. Silahkan coba lagi.')

            # program jika pengguna adalah user biasa
            elif peran == 'user':
                # tambah password
                if pilihan_user == '1':
                    website = input('Masukkan website atau platform: ')
                    username = input('Masukkan username: ')
                    password = input('Masukkan password: ')
                    dict_password[website] = {'username': username, 'password': password}
                    print(f'Password untuk {website} berhasil ditambahkan.')
                # lihat password
                elif pilihan_user == '2':
                    if not dict_password:
                        print('Tidak ada password yang terdaftar.')
                    else:
                        print('Daftar password:')
                        for website, data in dict_password.items():
                            print(f'{website}: {data['username']}: {data['password']}')
                # logout dari akun
                elif pilihan_user == '3':
                    print('Berhasil Logout.')
                    break
                else:
                    print('Pilihan anda tidak valid. Silahkan coba lagi.')
   
    # registrasi akun baru
    elif pilihan == '2':
        print('\n=== Registrasi Pengguna Baru ===')
        while True:
            username = input('Masukkan username baru: ')
            if username in data_akun:
                print('Username sudah ada. Silahkan pilih username lain.')
                continue
            password = input('Masukkan password baru: ')
            if len(password) < 5:
                print('Password minimal 5 karakter. Silahkan coba lagi.')
            else:
                data_akun[username] = password
                print(f'Registrasi pengguna baru berhasil! {username} telah ditambahkan.')
                break
   
    # berhenti menggunakan program
    elif pilihan == '3':
        print('Terima kasih telah menggunakan program ini!')
        break
    else: 
        print('Pilihan tidak valid. Silahkan coba lagi.')