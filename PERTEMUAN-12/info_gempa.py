from gempa import Gempa

# Membuat 5 objek Gempa
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Memanggil fungsi dampak() untuk masing-masing objek
print(f"{gempa1.lokasi}: {gempa1.dampak()}")
print(f"{gempa2.lokasi}: {gempa2.dampak()}")
print(f"{gempa3.lokasi}: {gempa3.dampak()}")
print(f"{gempa4.lokasi}: {gempa4.dampak()}")
print(f"{gempa5.lokasi}: {gempa5.dampak()}")
