from helpers.addData import tambah_task, daftar_task


def menu():
    print()
    print("────────────────────Menu────────────────────")
    print("1. Tambah Task")
    print("2. Daftar Task")
    print("3. Cari Task")
    print("4. Sortir Task")
    print("5. Laporan Statistik")
    print("6. Filter")
    print("7. Keluar")
    print("────────────────────────────────────────────")
    
while True :
    menu()
    pilihan = input("Pilihan : ")
    if pilihan == "1":
        tambah_task()
    elif pilihan == "2":
        daftar_task()
    elif pilihan == "3":
        pass
    elif pilihan == "4":
        pass
    elif pilihan == "5":
        pass
    elif pilihan == "6":
        pass
    elif pilihan == "7":
        break
