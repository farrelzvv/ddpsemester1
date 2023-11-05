bintang = int(input("Masukkan jumlah baris: "))

for baris in range(1, bintang + 1):
    for kolom in range(baris):
        print("*", end="")
    print() 
