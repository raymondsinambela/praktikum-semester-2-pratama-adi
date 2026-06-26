"""
=====================================================================
PRAKTIKUM ALGORITMA DAN PEMROGRAMAN 2 - PERTEMUAN 10
Tema   : Sistem Manajemen Nilai Mahasiswa menggunakan Dictionary dan Set
Konsep : - Dictionary sebagai struktur data utama
         - Set untuk menghitung jumlah nilai unik
         - Pemrograman modular (setiap fitur dipisah menjadi fungsi)
=====================================================================
"""

# ---------------------------------------------------------------------
# KONSTANTA GLOBAL
# ---------------------------------------------------------------------
KKM = 75  # Kriteria Ketuntasan Minimal untuk menentukan status lulus

# ---------------------------------------------------------------------
# STRUKTUR DATA UTAMA
# ---------------------------------------------------------------------
# Dictionary 'mahasiswa' menyimpan seluruh data dengan format:
# {
#     "NIM": {
#         "nama": "...",
#         "nilai": ...
#     }
# }
mahasiswa = {}


# =======================================================================
# FUNGSI BANTUAN: VALIDASI INPUT NILAI
# =======================================================================
def input_nilai():
    """
    Meminta input nilai dari pengguna dengan validasi ganda:
    1. Menggunakan try-except untuk memastikan input berupa angka.
    2. Memastikan nilai berada pada rentang 0 sampai 100.
    Mengembalikan nilai (float) yang valid.
    """
    while True:
        try:
            nilai = float(input("Masukkan nilai (0-100): "))
            if 0 <= nilai <= 100:
                return nilai
            print("⚠️  Nilai harus berada pada rentang 0 sampai 100.")
        except ValueError:
            print("⚠️  Input tidak valid. Harap masukkan angka.")


# =======================================================================
# 1. TAMBAH MAHASISWA
# =======================================================================
def tambah_mahasiswa():
    """
    Menambahkan data mahasiswa baru ke dalam dictionary 'mahasiswa'.
    - NIM tidak boleh kosong.
    - Jika NIM sudah terdaftar, pengguna akan diminta konfirmasi
      apakah ingin memperbarui (update) data tersebut.
    """
    print("\n--- TAMBAH DATA MAHASISWA ---")
    nim = input("Masukkan NIM   : ").strip()

    if nim == "":
        print("⚠️  NIM tidak boleh kosong. Data dibatalkan.")
        return

    # Jika NIM sudah ada, minta konfirmasi sebelum menimpa data
    if nim in mahasiswa:
        data_lama = mahasiswa[nim]
        konfirmasi = input(
            f"NIM '{nim}' sudah terdaftar atas nama '{data_lama['nama']}'. "
            "Perbarui data? (y/n): "
        ).strip().lower()
        if konfirmasi != "y":
            print("❎ Penambahan data dibatalkan.")
            return

    nama = input("Masukkan Nama  : ").strip()
    if nama == "":
        print("⚠️  Nama tidak boleh kosong. Data dibatalkan.")
        return

    nilai = input_nilai()

    mahasiswa[nim] = {"nama": nama, "nilai": nilai}
    print(f"✅ Data mahasiswa '{nama}' (NIM: {nim}) berhasil disimpan.")


# =======================================================================
# 2. TAMPILKAN SELURUH DATA
# =======================================================================
def tampilkan_semua():
    """
    Menampilkan seluruh data mahasiswa dalam bentuk tabel rapi.
    Setiap baris diberi nomor urut dan status kelulusan (KKM = 75).
    """
    print("\n--- DAFTAR SELURUH MAHASISWA ---")

    if tidak_ada_data():
        return

    garis = "-" * 65
    print(garis)
    print(f"{'No':<4}{'NIM':<15}{'Nama':<20}{'Nilai':<10}{'Status'}")
    print(garis)

    for nomor, (nim, data) in enumerate(mahasiswa.items(), start=1):
        status = "Lulus" if data["nilai"] >= KKM else "Tidak Lulus"
        print(
            f"{nomor:<4}{nim:<15}{data['nama']:<20}"
            f"{data['nilai']:<10.2f}{status}"
        )

    print(garis)


# =======================================================================
# 3. CARI MAHASISWA BERDASARKAN NIM
# =======================================================================
def cari_mahasiswa():
    """
    Mencari data mahasiswa berdasarkan NIM.
    Pencarian tidak membedakan huruf besar dan kecil (case-insensitive),
    sehingga NIM yang mengandung huruf tetap dapat ditemukan.
    """
    print("\n--- CARI MAHASISWA BERDASARKAN NIM ---")

    if tidak_ada_data():
        return

    nim_dicari = input("Masukkan NIM yang dicari: ").strip().lower()

    for nim, data in mahasiswa.items():
        if nim.lower() == nim_dicari:
            status = "Lulus" if data["nilai"] >= KKM else "Tidak Lulus"
            print("\n✅ Data ditemukan:")
            print(f"NIM    : {nim}")
            print(f"Nama   : {data['nama']}")
            print(f"Nilai  : {data['nilai']:.2f}")
            print(f"Status : {status}")
            return

    print("❌ Data dengan NIM tersebut tidak ditemukan.")


# =======================================================================
# 4. EDIT DATA MAHASISWA
# =======================================================================
def edit_mahasiswa():
    """
    Mengubah data (nama dan/atau nilai) mahasiswa berdasarkan NIM.
    Pencarian NIM bersifat case-insensitive.
    """
    print("\n--- EDIT DATA MAHASISWA ---")

    if tidak_ada_data():
        return

    nim_dicari = input("Masukkan NIM yang ingin diedit: ").strip().lower()
    nim_asli = cari_nim_asli(nim_dicari)

    if nim_asli is None:
        print("❌ Data dengan NIM tersebut tidak ditemukan.")
        return

    data_lama = mahasiswa[nim_asli]
    print(f"Data saat ini -> Nama: {data_lama['nama']}, Nilai: {data_lama['nilai']:.2f}")

    nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ").strip()
    ubah_nilai = input("Ubah nilai? (y/n): ").strip().lower()

    if nama_baru != "":
        data_lama["nama"] = nama_baru

    if ubah_nilai == "y":
        data_lama["nilai"] = input_nilai()

    print("✅ Data berhasil diperbarui.")


# =======================================================================
# 5. HAPUS MAHASISWA
# =======================================================================
def hapus_mahasiswa():
    """
    Menghapus data mahasiswa berdasarkan NIM.
    Sebelum menghapus, sistem akan meminta konfirmasi terlebih dahulu
    agar data tidak terhapus secara tidak sengaja.
    """
    print("\n--- HAPUS DATA MAHASISWA ---")

    if tidak_ada_data():
        return

    nim_dicari = input("Masukkan NIM yang ingin dihapus: ").strip().lower()
    nim_asli = cari_nim_asli(nim_dicari)

    if nim_asli is None:
        print("❌ Data dengan NIM tersebut tidak ditemukan.")
        return

    nama = mahasiswa[nim_asli]["nama"]
    konfirmasi = input(
        f"Yakin ingin menghapus data '{nama}' (NIM: {nim_asli})? (y/n): "
    ).strip().lower()

    if konfirmasi == "y":
        del mahasiswa[nim_asli]
        print("🗑️  Data berhasil dihapus.")
    else:
        print("❎ Penghapusan dibatalkan.")


# =======================================================================
# 6. TAMPILKAN JUMLAH MAHASISWA
# =======================================================================
def jumlah_mahasiswa():
    """
    Menampilkan jumlah total mahasiswa yang tersimpan dalam dictionary.
    Memanfaatkan fungsi bawaan len() pada dictionary.
    """
    print(f"\n📊 Jumlah total mahasiswa: {len(mahasiswa)} orang.")


# =======================================================================
# 7. TAMPILKAN JUMLAH NILAI UNIK (MENGGUNAKAN SET)
# =======================================================================
def jumlah_nilai_unik():
    """
    Menghitung jumlah nilai yang unik (tanpa duplikasi) menggunakan set.
    Set secara otomatis akan menghilangkan nilai-nilai yang sama.
    """
    print("\n--- JUMLAH NILAI UNIK ---")

    if tidak_ada_data():
        return

    # Mengambil seluruh nilai, lalu memasukkannya ke dalam set
    himpunan_nilai = {data["nilai"] for data in mahasiswa.values()}

    print(f"📊 Jumlah nilai unik: {len(himpunan_nilai)}")
    print(f"📋 Daftar nilai unik (terurut): {sorted(himpunan_nilai)}")


# =======================================================================
# 8. TAMPILKAN NILAI TERTINGGI
# =======================================================================
def nilai_tertinggi():
    """
    Mencari dan menampilkan mahasiswa dengan nilai tertinggi
    menggunakan fungsi max() dengan key berupa nilai mahasiswa.
    """
    print("\n--- NILAI TERTINGGI ---")

    if tidak_ada_data():
        return

    nim_terbaik = max(mahasiswa, key=lambda n: mahasiswa[n]["nilai"])
    data = mahasiswa[nim_terbaik]
    print(f"🏆 NIM: {nim_terbaik} | Nama: {data['nama']} | Nilai: {data['nilai']:.2f}")


# =======================================================================
# 9. TAMPILKAN NILAI TERENDAH
# =======================================================================
def nilai_terendah():
    """
    Mencari dan menampilkan mahasiswa dengan nilai terendah
    menggunakan fungsi min() dengan key berupa nilai mahasiswa.
    """
    print("\n--- NILAI TERENDAH ---")

    if tidak_ada_data():
        return

    nim_terendah = min(mahasiswa, key=lambda n: mahasiswa[n]["nilai"])
    data = mahasiswa[nim_terendah]
    print(f"🔻 NIM: {nim_terendah} | Nama: {data['nama']} | Nilai: {data['nilai']:.2f}")


# =======================================================================
# 10. TAMPILKAN NILAI RATA-RATA
# =======================================================================
def nilai_rata_rata():
    """
    Menghitung dan menampilkan rata-rata nilai seluruh mahasiswa.
    """
    print("\n--- NILAI RATA-RATA ---")

    if tidak_ada_data():
        return

    daftar_nilai = [data["nilai"] for data in mahasiswa.values()]
    rata = sum(daftar_nilai) / len(daftar_nilai)

    print(f"📊 Rata-rata nilai seluruh mahasiswa: {rata:.2f}")


# =======================================================================
# 11. URUTKAN DATA BERDASARKAN NIM
# =======================================================================
def urutkan_by_nim():
    """
    Menampilkan data mahasiswa yang sudah diurutkan berdasarkan NIM
    secara ascending menggunakan fungsi sorted().
    """
    print("\n--- DATA TERURUT BERDASARKAN NIM ---")

    if tidak_ada_data():
        return

    daftar_terurut = sorted(mahasiswa.items())
    cetak_tabel(daftar_terurut)


# =======================================================================
# 12. URUTKAN DATA BERDASARKAN NILAI
# =======================================================================
def urutkan_by_nilai():
    """
    Menampilkan data mahasiswa yang sudah diurutkan berdasarkan nilai
    secara descending (dari nilai tertinggi ke terendah).
    """
    print("\n--- DATA TERURUT BERDASARKAN NILAI (TERTINGGI -> TERENDAH) ---")

    if tidak_ada_data():
        return

    daftar_terurut = sorted(
        mahasiswa.items(), key=lambda item: item[1]["nilai"], reverse=True
    )
    cetak_tabel(daftar_terurut)


# =======================================================================
# 13. TAMPILKAN STATISTIK NILAI
# =======================================================================
def statistik_nilai():
    """
    Menampilkan statistik lengkap nilai mahasiswa, meliputi:
    - Jumlah mahasiswa
    - Nilai tertinggi, terendah, dan rata-rata
    - Jumlah nilai unik (menggunakan set)
    - Jumlah mahasiswa lulus dan tidak lulus berdasarkan KKM
    """
    print("\n--- STATISTIK NILAI MAHASISWA ---")

    if tidak_ada_data():
        return

    daftar_nilai = [data["nilai"] for data in mahasiswa.values()]
    himpunan_nilai = set(daftar_nilai)

    jumlah_lulus = sum(1 for n in daftar_nilai if n >= KKM)
    jumlah_tidak_lulus = len(daftar_nilai) - jumlah_lulus

    print("-" * 45)
    print(f"Jumlah Mahasiswa     : {len(mahasiswa)}")
    print(f"Nilai Tertinggi      : {max(daftar_nilai):.2f}")
    print(f"Nilai Terendah       : {min(daftar_nilai):.2f}")
    print(f"Nilai Rata-rata      : {sum(daftar_nilai) / len(daftar_nilai):.2f}")
    print(f"Jumlah Nilai Unik    : {len(himpunan_nilai)}")
    print(f"Jumlah Lulus (>={KKM})  : {jumlah_lulus} mahasiswa")
    print(f"Jumlah Tidak Lulus   : {jumlah_tidak_lulus} mahasiswa")
    print("-" * 45)


# =======================================================================
# FUNGSI BANTUAN TAMBAHAN
# =======================================================================
def tidak_ada_data():
    """
    Mengecek apakah dictionary 'mahasiswa' masih kosong.
    Mengembalikan True jika kosong (sekaligus menampilkan pesan),
    dan False jika sudah terdapat data.
    """
    if not mahasiswa:
        print("📭 Belum ada data mahasiswa yang tersimpan.")
        return True
    return False


def cari_nim_asli(nim_lower):
    """
    Mencari NIM asli (dengan huruf besar/kecil aslinya) berdasarkan
    NIM yang sudah di-lowercase. Digunakan untuk pencarian
    case-insensitive pada fungsi edit dan hapus.
    Mengembalikan NIM asli jika ditemukan, atau None jika tidak ada.
    """
    for nim in mahasiswa:
        if nim.lower() == nim_lower:
            return nim
    return None


def cetak_tabel(daftar_data):
    """
    Mencetak data mahasiswa dalam bentuk tabel rapi dengan penomoran.
    Menerima daftar pasangan (nim, data) yang sudah diurutkan
    dari fungsi pemanggil.
    """
    garis = "-" * 65
    print(garis)
    print(f"{'No':<4}{'NIM':<15}{'Nama':<20}{'Nilai':<10}{'Status'}")
    print(garis)

    for nomor, (nim, data) in enumerate(daftar_data, start=1):
        status = "Lulus" if data["nilai"] >= KKM else "Tidak Lulus"
        print(
            f"{nomor:<4}{nim:<15}{data['nama']:<20}"
            f"{data['nilai']:<10.2f}{status}"
        )

    print(garis)


# =======================================================================
# FUNGSI TAMPILAN MENU
# =======================================================================
def tampilkan_menu():
    """
    Menampilkan menu utama program kepada pengguna.
    """
    print("\n" + "=" * 50)
    print(" SISTEM MANAJEMEN NILAI MAHASISWA ".center(50, "="))
    print("=" * 50)
    print(" 1.  Tambah Mahasiswa")
    print(" 2.  Tampilkan Seluruh Data")
    print(" 3.  Cari Mahasiswa berdasarkan NIM")
    print(" 4.  Edit Data Mahasiswa")
    print(" 5.  Hapus Mahasiswa")
    print(" 6.  Tampilkan Jumlah Mahasiswa")
    print(" 7.  Tampilkan Jumlah Nilai Unik")
    print(" 8.  Tampilkan Nilai Tertinggi")
    print(" 9.  Tampilkan Nilai Terendah")
    print(" 10. Tampilkan Nilai Rata-rata")
    print(" 11. Urutkan Data berdasarkan NIM")
    print(" 12. Urutkan Data berdasarkan Nilai")
    print(" 13. Tampilkan Statistik Nilai")
    print(" 14. Keluar")
    print("=" * 50)


# =======================================================================
# FUNGSI UTAMA (MAIN PROGRAM / MENU LOOP)
# =======================================================================
def main():
    """
    Fungsi utama yang menjalankan menu interaktif secara terus-menerus
    sampai pengguna memilih opsi keluar (14).
    """
    # Pemetaan setiap pilihan menu ke fungsi terkait (tanpa argumen)
    pilihan_menu = {
        "1": tambah_mahasiswa,
        "2": tampilkan_semua,
        "3": cari_mahasiswa,
        "4": edit_mahasiswa,
        "5": hapus_mahasiswa,
        "6": jumlah_mahasiswa,
        "7": jumlah_nilai_unik,
        "8": nilai_tertinggi,
        "9": nilai_terendah,
        "10": nilai_rata_rata,
        "11": urutkan_by_nim,
        "12": urutkan_by_nilai,
        "13": statistik_nilai,
    }

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-14): ").strip()

        if pilihan == "14":
            print("\n👋 Terima kasih telah menggunakan program. Sampai jumpa!")
            break

        fungsi_terpilih = pilihan_menu.get(pilihan)

        if fungsi_terpilih is not None:
            fungsi_terpilih()
        else:
            print("⚠️  Pilihan tidak valid. Silakan masukkan angka 1-14.")


# =======================================================================
# TITIK MASUK PROGRAM
# =======================================================================
if __name__ == "__main__":
    main()