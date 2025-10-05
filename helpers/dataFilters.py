from datetime import datetime, timedelta

priority_map = {"High": 3, "Medium": 2, "Low": 1}

def parse_deadline(s):
    try:
        return datetime.strptime(s, "%Y %d %B %H:%M")
    except ValueError:
        return datetime.strptime(s, "%Y-%m-%d %H:%M")

def get_top_tasks(tasks, n=3):
    """Ambil task terpenting berdasarkan prioritas & deadline"""
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (-priority_map[t["priority"].capitalize()], parse_deadline(t["deadline"]))
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
            t["name"].capitalize().ljust(col_widths["name"]) + " │ " +
            t["deadline"].capitalize().ljust(col_widths["deadline"]) + " │ " +
            t["priority"].capitalize().ljust(col_widths["priority"]) + " │ " +
            t["status"].capitalize().ljust(col_widths["status"])
        )
        print(row)

    print("─" * (sum(col_widths.values()) + 12))


def filter_by_deadline(period, tasks):
    now = datetime.now()
    
    if period.lower() == "today" or period.lower() == "hari ini":
        start = datetime(now.year, now.month, now.day)
        end = start + timedelta(days=1)
        title_period = "Hari ini"
        
    elif period.lower() == "tomorrow" or period.lower() == "besok":
        start = datetime(now.year, now.month, now.day) + timedelta(days=1)
        end = start + timedelta(days=1)
        title_period = "Besok"
        
    elif period.lower() == "this week" or period.lower() == "minggu ini":
        start = datetime(now.year, now.month, now.day) - timedelta(days=now.weekday())
        end = start + timedelta(days=7)
        title_period = "Minggu ini"
        
    elif period.lower() == "this month" or period.lower() == "bulan ini":
        start = datetime(now.year, now.month, 1)
        if now.month == 12:
            end = datetime(now.year + 1, 1, 1)
        else :
            end = datetime(now.year, now.month + 1, 1)
        title_period = "Bulan ini"
        
    else :
        print("Periode tidak valid.")
        return
    
    filtered = [t for t in tasks if start <= parse_deadline(t["deadline"]) < end]
    data_task(f"Task dengan deadline {title_period}", filtered)

def filter_by_priority(priority, tasks):
    filtered = [t for t in tasks if t["priority"].lower() == priority.lower()]
    data_task(f"Task dengan prioritas {priority}", filtered)

def filter_by_status(status, tasks):
    filtered = [t for t in tasks if t["status"].lower() == status.lower()]
    data_task(f"Task dengan status {status}", filtered)


