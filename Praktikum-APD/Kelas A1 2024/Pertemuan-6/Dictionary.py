daftar_buku = {
    "Buku1": "Harry Potter",
    "Buku2": 'Gone Girl',
    "Buku3": 'Poppy War'
}
print(daftar_buku['Buku1'])

nama_dict = {
"key": "value"
}
print(nama_dict["key"])

biodata = {
    'Nama': 'Azira Faradina',
    'NIM': '2409106016',
    'KRS': ['APD', 'PTI', 'ENGLISH'],
    'Mahasiswa Aktif': True,
    'Social Media': {
        'Intagram': '@azirabfr',
        'twitter': '@ziraaaxo'
    }
}

# cara ke dua membuat dictionary
games = dict(Sekiro = "Action", Pokemon = "Adventure",
Valorant = "FPS")
print(games)

# memanggil data di dalam dictionary
print(biodata['KRS'][1])

# pakai fungsi get
print(biodata.get('Nama'))
print(biodata.get('Alamat', 'Kosong'))

# perulangan
for i in biodata:
    print(i) # hanya print q

for i, j in biodata.items():
    print(f'{i}: {j}')

for i in biodata:
    print(biodata[i])

# menambahkah item pada dictionary
film = {
    "Avenger Endgame" : "Action",
    "Sherlock Holmes" : "Mystery",
    "The Conjuring" : "Horror"
    }
print(film) #Sebelum Ditambah
film['Zombieland'] = 'Comedy'
film.update({'Hours': 'Thriller'})
print(film) # setelah ditambah

# menghapus item pada dictionary
# cara 1
print(film) # sebelum dihapus
del film['The Conjuring']
print(film) # setelah dihapus

# cara 2
hapus = film.pop('Avenger Endgame')
print(film)
print(f'Key yang dihapus = {hapus}')

# cara 3
print(film) # sebelum dihapus
film.clear()
print(film) # setelah dihapus

# fungsi yang bisa dipakai
# mengetahui panjang
data = {
"Nama" : "Azira",
"Umur" : 18,
"Jurusan" : "Informatika"
}
print("Jumlah Data = ", len(data))

# copy
buku = {
    'No Longer Human': 'Osamu Dazai',
    'Harry Potter': 'J. K. Rowlings',
    'Hamlet': 'William Shakespeare'
}
pinjam = buku.copy()
print("Dictionary yang Telah Disalin : ", pinjam)

#fromkeys
key = 'apel', 'jeruk', 'mangga'
value = 1

buah = dict.fromkeys(key, value)
print(buah)

# keys dan value
Nilai = {
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 78,
    "Fisika" : 80
}
# menggunakan keys
for i in Nilai.keys():
    print(i)
print("")
# menggunakan value
for i in Nilai.values():
    print(i)

# setdefault
Nilai = {
    "Matematika" : 100,
    "B. Indonesia" : 90,
    "B. Inggris" : 100
}
# sebelum Setdefault
print(Nilai)
print("")
# menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
# setelah menggunakan setdefault
print(Nilai)

# list dan nested list dictionary
Musik = {
    "The Chainsmoker" : ["All we Know", "The Paris"],
    "Laufey" : ['Promise', 'From the Start'],
    "Chappel Roan" : ['Good Luck, Babe!', 'Hot to Go!']
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
    print("")

# nested dictionary
mahasiswa = {
16 : {"Nama" : "Azira", "Umur" : 18},
17 : {"Nama" : "Alank", "Umur" : 18}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
    for key_a, value_a in value.items():
        print (key_a, " : ", value_a)
    print('')

# sebelum dilakukan perubahan
print(mahasiswa)
# menambah item
mahasiswa[16]['Angkatan'] = 2024
print(mahasiswa)
# mengubah item
mahasiswa[16]['Umur'] = 20
print(mahasiswa)
# menghapus item
del mahasiswa[16]['Nama']
print(mahasiswa)