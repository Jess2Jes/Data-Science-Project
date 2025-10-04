# Pengurutan Data 
import datetime
from datetime import *

# Contoh data: 
datas = [("tidur", f"{datetime.now().date()} 22:00"), 
        ("mengerjakan kuis matkul Data Science", f"{datetime.now().date()} 08:30"), 
        ("sarapan", f"{datetime.now().date()} 08:00"), 
        ("jogging", f"{datetime.now().date()} 07:30"),
        ("menulis laporan pengerjaan project OOP", f"{datetime.now().date()} 09:00"),
        ("mengikuti kelas Data Science", f"{datetime.now().date()} 17:45")]

# Cetak data sebelum disortir
def cetak_data_unsorted(datas):
    print("\n" + "Daftar Task/Tugas Sebelum Disortir".center(80, '-')
        + "\n")
    for idx, data in enumerate(datas,start=1):
        print(f"-> Tugas-{idx}: {data[0].title()} ({data[1]})")
    print("\n" + "-"*80)

# Proses pengurutan data
def urutkan_task(datas):
    sort_datas = sorted(datas, key=lambda x: x[1])
    return sort_datas

# Cetak data setelah disortir
def cetak_data_sorted(datas):
    print("\n" + "Daftar Task/Tugas Setelah Disortir".center(80, '-')
        + "\n")
    for idx, data in enumerate(datas,start=1):
        print(f"-> Tugas-{idx}: {data[0].title()} ({data[1]})")
    print("\n" + "-"*80)

cetak_data_unsorted(datas)
new_datas = urutkan_task(datas)
cetak_data_sorted(new_datas)#jessica
