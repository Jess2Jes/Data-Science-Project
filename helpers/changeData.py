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

def selesaikan_task(tasks, name):
    for data in tasks:
        if data["name"].lower() == name.lower():
            data["status"] = "Completed"
            print(f"\n🎉 Task '{name}' telah diselesaikan!")
            return True
    print(f"\n⚠️ Task '{name}' tidak ditemukan.")
    return False
