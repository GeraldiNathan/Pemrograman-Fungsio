import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = [item[1] for item in data_transaksi]
jumlah_terjual = [item[2] for item in data_transaksi]

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.scatter(harga_produk, jumlah_terjual, color='blue', label='Jumlah Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Terjual')
plt.legend()
plt.show()

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda item: item[1] * item[2], data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
fig, ax = plt.subplots()
produk_labels = [item[0] for item in data_transaksi]
bar_chart = ax.bar(produk_labels, pendapatan_produk, color='green', label='Pendapatan')

# Menambahkan label dan legend
plt.xlabel('Produk')
plt.ylabel('Pendapatan')
plt.title('Pendapatan Produk')
ax.legend()

# Menambahkan nilai pendapatan di atas setiap bar
for i, v in enumerate(pendapatan_produk):
    ax.text(i, v + 1, str(v), ha='center', va='bottom', color='black')

plt.show()
