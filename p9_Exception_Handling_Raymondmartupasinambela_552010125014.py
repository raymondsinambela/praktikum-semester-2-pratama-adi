# Praktikum 9 - Exception Handling
# Raymond martupa sinambela - 552010125014
# ================================================================
# PROGRAM EXCEPTION HANDLING & INPUT VALIDASI
# Modul Praktikum – Algoritma dan Pemrograman 2
# ----------------------------------------------------------------
# Isi:
#   Latihan 1 : Validasi Input Angka    (try/except ValueError)
#   Latihan 2 : Pembagian Aman          (ValueError + ZeroDivisionError)
#   Latihan 3 : Program Berbasis Menu   (modular + exception handling)
#
# Konsep exception handling yang digunakan:
#   try    → blok kode yang mungkin memunculkan error
#   except → blok penanganan jika error terjadi
#   else   → dijalankan hanya jika try TIDAK menghasilkan error
#   finally→ selalu dijalankan, baik error maupun tidak
# ================================================================


# ================================================================
# LATIHAN 1 – VALIDASI INPUT ANGKA
# ================================================================

# ----------------------------------------------------------------
# FUNGSI: input_angka()
# ----------------------------------------------------------------
# Tujuan   : Meminta input angka dari pengguna secara berulang
#            sampai input yang diberikan benar-benar berupa angka.
#            Program tidak akan berhenti meskipun pengguna
#            memasukkan huruf, simbol, atau teks sembarang.
#
# Mekanisme:
#   - Loop while True berjalan terus hingga return dieksekusi.
#   - float(input(...)) dicoba di dalam blok try.
#   - Jika bukan angka → float() memunculkan ValueError.
#   - except ValueError menangkap error lalu meminta ulang.
#   - Jika angka valid → return langsung mengembalikan nilai.
#
# Exception yang ditangani:
#   ValueError  → input tidak dapat dikonversi ke float
#
# Return : float – angka valid yang dimasukkan pengguna
# ----------------------------------------------------------------
def input_angka():
    while True:                          # Loop tanpa batas sampai input valid
        try:
            # Coba konversi input ke float; akan error jika bukan angka
            angka = float(input("  Masukkan angka: "))
            return angka                 # Jika berhasil, kembalikan nilai

        except ValueError:
            # Ditangkap jika input tidak bisa dikonversi ke float
            # Contoh pemicu: "abc", "dua", "@#$", string kosong
            print("   Input tidak valid. Masukkan angka (contoh: 42 atau 3.14).")


# ----------------------------------------------------------------
# FUNGSI: jalankan_latihan1()
# ----------------------------------------------------------------
# Tujuan   : Menjalankan demonstrasi Latihan 1 secara interaktif.
#            Memanggil input_angka() dan menampilkan hasilnya.
# ----------------------------------------------------------------
def jalankan_latihan1():
    print("\n" + "=" * 55)
    print("  LATIHAN 1 – VALIDASI INPUT ANGKA")
    print("=" * 55)
    print("  Program akan terus meminta input hingga angka valid.")
    print("  Coba masukkan huruf atau simbol untuk melihat validasi.\n")

    angka = input_angka()   # Panggil fungsi validasi

    # Tampilkan hasil jika input valid
    print(f"\n   Angka valid diterima   : {angka}")
    print(f"   Tipe data              : {type(angka).__name__}")
    print(f"   Nilai bulat (int)      : {int(angka)}")
    print(f"   Nilai desimal (float)  : {angka:.4f}")


# ================================================================
# LATIHAN 2 – PEMBAGIAN AMAN
# ================================================================

# ----------------------------------------------------------------
# FUNGSI: pembagian_aman(a, b)
# ----------------------------------------------------------------
# Tujuan   : Melakukan operasi pembagian a / b dengan aman,
#            menangani dua kemungkinan error yang bisa terjadi.
#
# Exception yang ditangani:
#   ZeroDivisionError → penyebut (b) bernilai nol
#   (ValueError sudah ditangani sebelum fungsi ini dipanggil)
#
# Blok else    : dijalankan hanya jika pembagian BERHASIL tanpa error
# Blok finally : selalu dijalankan sebagai pesan penutup operasi
#
# Parameter : a (float) – pembilang
#             b (float) – penyebut
# Return    : float – hasil pembagian, atau None jika gagal
# ----------------------------------------------------------------
def pembagian_aman(a, b):
    hasil = None   # Nilai default jika terjadi error

    try:
        # Coba lakukan pembagian; akan error jika b == 0
        hasil = a / b

    except ZeroDivisionError:
        # Ditangkap jika penyebut bernilai tepat 0
        # Python memunculkan ZeroDivisionError untuk x / 0
        print("   ZeroDivisionError : Tidak boleh membagi dengan nol.")

    else:
        # Blok else hanya jalan jika try TIDAK menghasilkan error sama sekali
        # Tempatkan logika sukses di sini, bukan di dalam try
        print(f"   Operasi berhasil  : {a} ÷ {b} = {hasil:.4f}")

    finally:
        # Blok finally SELALU dijalankan, baik error maupun tidak
        # Cocok untuk membersihkan resource atau mencetak pesan akhir
        print("  ℹ Operasi pembagian selesai diproses.")

    return hasil   # None jika error, float jika sukses


# ----------------------------------------------------------------
# FUNGSI: jalankan_latihan2()
# ----------------------------------------------------------------
# Tujuan   : Menjalankan demonstrasi Latihan 2.
#            Meminta dua input angka dari pengguna lalu
#            memanggil pembagian_aman() untuk operasi pembagian.
# ----------------------------------------------------------------
def jalankan_latihan2():
    print("\n" + "=" * 55)
    print("  LATIHAN 2 – PEMBAGIAN AMAN")
    print("=" * 55)
    print("  Dua jenis error akan ditangani:")
    print("  1. Input bukan angka   → ValueError")
    print("  2. Penyebut bernilai 0 → ZeroDivisionError\n")

    try:
        # Coba terima dua input angka dari pengguna
        a = float(input("  Masukkan pembilang : "))
        b = float(input("  Masukkan penyebut  : "))

    except ValueError:
        # Ditangkap jika salah satu input tidak bisa dikonversi ke float
        print("   ValueError : Input harus berupa angka, bukan teks.")
        return   # Hentikan fungsi jika input tidak valid

    print()
    # Lanjutkan ke pembagian jika kedua input valid
    pembagian_aman(a, b)


# ================================================================
# LATIHAN 3 – PROGRAM BERBASIS MENU
# ================================================================

# ----------------------------------------------------------------
# FUNGSI: input_nilai(data)
# ----------------------------------------------------------------
# Tujuan   : Meminta satu nilai dari pengguna dan menyimpannya
#            ke dalam list data yang diteruskan sebagai parameter.
#
# Exception yang ditangani:
#   ValueError → input tidak bisa dikonversi ke float
#
# Validasi tambahan:
#   Nilai harus berada dalam rentang 0–100.
#   Nilai di luar rentang ditolak dengan pesan informatif.
#
# Parameter : data (list) – list nilai yang akan ditambahkan
# Return    : None – memodifikasi list secara langsung (by reference)
# ----------------------------------------------------------------
def input_nilai(data):
    try:
        nilai = float(input("  Masukkan nilai (0–100): "))

        # Validasi rentang nilai setelah konversi berhasil
        if 0 <= nilai <= 100:
            data.append(nilai)    # Tambahkan nilai ke list
            print(f"  Nilai {nilai} berhasil ditambahkan. Total data: {len(data)}")
        else:
            # Nilai di luar 0–100 ditolak secara logis (bukan error Python)
            print(f"  Nilai {nilai} di luar rentang 0–100. Data tidak disimpan.")

    except ValueError:
        # Ditangkap jika input adalah teks atau karakter non-numerik
        print("  ValueError : Input tidak valid. Masukkan angka antara 0 dan 100.")


# ----------------------------------------------------------------
# FUNGSI: hitung_rata(data)
# ----------------------------------------------------------------
# Tujuan   : Menghitung dan menampilkan statistik dari nilai yang
#            tersimpan dalam list, termasuk rata-rata, nilai
#            tertinggi, nilai terendah, dan jumlah data.
#
# Penanganan kondisi khusus:
#   Jika list kosong → informasikan tanpa error (hindari ZeroDivisionError
#   yang terjadi jika sum(data)/len(data) dipanggil pada list kosong).
#
# Parameter : data (list of float) – daftar nilai mahasiswa
# Return    : None
# ----------------------------------------------------------------
def hitung_rata(data):
    # Periksa apakah list kosong sebelum melakukan kalkulasi
    if len(data) == 0:
        print("   Data masih kosong. Masukkan nilai terlebih dahulu.")
        return   # Hentikan fungsi agar tidak terjadi ZeroDivisionError

    # Hitung statistik dasar
    rata_rata = sum(data) / len(data)   # Rata-rata = jumlah total / banyak data
    nilai_max = max(data)               # Nilai tertinggi dalam list
    nilai_min = min(data)               # Nilai terendah dalam list

    # Tentukan grade berdasarkan rata-rata
    if   rata_rata >= 85: grade = "A – Sangat Baik"
    elif rata_rata >= 70: grade = "B – Baik"
    elif rata_rata >= 55: grade = "C – Cukup"
    elif rata_rata >= 40: grade = "D – Kurang"
    else                : grade = "E – Tidak Lulus"

    # Tampilkan seluruh hasil kalkulasi
    print(f"\n  Jumlah data    : {len(data)}")
    print(f"  Rata-rata      : {rata_rata:.2f}")
    print(f"  Nilai tertinggi: {nilai_max:.2f}")
    print(f"  Nilai terendah : {nilai_min:.2f}")
    print(f"  Grade rata-rata: {grade}")


# ----------------------------------------------------------------
# FUNGSI: tampilkan_data(data)
# ----------------------------------------------------------------
# Tujuan   : Menampilkan seluruh data nilai dalam format tabel
#            yang rapi, disertai nomor urut dan status kelulusan.
#
# Penanganan kondisi khusus:
#   Jika list kosong → informasikan tanpa error.
#
# Parameter : data (list of float) – daftar nilai mahasiswa
# Return    : None
# ----------------------------------------------------------------
def tampilkan_data(data):
    if len(data) == 0:
        # Tangani list kosong agar tidak terjadi error saat iterasi
        print("   Data masih kosong. Belum ada nilai yang dimasukkan.")
        return

    # Cetak header tabel
    print(f"\n  {'No':>4}  {'Nilai':>8}  {'Status'}")
    print(f"  {'-'*4}  {'-'*8}  {'-'*12}")

    # Cetak setiap nilai beserta status kelulusannya
    for i, nilai in enumerate(data):
        status = "Lulus" if nilai >= 55 else "Tidak Lulus"
        print(f"  {i+1:>4}  {nilai:>8.2f}  {status}")

    print(f"  {'-'*4}  {'-'*8}  {'-'*12}")
    print(f"  Total: {len(data)} data nilai")


# ----------------------------------------------------------------
# FUNGSI: hapus_data(data)
# ----------------------------------------------------------------
# Tujuan   : Menghapus satu nilai dari list berdasarkan nomor urut
#            yang dimasukkan pengguna.
#
# Exception yang ditangani:
#   ValueError    → input nomor bukan angka bulat
#   IndexError    → nomor urut di luar rentang index list
#
# Parameter : data (list of float) – daftar nilai mahasiswa
# Return    : None – memodifikasi list secara langsung
# ----------------------------------------------------------------
def hapus_data(data):
    if len(data) == 0:
        print("   Data masih kosong. Tidak ada yang bisa dihapus.")
        return

    # Tampilkan data terlebih dahulu agar pengguna tahu nomor yang valid
    tampilkan_data(data)

    try:
        nomor = int(input("\n  Masukkan nomor data yang ingin dihapus: "))

        # Konversi nomor urut (1-based) ke index Python (0-based)
        index = nomor - 1

        # Akses elemen; akan memunculkan IndexError jika di luar rentang
        nilai_dihapus = data[index]
        data.pop(index)           # Hapus elemen dari list
        print(f"   Nilai {nilai_dihapus} berhasil dihapus.")

    except ValueError:
        # Ditangkap jika input nomor bukan bilangan bulat
        print("   ValueError : Nomor urut harus berupa bilangan bulat.")

    except IndexError:
        # Ditangkap jika nomor urut melebihi jumlah data
        print(f"   IndexError : Nomor tidak valid. Rentang yang tersedia: 1–{len(data)+1}.")


# ----------------------------------------------------------------
# FUNGSI: menu()
# ----------------------------------------------------------------
# Tujuan   : Menjalankan program utama berbasis menu yang berjalan
#            terus menerus sampai pengguna memilih keluar.
#            Setiap pilihan menu memanggil fungsi yang sesuai.
#
# Menu yang tersedia:
#   1. Input Nilai    → input_nilai()
#   2. Hitung Rata    → hitung_rata()
#   3. Tampilkan Data → tampilkan_data()
#   4. Hapus Data     → hapus_data()
#   5. Keluar         → break (hentikan loop)
#
# Exception yang ditangani:
#   KeyboardInterrupt → pengguna menekan Ctrl+C
# ----------------------------------------------------------------
def menu():
    data = []   # List kosong sebagai wadah nilai; dibagi ke semua fungsi

    # Loop utama program; hanya berhenti jika pilihan "5" atau Ctrl+C
    while True:
        # Tampilkan menu setiap putaran
        print("\n" + "─" * 40)
        print("  MENU UTAMA")
        print("─" * 40)
        print("  1. Input Nilai")
        print("  2. Hitung Rata-rata & Statistik")
        print("  3. Tampilkan Semua Data")
        print("  4. Hapus Data")
        print("  5. Keluar")
        print("─" * 40)

        try:
            pilihan = input("  Pilih menu (1-5): ").strip()   # Terima pilihan menu

        except KeyboardInterrupt:
            # Tangkap Ctrl+C agar program keluar dengan bersih tanpa traceback
            print("\n\n  Program dihentikan oleh pengguna.")
            break

        # Routing pilihan menu ke fungsi yang sesuai
        if   pilihan == "1":
            input_nilai(data)       # Tambah nilai baru
        elif pilihan == "2":
            hitung_rata(data)       # Tampilkan statistik
        elif pilihan == "3":
            tampilkan_data(data)    # Tampilkan semua data
        elif pilihan == "4":
            hapus_data(data)        # Hapus satu data
        elif pilihan == "5":
            print("\n  Terima kasih. Program selesai.")
            break                   # Keluar dari loop → program berakhir
        else:
            # Tangkap pilihan di luar 1–5
            print(f"   Pilihan '{pilihan}' tidak valid. Masukkan angka 1–5.")


# ================================================================
# PROGRAM UTAMA – MENJALANKAN SEMUA LATIHAN SECARA BERURUTAN
# ================================================================

print("╔═══════════════════════════════════════════════════════╗")
print("║   EXCEPTION HANDLING & INPUT VALIDASI                ║")
print("║   Latihan 1 | Latihan 2 | Latihan 3 (Menu)           ║")
print("╚═══════════════════════════════════════════════════════╝")

# ── Latihan 1: Validasi Input Angka ──────────────────────────────
jalankan_latihan1()

# ── Latihan 2: Pembagian Aman ─────────────────────────────────────
jalankan_latihan2()

# ── Latihan 3: Program Berbasis Menu ─────────────────────────────
print("\n" + "=" * 55)
print("  LATIHAN 3 – PROGRAM BERBASIS MENU")
print("=" * 55)
print("  Program menu akan berjalan terus hingga Anda memilih")
print("  menu 5 (Keluar) atau menekan Ctrl+C.\n")
menu()


# ================================================================
# KESIMPULAN
# ================================================================
# Exception handling adalah mekanisme penting yang membuat program
# lebih tangguh dan ramah pengguna. Blok try menampung kode yang
# berpotensi error; except menangkap dan menangani error secara
# spesifik per jenisnya; else hanya berjalan jika try sukses tanpa
# error; finally selalu berjalan untuk membersihkan resource.
#
# Pada program ini terdapat tiga jenis exception yang ditangani:
# ValueError untuk input non-numerik, ZeroDivisionError untuk
# pembagian dengan nol, dan IndexError untuk akses indeks di luar
# rentang list. Penggunaan exception handling yang tepat mencegah
# program crash secara tiba-tiba dan memungkinkan pengguna
# mendapatkan pesan error yang informatif sehingga mereka tahu
# apa yang harus diperbaiki. Program berbasis menu (Latihan 3)
# menggabungkan loop while True dengan exception handling untuk
# menciptakan antarmuka yang responsif dan tidak mudah rusak
# meskipun pengguna memberikan input yang tidak terduga.
# ================================================================