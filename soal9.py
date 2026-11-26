print("===== DISKON BELANJA =====")

print("1 = Member")
print("2 = Nonmember")
x = int(input("MASUKAN JENIS PELANGGAN : "))

match x:
    case 1:
        y = int(input("MASUKAN TOTAL BELANJA (Rp) : "))
        if y >= 100000:
            print("Selamat, Anda Mendapatkan Diskon 10%")
        else:
            print("Anda Tidak Mendapatkan Diskon")
    case 2:
        y = int(input("MASUKAN TOTAL BELANJA (Rp) : "))
        if y >= 100000:
            print("Selamat, Anda Mendapatkan Diskon 5%")
        else:
            print("Anda Tidak Mendapatkan Diskon")
    case _:
        print("PILIHAN TIDAK ADA")