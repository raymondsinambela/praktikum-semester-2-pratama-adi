# Praktikum 3 - Rekursi
# Raymond martupa sinambela - 552010125014
# Program ini mengimplementasikan beberapa fungsi matematika menggunakan rekursi dan iterasi, serta menampilkan hasilnya dengan format yang rapi. 
# Fungsi-fungsi yang diimplementasikan meliputi faktorial, deret aritmatika, dan deret Fibonacci.

# ============================================================
# PROGRAM MATEMATIKA: Faktorial, Aritmatika, dan Fibonacci
# ============================================================


# ------------------------------------------------------------
# BAGIAN 1: FAKTORIAL REKURSIF
# Menghitung n! dengan cara memanggil dirinya sendiri
# Basis rekursi: 0! = 1 dan 1! = 1
# Contoh: 5! = 5 × 4 × 3 × 2 × 1 = 120
# ------------------------------------------------------------
def faktorial_rekursif(n):
    # Basis: faktorial dari 0 atau 1 adalah 1
    if n == 0 or n == 1:
        return 1
    # Rekursi: n! = n × (n-1)!
    return n * faktorial_rekursif(n - 1)


# ------------------------------------------------------------
# BAGIAN 2: FAKTORIAL ITERATIF
# Menghitung n! menggunakan perulangan (loop)
# Tidak menggunakan rekursi, lebih hemat memori untuk n besar
# Contoh: 5! = 1 × 2 × 3 × 4 × 5 = 120
# ------------------------------------------------------------
def faktorial_iteratif(n):
    hasil = 1  # Nilai awal pengali (identitas perkalian)
    # Kalikan semua bilangan dari 2 hingga n
    for i in range(2, n + 1):
        hasil *= i  # hasil = hasil × i
    return hasil


# ------------------------------------------------------------
# BAGIAN 3: DERET ARITMATIKA 1 SAMPAI N
# Menghitung jumlah semua bilangan bulat dari 1 hingga n
# Rumus: S = n(n+1)/2
# Contoh: S(5) = 1+2+3+4+5 = 15
# ------------------------------------------------------------
def deret_aritmatika(n):
    hasil = 0  # Nilai awal penjumlahan
    # Jumlahkan semua bilangan dari 1 hingga n
    for i in range(1, n + 1):
        hasil += i  # hasil = hasil + i
    return hasil


# ------------------------------------------------------------
# BAGIAN 4: FIBONACCI REKURSIF
# Menghitung bilangan ke-n dalam deret Fibonacci
# Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Basis: F(0) = 0, F(1) = 1
# Rekursi: F(n) = F(n-1) + F(n-2)
# Contoh: F(6) = 8
# ------------------------------------------------------------
def fibonacci_rekursif(n):
    # Basis rekursi: F(0) = 0 dan F(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Rekursi: F(n) = F(n-1) + F(n-2)
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)


# ============================================================
# BAGIAN UTAMA: MENJALANKAN SEMUA FUNGSI
# ============================================================

print("=" * 55)
print("   PROGRAM MATEMATIKA: Faktorial, Deret, Fibonacci")
print("=" * 55)

# --- Uji Faktorial ---
angka = int(input("\nMasukkan angka untuk faktorial: "))
print(f"\n[Faktorial Rekursif]  {angka}! = {faktorial_rekursif(angka)}")
print(f"[Faktorial Iteratif]  {angka}! = {faktorial_iteratif(angka)}")

# --- Uji Deret Aritmatika ---
angka2 = int(input("\nMasukkan nilai n untuk deret 1 hingga n: "))
print(f"\n[Deret Aritmatika]    1 + 2 + ... + {angka2} = {deret_aritmatika(angka2)}")

# --- Uji Fibonacci ---
angka3 = int(input("\nMasukkan posisi ke-n untuk Fibonacci: "))
print(f"\n[Fibonacci Rekursif]  F({angka3}) = {fibonacci_rekursif(angka3)}")

# --- Tampilkan Deret Fibonacci ---
print(f"\n[Deret Fibonacci 0 s/d {angka3}]")
deret = [fibonacci_rekursif(i) for i in range(angka3 + 1)]
print(" → ".join(str(x) for x in deret))

print("\n" + "=" * 55)

# ============================================================
# tanggapan:
# Rekursi lebih mudah dipahami dan lebih elegan untuk masalah yang
# Rekursi lebih elegan namun boros memori; iterasi lebih
# efisien untuk data besar. Fibonacci rekursif memiliki
# kompleksitas eksponensial, cocok hanya untuk nilai n kecil.
# ============================================================