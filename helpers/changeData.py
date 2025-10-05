#ec
# Penghapusan data

data_schedules = [
    ("Beras 5kg", "Rp 75.000"),
    ("Minyak Goreng 2L", "Rp 40.000"),
    ("Telur 1kg", "Rp 28.000"),
    ("Gula Pasir 1kg", "Rp 15.000"),
    ("Sabun Mandi", "Rp 10.000"),
    ("Shampoo", "Rp 25.000")
]

def cetak_data_awal(data_schedules):
    print()
    print("Daftar Barang Belanjaan Sebelum Dihapus")
    print()
    for idx, data in enumerate(data_schedules, start=1):
        print(f"{idx}.Barang : {data[0]} (Harga: {data[1]})")

def hapus_data(data_schedules, nama_barang):
    for data in data_schedules:
        if data[0].lower() == nama_barang.lower():
            data_schedules.remove(data)
            return True
    return False

def cetak_data_hapus(datas):
    print()
    print("Daftar Barang Belanjaan Setelah Dihapus")
    print()
    if datas:
        for idx, data in enumerate(data_schedules, start=1):
            print(f"{idx}.Barang : {data[0]} (Harga: {data[1]})")
    else:
        print("Semua barang sudah dihapus.")

cetak_data_awal(data_schedules)

hapus = "Telur 1kg" 
if hapus_data(data_schedules, hapus):
    print("-"*50)
    print(f"Barang '{hapus}' berhasil dihapus!")
else:
    print()
    print(f"Barang '{hapus}' tidak ditemukan!")

cetak_data_hapus(data_schedules)
