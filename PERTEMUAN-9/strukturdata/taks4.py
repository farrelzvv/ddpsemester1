def konsonan(kalimat):
    vocal = "aiueo "
    hasil = ""
    for huruf in kalimat:
        if huruf not in vocal:
            hasil += huruf
    return hasil

print(konsonan("Nurul Fikri"))