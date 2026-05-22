# Praktikum 4 - Analisis Kompleksitas Algoritma
# Raymond martupa sinambela - 552010125014
# menganalisis kompleksitas algoritma menggunakan notasi Big-O.


# ============================================================
# PROGRAM ANALISIS KOMPLEKSITAS ALGORITMA
# Latihan 1 – 4: O(n), O(2n), O(n²), Linear vs Nested Loop
# ============================================================


# ============================================================
# LATIHAN 1 – MENGHITUNG JUMLAH ITERASI: O(n)
# Satu loop tunggal dari 0 hingga n-1
# Setiap putaran = 1 langkah → total langkah = n
# Kompleksitas: O(n) — LINEAR
# ============================================================
def latihan_1(n):
    print("\n" + "=" * 50)
    print("  LATIHAN 1 – Loop Tunggal O(n)")
    print("=" * 50)

    count = 0  # Penghitung jumlah iterasi

    # Perulangan dari 0 hingga n-1, setiap langkah dicatat
    for i in range(n):
        count += 1  # Tambah hitungan setiap iterasi
        # Tampilkan langkah secara detail
        print(f"  Langkah {count:>3} → i = {i}")

    # Tampilkan ringkasan hasil
    print(f"\n  ✔ Total iterasi untuk n={n}: {count}")
    print(f"  ✔ Kompleksitas: O(n) — setiap penambahan n, iterasi bertambah 1")
    return count


# ============================================================
# LATIHAN 2 – DUA LOOP BERURUTAN: O(2n) ≈ O(n)
# Loop pertama berjalan n kali, lalu loop kedua berjalan n kali
# Total langkah = n + n = 2n → disederhanakan menjadi O(n)
# Kompleksitas: O(n) — masih LINEAR (konstanta diabaikan)
# ============================================================
def latihan_2(n):
    print("\n" + "=" * 50)
    print("  LATIHAN 2 – Dua Loop Berurutan O(2n) ≈ O(n)")
    print("=" * 50)

    count = 0  # Penghitung total iterasi gabungan

    # Loop pertama: berjalan sebanyak n kali
    print("\n  [Loop ke-1]")
    for i in range(n):
        count += 1
        print(f"  Langkah {count:>3} → loop-1, i = {i}")

    # Loop kedua: berjalan sebanyak n kali (berurutan, bukan bersarang)
    print("\n  [Loop ke-2]")
    for j in range(n):
        count += 1
        print(f"  Langkah {count:>3} → loop-2, j = {j}")

    # Tampilkan ringkasan hasil
    print(f"\n  ✔ Total iterasi untuk n={n}: {count}  (= 2 × {n})")
    print(f"  ✔ Kompleksitas: O(2n) → disederhanakan O(n)")
    return count


# ============================================================
# LATIHAN 3 – LOOP BERSARANG: O(n²)
# Untuk setiap i (n kali), loop dalam berjalan n kali
# Total langkah = n × n = n²
# Kompleksitas: O(n²) — KUADRATIK, pertumbuhan sangat cepat
# ============================================================
def latihan_3(n):
    print("\n" + "=" * 50)
    print("  LATIHAN 3 – Loop Bersarang O(n²)")
    print("=" * 50)

    count = 0  # Penghitung total iterasi

    # Loop luar: berjalan n kali
    for i in range(n):
        # Loop dalam: untuk setiap i, berjalan n kali
        for j in range(n):
            count += 1
            # Cetak setiap langkah (dibatasi agar tidak terlalu panjang)
            if n <= 5:
                print(f"  Langkah {count:>4} → i={i}, j={j}")

    # Jika n besar, tampilkan ringkasan saja
    if n > 5:
        print(f"  (Detail langkah disembunyikan untuk n={n} — terlalu panjang)")

    # Tampilkan ringkasan hasil
    print(f"\n  ✔ Total iterasi untuk n={n}: {count}  (= {n} × {n})")
    print(f"  ✔ Kompleksitas: O(n²) — kuadratik, jauh lebih lambat dari O(n)")
    return count


# ============================================================
# LATIHAN 4A – LINEAR SEARCH: O(n)
# Mencari target dalam daftar satu per satu
# Berhenti segera setelah target ditemukan (best case O(1))
# Worst case: target di akhir atau tidak ada → O(n)
# ============================================================
def linear_search(data, target):
    print("\n" + "=" * 50)
    print("  LATIHAN 4A – Linear Search O(n)")
    print("=" * 50)
    print(f"  Data  : {data}")
    print(f"  Target: {target}")
    print()

    count = 0  # Penghitung langkah pencarian

    # Periksa setiap elemen satu per satu
    for item in data:
        count += 1
        print(f"  Langkah {count} → periksa {item}", end="")

        # Jika ditemukan, hentikan pencarian
        if item == target:
            print(f"  ← DITEMUKAN! ✔")
            break
        else:
            print(f"  (bukan {target})")

    else:
        # Blok else dijalankan jika loop selesai tanpa break (tidak ditemukan)
        print(f"  → Target {target} TIDAK ditemukan dalam data.")

    print(f"\n  ✔ Jumlah langkah: {count} dari {len(data)} elemen")
    print(f"  ✔ Kompleksitas: O(n) — linear search")
    return count


# ============================================================
# LATIHAN 4B – NESTED LOOP COMPARISON: O(n²)
# Membandingkan setiap elemen dengan semua elemen lainnya
# Total langkah = n × n = n²
# Kompleksitas: O(n²) — jauh lebih lambat dari linear search
# ============================================================
def nested_loop_comparison(data):
    print("\n" + "=" * 50)
    print("  LATIHAN 4B – Nested Loop O(n²)")
    print("=" * 50)
    print(f"  Data: {data}")
    print()

    count = 0  # Penghitung total perbandingan

    # Loop luar: ambil setiap elemen i
    for i in data:
        # Loop dalam: bandingkan i dengan setiap elemen j
        for j in data:
            count += 1
            print(f"  Langkah {count:>3} → bandingkan {i} dengan {j}")

    print(f"\n  ✔ Jumlah langkah: {count}  (= {len(data)} × {len(data)})")
    print(f"  ✔ Kompleksitas: O(n²) — pertumbuhan eksponensial kuadratik")
    return count


# ============================================================
# BAGIAN UTAMA – MENJALANKAN SEMUA LATIHAN
# ============================================================

print("╔══════════════════════════════════════════════════╗")
print("║   ANALISIS KOMPLEKSITAS ALGORITMA — BIG-O       ║")
print("╚══════════════════════════════════════════════════╝")

# --- Latihan 1: O(n) ---
n1 = int(input("\n[Latihan 1] Masukkan nilai n: "))
hasil_l1 = latihan_1(n1)

# --- Latihan 2: O(2n) ---
n2 = int(input("\n[Latihan 2] Masukkan nilai n: "))
hasil_l2 = latihan_2(n2)

# --- Latihan 3: O(n²) ---
n3 = int(input("\n[Latihan 3] Masukkan nilai n (disarankan ≤ 5 untuk detail): "))
hasil_l3 = latihan_3(n3)

# --- Latihan 4A: Linear Search ---
data_search = [1, 3, 5, 7, 9, 11, 13]
target = int(input("\n[Latihan 4A] Masukkan angka yang dicari: "))
hasil_l4a = linear_search(data_search, target)

# --- Latihan 4B: Nested Loop ---
data_nested = [1, 3, 5, 7, 9]
hasil_l4b = nested_loop_comparison(data_nested)

# --- Tabel Perbandingan Akhir ---
print("\n" + "=" * 50)
print("  TABEL PERBANDINGAN HASIL")
print("=" * 50)
print(f"  {'Latihan':<30} {'Iterasi':>8}  {'Big-O'}")
print(f"  {'-'*45}")
print(f"  {'Latihan 1 – Loop tunggal':<30} {hasil_l1:>8}  O(n)")
print(f"  {'Latihan 2 – Dua loop berurutan':<30} {hasil_l2:>8}  O(2n) ≈ O(n)")
print(f"  {'Latihan 3 – Loop bersarang':<30} {hasil_l3:>8}  O(n²)")
print(f"  {'Latihan 4A – Linear search':<30} {hasil_l4a:>8}  O(n)")
print(f"  {'Latihan 4B – Nested comparison':<30} {hasil_l4b:>8}  O(n²)")
print("=" * 50)

# ============================================================
# PENDAPAT (30 kata):
# O(n) efisien dan scalable; O(n²) berbahaya untuk data besar
# karena pertumbuhannya kuadratik. Pilih algoritma linear
# search dibanding nested loop demi performa optimal.
# ============================================================