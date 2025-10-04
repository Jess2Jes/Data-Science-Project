from datetime import datetime

tasks = [
    {"id": 1, "name": "Kerjakan Tugas Basis Data", "deadline": "2025-10-05", "priority": "High", "status": "Pending"},
    {"id": 2, "name": "Belajar Algoritma", "deadline": "2025-10-06", "priority": "Medium", "status": "In Progress"},
    {"id": 3, "name": "Buat Slide Presentasi", "deadline": "2025-10-08", "priority": "High", "status": "Completed"},
    {"id": 4, "name": "Rapat Tim", "deadline": "2025-10-04", "priority": "Low", "status": "Pending"},
    {"id": 5, "name": "Kerjakan Tugas PBO", "deadline": "2025-10-04", "priority": "High", "status": "Pending"},
]


def tambah_task():
    while True :
        try:
            total_task = int(input("Berapa total task yang ingin ditambahkan : "));print()
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        
    for task in range(1, total_task + 1):
        while True:
            task = str(input(f"Task {task} : ")).lower()
            dupe = False
            for i in tasks:
                if task == i[0].lower():
                    dupe = True
                    break
            if dupe:
                print("Task sudah ada.\n")
                continue
            else:
                break
        
        while True:
            try : task_time = input("Masukkan waktu task (YYYY-MM-DD HH:MM): ");print()
            except ValueError : print("Format waktu salah. Harap masukkan waktu dalam format YYYY-MM-DD HH:MM.")
            waktu = datetime.strptime(task_time, "%Y-%m-%d %H:%M")
            if waktu <= datetime.now():
                print("Waktu task tidak boleh sebelum waktu saat ini.")
                continue
            else: 
                try :
                    waktu = datetime.strptime(task_time, "%Y-%m-%d %H:%M")
                    break
                except ValueError:
                    print("Format waktu salah. Harap masukkan waktu dalam format YYYY-MM-DD HH:MM.")
                    continue
            
        tasks.append((task, waktu))
                
def daftar_task():
    print("─────────────Daftar Task───────────────────")
    print(f"Total Task : {len(tasks)}")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i][0].lower().capitalize()} - {tasks[i][1].strftime('%Y %d %B %I:%M %p')}")
    
