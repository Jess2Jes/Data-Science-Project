#contoh cari
my_list = ["apel", "air", "ikan", "monyet", "sapi"]
print(my_list)
cari=input("Cari data :")

for index, data in enumerate(my_list):
    print(f"Index: {index}, data: {data}/n")
if cari in my_list:
    print(f"{cari} is present in the list/n")
else:
    print(f"{cari} is not present in the list/n")

#contoh ubah
print(my_list)
pilih=input("Pilih data yang mau diubah :")
new=input("Diubah menjadi : ")
replace = my_list.index(pilih)
my_list[replace] =  new
print(my_list)
