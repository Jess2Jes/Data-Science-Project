from datetime import datetime

def tambah_task(tasks):
    while True :
        try:
            total_task = int(input("Berapa total task yang ingin ditambahkan : "))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        
    for t in range(total_task):
        next_id = max([t["id"] for t in tasks], default=0) + 1
        while True:
            task_name = str(input(f"Task {next_id} : ")).lower()
            dupe = False
            for t in tasks:
                if task_name.lower() == t["name"].lower():
                    dupe = True
                    break
            if dupe:
                print("Task sudah ada.\n")
                continue
            else:
                break
        
        while True:
            task_time = input("Masukkan waktu task (YYYY-MM-DD HH:MM) SPASI TIDAK DIPERBOLEHKAN \n ");print()
            try : 
                waktu = datetime.strptime(task_time, "%Y-%m-%d %H:%M")
                if waktu <= datetime.now():
                    print("Waktu task tidak boleh sebelum waktu saat ini.")
                    continue
                break
            except ValueError:
                print("Format waktu salah. Harap masukkan waktu dalam format YYYY-MM-DD HH:MM.")
        """
        Mengambil ID terbesar dari daftar task dan default=0 
        digunakan jika daftar tugas kosong, 
        sehingga max([]) tidak mmbuat program crash. 
        Maka, ia akan mengembalikan nilai 0.
        
        Dan juga kl misalny ini agar id tersebut gausah diinput user dia akan otomatis 1 utkt ask pertama
        misalnya belum ada task maka otomatis max(0) + 1 = 1 jadi id pertamanya adalah 1
        """
        while True:
            prioritas = input("Masukkan prioritas task (High, Medium, Low): ").lower()
            if prioritas not in ("high", "medium", "low"):
                print("Prioritas tidak valid. Harap masukkan High, Medium, atau Low.")
                continue
            break
        
        while True:
            status = input("Masukkan status task (Pending, In Progress, Completed): ").lower()
            if status not in ("pending", "in progress", "completed"):
                print("Status tidak valid. Harap masukkan Pending, In Progress, atau Completed.")
                continue
            break
        
        tasks.append({
            "id": next_id,
            "name": task_name.title(),
            "deadline": waktu.strftime("%Y %d %B %H:%M"),  # konversi datetime to string
            "priority": prioritas.title(),
            "status": status.title()
        })
        
        print(f"Task {next_id} : {task_name} berhasil ditambahkan.\n")

                
