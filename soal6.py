print("===== MENENTUKAN NAMA BULAN =====")

x = int(input("MASUKAN BULAN KE-(1-6): "))

match x:
    case 1:
        print("JANUARI")
    case 2:
        print("FEBRUARI")
    case 3:
        print("MARET")
    case 4:
        print("APRIL")
    case 5:
        print("MEI")
    case 6:
        print("JUNI")
    case _:
         print("Bulan Tidak Tersedia")