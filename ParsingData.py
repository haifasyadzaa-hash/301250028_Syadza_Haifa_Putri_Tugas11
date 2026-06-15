# TUGAS 11
# Parsing file log menggunakan Set

jumlah_aktivitas = 0
user_unik = set()

try:
    with open("Tugas 11 (Parsing data)/log.txt", "r") as file:
        for baris in file:
            jumlah_aktivitas += 1

            data = baris.strip().split(",")

            if len(data) >= 2:
                user_unik.add(data[0])

    print("Jumlah aktivitas :", jumlah_aktivitas)
    print("Jumlah user unik :", len(user_unik))

except FileNotFoundError:
    print("File log tidak ditemukan.")