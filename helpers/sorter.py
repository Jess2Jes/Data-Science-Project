from datetime import datetime

# Proses pengurutan data berdasarkan deadline (ascending)
def urutkan_task_deadline_asc(tasks):
    tasks.sort(key=lambda x: datetime.strptime(x["deadline"], "%Y %d %B %H:%M"))

# Proses pengurutan data berdasarkan deadline (descending)
def urutkan_task_deadline_dsc(tasks):
    tasks.sort(key=lambda x: datetime.strptime(x["deadline"], "%Y %d %B %H:%M"), reverse=True)

# Proses pengurutan data berdasarkan alphabetik (nama tugas) (ascending)
def urutkan_task_name_asc(tasks):
    tasks.sort(key=lambda x: x["name"].lower())

# Proses pengurutan data berdasarkan alphabetik (nama tugas) (descending)
def urutkan_task_name_dsc(tasks):
    tasks.sort(key=lambda x: x["name"].lower(), reverse=True)

# Proses pengurutan data berdasarkan id (ascending)
def urutkan_task_id_asc(tasks):
    tasks.sort(key=lambda x: x["id"])

# Proses pengurutan data berdasarkan id (ascending)
def urutkan_task_id_dsc(tasks):
    tasks.sort(key=lambda x: x["id"], reverse=True)

# Proses pengurutan data berdasarkan priority (Low -> Medium -> High)
def urutkan_task_priority_asc(tasks):
    task_priority = {"Low": 1, "Medium": 2, "High": 3}
    tasks.sort(key=lambda x: task_priority[x["priority"].capitalize()])

# Proses pengurutan data berdasarkan priority (High -> Medium -> Low)
def urutkan_task_priority_dsc(tasks):
    task_priority = {"Low": 1, "Medium": 2, "High": 3}
    tasks.sort(key=lambda x: task_priority[x["priority"].capitalize()], reverse=True)

# Proses pengurutan data berdasarkan status (Pending -> In Progress -> Completed)
def urutkan_task_status_asc(tasks):
    task_status = {"Pending": 1, "In Progress": 2, "Completed": 3}
    tasks.sort(key=lambda x: task_status[x["status"].title()])
    
# Proses pengurutan data berdasarkan status (Completed -> In Progress -> Pending)
def urutkan_task_status_dsc(tasks):
    task_status = {"Pending": 1, "In Progress": 2, "Completed": 3}
    tasks.sort(key=lambda x: task_status[x["status"].title()], reverse=True)

