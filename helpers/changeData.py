from datetime import datetime

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
        if tasks[i]["status"].lower() == "completed":
            tasks.pop(i)

def cetak_data_hapus(tasks):
    print("\nDaftar Tugas Setelah Dihapus\n")
    if tasks:
        for idx, data in enumerate(tasks, start=1):
            print(f"{idx}. {data['name']}, {data['deadline']}, {data['priority']}, {data['status']}")
    else:
        print("Semua tugas sudah dihapus.")

def _format_deadline_value(value: str) -> str:
    try:
        dt = datetime.strptime(value, "%Y-%m-%d %H:%M")
        return dt.strftime("%Y %d %B %H:%M")
    except ValueError as e:
        raise ValueError("⚠ Format deadline tidak valid! Gunakan format: YYYY-MM-DD HH:MM") from e

def _normalize_priority(value: str) -> str:
    allowed = {"high": "High", "medium": "Medium", "low": "Low"}
    key = value.strip().lower()
    if key not in allowed:
        raise ValueError("⚠ Prioritas hanya boleh: High / Medium / Low")
    return allowed[key]

def _normalize_status(value: str) -> str:
    allowed = {"pending": "Pending", "in progress": "In Progress", "completed": "Completed"}
    key = value.strip().lower()
    if key not in allowed:
        raise ValueError("⚠ Status hanya boleh: Pending / In Progress / Completed")
    return allowed[key]

def ubah_task(tasks, old_name, field, new_value):
    task = next((d for d in tasks if d["name"].lower() == old_name.lower()), None)
    if not task:
        print(f"\n⚠ Task '{old_name}' tidak ditemukan.")
        return False

    if field not in task:
        print(f"\n⚠ Field '{field}' tidak ditemukan!")
        return False

    transformers = {
        "deadline": _format_deadline_value,
        "priority": _normalize_priority,
        "status": _normalize_status,
    }

    try:
        transform = transformers.get(field, lambda x: x)
        task[field] = transform(new_value)
    except ValueError as ve:
        print(f"\n{ve}")
        return False

    print(f"\n✅ Task '{old_name}' berhasil diubah: {field} → {task[field]}")
    return True

def selesaikan_task(tasks, name):
    for data in tasks:
        if data["name"].lower() == name.lower():
            if data["status"].lower() == "completed":
                print(f"\nTask '{name}' sudah berstatus 'Selesai/Completed'!")
            else:
                data["status"] = "Completed"
                print(f"\n🎉 Task '{name}' telah diselesaikan!")
                return True
    print(f"\n⚠️ Task '{name}' tidak ditemukan.")
    return False