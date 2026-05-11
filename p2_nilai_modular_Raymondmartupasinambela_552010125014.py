# Praktikum 2 - IPO
# Raymond martupa sinambela - 552010125014

#input nilai

def input_nilai():
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    return nilai_tugas, nilai_uts, nilai_uas

def menu():
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
        else:
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

#


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