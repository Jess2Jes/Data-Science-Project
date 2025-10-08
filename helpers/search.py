##tasks = [
##    {"id": 1, "name": "Kerjakan Tugas Basis Data", "deadline": "2025-10-05", "priority": "High", "status": "Pending"},
##    {"id": 2, "name": "Belajar Algoritma", "deadline": "2025-10-06", "priority": "Medium", "status": "In Progress"},
##    {"id": 3, "name": "Buat Slide Presentasi", "deadline": "2025-10-08", "priority": "High", "status": "Completed"},
##    {"id": 4, "name": "Rapat Tim", "deadline": "2025-10-04", "priority": "Low", "status": "Pending"},
##    {"id": 5, "name": "Kerjakan Tugas PBO", "deadline": "2025-10-04", "priority": "High", "status": "Pending"},
##]

def kemiripan(a, b):
    a, b = a.lower(), b.lower()
    sama = sum(1 for huruf in a if huruf in b)
    return sama / max(len(a), len(b))

def cari_task(tasks):
    while True:
        keyword = input("\nMasukkan nama task yang ingin dicari: ").lower()
        found = [t for t in tasks if keyword in t['name'].lower()]

        if not found:
            print(f"\nTask dengan nama '{keyword}' tidak ditemukan.")

            # cari task paling mirip
            kandidat = None
            skor_tertinggi = 0
            for t in tasks:
                skor = kemiripan(keyword, t['name'])
                if skor > skor_tertinggi:
                    skor_tertinggi = skor
                    kandidat = t
            if skor_tertinggi >= 0.4:  # batas kemiripan 40%
                print(f"Mungkin maksud Anda: '{kandidat['name']}'?")
        else:
            print(f"\nHasil pencarian untuk => '{keyword}':\n")
            for idx, t in enumerate(found, start=1):
                pnjg_garis = f"{idx}. {t['name']}, {t['deadline']}, {t['priority']}, {t['status']}"
                garis = "─" * len(pnjg_garis)
                print("\n" + garis)
                print(pnjg_garis)
        while True:
            lanjut = input("\nApakah ingin lanjut cari (iya/tidak)? ").lower()
            if lanjut == "tidak":
                print("\nPencarian selesai.")
                return  # keluar dari seluruh fungsi
            elif lanjut == "iya":
                break  # keluar dari loop 'lanjut' dan kembali ke atas (input keyword baru)
            else:
                print("Input tidak valid. Harap masukkan ('iya' / 'tidak')")

