# Pengurutan Data 

# Contoh data: 
tasks = [
    {"id": 1, "name": "Belajar Algoritma", "deadline": "2025-10-06 12:57 PM", "priority": "Medium", "status": "In Progress"},
    {"id": 2, "name": "Kerjakan Tugas Basis Data", "deadline": "2025-10-05 13:00 PM", "priority": "High", "status": "Pending"},
    {"id": 3, "name": "Buat Slide Presentasi", "deadline": "2025-10-08 16:49 PM", "priority": "High", "status": "Completed"},
    {"id": 4, "name": "Rapat Tim", "deadline": "2025-10-04 15:00 PM", "priority": "Low", "status": "Completed"},
    {"id": 5, "name": "Kerjakan Tugas PBO", "deadline": "2025-10-04 09:00 AM", "priority": "High", "status": "Completed"},
]

# Proses pengurutan data berdasarkan deadline (ascending)
def urutkan_task_deadline_asc(tasks):
    tasks.sort(key=lambda x: x["deadline"])

# Proses pengurutan data berdasarkan deadline (descending)
def urutkan_task_deadline_dsc(tasks):
    tasks.sort(key=lambda x: x["deadline"], reverse=True)

# Proses pengurutan data berdasarkan alphabetik (nama tugas) (ascending)
def urutkan_task_name_asc(tasks):
    tasks.sort(key=lambda x: x["name"])

# Proses pengurutan data berdasarkan alphabetik (nama tugas) (descending)
def urutkan_task_name_dsc(tasks):
    tasks.sort(key=lambda x: x["name"], reverse=True)

# Proses pengurutan data berdasarkan priority (Low -> Medium -> High)
def urutkan_task_priority_asc(tasks):
    tasks.sort(key=lambda x: x["priority"][-1], reverse=True)

# Proses pengurutan data berdasarkan priority (High -> Medium -> Low)
def urutkan_task_priority_dsc(tasks):
    tasks.sort(key=lambda x: x["priority"][-1])

# Proses pengurutan data berdasarkan status (Pending -> In Progress -> Completed)
def urutkan_task_status_asc(tasks):
    tasks.sort(key=lambda x: x["status"][0], reverse=True)

# Proses pengurutan data berdasarkan status (Completed -> In Progress -> Pending)
def urutkan_task_status_dsc(tasks):
    tasks.sort(key=lambda x: x["status"][0])

def main_sortir():
    while True:
        print("\n" + "────────────────────Pengurutan Task────────────────────")
        print("1. Pengurutan Task berdasarkan Waktu Deadline")
        print("2. Pengurutan Task berdasarkan Nama Tugas")
        print("3. Pengurutan Task berdasarkan Prioritas")
        print("4. Pengurutan Task berdasarkan Status")
        print("5. Keluar")
        print("───────────────────────────────────────────────────────")
        try: 
            pilihan = int(input("Pilihan (1-5): "))
        except ValueError:
            print("\nMasukkan digit dalam pilihan.")
        else:
            if (pilihan == 1):
                    pilihan_user = input("\nPengurutan berdasarkan Ascending/Descending:\n").lower()
                    if (pilihan_user == "ascending"):
                        urutkan_task_deadline_asc(tasks)
                    elif (pilihan_user == "descending"):
                        urutkan_task_deadline_dsc(tasks)
                        
                    else:
                        print("\nSalah input. Silakan coba lagi...")

            elif (pilihan == 2):
                    pilihan_user = input("\nPengurutan berdasarkan Ascending/Descending:\n").lower()
                    if (pilihan_user == "ascending"):
                        urutkan_task_name_asc(tasks)
                    elif (pilihan_user == "descending"):
                        urutkan_task_name_dsc(tasks)
                    else:
                        print("\nSalah input. Silakan coba lagi...")

            elif (pilihan == 3):
                    pilihan_user = input("\nPengurutan berdasarkan Ascending/Descending:\n").lower()
                    if (pilihan_user == "ascending"):
                        urutkan_task_priority_asc(tasks)
                    elif (pilihan_user == "descending"):
                        urutkan_task_priority_dsc(tasks)
                    else:
                        print("\nSalah input. Silakan coba lagi...")

            elif (pilihan == 4):
                    pilihan_user = input("\nPengurutan berdasarkan Ascending/Descending:\n").lower()
                    if (pilihan_user == "ascending"):
                        urutkan_task_status_asc(tasks)
                    elif (pilihan_user == "descending"):
                        urutkan_task_status_dsc(tasks)
                    else:
                        print("\nSalah input. Silakan coba lagi...")

            elif (pilihan == 5):
                break

            else:
                print("\nPilih pilihan antara (1-5).")

if __name__ == "__main__":
    main_sortir()
