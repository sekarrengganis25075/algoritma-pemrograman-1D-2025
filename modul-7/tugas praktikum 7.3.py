kupon = {
    "LAGINGIRIT": 10,
    "BOKEK": 20,
    "AKHIRBULAN": 50
}

def tambah_kupon():
    kode = input("Masukkan kode kupon baru: ").upper()
    if kode in kupon:
        print("Kode kupon sudah terdaftar.\n")
        return
    try:
        diskon = int(input("Masukkan persentase diskon: "))
    except ValueError:
        print("Diskon harus berupa angka.\n")
        return

    kupon[kode] = diskon
    print(f"Kupon '{kode}' berhasil ditambahkan.\n")

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.\n")
    else:
        print("\n=== DAFTAR KUPON TERSEDIA ===")
        for kode, diskon in kupon.items():
            print(f"Kode Kupon : {kode}\tDiskon : {diskon}%")
        print()

def update_kupon():
    kode = input("Masukkan kode kupon yang ingin diperbarui: ").upper()
    if kode not in kupon:
        print("Kode kupon tidak ditemukan.\n")
        return
    try:
        diskon_baru = int(input("Masukkan diskon baru (%): "))
    except ValueError:
        print("Diskon harus berupa angka.\n")
        return

    kupon[kode] = diskon_baru
    print(f"Diskon kupon '{kode}' berhasil diperbarui.\n")

def hapus_kupon():
    kode = input("Masukkan kode kupon yang ingin dihapus: ").upper()
    if kode in kupon:
        del kupon[kode]
        print(f"Kupon '{kode}' berhasil dihapus.\n")
    else:
        print("Kode kupon tidak ditemukan.\n")

def proses_transaksi():
    try:
        total = int(input("Masukkan total belanja: "))
    except ValueError:
        print("Total belanja harus berupa angka.\n")
        return

    kode = input("Masukkan kode kupon: ").upper()

    if kode not in kupon:
        print("Kode kupon tidak valid atau sudah digunakan.\n")
        return

    diskon = kupon[kode]
    potongan = total * (diskon / 100)
    total_bayar = total - potongan

    print("\n=== RINCIAN TRANSAKSI ===")
    print(f"Total Belanja : Rp {total:,.2f}")
    print(f"Diskon        : {diskon}%")
    print(f"Potongan      : Rp {potongan:,.2f}")
    print(f"Total Bayar   : Rp {total_bayar:,.2f}\n")

    del kupon[kode]
    print(f"Kupon '{kode}' telah digunakan dan dihapus dari sistem.\n")

def menu():
    while True:
        print("=== SISTEM VALIDASI KUPON DISKON ===")
        print("1. Tambah Kupon")
        print("2. Tampilkan Kupon")
        print("3. Update Kupon")
        print("4. Hapus Kupon")
        print("5. Proses Transaksi")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_kupon()
        elif pilihan == "2":
            tampilkan_kupon()
        elif pilihan == "3":
            update_kupon()
        elif pilihan == "4":
            hapus_kupon()
        elif pilihan == "5":
            proses_transaksi()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

menu()