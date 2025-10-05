from helpers.addData import *
from helpers.dataFilters import *

tasks = [
    {"id": 1, "name": "Kerjakan Tugas Basis Data", "deadline": "2025-10-05 13:00", "priority": "High", "status": "Pending"},
    {"id": 2, "name": "Belajar Algoritma", "deadline": "2025-10-06 12:57", "priority": "Medium", "status": "In Progress"},
    {"id": 3, "name": "Buat Slide Presentasi", "deadline": "2025-10-08 16:49", "priority": "High", "status": "Completed"},
    {"id": 4, "name": "Rapat Tim", "deadline": "2025-10-04 15:00", "priority": "Low", "status": "Completed"},
    {"id": 5, "name": "Kerjakan Tugas PBO", "deadline": "2025-10-04 15:00", "priority": "High", "status": "Completed"},
]
def menu_filter_deadline():
    print("\nFilter berdasarkan deadline:")
    print("1. Hari ini")
    print("2. Besok")
    print("3. Minggu ini")
    print("4. Bulan ini")
    pilihan_deadline = input("Pilih opsi (1-4): ")

    if pilihan_deadline == "1":
        filter_by_deadline("today", tasks)
    elif pilihan_deadline == "2":
        filter_by_deadline("tomorrow", tasks)
    elif pilihan_deadline == "3":
        filter_by_deadline("this week", tasks)
    elif pilihan_deadline == "4":
        filter_by_deadline("this month", tasks)
    else:
        print("Pilihan tidak valid.")
        
def menu_filter():
    while True:
        print("\n──────────Task Schedule Filter──────────")
        print("1. Filter berdasarkan deadline")
        print("2. Filter berdasarkan prioritas")
        print("3. Filter berdasarkan status")
        print("4. Lihat TOP 3 Task Paling Penting")
        print("5. Keluar dari menu filter")
        print("──────────────────────────────────────────")

        pilihan_filter = input("Pilih menu (1-6): ")

        if pilihan_filter == "1":
            menu_filter_deadline()
        elif pilihan_filter == "2":
            prio = input("Masukkan prioritas (High/Medium/Low): ")
            filter_by_priority(prio, tasks)

        elif pilihan_filter == "3":
            stat = input("Masukkan status (Pending/In Progress/Completed): ")
            filter_by_status(stat, tasks)

        elif pilihan_filter == "4":
            data_task("TOP 3 Task Paling Penting", get_top_tasks(tasks, 3))

        elif pilihan_filter == "5":
            print("Kembali ke menu utama.")
        else:
            print("Pilihan tidak valid, coba lagi.")
    
def menu_utama():
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
    menu_utama()
    pilihan = input("Pilihan : ")
    if pilihan == "1":
        tambah_task(tasks)
    elif pilihan == "2":
        data_task("Semua Task", tasks)
    elif pilihan == "3":
        pass
    elif pilihan == "4":
        pass
    elif pilihan == "5":
        pass
    elif pilihan == "6":
        menu_filter()
    elif pilihan == "7":
        break


