inventaris = {}

def tampilkan_barang():
    if not inventaris:
        print("Belum ada data barang.")
    else:
        print("\n=== DAFTAR BARANG ===")
        for id_barang, data in inventaris.items():
            print(f"ID Barang : {id_barang}")
            print(f"Nama      : {data[0]}")
            print(f"Harga     : {data[1]}")
            print(f"Stok      : {data[2]}\n")

def cari_barang():
    id_barang = input("Masukkan ID barang yang dicari: ")
    if id_barang in inventaris:
        print(f"ID Barang : {id_barang}")
        print(f"Nama      : {inventaris[id_barang][0]}")
        print(f"Harga     : {inventaris[id_barang][1]}")
        print(f"Stok      : {inventaris[id_barang][2]}\n")
    else:
        print("Barang tidak ditemukan.\n")

def tambah_barang():
    id_barang = input("Masukkan ID barang: ")
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan.\n")

def update_stok():
    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    if id_barang in inventaris:
        stok_baru = int(input("Masukkan stok baru: "))
        if stok_baru < 0:
            print("Stok tidak boleh kosong\n")
            return
            
        inventaris[id_barang][2] = stok_baru
        print("Stok berhasil diperbarui.\n")
    else:
        print("Barang tidak ditemukan.\n")

def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.\n")
    else:
        print("Barang tidak ditemukan.\n")

while True:
    print("\n=== MENU INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_barang()
    elif pilih == "2":
        cari_barang()
    elif pilih == "3":
        tambah_barang()
    elif pilih == "4":
        update_stok()
    elif pilih == "5":
        hapus_barang()
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.\n")