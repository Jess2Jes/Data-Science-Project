from datetime import datetime
tasks = []

def tambah_task(task):
    while True :
        try:
            total_task = int(input("Berapa total task yang ingin ditambahkan : "));print()
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        
    for task in range(total_task):
        while True:
            task = str(input("Masukkan task : ")).lower()
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
    print("─────────────Daftar Task─────────────")
    print(f"Total Task : {len(tasks)}")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i][0].lower().capitalize()} - {tasks[i][1].strftime('%Y %d %B %I:%M %p')}")
    
tambah_task(tasks)
daftar_task()
