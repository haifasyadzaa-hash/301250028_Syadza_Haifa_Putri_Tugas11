# TUGAS 9
# Gunakan Dictionary untuk penyimpanan data

data_mahasiswa = {}

while True:
    print("\n=== MENU ===")
    print("1. Tambah Data")
    print("2. Cari Data")
    print("3. Tampilkan Data")
    print("4. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        nim = input("Masukkan NIM : ")
        nama = input("Masukkan Nama : ")

        data_mahasiswa[nim] = nama
        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        nim = input("Masukkan NIM yang dicari : ")

        if nim in data_mahasiswa:
            print("Nama :", data_mahasiswa[nim])
        else:
            print("Data tidak ditemukan.")

    elif pilihan == "3":
        print("\nDaftar Mahasiswa")
        for nim, nama in data_mahasiswa.items():
            print(nim, "-", nama)

    elif pilihan == "4":
        break

    else:
        print("Pilihan tidak tersedia.")