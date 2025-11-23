def tambah(data, deret):
    for x in deret:
        data.append(int(x))

def tampilkan(data):
    print("Data:", data if data else "(Kosong)")

def ubah(data, pos, nilai):
    data[pos] = nilai

def hapus(data, pos):
    data.pop(pos)

def cek_sama(data):
    if len(data) % 2 != 0:
        return None
    t = len(data) // 2
    kiri = sum(data[:t])
    kanan = sum(data[t:])
    return kiri, kanan, kiri == kanan

print("PROGRAM PEMERIKSAAN ANGKA")

data = []

while True:
    print("\n1. Input Angka")
    print("2. Tampilkan")
    print("3. Ubah")
    print("4. Hapus")
    print("5. Cek Pembagian")
    print("6. Keluar")
    p = input("Pilih (1-6): ")

    if p == "1":
        deret = input("Masukkan deretan angka: ")
        if deret.isdigit():
            tambah(data, deret)
            print("Ditambahkan.")
        else:
            print("Harus angka!")

    elif p == "2":
        tampilkan(data)

    elif p == "3":
        tampilkan(data)
        if data:
            pos = int(input("Posisi diubah (mulai 1): ")) - 1
            nilai = int(input("Nilai baru: "))
            ubah(data, pos, nilai)
            print("Diubah.")

    elif p == "4":
        tampilkan(data)
        if data:
            pos = int(input("Posisi hapus (mulai 1): ")) - 1
            hapus(data, pos)
            print("Dihapus.")

    elif p == "5":
        hasil = cek_sama(data)
        if hasil is None:
            print("Data ganjil → Tidak bisa dibagi.")
        else:
            kiri, kanan, status = hasil
            t = len(data)//2
            print(f"Kiri : {data[:t]} = {kiri}")
            print(f"Kanan: {data[t:]} = {kanan}")
            print("Hasil:", status)

    elif p == "6":
        print("Selesai.")
        break

    else:
        print("Pilihan salah!")