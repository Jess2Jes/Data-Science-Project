#ec
# Penghapusan data
tasks = [
    {"name": "Kerjakan Tugas Basis Data", "deadline": "2025-10-05 13:00", "priority": "High", "status": "Pending"},
    {"name": "Belajar Algoritma", "deadline": "2025-10-06 12:57", "priority": "Medium", "status": "In Progress"},
    {"name": "Buat Slide Presentasi", "deadline": "2025-10-08 16:49", "priority": "High", "status": "Completed"},
    {"name": "Rapat Tim", "deadline": "2025-10-04 15:00", "priority": "Low", "status": "Completed"},
    {"name": "Kerjakan Tugas PBO", "deadline": "2025-10-04 15:00", "priority": "High", "status": "Completed"},
]

def cetak_data_awal(tasks):
    print()
    print("Daftar Barang Belanjaan Sebelum Dihapus")
    print()
    for idx, data in enumerate(tasks, start=1):
        print(f"{idx}. {data['name']}, , {data['deadline']}, {data['priority']}, {data['status']}")

def hapus_data(tasks, name):
    for data in tasks:
        if data["name"].lower() == name.lower():
            tasks.remove(data)
            return True
    return False

def cetak_data_hapus(data_):
    print()
    print("Daftar Barang Belanjaan Setelah Dihapus")
    print()
    if data_:
        for idx, data in enumerate(tasks, start=1):
            print(f"{idx}. {data['name']}, , {data['deadline']}, {data['priority']}, {data['status']}")
    else:
        print("Semua barang sudah dihapus.")

cetak_data_awal(tasks)

hapus = input("\nMasukkan nama tugas yang ingin dihapus: ")

if hapus_data(tasks, hapus):
    print(f"\n✅ Tugas '{hapus}' berhasil dihapus!")
else:
    print(f"\n⚠️ Tugas '{hapus}' tidak ditemukan!")

cetak_data_hapus(tasks)

# ubah tasks
def ubah_task(tasks, old_name, field, new_value):
    for data in tasks:
        if data["name"].lower() == old_name.lower():
            if field in data:
                data[field] = new_value
                print(f"\n✅ Task '{old_name}' berhasil diubah: {field} → {new_value}")
                return True
            else:
                print(f"\n⚠️ Field '{field}' tidak ditemukan!")
                return False
    print(f"\n⚠️ Task '{old_name}' tidak ditemukan.")
    return False

# selesaikan tasks
def selesaikan_task(tasks, name):
    for data in tasks:
        if data["name"].lower() == name.lower():
            data["status"] = "Completed"
            print(f"\n🎉 Task '{name}' telah diselesaikan!")
            return True
    print(f"\n⚠️ Task '{name}' tidak ditemukan.")
    return False