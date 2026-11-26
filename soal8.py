print("===== MENENTUKAN KELULUSAN SISWA =====")

print("1 = Teori")
print("2 = Praktik")
x = int(input("PILIH KATEGORI UJIAN : "))

match x:
    case 1:
        y = int(input("MASUKAN NILAI UJIAN : "))
        if y >= 75:
            print("Selamat, Anda Lulus")
        else:
            print("Maaf, Anda Belum Lulus")
    case 2:
        y = int(input("MASUKAN NILAI UJIAN : "))
        if y >= 75:
            print("Selamat, Anda Lulus")
        else:
            print("Maaf, Anda Belum Lulus")
    case _:
        print("PILIHAN TIDAK ADA")
        