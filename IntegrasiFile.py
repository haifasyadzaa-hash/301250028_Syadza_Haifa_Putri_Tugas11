# TUGAS 10
# Simpan dan baca data dari file

data_mahasiswa = {}

try:
    with open("data_mahasiswa.txt", "r") as file:
        for baris in file:
            nim, nama = baris.strip().split(",")
            data_mahasiswa[nim] = nama

except FileNotFoundError:
    print("File belum ada.")

nim = input("Masukkan NIM : ")
nama = input("Masukkan Nama : ")

data_mahasiswa[nim] = nama

with open("data_mahasiswa.txt", "w") as file:
    for nim, nama in data_mahasiswa.items():
        file.write(f"{nim},{nama}\n")

print("Data berhasil disimpan.")