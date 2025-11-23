while True:
    def faktorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * faktorial(n - 1)
    
    n = int(input("Masukkan bilangan bulat non-negatif: "))

    if n < 0:
        print("Tidak bisa menghitung faktorial dari bilangan negatif!")
        continue
    else:
        hasil = faktorial(n)
        print(f"Faktorial dari {n} adalah {hasil}")
        
    lanjut = input("Apakah ingin lanjut (y/n): ").lower()
    if lanjut == "n":
        print("Program selesai. Terima kasih")
        break