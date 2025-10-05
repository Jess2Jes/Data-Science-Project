from datetime import datetime
def laporan_statistik(tasks, garis="─"):
    if not tasks:
        print("Belum ada task untuk ditampilkan.")
        return

    lines = []

    lines.append(f"Total tugas: {len(tasks)}")
    lines.append("")  # empty line for spacing

    # Status
    lines.append("Jumlah tugas per status:")
    stat_status = {}
    for t in tasks:
        stat_status[t["status"]] = stat_status.get(t["status"], 0) + 1
    for status, jumlah in stat_status.items():
        lines.append(f"  - {status}: {jumlah}")
    lines.append("")

    # Durasi tugas selesai
    total_durasi = 0
    jumlah_selesai = 0
    for t in tasks:
        if t["status"].lower() == "completed":
            start = datetime.strptime(t["deadline"], "%Y-%m-%d %H:%M")
            end = datetime.now()
            durasi = (end - start).days
            total_durasi += durasi
            jumlah_selesai += 1
    rata_durasi = total_durasi / jumlah_selesai if jumlah_selesai else 0
    lines.append(f"Rata-rata durasi tugas selesai: {rata_durasi:.2f} hari")
    lines.append("")

    # Prioritas
    lines.append("Jumlah tugas per prioritas:")
    stat_priority = {}
    for t in tasks:
        stat_priority[t["priority"]] = stat_priority.get(t["priority"], 0) + 1
    for prio, jumlah in stat_priority.items():
        lines.append(f"  - {prio}: {jumlah}")
    lines.append("")

    # Tugas tertinggi & terendah
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    tertinggi = max(tasks, key=lambda x: priority_map.get(x["priority"], 0))
    terendah = min(tasks, key=lambda x: priority_map.get(x["priority"], 0))
    lines.append(f"Tugas dengan prioritas tertinggi ({tertinggi['priority']}):")
    lines.append(f"  {tertinggi['name']} (status: {tertinggi['status']})")
    lines.append(f"Tugas dengan prioritas terendah ({terendah['priority']}):")
    lines.append(f"  {terendah['name']} (status: {terendah['status']})")

    # Calculate max line length
    max_length = max(len(line) for line in lines)

    # Build the box
    print(f"┌{garis * (max_length + 2)}┐")
    print(f"│ {'Laporan Statistik'.center(max_length)} │")
    print(f"├{garis * (max_length + 2)}┤")
    for line in lines:
        print(f"│ {line.ljust(max_length)} │")
    print(f"└{garis * (max_length + 2)}┘")
