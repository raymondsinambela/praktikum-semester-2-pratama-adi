# Praktikum 2 - IPO
# Raymond martupa sinambela - 552010125014

#input nilai

def input_nilai():
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    return nilai_tugas, nilai_uts, nilai_uas

def menu(): #menampilkan menu
    print("="*90)
    print("menu")
    print("="*90)
    print("input 1 untuk keluar")
    print("input apa saja untuk memulai")
    while True:
        pilihan = input("Masukkan pilihan 1 untuk keluar : ")
        if pilihan == "1":
            print("Terima kasih!")
            break  # keluar dari program
        else: # PROSES PERHITUNGAN NILAI 
            nilai_tugas, nilai_uts, nilai_uas = input_nilai()  # tangkap returnnya
            nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
            print("="*90)
            print("HASIL NILAI")
            print("="*90)
            print("Nilai tugas : ", nilai_tugas)
            print("Nilai UTS   : ", nilai_uts)
            print("Nilai UAS   : ", nilai_uas)
            print("Nilai akhir : ", nilai_akhir)
menu()  # panggil lagi untuk input berikutnya

#menghitung bangun datar

import math

# ─── Modul Validasi ───────────────────────────────────
def validasi_input(nilai, nama):
    if not isinstance(nilai, (int, float)) or nilai <= 0:
        raise ValueError(f"Input '{nama}' harus berupa angka positif.")
    return nilai

# ─── Modul Proses ─────────────────────────────────────
def hitung_lingkaran(r):
    validasi_input(r, "jari-jari")
    luas     = math.pi * r ** 2
    keliling = 2 * math.pi * r
    return round(luas, 2), round(keliling, 2)

def hitung_persegi(s):
    validasi_input(s, "sisi")
    luas     = s ** 2
    keliling = 4 * s
    return round(luas, 2), round(keliling, 2)

def hitung_persegi_panjang(p, l):
    validasi_input(p, "panjang")
    validasi_input(l, "lebar")
    luas     = p * l
    keliling = 2 * (p + l)
    return round(luas, 2), round(keliling, 2)

def hitung_segitiga(a, t, sisi_miring=None):
    validasi_input(a, "alas")
    validasi_input(t, "tinggi")
    luas = 0.5 * a * t
    keliling = (a + t + sisi_miring) if sisi_miring else "Tidak dapat dihitung"
    return round(luas, 2), keliling

# ─── Modul Output ─────────────────────────────────────
def tampilkan_hasil(nama_bangun, luas, keliling):
    print(f"\n{'='*30}")
    print(f"  Bangun  : {nama_bangun}")
    print(f"  Luas    : {luas}")
    print(f"  Keliling: {keliling}")
    print(f"{'='*30}")

# ─── Modul Menu ───────────────────────────────────────
def tampilkan_menu():
    print("\n╔══════════════════════════════╗")
    print("║   KALKULATOR BANGUN DATAR    ║")
    print("╠══════════════════════════════╣")
    print("║  1. Lingkaran                ║")
    print("║  2. Persegi                  ║")
    print("║  3. Persegi Panjang          ║")
    print("║  4. Segitiga                 ║")
    print("║  5. Keluar                   ║")
    print("╚══════════════════════════════╝")

# ─── Modul Input Aman ─────────────────────────────────
def input_angka(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai <= 0:
                print(" Masukkan angka positif.")
                continue
            return nilai
        except ValueError:
            print(" Input tidak valid. Harap masukkan angka.")

# ─── Program Utama ────────────────────────────────────
def main():
    while True:
        tampilkan_menu()
        pilihan = input("  Masukkan pilihan (1-5): ").strip()

        try:
            if pilihan == "1":
                r = input_angka("  Jari-jari: ")
                luas, keliling = hitung_lingkaran(r)
                tampilkan_hasil("Lingkaran", luas, keliling)

            elif pilihan == "2":
                s = input_angka("  Sisi: ")
                luas, keliling = hitung_persegi(s)
                tampilkan_hasil("Persegi", luas, keliling)

            elif pilihan == "3":
                p = input_angka("  Panjang: ")
                l = input_angka("  Lebar  : ")
                luas, keliling = hitung_persegi_panjang(p, l)
                tampilkan_hasil("Persegi Panjang", luas, keliling)

            elif pilihan == "4":
                a  = input_angka("  Alas  : ")
                t  = input_angka("  Tinggi: ")
                sm = input_angka("  Sisi miring (0 jika tidak tahu): ")
                luas, keliling = hitung_segitiga(a, t, sm if sm > 0 else None)
                tampilkan_hasil("Segitiga", luas, keliling)

            elif pilihan == "5":
                print("\n  Terima kasih. Sampai jumpa, Tuan.\n")
                break

            else:
                print(" Pilihan tidak valid. Silakan coba lagi.")

        except ValueError as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()

# Program untuk menentukan nilai huruf berdasarkan nilai angka

nilai = int(input("Masukkan nilai: "))
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 60:
    print("Nilai D")

# Menurut saya, konsep IPO sangat membantu dalam pembuatan program karena alur kerja program menjadi lebih jelas dan terstruktur. 
# Pada program ini, bagian input digunakan untuk menerima data dari pengguna seperti nilai dan ukuran bangun datar. 
# Bagian proses berfungsi untuk menghitung nilai akhir, luas, dan keliling menggunakan rumus tertentu. 
# Setelah data diproses, hasilnya ditampilkan pada bagian output sehingga pengguna dapat melihat hasil perhitungan dengan mudah. 
# Dengan adanya konsep IPO, program menjadi lebih mudah dipahami, dikembangkan, dan diperbaiki jika terjadi kesalahan.