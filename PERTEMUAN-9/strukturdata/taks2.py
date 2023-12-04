def membalikan_buah(original_list):
    length = len(original_list)

    for i in range(length // 2):
        # Tukar elemen antara awal dan akhir
        original_list[i], original_list[length - i - 1] = original_list[length - i - 1], original_list[i]

# Contoh penggunaan
buah_asli = ["apel", "jeruk", "anggur", "pisang"]

# Membuat copy list agar buah_asli tetap utuh
buah_terbalik = buah_asli[:]
membalikan_buah(buah_terbalik)

print("Buah Asli:", buah_asli)
print("Buah Terbalik (tanpa reverse bawaan):", buah_terbalik)
