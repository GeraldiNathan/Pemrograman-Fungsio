# Inisialisasi data peserta sebagai list
data_peserta = []

# Fungsi untuk menambahkan peserta baru oleh admin
def tambah_peserta():
    id_peserta = len(data_peserta)
    nama = input("Masukkan Nama Peserta: ")
    nilai = float(input("Masukkan Nilai Peserta: "))
    hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"
    data_peserta.append({"ID": id_peserta, "Nama": nama, "Nilai": nilai, "Hasil Akhir": hasil_akhir})

# Fungsi untuk menampilkan nilai dan hasil akhir peserta
def tampilkan_nilai_dan_hasil(id_peserta):
    if id_peserta < len(data_peserta):
        peserta = data_peserta[id_peserta]
        print("\nData Peserta:")
        print("ID  | Nama          | Nilai  | Hasil Akhir")
        print("----------------------------------------")
        print(f"{peserta['ID']}   | {peserta['Nama']}   | {peserta['Nilai']}     | {peserta['Hasil Akhir']}")
    else:
        print("ID Peserta tidak valid.")

# Program Utama
while True:
    print("\nMenu:")
    print("1. Login Admin")
    print("2. Login Peserta")
    print("3. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")
        
        if username == "admin" and password == "admin123":
            while True:
                print("\nMenu Admin:")
                print("1. Tambah Peserta")
                print("2. Keluar")
                
                admin_pilihan = input("Pilih menu admin: ")
                
                if admin_pilihan == "1":
                    tambah_peserta()
                elif admin_pilihan == "2":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        else:
            print("Username atau password admin salah.")
    elif pilihan == "2":
        id_peserta = int(input("Masukkan ID Peserta: "))
        tampilkan_nilai_dan_hasil(id_peserta)
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")