from datetime import datetime

#  DATA TUGAS 
# Format: (id, judul, status, kategori, assigned_to, start, end, prioritas)
data_tugas = [
    (1, "Membuat class Python", "done", "OOP", "Steven", "2025-10-01", "2025-10-03", 1),
    (2, "Analisis dataset COVID", "in progress", "Data Science", "Hans", "2025-10-02", None, 3),
    (3, "Membuat grafik matplotlib", "done", "Data Science", "Jessica", "2025-09-28", "2025-10-01", 5),
    (4, "Diskusi etika digital", "pending", "Agama", "Kindy", "2025-10-04", None, 2),
    (5, "Menulis refleksi keagamaan", "done", "Agama", "EC", "2025-09-25", "2025-09-27", 4),
]

#  STATISTIK STATUS 
stat_status = {}
for tugas in data_tugas:
    status = tugas[2]
    stat_status[status] = stat_status.get(status, 0) + 1

#  RATA-RATA DURASI TUGAS SELESAI 
total_durasi = 0
jumlah_selesai = 0
for tugas in data_tugas:
    if tugas[2] == "done" and tugas[6]:
        start = datetime.strptime(tugas[5], "%Y-%m-%d")
        end = datetime.strptime(tugas[6], "%Y-%m-%d")
        durasi = (end - start).days
        total_durasi += durasi
        jumlah_selesai += 1
rata_durasi = total_durasi / jumlah_selesai if jumlah_selesai > 0 else 0

#  TUGAS PER KATEGORI & USER 
stat_kategori = {}
stat_user = {}
for tugas in data_tugas:
    kategori = tugas[3]
    user = tugas[4]
    stat_kategori[kategori] = stat_kategori.get(kategori, 0) + 1
    stat_user[user] = stat_user.get(user, 0) + 1

#  PRIORITAS TERTINGGI & TERENDAH 
prioritas_tertinggi = float('inf')
prioritas_terendah = float('-inf')
tugas_max = []
tugas_min = []
for tugas in data_tugas:
    prioritas = tugas[7]
    if prioritas < prioritas_tertinggi:
        prioritas_tertinggi = prioritas
        tugas_max = [tugas]
    elif prioritas == prioritas_tertinggi:
        tugas_max.append(tugas)
    if prioritas > prioritas_terendah:
        prioritas_terendah = prioritas
        tugas_min = [tugas]
    elif prioritas == prioritas_terendah:
        tugas_min.append(tugas)

# FILTER TUGAS AKTIF & PRIORITAS 
tugas_dikerjakan = [t for t in data_tugas if t[2] in ("pending", "in progress")]
tugas_high = [t for t in data_tugas if t[7] in (1, 2)]
tugas_low = [t for t in data_tugas if t[7] in (4, 5)]

#  CETAK LAPORAN 
print("=== Laporan Tugas ===")
print(f"Total tugas: {len(data_tugas)}")

print("\nJumlah tugas per status:")
for status, jumlah in stat_status.items():
    print(f"  - {status}: {jumlah}")

print(f"\nRata-rata durasi tugas selesai: {rata_durasi:.2f} hari")

print("\nTugas per kategori:")
for kategori, jumlah in stat_kategori.items():
    print(f"  - {kategori}: {jumlah}")

print("\nTugas per user:")
for user, jumlah in stat_user.items():
    print(f"  - {user}: {jumlah}")

print(f"\nTugas dengan prioritas tertinggi ({prioritas_tertinggi}):")
for t in tugas_max:
    print(f"  - {t[1]} (oleh {t[4]}, status: {t[2]})")

print(f"\nTugas dengan prioritas terendah ({prioritas_terendah}):")
for t in tugas_min:
    print(f"  - {t[1]} (oleh {t[4]}, status: {t[2]})")

print(f"\nTotal tugas yang harus dikerjakan: {len(tugas_dikerjakan)}")
for t in tugas_dikerjakan:
    print(f"  - {t[1]} (oleh {t[4]}, status: {t[2]}, prioritas: {t[7]})")

print(f"\nTugas dengan prioritas tinggi ({len(tugas_high)}):")
for t in tugas_high:
    print(f"  - {t[1]} (oleh {t[4]}, status: {t[2]}, prioritas: {t[7]})")

print(f"\nTugas dengan prioritas rendah ({len(tugas_low)}):")
for t in tugas_low:
    print(f"  - {t[1]} (oleh {t[4]}, status: {t[2]}, prioritas: {t[7]})")
