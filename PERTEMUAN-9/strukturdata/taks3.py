def duplikasi(list_buah):
    duplicated_list = []

    for buah in list_buah:
        duplicated_list.extend([buah, buah])

    return duplicated_list

# Contoh penggunaan
buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(buah_asli)

print("Buah Asli:", buah_asli)
print("Hasil Duplikasi:", hasil_duplikasi)
