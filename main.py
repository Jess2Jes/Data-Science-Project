from helpers.addData import tambah_task
from helpers.dataFilters import data_task, filter_by_deadline, filter_by_priority, filter_by_status, get_top_tasks
from helpers.reports import laporan_statistik
from helpers.sorter import (
    urutkan_task_deadline_asc, urutkan_task_deadline_dsc,
    urutkan_task_name_asc, urutkan_task_name_dsc,
    urutkan_task_priority_asc, urutkan_task_priority_dsc,
    urutkan_task_status_asc, urutkan_task_status_dsc,
    urutkan_task_id_asc, urutkan_task_id_dsc
)
from helpers.changeData import (
    ubah_task, selesaikan_task, hapus_data, hapus_task_selesai
)
from helpers.search import cari_task
INVALID_CHOICE = "Pilihan tidak valid, coba lagi."

tasks = [
    {"id": 1, "name": "Kerjakan Tugas Basis Data", "deadline": "2025 05 October 13:00", "priority": "High", "status": "Pending"},
    {"id": 2, "name": "Belajar Algoritma", "deadline": "2025 06 October 12:57", "priority": "Medium", "status": "In Progress"},
    {"id": 3, "name": "Buat Slide Presentasi", "deadline": "2025 08 October 16:49", "priority": "High", "status": "Completed"},
    {"id": 4, "name": "Rapat Tim", "deadline": "2025 04 October 15:00", "priority": "Low", "status": "Completed"},
    {"id": 5, "name": "Kerjakan Tugas PBO", "deadline": "2025 04 October 15:00", "priority": "High", "status": "Completed"},
]

garis = "─" * 25

def menu_sortir():
    def mline():
        print("─" * 54)

    sort_map = {
        "1": ("Deadline", {
            "ascending": urutkan_task_deadline_asc,
            "descending": urutkan_task_deadline_dsc
        }),
        "2": ("Nama", {
            "ascending": urutkan_task_name_asc,
            "descending": urutkan_task_name_dsc
        }),
        "3": ("Prioritas", {
            "ascending": urutkan_task_priority_asc,
            "descending": urutkan_task_priority_dsc
        }),
        "4": ("Status", {
            "ascending": urutkan_task_status_asc,
            "descending": urutkan_task_status_dsc
        }),
        "5": ("ID", {
            "ascending": urutkan_task_id_asc,
            "descending": urutkan_task_id_dsc
        }),
    }

    while True:
        print("\n──────────────────────Pengurutan Task──────────────────────")
        print("1. Berdasarkan Deadline")
        print("2. Berdasarkan Nama")
        print("3. Berdasarkan Prioritas")
        print("4. Berdasarkan Status")
        print("5. Berdasarkan ID")
        print("6. Kembali")
        mline()
        pilihan_sort = input("Pilih opsi (1-6): ").strip()

        if pilihan_sort == "6":
            break

        cfg = sort_map.get(pilihan_sort)
        if not cfg:
            print("Pilihan tidak valid.")
            continue

        label, funcs = cfg
        arah = input("Ascending/Descending? ").strip().lower()
        func = funcs.get(arah)
        if not func:
            print("Input salah")
            continue

        func(tasks)
        data_task(f"Tasks setelah pengurutan {label}", tasks)

def menu_filter_deadline():
    print("\nFilter berdasarkan deadline:")
    print("─────────────────────────────────────────────────────────")
    print("1. Hari ini")
    print("2. Besok")
    print("3. Minggu ini")
    print("4. Bulan ini")
    print("─────────────────────────────────────────────────────────")
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
        print(f"\n{garis}Task Schedule Filter{garis}")
        print("1. Filter berdasarkan deadline")
        print("2. Filter berdasarkan prioritas")
        print("3. Filter berdasarkan status")
        print("4. Lihat TOP 3 Task Paling Penting")
        print("5. Keluar dari menu filter")
        print(f"{garis*2 + '─'*20}")
        pilihan_filter = input("Pilih menu (1-5): ")

        if pilihan_filter == "1":
            menu_filter_deadline()
        elif pilihan_filter == "2":
            prio = input("Masukkan prioritas (High/Medium/Low): ").capitalize()
            filter_by_priority(prio, tasks)
        elif pilihan_filter == "3":
            stat = input("Masukkan status (Pending/In Progress/Completed): ").capitalize()
            filter_by_status(stat, tasks)
        elif pilihan_filter == "4":
            data_task("TOP 3 Task Paling Penting", get_top_tasks(tasks, 3))
        elif pilihan_filter == "5":
            print("Kembali ke menu utama.")
            break
        else:
            print(INVALID_CHOICE)

def menu_utama():
    print("\n╭──────────────────────────────╮")
    print("│         📜 MAIN MENU         │")
    print("╰──────────────────────────────╯")
    print("╭───────────────────────────────╮")
    print("│ 1.  📝 Tambah Task            │")
    print("│ 2.  📋 Daftar Task            │")
    print("│ 3.  🔍 Cari Task              │")
    print("│ 4.  🧩 Sortir Task            │")
    print("│ 5.  📊 Laporan Statistik      │")
    print("│ 6.  🧭 Filter                 │")
    print("│ 7.  🗑️  Hapus Task             │")
    print("│ 8.  ✏️  Ubah Task              │")
    print("│ 9.  ✅ Tandai Task Selesai    │")
    print("│ 10. 🚪 Keluar                 │")
    print("╰───────────────────────────────╯")

while True:
    menu_utama()
    pilihan = input("Pilihan : ")
    if pilihan == "1":
        tambah_task(tasks)
    elif pilihan == "2":
        data_task("Semua Task", tasks)
    elif pilihan == "3":
        cari_task(tasks)
    elif pilihan == "4":
        menu_sortir()
    elif pilihan == "5":
        laporan_statistik(tasks)
    elif pilihan == "6":
        menu_filter()
    elif pilihan == "7":
        print("Hapus Task:")
        print("1. Hapus task secara spesifik")
        print("2. Hapus semua task yang sudah selesai")
        opsi_hapus = input("Pilih opsi (1/2): ")

        if opsi_hapus == "1":
            hapus = input("Masukkan nama tugas yang ingin dihapus: ")
            if hapus_data(tasks, hapus):
                print(f"\n✅ Tugas '{hapus}' berhasil dihapus!")
            else:
                print(f"\n⚠️ Tugas '{hapus}' tidak ditemukan!")
        elif opsi_hapus == "2":
            hapus_task_selesai(tasks)
            print("\n✅ Semua task yang selesai berhasil dihapus!")
        else:
            print(INVALID_CHOICE)
    elif pilihan == "8":
        old_name = input("Nama task yang ingin diubah: ")
        field = input("Field yang ingin diubah (name/deadline/priority/status): ").lower()
        if field == "deadline":
            new_value = input("Masukkan nilai baru (YYYY-MM-DD HH:MM): ")
        else:
            new_value = input("Masukkan nilai baru: ")
        ubah_task(tasks, old_name, field, new_value)
    elif pilihan == "9":
        name = input("Nama task yang ingin diselesaikan: ").lower()
        selesaikan_task(tasks, name)
    elif pilihan == "10":
        print("\nTerima kasih telah menggunakan App Demo kami.\n")
        break
    else:
        print(INVALID_CHOICE)