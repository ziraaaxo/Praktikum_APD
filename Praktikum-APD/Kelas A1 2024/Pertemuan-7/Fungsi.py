# fungsi tanpa parameter
def nama_fungsi():
    print('Ini adalah fungsi di Python')
nama_fungsi()

# fungsi dengan parameter
# def fungsi(parameter):
#     print(parameter)
# fungsi(parameter)

# membuat fungsi dengan parameter (sisi)
def luas_persegi(sisi):
    luas = sisi * sisi
    print(f'Luas persegi adalah: {luas}')
# memanggil fungsi luas_persegi
luas_persegi(10) # ini langsung keluar output

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
luas = luas_persegi(2) # variabel global
print(luas_persegi(10))
# print(luas)

# variabel global
nama = 'azira'
matkul = 'English'

# variabel lokal
def info():
    nama = 'nuno'
    matkul = 'apd'
    # mengakses variabel lokal
    print('Nama saya adalah', nama)
    print('Matkul yang saya senangi adalah', matkul)
# mengakses variabel global
print('Nama saya adalah', nama)
print('Matkul yang saya senangi adalah', matkul)
# memanggil fungsi info
info()

# program menggunakan fungsi
# menampilkan semua data
password = []
def show_data():
    if len(password) <= 0:
        print('Belum ada data yang tersimpan.')
    else:
        print('Indeks', 'Password')
        for i in range(len(password)):
            print(i, password(i))
# fungsi untuk menambah data
def insert_data():
    password_baru = input('Masukkan password anda: ')
    password.append(password_baru)
# fungsi untuk edit data
def edit_data():
    show_data()
    i = input('Masukkan index: ')
    if(i >= len(password) or i < 0):
        print('ID salah.')
    else:
        password_edit = input('Password baru: ')
        password[i] = password_edit
# fungsi untuk menghapus data
def delete_data():
    show_data()
    i = input('Masukkan ID buku: ')
    if(i >= len(password) or i < 0):
        print('ID salah.')
    else:
        password.remove(password[i])

# fungsi untuk menampilkan menu
def show_menu():
    print("""\n
    ===========================
    |          Menu           |
    ===========================
    |     1. Tampilkan data   |
    |     2. Tambah data      |
    |     3. Edit data        |
    |     4. Hapus data       |
    |     5. Keluar           |
    ===========================
    """)
    menu = input('Pilih menu: ')
    print('\n')
    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print ("Salah pilih!")
# membuat main loop program
if __name__== '__main__':
    while(True):
        show_menu()