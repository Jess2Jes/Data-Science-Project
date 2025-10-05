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
    task_priority = {"Low": 1, "Medium": 2, "High": 3}
    tasks.sort(key=lambda x: task_priority[x["priority"]])

# Proses pengurutan data berdasarkan priority (High -> Medium -> Low)
def urutkan_task_priority_dsc(tasks):
    task_priority = {"Low": 1, "Medium": 2, "High": 3}
    tasks.sort(key=lambda x: task_priority[x["priority"]], reverse=True)

# Proses pengurutan data berdasarkan status (Pending -> In Progress -> Completed)
def urutkan_task_status_asc(tasks):
    task_status = {"Pending": 1, "In Progress": 2, "Completed": 3}
    tasks.sort(key=lambda x: task_status[x["status"]])

# Proses pengurutan data berdasarkan status (Completed -> In Progress -> Pending)
def urutkan_task_status_dsc(tasks):
    task_status = {"Pending": 1, "In Progress": 2, "Completed": 3}
    tasks.sort(key=lambda x: task_status[x["status"]], reverse=True)

