#Membuat Fungsi Luas Bangun Datar

#Fungsi Pertama
def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi :", luas)
    print("Keliling Persegi :", keliling)

#Fungsi Kedua
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang :", luas)
    print("Keliling Persegi Panjang :", keliling)

#Fungsi Ketiga
def lingkaran(jari2):
    phi = 3.14
    luas = phi * jari2 * jari2
    keliling = 2 * phi * jari2
    print("Luas Lingkaran :", luas)
    print("Keliling Lingkaran :", keliling)

#Fungsi Keempat
def segitiga_sama_sisi(alas, tinggi):
    luas = 1/2 * alas * tinggi
    keliling = alas * 3
    print("Luas Segitiga Sama Sisi :", luas)
    print("Keliling Segitiga Sama Sisi :", keliling)

#Fungsi Kelima
def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("Luas Belah Ketupat :", luas)
    print("Keliling Belah Ketupat :", keliling)

#Fungsi Keenam
def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * alas + sisi_miring
    print("Luas Jajar Genjang :", luas)
    print("Keliling Jajar Genjang :", keliling)

#Fungsi Ketujuh 
def layang_layang(diagonal1, diagonal2, sisi_atas, sisi_bawah):
    luas = diagonal1 * diagonal2 * 0.5
    keliling = sisi_atas * 2 + sisi_bawah * 2
    print("Luas Layang Layang :", luas)
    print("Keliling Layang Layang :", keliling)