# # Sequence
# barang = ('Buku', 2000, 'Pensil', 1500, 'Penggaris', 5000)

# def split_tuple(data__tuple):
#     return data__tuple[::2], data__tuple[1::2]

# def created_dict(harga_barang, list_barang):
#     return dict(zip(harga_barang, list_barang))

# list_harga_barang, list_nama_barang = created_dict(barang)
# data_tuple = created_dict(list_harga_barang, list_nama_barang)

# print(barang)
# print(list_nama_barang, list_harga_barang)
# print(data_tuple)

# # Function num bool
# def is_prima(num):
#     return num > 1 and all(num % i for i in range(2, int(num**0.5) + 1))

# angka = 13
# hasil = is_prima(angka)
# print(hasil)

# # Function palindrome bool
# def is_palindrome(s):
#     clean_s = ''.join(filter(str.isalnum, s.lower()))
#     return clean_s == clean_s[::-1]

# string = 'radar'
# print(is_palindrome(string))

# # Pure Function
# def tambah_angka(angka, total=0):
#     return total + angka

# total_awal = 0
# hasil = tambah_angka(5, total_awal)
# print(hasil)


# # Lambda
# tambah_angka = lambda angka, total=0: total + angka

# total_awal =0
# hasil = tambah_angka(5, total_awal)
# print(hasil)

# # Lambda 1.0

# klasifikasi_angka = lambda x: "Positif" if x > 0 else ("Negatif" if x < 0 else "Nol")
# pencarian_angka = lambda list_angka, find: "found" if find in list_angka else "not found"

# angka = 5
# hasil_klasifikasi = klasifikasi_angka(angka)
# print(f"{angka} adalah angka {hasil_klasifikasi}")

# list_angka = [1, 2, 3, 4, 5]
# angka_cari = 3
# hasil_pencarian = pencarian_angka(list_angka, angka_cari)
# print(f"Angka {angka_cari} {hasil_pencarian}")

# # List Compre
# ganjil = [angka for angka in range (51) if angka % 2 != 0]
# print(ganjil)

# # Generator
# def generate_ganjil():
#     for angka in range(51):
#         if angka % 2 !=  0:
#             yield angka

# generate_ganjil = generate_ganjil()

# for angka in generate_ganjil:
#     print(angka)

# # HOF
# def sisagold(nim, value):
#     last_digit = int(str(nim)[-1])
    
#     if last_digit % 2 == 1: 
#         return value - 5
#     else:  
#         return lambda x: x - 5

# nim_ganjil = 351
# nim_genap = 352

# hasil_ganjil = sisagold(nim_ganjil, 10)
# print("Hasil untuk NIM ganjil:", hasil_ganjil)

# fungsi_kurang_genap = sisagold(nim_genap, 10)
# hasil_genap = fungsi_kurang_genap(5)
# print("Hasil untuk NIM genap:", hasil_genap)


# # list map lambda
# print(list(map(lambda y: y * 2, filter(lambda x: x% 2 == 1, range(10)))))

# # Closure
# def hitung_pangkat(exponent):
#     def pangkat(base):
#         return base ** exponent
    
#     return pangkat

# pangkat_dua = hitung_pangkat(2)
# pangkat_tiga = hitung_pangkat(3)

# print(pangkat_dua(2))
# print(pangkat_tiga(2))
