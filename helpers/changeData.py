def cetak_data_awal(tasks):
    print("\nDaftar Tugas Sebelum Dihapus\n")
    for idx, data in enumerate(tasks, start=1):
        print(f"{idx}. {data['name']}, {data['deadline']}, {data['priority']}, {data['status']}")

def hapus_data(tasks, name):
    for data in tasks:
        if data["name"].lower() == name.lower():
            tasks.remove(data)
            return True
    return False

def hapus_task_selesai(tasks):
    for i in range(len(tasks)-1, -1, -1):
        if tasks[i]["status"] == "Completed" :
            tasks.pop(i)

def cetak_data_hapus(tasks):
    print("\nDaftar Tugas Setelah Dihapus\n")
    if tasks:
        for idx, data in enumerate(tasks, start=1):
            print(f"{idx}. {data['name']}, {data['deadline']}, {data['priority']}, {data['status']}")
    else:
        print("Semua tugas sudah dihapus.")
from datetime import datetime

def ubah_task(tasks, old_name, field, new_value):
    for data in tasks:
        if data["name"].lower() == old_name.lower():
            if field not in data:
                print(f"\n⚠ Field '{field}' tidak ditemukan!")
                return False

            if field == "deadline":
                try:
                    datetime.strptime(new_value, "%Y %d %B %H:%M")
                except ValueError:
                    print("\n⚠ Format deadline tidak valid! Gunakan format: YYYY DD Month HH:MM")
                    return False

            elif field == "priority":
                if new_value not in ["High", "Medium", "Low"]:
                    print("\n⚠ Prioritas hanya boleh: High / Medium / Low")
                    return False

            elif field == "status":
                if new_value not in ["Pending", "In Progress", "Completed"]:
                    print("\n⚠ Status hanya boleh: Pending / In Progress / Completed")
                    return False

            data[field] = new_value
            print(f"\n✅ Task '{old_name}' berhasil diubah: {field} → {new_value}")
            return True

    print(f"\n⚠ Task '{old_name}' tidak ditemukan.")
    return False


def selesaikan_task(tasks, name):
    for data in tasks:
        if data["name"].lower() == name.lower():
            data["status"] = "Completed"
            print(f"\n🎉 Task '{name}' telah diselesaikan!")
            return True
    print(f"\n⚠️ Task '{name}' tidak ditemukan.")
    return False
