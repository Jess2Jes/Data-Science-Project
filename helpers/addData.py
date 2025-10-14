from datetime import datetime

def _prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

def _is_unique_name(tasks, name_lower: str) -> bool:
    return all(name_lower != t["name"].lower() for t in tasks)

def _prompt_unique_task_name(tasks, next_id: int) -> str:
    while True:
        task_name = str(input(f"Task {next_id} : ")).strip()
        if not task_name:
            print("Nama task tidak boleh kosong.\n")
            continue
        if not _is_unique_name(tasks, task_name.lower()):
            print("Task sudah ada.\n")
            continue
        return task_name

def _prompt_future_datetime() -> datetime:
    while True:
        task_time = input("Masukkan waktu task (YYYY-MM-DD HH:MM) SPASI TIDAK DIPERBOLEHKAN SETELAH MM\n ")
        print()
        try:
            waktu = datetime.strptime(task_time, "%Y-%m-%d %H:%M")
            if waktu <= datetime.now():
                print("Waktu task tidak boleh sebelum waktu saat ini.")
                continue
            return waktu
        except ValueError:
            print("Format waktu salah. Harap masukkan waktu dalam format YYYY-MM-DD HH:MM.")

def _prompt_choice(prompt: str, allowed: tuple[str, ...]) -> str:
    allowed_lower = tuple(a.lower() for a in allowed)
    while True:
        val = input(prompt).strip().lower()
        if val not in allowed_lower:
            print(f"Input tidak valid. Harap masukkan salah satu dari: {', '.join(allowed)}.")
            continue
        return val.title()

def tambah_task(tasks):
    total_task = _prompt_int("Berapa total task yang ingin ditambahkan : ")
    for _ in range(total_task):
        next_id = max([t["id"] for t in tasks], default=0) + 1

        task_name = _prompt_unique_task_name(tasks, next_id)
        waktu = _prompt_future_datetime()
        prioritas = _prompt_choice("Masukkan prioritas task (High, Medium, Low): ", ("High", "Medium", "Low"))
        status = _prompt_choice("Masukkan status task (Pending, In Progress, Completed): ", ("Pending", "In Progress", "Completed"))

        tasks.append({
            "id": next_id,
            "name": task_name.title(),
            "deadline": waktu.strftime("%Y %d %B %H:%M"),
            "priority": prioritas,
            "status": status
        })
        print(f"Task {next_id} : {task_name} berhasil ditambahkan.\n")