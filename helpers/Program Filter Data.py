from datetime import datetime

tasks = [
    {"id": 1, "name": "Kerjakan Tugas Basis Data", "deadline": "2025-10-05 14:30", "priority": "High", "status": "Pending"},
    {"id": 2, "name": "Belajar Algoritma", "deadline": "2025-10-06 09:00", "priority": "Medium", "status": "In Progress"},
    {"id": 3, "name": "Buat Slide Presentasi", "deadline": "2025-10-08 16:15", "priority": "High", "status": "Completed"},
    {"id": 4, "name": "Rapat Tim", "deadline": "2025-10-04 11:00", "priority": "Low", "status": "Pending"},
    {"id": 5, "name": "Kerjakan Tugas PBO", "deadline": "2025-10-04 13:45", "priority": "High", "status": "Pending"},
]

priority_map = {"High": 3, "Medium": 2, "Low": 1}

def parse_deadline(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M")

def get_top_tasks(tasks, n=3):
    """Ambil task terpenting berdasarkan prioritas & deadline"""
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (-priority_map[t["priority"]], parse_deadline(t["deadline"]))
    )
    return sorted_tasks[:n]

def print_table(title, data):
    if not data:
        print(f"{title}: (Tidak ada data)")
        return

    # hitung lebar secara dinamis
    col_widths = {
        "id": max(len("ID"), max(len(str(t["id"])) for t in data)),
        "name": max(len("Task"), max(len(t["name"]) for t in data)),
        "deadline": max(len("Deadline"), max(len(t["deadline"]) for t in data)),
        "priority": max(len("Priority"), max(len(t["priority"]) for t in data)),
        "status": max(len("Status"), max(len(t["status"]) for t in data))
    }

    print("\n" + "─" * (sum(col_widths.values()) + 12))  
    print(title.center(sum(col_widths.values()) + 12))
    print("─" * (sum(col_widths.values()) + 12))

    header = (
        "ID".ljust(col_widths["id"]) + " │ " +
        "Task".ljust(col_widths["name"]) + " │ " +
        "Deadline".ljust(col_widths["deadline"]) + " │ " +
        "Priority".ljust(col_widths["priority"]) + " │ " +
        "Status".ljust(col_widths["status"])
    )
    print(header)
    print("─" * (sum(col_widths.values()) + 12))

    for t in data:
        row = (
            str(t["id"]).ljust(col_widths["id"]) + " │ " +
            t["name"].ljust(col_widths["name"]) + " │ " +
            t["deadline"].ljust(col_widths["deadline"]) + " │ " +
            t["priority"].ljust(col_widths["priority"]) + " │ " +
            t["status"].ljust(col_widths["status"])
        )
        print(row)

    print("─" * (sum(col_widths.values()) + 12))


def filter_by_deadline(date):
    filtered = [t for t in tasks if parse_deadline(t["deadline"]) <= parse_deadline(date)]
    print_table(f"Task dengan deadline sebelum {date}", filtered)

def filter_by_priority(priority):
    filtered = [t for t in tasks if t["priority"].lower() == priority.lower()]
    print_table(f"Task dengan prioritas {priority}", filtered)

def filter_by_status(status):
    filtered = [t for t in tasks if t["status"].lower() == status.lower()]
    print_table(f"Task dengan status {status}", filtered)

while True:
    print("\n──────────Task Schedule Filter──────────")
    print("1. Lihat semua task")
    print("2. Filter berdasarkan deadline")
    print("3. Filter berdasarkan prioritas")
    print("4. Filter berdasarkan status")
    print("5. Lihat TOP 3 Task Paling Penting")
    print("6. Keluar")
    print("──────────────────────────────────────────")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        print_table("Semua Task", tasks)
    elif pilihan == "2":
        tanggal = input("Masukkan tanggal batas (YYYY-MM-DD): ")
        filter_by_deadline(tanggal)
    elif pilihan == "3":
        prio = input("Masukkan prioritas (High/Medium/Low): ")
        filter_by_priority(prio)
    elif pilihan == "4":
        stat = input("Masukkan status (Pending/In Progress/Completed): ")
        filter_by_status(stat)
    elif pilihan == "5":
        print_table("TOP 3 Task Paling Penting", get_top_tasks(tasks, 3))
    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
