print("===== BIOSKOP =====")

x = int(input("MASUKAN UMUR : "))

if x >= 17:
    print("1.Horor")
    print("2.Komedi")
    print("3.Keluarga")
    print("4.Aksi")
    y = int(input("PILIH GENRE FILM : "))
    match y:
        case 1:
            print("1.Horor Indonesia")
            print("2.Horor Luar Negeri")
            z = int(input("PILIH SUB-GENRE FILM : "))
            match z:
                case 1:
                    print("Selamat Menyaksikan Film Horor Indonesia")
                case 2:
                    print("Selamat Menyaksikan Film Horor Luar Negeri")
                case _:
                    print("PILIHAN TIDAK TERSEDIA")
        case 2:
            print("1.Komedi Indonesia")
            print("2.Komedi Luar Negeri")
            z = int(input("PILIH SUB-GENRE FILM : "))
            match z:
                case 1:
                    print("Selamat Menyaksikan Film Komedi Indonesia")
                case 2:
                    print("Selamat Menyaksikan Film Komedi Luar Negeri")
                case _:
                    print("PILIHAN TIDAK TERSEDIA")
        case 3:
            print("1.Keluarga Indonesia")
            print("2.Keluarga Luar Negeri")
            z = int(input("PILIH SUB-GENRE FILM : "))
            match z:
                case 1:
                    print("Selamat Menyaksikan Film Keluarga Indonesia")
                case 2:
                    print("Selamat Menyaksikan Film Keluarga Luar Negeri")
                case _:
                    print("PILIHAN TIDAK TERSEDIA")
        case 4:
            print("1.Aksi Indonesia")
            print("2.Aksi Hollywood")
            print("3.Aksi Bollywood")
            z = int(input("PILIH SUB-GENRE FILM : "))
            match z:
                case 1:
                    print("Selamat Menyaksikan Film Aksi Indonesia")
                case 2:
                    print("Selamat Menyaksikan Film Aksi Hollywood")
                case 3:
                    print("Selamat Menyaksikan Film Aksi Bollywood")
                case _:
                    print("PILIHAN TIDAK TERSEDIA")
        case _:
            print("PILIHAN TIDAK TERSEDIA")
else:
    print("1. 2Dimensi")
    print("2. 3Dimensi")
    y = int(input("PILIH GENRE FILM : "))
    match y:
        case 1:
            print("1.Naruto")
            print("2.OnePiece")
            z = int(input("PILIH JUDUL FILM : "))
            match z:
                case 1:
                    print("Selamat Menyaksikan Film Naruto")
                case 2:
                    print("Selamat Menyaksikan Film OnePiece")
                case _:
                    print("PILIHAN TIDAK TERSEDIA")
        case 2:
            print("1.Nemo")
            print("2.Kungfu Panda")
            z = int(input("PILIH JUDUL FILM : "))
            match z:
                case 1:
                    print("Selamat Menyaksikan Film Nemo")
                case 2:
                    print("Selamat Menyaksikan Film Kungfu Panda")
                case _:
                    print("PILIHAN TIDAK TERSEDIA")
        case _:
            print("PILIHAN TIDAK TERSEDIA")