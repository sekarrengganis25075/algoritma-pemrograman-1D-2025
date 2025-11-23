a = tuple(map(int, input("Masukkan tuple pertama (pisahkan dengan spasi): ").split()))
b = tuple(map(int, input("Masukkan tuple kedua (pisahkan dengan spasi): ").split()))

gabung = a + b

hasil = () 
for x in gabung:
    if x not in hasil:
        hasil += (x,)

hasil = list(hasil)
for i in range(len(hasil)):
    for j in range(len(hasil) - 1):
        if hasil[j] < hasil[j + 1]:
            hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

print("\nHasil akhir:", tuple(hasil))