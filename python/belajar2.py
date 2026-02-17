# Fungsi Menghitung
def math(a, b, choose):
    if choose == 1:
        print(f"Hasil: {a + b}")
    elif choose == 2:
        print(f"Hasil: {a - b}")
    else:
        print("Pilihan Tidak Valid")

# Input User Menggunakan Tipe Data Integer
a = int(input("Input Nilai A: "))
b = int(input("Input Nilai B: "))
# Pilihan User Untuk Menghitung
choose = int(input("Choose 1.Penjumlahan 2.Pengurangan: "))

# Memanggil Fungsi
math(a, b, choose)
