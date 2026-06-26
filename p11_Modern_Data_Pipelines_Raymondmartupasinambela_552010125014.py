from collections import Counter

# ======================================
# MEMBACA FILE TXT
# ======================================
def baca_txt(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                # Pisahkan berdasarkan koma
                kolom = baris.split(",")

                if len(kolom) < 3:
                    continue

                try:
                    nama = kolom[0].strip()
                    umur = int(kolom[1].strip())
                    alamat = kolom[2].strip()

                    data.append({
                        "nama": nama,
                        "umur": umur,
                        "alamat": alamat
                    })

                except ValueError:
                    continue

        return data

    except FileNotFoundError:
        print("❌ File tidak ditemukan")
        return []


# ======================================
# TAMPILKAN DATA
# ======================================
def tampilkan_data(data):

    print("\nDAFTAR DATA")
    print("-" * 80)

    for i, orang in enumerate(data, start=1):
        print(
            f"{i:3}. "
            f"{orang['nama']:<25}"
            f"{orang['umur']:>3} tahun | "
            f"{orang['alamat']}"
        )


# ======================================
# STATISTIK
# ======================================
def statistik(data):

    umur_list = [x["umur"] for x in data]

    rata = sum(umur_list) / len(umur_list)

    tertua = max(data, key=lambda x: x["umur"])
    termuda = min(data, key=lambda x: x["umur"])

    print("\nSTATISTIK DATA")
    print("-" * 40)

    print(f"Jumlah Data      : {len(data)}")
    print(f"Rata-rata Umur   : {rata:.2f}")
    print(f"Tertua           : {tertua['nama']} ({tertua['umur']} tahun)")
    print(f"Termuda          : {termuda['nama']} ({termuda['umur']} tahun)")

    return rata, tertua, termuda


# ======================================
# CARI NAMA
# ======================================
def cari_nama(data):

    keyword = input("\nMasukkan nama yang dicari: ").lower()

    hasil = []

    for orang in data:
        if keyword in orang["nama"].lower():
            hasil.append(orang)

    if hasil:

        print("\nHASIL PENCARIAN")
        print("-" * 60)

        for orang in hasil:
            print(
                f"{orang['nama']} | "
                f"{orang['umur']} tahun | "
                f"{orang['alamat']}"
            )

    else:
        print("Data tidak ditemukan.")


# ======================================
# JUMLAH PER KOTA
# ======================================
def statistik_kota(data):

    kota_counter = Counter()

    for orang in data:

        alamat = orang["alamat"]

        if "," in alamat:
            kota = alamat.split(",")[-1].strip()
            kota_counter[kota] += 1

    print("\nJUMLAH DATA PER KOTA")
    print("-" * 40)

    for kota, jumlah in kota_counter.most_common():
        print(f"{kota:<15} : {jumlah}")


# ======================================
# SIMPAN LAPORAN
# ======================================
def simpan_laporan(data):

    umur_list = [x["umur"] for x in data]

    rata = sum(umur_list) / len(umur_list)

    tertua = max(data, key=lambda x: x["umur"])
    termuda = min(data, key=lambda x: x["umur"])

    with open("laporan.txt", "w", encoding="utf-8") as file:

        file.write("LAPORAN DATA PENDUDUK\n")
        file.write("=" * 40 + "\n")

        file.write(f"Jumlah Data    : {len(data)}\n")
        file.write(f"Rata-rata Umur : {rata:.2f}\n")
        file.write(
            f"Tertua         : {tertua['nama']} ({tertua['umur']} tahun)\n"
        )
        file.write(
            f"Termuda        : {termuda['nama']} ({termuda['umur']} tahun)\n"
        )

    print("\n✅ Laporan disimpan ke laporan.txt")


# ======================================
# MENU
# ======================================
def menu(data):

    while True:

        print("\n")
        print("=" * 40)
        print("MENU PROGRAM")
        print("=" * 40)
        print("1. Tampilkan Data")
        print("2. Statistik")
        print("3. Cari Nama")
        print("4. Statistik Kota")
        print("5. Simpan Laporan")
        print("0. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            tampilkan_data(data)

        elif pilihan == "2":
            statistik(data)

        elif pilihan == "3":
            cari_nama(data)

        elif pilihan == "4":
            statistik_kota(data)

        elif pilihan == "5":
            simpan_laporan(data)

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


# ======================================
# MAIN
# ======================================
def main():

    nama_file = input("Masukkan nama file TXT (contoh : NamaFile.txt): ")

    data = baca_txt(nama_file)

    if not data:
        print("Tidak ada data.")
        return

    print(f"\nBerhasil membaca {len(data)} data.")

    menu(data)


if __name__ == "__main__":
    main()