from datetime import datetime

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

def data_task(title, data):
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


def filter_by_deadline(date, tasks):
    filtered = [t for t in tasks if parse_deadline(t["deadline"]) <= parse_deadline(date)]
    data_task(f"Task dengan deadline sebelum {date}", filtered)

def filter_by_priority(priority, tasks):
    filtered = [t for t in tasks if t["priority"].lower() == priority.lower()]
    data_task(f"Task dengan prioritas {priority}", filtered)

def filter_by_status(status, tasks):
    filtered = [t for t in tasks if t["status"].lower() == status.lower()]
    data_task(f"Task dengan status {status}", filtered)


