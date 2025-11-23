def tambah_data(daftar, data):
    daftar.append(data)

def hapus_data(daftar, id_hapus):
    for i, d in enumerate(daftar):
        if d[0] == id_hapus:
            daftar.pop(i)
            return True
    return False

def tampilkan_semua(sumatera, kalimantan, jawa):
    daftar_daerah = [
        ("SUMATERA", sumatera),
        ("KALIMANTAN", kalimantan),
        ("JAWA", jawa)
    ]

    for nama, data in daftar_daerah:
        print(f"\n--- {nama} ---")
        if not data:
            print("(Belum ada data)")
        else:
            for i, d in enumerate(data, 1):
                print(f"{i}. [{d[0]}] {d[1]} - Asal: {d[2]} - Santri: {d[3]}")

sumatera, kalimantan, jawa = [], [], []
idc = 1  

while True:
    print("\n=== MENU KUNJUNGAN SANTRI ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Semua Data")
    print("4. Keluar")

    p = input("Pilih (1-4): ")

    if p == "1":
        daerah_map = {"1": "Sumatera", "2": "Kalimantan", "3": "Jawa"}
        d = input("\nPilih daerah (1-3) 1.Sumatera, 2. Kalimantan, 3. Jawa: ")

        if d not in daerah_map:
            print("Pilihan tidak valid!")
            continue

        nama = input("Nama pengunjung: ")
        santri = input("Nama santri dijenguk: ")
        asal = daerah_map[d]

        data = [f"ID{idc:03d}", nama, asal, santri]
        idc += 1

        if asal == "Sumatera": tambah_data(sumatera, data)
        elif asal == "Kalimantan": tambah_data(kalimantan, data)
        else: tambah_data(jawa, data)

        print("Data berhasil ditambahkan.")

    elif p == "2":
        id_h = input("Masukkan ID yang ingin dihapus: ")
        ditemukan = (
            hapus_data(sumatera, id_h) or
            hapus_data(kalimantan, id_h) or
            hapus_data(jawa, id_h)
        )
        print("Data dihapus." if ditemukan else "ID tidak ditemukan.")

    elif p == "3":
        tampilkan_semua(sumatera, kalimantan, jawa)

    elif p == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")