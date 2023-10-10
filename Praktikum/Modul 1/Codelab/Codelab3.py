def hitung_nilai_akhir(uts, uas):
    return 0.3 * uts + 0.7 * uas


def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir


# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


def main():
    data_mahasiswa = {
        'Yovi': {'uts': 55, 'uas': 90},
        'Jody': {'uts': 75, 'uas': 70},
        'Iqbal': {'uts': 90, 'uas': 40},
        'Rizky': {'uts': 80, 'uas': 80}
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()
