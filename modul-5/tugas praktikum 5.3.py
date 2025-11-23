while True:
    def hitung_gaji(nama, jabatan, gaji_pokok):
        pajak = 0.05 * gaji_pokok
        if jabatan.lower() == "manager":
            tunjangan = 0.10 * gaji_pokok
        elif jabatan.lower() == "staff":
            tunjangan = 0.05 * gaji_pokok
        else:
            tunjangan = 0

        gaji_bersih = gaji_pokok - pajak + tunjangan

        print("\n=== Rincian Gaji Karyawan ===")
        print(f"Nama Karyawan : {nama}")
        print(f"Jabatan       : {jabatan}")
        print(f"Gaji Pokok    : Rp{gaji_pokok:,.0f}")
        print(f"Tunjangan     : Rp{tunjangan:,.0f}")
        print(f"Pajak (5%)    : Rp{pajak:,.0f}")
        print(f"Gaji Bersih   : Rp{gaji_bersih:,.0f}")
        return gaji_bersih

    while True:
        nama = input("Masukkan nama karyawan: ")
        if any(ch.isdigit() for ch in nama):
            print("Peringatan: Nama mengandung angka, kemungkinan typo.")
            continue
        elif nama.isupper():
            print("Catatan: Nama semuanya huruf besar.")
            continue
        elif nama.islower():
            print("Catatan: Nama semuanya huruf kecil.")
            continue
        else:
            break

    while True:
        jabatan = input("Masukkan jabatan (Manager/Staff): ")
        if any(ch.isdigit() for ch in jabatan):
            print("Peringatan: Jabatan mengandung angka, kemungkinan typo.")
            continue
        elif jabatan.isupper():
            print("Catatan: Jabatan semuanya huruf besar.")
            continue
        elif jabatan.islower():
            print("Catatan: Jabatan semuanya huruf kecil.")
            continue
        else:
            break

    while True:
        try:
            gaji_pokok = int(input("Masukkan gaji pokok: "))
            if gaji_pokok < 0: 
                print("Peringatan: Gaji tidak boleh minus!")
                continue
            elif gaji_pokok < 1000000:  
                print("Catatan: Gaji pokok tergolong kecil.")
                break
            else:
                break
        except ValueError:
            print("Peringatan: Masukkan angka yang valid!")

    hitung_gaji(nama, jabatan, gaji_pokok)

    lanjut = input("\nApakah ingin lanjut (y/n): ").lower()
    if lanjut == "n":
        print("Program selesai. Terima kasih")
        break