# Praktikum 6 - sorting
# Raymond martupa sinambela - 552010125014
# ================================================================
# PROGRAM ALGORITMA PENGURUTAN (SORTING)
# Modul Praktikum 7 – Algoritma dan Pemrograman 2
# Isi:
#   Latihan 1 : Bubble Sort
#   Latihan 2 : Selection Sort
#   Latihan 3 : Insertion Sort
#   Latihan 4 : Tabel Perbandingan (6, 10, 20 elemen)
#   Challenge  : Insertion Sort – hampir terurut vs acak
# ================================================================

import random


# ================================================================
# LATIHAN 1 – BUBBLE SORT
# ----------------------------------------------------------------
# Cara kerja:
#   Bandingkan dua elemen yang bersebelahan (data[j] dan data[j+1]).
#   Jika elemen kiri lebih besar, tukar posisi keduanya.
#   Ulangi proses hingga seluruh data terurut dari kecil ke besar.
#   Setiap satu putaran luar (pass), elemen terbesar "menggelembung"
#   ke posisi paling kanan yang belum terisi.
#
# Kompleksitas waktu:
#   - Best case  : O(n)   → data sudah terurut (dengan optimasi early stop)
#   - Worst case : O(n²)  → data terbalik
#   - Average    : O(n²)
#
# Parameter  : data (list) – daftar angka yang akan diurutkan
# Return     : (list terurut, jumlah perbandingan)
# ================================================================
def bubble_sort(data):
    n     = len(data)   # Jumlah elemen dalam daftar
    count = 0           # Penghitung jumlah perbandingan antar elemen

    # Loop luar: setiap iterasi memindahkan 1 elemen terbesar ke akhir
    # Setelah pass ke-i, elemen ke-(n-i) sudah berada di posisi final
    for i in range(n):

        # Loop dalam: bandingkan pasangan elemen yang berdekatan
        # Batas atas dikurangi i karena i elemen terakhir sudah terurut
        for j in range(0, n - i - 1):

            count += 1  # Tambah hitungan setiap ada perbandingan

            # Jika elemen kiri lebih besar dari elemen kanan, tukar
            # Python mendukung swap satu baris tanpa variabel temp
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data, count  # Kembalikan data terurut dan total perbandingan


# ================================================================
# LATIHAN 2 – SELECTION SORT
# ----------------------------------------------------------------
# Cara kerja:
#   Cari elemen terkecil dari bagian data yang belum terurut,
#   lalu pindahkan (tukar) ke posisi paling kiri yang tersedia.
#   Proses diulang mulai dari posisi berikutnya hingga data habis.
#
# Perbedaan utama dari Bubble Sort:
#   Selection Sort selalu melakukan n*(n-1)/2 perbandingan,
#   tidak peduli apakah data sudah terurut atau belum.
#   Jumlah pertukaran (swap) minimal – hanya 1 swap per pass.
#
# Kompleksitas waktu:
#   - Best / Worst / Average : O(n²) → selalu konsisten
#
# Parameter  : data (list) – daftar angka yang akan diurutkan
# Return     : (list terurut, jumlah perbandingan)
# ================================================================
def selection_sort(data):
    n     = len(data)   # Jumlah elemen dalam daftar
    count = 0           # Penghitung jumlah perbandingan

    # Loop luar: tentukan posisi yang akan diisi elemen minimum
    for i in range(n):

        min_index = i   # Asumsikan elemen ke-i adalah yang terkecil dulu

        # Loop dalam: cari elemen terkecil dari posisi i+1 hingga akhir
        for j in range(i + 1, n):

            count += 1  # Tambah hitungan setiap ada perbandingan

            # Jika ditemukan elemen lebih kecil, perbarui indeks minimum
            if data[j] < data[min_index]:
                min_index = j   # Catat posisi elemen terkecil baru

        # Tukar elemen posisi i dengan elemen terkecil yang ditemukan
        # Jika min_index == i, swap tidak mengubah apa pun (tetap efisien)
        data[i], data[min_index] = data[min_index], data[i]

    return data, count  # Kembalikan data terurut dan total perbandingan


# ================================================================
# LATIHAN 3 – INSERTION SORT
# ----------------------------------------------------------------
# Cara kerja:
#   Anggap elemen pertama sudah "terurut" (karena hanya 1 elemen).
#   Ambil elemen berikutnya sebagai 'key', lalu sisipkan ke posisi
#   yang tepat di antara elemen-elemen yang sudah terurut di kirinya.
#   Geser semua elemen yang lebih besar dari key ke kanan satu posisi
#   untuk memberi ruang bagi key.
#
# Keunggulan:
#   Sangat efisien pada data yang hampir terurut karena loop while
#   hanya aktif sedikit atau tidak aktif sama sekali.
#
# Kompleksitas waktu:
#   - Best case  : O(n)   → data sudah terurut (while tidak aktif)
#   - Worst case : O(n²)  → data terbalik total
#   - Average    : O(n²)
#
# Parameter  : data (list) – daftar angka yang akan diurutkan
# Return     : (list terurut, jumlah perbandingan)
# ================================================================
def insertion_sort(data):
    count = 0   # Penghitung jumlah perbandingan

    # Mulai dari elemen kedua (indeks 1)
    # Elemen pertama (indeks 0) dianggap sudah terurut sendiri
    for i in range(1, len(data)):

        key = data[i]   # Elemen yang akan disisipkan ke posisi yang tepat
        j   = i - 1     # Mulai bandingkan dari elemen tepat di sebelah kiri

        # Geser elemen yang lebih besar dari key ke satu posisi ke kanan
        # Loop berhenti jika sudah mencapai ujung kiri atau elemen ≤ key
        while j >= 0 and data[j] > key:
            count      += 1     # Tambah hitungan setiap ada perbandingan
            data[j + 1] = data[j]   # Geser elemen ke kanan
            j          -= 1         # Mundur satu posisi ke kiri

        # Hitung satu perbandingan terakhir yang menghentikan loop while
        # (perbandingan saat data[j] <= key atau j sudah habis)
        if j >= 0:
            count += 1

        # Sisipkan key ke posisi yang benar (tepat setelah j)
        data[j + 1] = key

    return data, count  # Kembalikan data terurut dan total perbandingan


# ================================================================
# LATIHAN 4 – TABEL PERBANDINGAN TIGA ALGORITMA SORTING
# ----------------------------------------------------------------
# Menguji ketiga algoritma pada ukuran data 6, 10, dan 20 elemen
# menggunakan data acak yang SAMA (random.seed agar reproducible).
# Mencatat jumlah perbandingan lalu menampilkan dalam bentuk tabel.
# ================================================================
def cetak_tabel_perbandingan():
    print("\n" + "=" * 62)
    print("  LATIHAN 4 – TABEL PERBANDINGAN TIGA SORTING ALGORITHM")
    print("=" * 62)

    ukuran_data = [6, 10, 20]   # Ukuran data yang akan diuji

    # Cetak baris header tabel
    print(f"\n  {'Jumlah Data':>13} | {'Bubble':>9} | {'Selection':>11} | {'Insertion':>11}")
    print(f"  {'-'*13}-+-{'-'*9}-+-{'-'*11}-+-{'-'*11}")

    # Jalankan pengujian untuk setiap ukuran data
    for n in ukuran_data:
        random.seed(42)                         # Seed tetap agar data selalu sama
        data = random.sample(range(1, 100), n)  # Buat data acak tanpa duplikat

        # Jalankan ketiga algoritma menggunakan salinan data yang sama
        _, c_bubble    = bubble_sort(data[:])
        _, c_selection = selection_sort(data[:])
        _, c_insertion = insertion_sort(data[:])

        # Cetak satu baris hasil untuk ukuran data ini
        print(f"  {n:>13} | {c_bubble:>9} | {c_selection:>11} | {c_insertion:>11}")

    # Cetak baris analisis di bawah tabel
    print()
    print("  Analisis:")
    print("  • Insertion Sort paling sedikit perbandingan pada data acak")
    print("  • Selection Sort selalu n*(n-1)/2 perbandingan (paling konsisten)")
    print("  • Insertion Sort paling stabil pada data hampir terurut (mendekati O(n))")


# ================================================================
# CHALLENGE – INSERTION SORT: DATA HAMPIR TERURUT vs DATA ACAK
# ----------------------------------------------------------------
# Tujuan:
#   Membuktikan secara empiris bahwa Insertion Sort jauh lebih
#   efisien pada data yang hampir terurut dibandingkan data acak.
#
# Metode:
#   - Data hampir terurut : list [1..n] lalu 2 pasang elemen ditukar
#   - Data acak           : urutan sepenuhnya tidak beraturan
#   Kedua data berukuran sama (n=20) agar perbandingan adil.
# ================================================================
def challenge_insertion_sort():
    print("\n" + "=" * 62)
    print("  CHALLENGE – INSERTION SORT: Hampir Terurut vs Acak")
    print("=" * 62)

    n = 20  # Ukuran data yang digunakan untuk kedua pengujian

    # Buat data hampir terurut:
    #   Mulai dari urutan sempurna [1, 2, 3, ..., 20]
    #   lalu tukar 2 pasang elemen secara manual agar "hampir terurut"
    data_hampir = list(range(1, n + 1))     # Data awal terurut sempurna
    data_hampir[3],  data_hampir[11] = data_hampir[11],  data_hampir[3]   # Tukar posisi 3 & 11
    data_hampir[7],  data_hampir[16] = data_hampir[16],  data_hampir[7]   # Tukar posisi 7 & 16

    # Buat data acak:
    #   Ambil 20 angka berbeda dari 1–100 secara acak
    random.seed(99)                                 # Seed untuk reproducibility
    data_acak = random.sample(range(1, 101), n)     # Data benar-benar acak

    # Jalankan Insertion Sort pada kedua data
    hasil_hampir, c_hampir = insertion_sort(data_hampir[:])
    hasil_acak,   c_acak   = insertion_sort(data_acak[:])

    # Tampilkan data input dan hasil perbandingan
    print(f"\n  Data hampir terurut : {data_hampir}")
    print(f"  Hasil               : {hasil_hampir}")
    print(f"  Jumlah perbandingan : {c_hampir}")

    print(f"\n  Data acak           : {data_acak}")
    print(f"  Hasil               : {hasil_acak}")
    print(f"  Jumlah perbandingan : {c_acak}")

    # Hitung dan tampilkan selisih efisiensi
    selisih = c_acak - c_hampir
    persen  = (selisih / c_acak * 100) if c_acak > 0 else 0

    print(f"\n  Selisih             : {selisih} langkah lebih sedikit")
    print(f"  Efisiensi           : {persen:.1f}% lebih hemat pada data hampir terurut")

    # Penjelasan mengapa perbedaan ini terjadi
    print()
    print("  Penjelasan perbedaan:")
    print("  • Data hampir terurut → loop while jarang aktif karena elemen")
    print("    kiri sudah berada di urutan yang benar → perbandingan sedikit")
    print("  • Data acak → loop while aktif banyak, elemen harus digeser")
    print("    berkali-kali sebelum key menemukan posisi tepatnya")
    print("  • Ini membuktikan: Insertion Sort = O(n) best case, O(n²) worst case")


# ================================================================
# BAGIAN UTAMA – MENJALANKAN SEMUA LATIHAN SECARA BERURUTAN
# ================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║   ALGORITMA PENGURUTAN: Bubble | Selection | Insertion    ║")
print("╚════════════════════════════════════════════════════════════╝")

# ── Latihan 1: Bubble Sort ────────────────────────────────────────
data_uji = [5, 2, 9, 1, 5, 6]  # Data uji standar 6 elemen

print("\n" + "=" * 62)
print("  LATIHAN 1 – BUBBLE SORT")
print("=" * 62)
print(f"  Data awal             : {data_uji}")

hasil, langkah = bubble_sort(data_uji[:])   # Kirim salinan agar data asli tidak berubah
print(f"  Hasil terurut         : {hasil}")
print(f"  Jumlah perbandingan   : {langkah}")
print(f"  Kompleksitas          : O(n²)")

# ── Pengujian berbagai ukuran data untuk Bubble Sort ─────────────
print("\n  [Pengujian berbagai ukuran data]")
for ukuran in [6, 10, 20]:
    random.seed(42)
    d = random.sample(range(1, 100), ukuran)    # Data acak berukuran bervariasi
    _, c = bubble_sort(d[:])
    print(f"  n={ukuran:<3} → {c} perbandingan")

# ── Latihan 2: Selection Sort ─────────────────────────────────────
data_uji = [5, 2, 9, 1, 5, 6]  # Reset data uji

print("\n" + "=" * 62)
print("  LATIHAN 2 – SELECTION SORT")
print("=" * 62)
print(f"  Data awal             : {data_uji}")

hasil, langkah = selection_sort(data_uji[:])
print(f"  Hasil terurut         : {hasil}")
print(f"  Jumlah perbandingan   : {langkah}")
print(f"  Kompleksitas          : O(n²)")

print("\n  [Pengujian berbagai ukuran data]")
for ukuran in [6, 10, 20]:
    random.seed(42)
    d = random.sample(range(1, 100), ukuran)
    _, c = selection_sort(d[:])
    print(f"  n={ukuran:<3} → {c} perbandingan")

# ── Latihan 3: Insertion Sort ─────────────────────────────────────
data_uji = [5, 2, 9, 1, 5, 6]

print("\n" + "=" * 62)
print("  LATIHAN 3 – INSERTION SORT")
print("=" * 62)
print(f"  Data awal             : {data_uji}")

hasil, langkah = insertion_sort(data_uji[:])
print(f"  Hasil terurut         : {hasil}")
print(f"  Jumlah perbandingan   : {langkah}")
print(f"  Kompleksitas          : O(n²) worst | O(n) best")

print("\n  [Pengujian berbagai ukuran data]")
for ukuran in [6, 10, 20]:
    random.seed(42)
    d = random.sample(range(1, 100), ukuran)
    _, c = insertion_sort(d[:])
    print(f"  n={ukuran:<3} → {c} perbandingan")

# ── Latihan 4: Tabel Perbandingan ────────────────────────────────
cetak_tabel_perbandingan()

# ── Challenge ────────────────────────────────────────────────────
challenge_insertion_sort()

# ================================================================
# KESIMPULAN
# ----------------------------------------------------------------
# Bubble Sort dan Selection Sort selalu O(n²) tanpa pengecualian.
# Insertion Sort unggul pada data hampir terurut karena loop dalam
# jarang aktif sehingga mendekati kompleksitas linear O(n).
# Untuk data kecil semua algoritma layak; data besar gunakan
# algoritma yang lebih efisien seperti Merge Sort atau Quick Sort.
# ================================================================