x = 2
x = int(input("Masukkan angka x: "))
match x:
    case 1:
        print('False')
    case 2:
        print('True')
    case _:
        print("I don't know")