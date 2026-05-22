# Praktikum 5 - linear search dan binary search
# Raymond martupa sinambela - 552010125014
# ============================================================
#  Search Algorithm Comparison
#  Linear Search vs Binary Search
#  Latihan 1, 2, 3 & Challenge
# ============================================================


def linear_search(data, target):
    # Menelusuri setiap elemen dari kiri ke kanan satu per satu.
    # Tidak memerlukan data terurut.
    # Kompleksitas: O(n) — langkah bertambah seiring panjang data.
    count = 0
    for i in range(len(data)):
        count += 1
        if data[i] == target:
            return i, count  # Kembalikan posisi dan jumlah langkah
    return -1, count  # -1 berarti target tidak ditemukan


def binary_search(data, target):
    # Membelah ruang pencarian menjadi dua pada setiap iterasi.
    # SYARAT WAJIB: data harus sudah terurut secara menaik.
    # Kompleksitas: O(log n) — jauh lebih efisien pada data besar.
    low, high, count = 0, len(data) - 1, 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if data[mid] == target:
            return mid, count       # Target ditemukan tepat di tengah
        elif data[mid] < target:
            low = mid + 1           # Buang sisi kiri, cari di kanan
        else:
            high = mid - 1          # Buang sisi kanan, cari di kiri
    return -1, count  # -1 berarti target tidak ditemukan


def print_separator(char="─", width=60):
    # Fungsi bantu untuk mencetak garis pemisah antar bagian output.
    print(char * width)


def run_test(label, data, target, allow_binary=True):
    # Menjalankan kedua algoritma pada satu kasus uji,
    # lalu mencetak posisi dan jumlah langkah masing-masing.
    pos_l, steps_l = linear_search(data, target)
    print(f"  Target       : {target}")
    print(f"  Linear Search: posisi={pos_l}, langkah={steps_l}")
    if allow_binary:
        pos_b, steps_b = binary_search(data, target)
        print(f"  Binary Search: posisi={pos_b}, langkah={steps_b}")
    print()


# ============================================================
#  LATIHAN 1 & 2 — Data kecil
# ============================================================
print_separator("=")
print("  LATIHAN 1 & 2 — Data kecil: [4, 8, 15, 16, 23, 42]")
print_separator("=")

data_kecil = [4, 8, 15, 16, 23, 42]
kasus = [
    ("Target di awal",   4),
    ("Target di tengah", 15),
    ("Target di akhir",  42),
    ("Target tidak ada", 99),
]
for label, target in kasus:
    print(f"[{label}]")
    run_test(label, data_kecil, target)

# Kesimpulan Latihan 1 & 2:
# Pada data kecil, perbedaan langkah belum terlalu signifikan.
# Linear unggul hanya jika target kebetulan berada di awal data.
# Binary Search lebih konsisten di posisi tengah hingga akhir.


# ============================================================
#  LATIHAN 3 — Data besar (1–100)
# ============================================================
print_separator("=")
print("  LATIHAN 3 — Data besar: [1 … 100]")
print_separator("=")

data_besar = list(range(1, 101))
kasus_besar = [
    ("Target di awal",   1),
    ("Target di tengah", 50),
    ("Target di akhir",  100),
    ("Target tidak ada", 999),
]
for label, target in kasus_besar:
    print(f"[{label}]")
    run_test(label, data_besar, target)

# Kesimpulan Latihan 3:
# Keunggulan Binary Search semakin nyata pada data besar.
# Target=50 diselesaikan Binary dalam 1 langkah vs 50 langkah Linear.
# Target=100 diselesaikan Binary dalam 7 langkah vs 100 langkah Linear.
# Rumus maksimum Binary Search: log2(100) ≈ 7 langkah.


# ============================================================
#  CHALLENGE — Binary Search pada data TIDAK terurut
# ============================================================
print_separator("=")
print("  CHALLENGE — Binary Search pada data tidak terurut")
print_separator("=")

data_acak = [42, 8, 15, 4, 23, 16]
print(f"  Data (tidak terurut): {data_acak}")
print()

for target in [4, 42, 15]:
    pos_l, steps_l = linear_search(data_acak, target)
    pos_b, steps_b = binary_search(data_acak, target)
    status = "✓ Benar" if pos_l == pos_b else "✗ SALAH (false negative)"
    print(f"  Target {target:>2} | Linear: posisi={pos_l} | Binary: posisi={pos_b} | {status}")

print()
print_separator()

# Kesimpulan Challenge:
# Binary Search pada data tidak terurut menghasilkan false negative —
# target yang sesungguhnya ada di data dikembalikan sebagai -1 (tidak ditemukan).
# Penyebabnya: saat data[mid] < target, algoritma membuang seluruh sisi kiri.
# Asumsi ini hanya valid jika semua elemen kiri memang lebih kecil dari target,
# yang hanya terjamin pada data yang sudah terurut.
# Solusi: urutkan data terlebih dahulu dengan sorted() sebelum Binary Search.
print_separator()