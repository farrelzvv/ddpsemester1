print("Selamat datang di aplikasi untuk menghitung luas bangun datar")
print("Pilih nomor 1 untuk menghitung luas persegi")
print("Pilih nomor 2 untuk menghitung luas Lingkaran")
print("Pilih nomor 3 untuk menghitung luas segitiga")


# Program Python untuk menghitung luas persegi dengan match case (Python 3.10)

LuasBangunDatar = int(input("Masukan sistem kebutuhan kalian " ))

match LuasBangunDatar:  
    case 1:
        sisi = int(input("Masukan sisi " ))
        hasil = int(sisi * sisi * sisi)
        print ("Luas persegi yang memiliki sisi ", sisi, "ialah", hasil)
    case 2:
        jariJari = int (input("masukan jari-jari " ))
        hasil = int(3.14 * jariJari * jariJari)
        print ("Luas lingkaran yang memiliki jari-jari ", jariJari, "ialah", hasil)
    case 3:
        alas = int (input(("masukan alas " )))
        tinggi = int (input(("masukan tinggi " )))
        hasil = int(1.2 * alas * tinggi)
        print ("Luas segitiga yang memiliki alas ", alas, "dan tinggi ", tinggi, "ialah", hasil)
    case _ :
        print("Masukan Angka yang sesuai ")
    

    
        
