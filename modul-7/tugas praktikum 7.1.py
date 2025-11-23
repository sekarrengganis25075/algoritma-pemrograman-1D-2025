contacts = {}

def validasi_nama(nama):
    if not nama.replace(" ", "").isalpha():
        return "Nama hanya boleh berisi huruf."
    if nama in contacts:
        return "Nama sudah terdaftar."
    return None

def validasi_telepon(telepon):
    if not telepon.isdigit():
        return "Nomor telepon harus angka."
    if len(telepon) < 8:
        return "Nomor telepon minimal 8 digit."
    for data in contacts.values():
        if telepon == data[0]:
            return "Nomor telepon sudah digunakan kontak lain."
    return None

def validasi_email(email):
    if "@" not in email or "." not in email:
        return "Format email tidak valid."
    return None

def tampilkan_kontak():
    if not contacts:
        print("Belum ada kontak tersimpan.")
    else:
        print("\n=== DAFTAR KONTAK ===")
        for nama, data in contacts.items():
            print(f"Nama    : {nama}")
            print(f"Telepon : {data[0]}")
            print(f"Email   : {data[1]}\n")

def cari_kontak():
    nama = input("Masukkan nama kontak yang dicari: ")
    if nama in contacts:
        print(f"Nama    : {nama}")
        print(f"Telepon : {contacts[nama][0]}")
        print(f"Email   : {contacts[nama][1]}\n")
    else:
        print("Kontak tidak ditemukan.\n")

def tambah_kontak():
    while True:
        nama = input("Masukkan nama: ")
        cek = validasi_nama(nama)
        if cek:
            print(cek)
        else:
            break

    while True:
        telepon = input("Masukkan nomor telepon: ")
        cek = validasi_telepon(telepon)
        if cek:
            print(cek)
        else:
            break

    while True:
        email = input("Masukkan email: ")
        cek = validasi_email(email)
        if cek:
            print(cek)
        else:
            break

    contacts[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan.\n")

def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    if nama in contacts:
        while True:
            email_baru = input("Masukkan email baru: ")
            cek = validasi_email(email_baru)
            if cek:
                print(cek)
            else:
                break

        contacts[nama][1] = email_baru
        print("Email berhasil diperbarui.\n")
    else:
        print("Kontak tidak ditemukan.\n")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in contacts:
        del contacts[nama]
        print("Kontak berhasil dihapus.\n")
    else:
        print("Kontak tidak ditemukan.\n")

while True:
    print("\n=== CONTACT BOOK MENU ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak baru")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_kontak()
    elif pilih == "2":
        cari_kontak()
    elif pilih == "3":
        tambah_kontak()
    elif pilih == "4":
        update_email()
    elif pilih == "5":
        hapus_kontak()
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.\n")