#Program Pencarian dan Perubahan Data
def tampilkan_tasks():
    print("Daftar Tugas:")
    for index, i in enumerate(tasks):
        print(f"{index+1}. {i['name']} | Deadline: {i['deadline']} | Priority: {i['priority']} | Status: {i['status']}")
    print()


def cari_dan_ubah():
    tampilkan_tasks()
    cari = input("Masukkan nama tugas yang ingin dicari: ").lower()

    found = False
    for data in tasks:
        if cari in data['name'].lower():
            found = True
            print(f"\nDitemukan: {data}")
            
            ubah = input("Apakah ingin mengubah data ini? (iya/tidak): ").lower()
            if ubah == 'iya':
                print("\nPilih kolom yang ingin diubah:")
                print("1. Name")
                print("2. Deadline")
                print("3. Priority")
                print("4. Status")
                pilihan = input("Masukkan nomor pilihan: ")

                if pilihan == "1":
                    data_baru = input("Masukkan nama baru: ")
                    data["name"] = data_baru
                    
                elif pilihan == "2":
                    data_baru = input("Masukkan deadline baru (YYYY-MM-DD): ")
                    data["deadline"] = data_baru

                elif pilihan == "3":
                    data_baru = input("Masukkan priority baru (High/Medium/Low): ")
                    data["priority"] = data_baru

                elif pilihan == "4":
                    data_baru = input("Masukkan status baru (Pending/In Progress/Completed): ")
                    data["status"] = data_baru

                else:
                    print("Pilihan tidak valid.")
                    return

                print("\nData berhasil diubah:")
                print(data)
            else:
                break

    if not found:
        print(f"Data dengan nama '{cari}' tidak ditemukan.\n")
        cari_dan_ubah()
        
    tampilkan_tasks()


#Data Awal
tasks = [
    {"id": 1, "name": "Kerjakan Tugas Basis Data", "deadline": "2025-10-05", "priority": "High", "status": "Pending"},
    {"id": 2, "name": "Belajar Algoritma", "deadline": "2025-10-06", "priority": "Medium", "status": "In Progress"},
    {"id": 3, "name": "Buat Slide Presentasi", "deadline": "2025-10-08", "priority": "High", "status": "Completed"},
    {"id": 4, "name": "Rapat Tim", "deadline": "2025-10-04", "priority": "Low", "status": "Pending"},
    {"id": 5, "name": "Kerjakan Tugas PBO", "deadline": "2025-10-04", "priority": "High", "status": "Pending"},
]

#Program
cari_dan_ubah()
