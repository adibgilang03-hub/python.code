print("===== APK MENU MINUMAN =====")
print("Es Teh   | Rp5.000")
print("Es Jeruk | Rp7.000")
print("Kopi     | Rp8.000")
print("Susu     | Rp6.000")

x = int(input("PILIH MENU(1-4): "))

match x:
    case 1:
        print("Es Teh   | Rp5.000")
    case 2:
        print("Es Jeruk | Rp7.000")
    case 3:
        print("Kopi     | Rp8.000")
    case 4:
        print("Susu     | Rp6.000")
    case _:
         print("Menu Tidak Tersedia")