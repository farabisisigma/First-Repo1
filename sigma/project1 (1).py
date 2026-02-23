print("==== Welcome To Refiuse ====")

menu = ["Mulai Game", "Daftar Ending Yang Ditemukan"]

def mulai_game(nama):
    if nama == "":
        nama = input("Masukkan nama kamu disini: ")

    print(f"""
Suatu hari {nama} sedang bersekolah,
akan tetapi ada berita yang muncul di sosial media dan televisi
tentang seseorang mencoba menyerang orang lain
dengan keadaan leher yang terluka.""")
    input("")

    print(f"""{nama} terkejut dan langsung keluar dari kelas.
{nama} melihat banyak orang yang panik dan terjadi kekacauan di sekolah tersebut.
""")

    print(f"""{nama} pun bertemu dengan seseorang yang berjalan dengan sempoyongan.
{nama} mencoba membantu dia tetapi {nama} melihat tangan dan leher dia ada bekas luka gigitan.""")
    input("")

    while True:
        print(f"Apa yang akan {nama} lakukan terhadap seseorang tersebut?")
        print("1. Meninggalkannya lalu pergi dari sana")
        print("2. Menolongnya walaupun ia tergigit")

        pilih_awal = input("Tentukan sekarang: ")

        if pilih_awal == "1":
            print(f"{nama} pergi dari sana lalu ia menuju ke atap sekolah dengan tergesa-gesa.")
            print(f"Setibanya {nama} di atap, ia melihat keadaan kota dengan penuh asap di mana-mana.")
            input("")

            print(f"Lily: Kakak {nama}! Kamu baik-baik saja!?")
            print(f"{nama}: Kakak tidak apa-apa, Lily! Tetap di sana!")
            print("Secara tiba-tiba ada zombie datang.")

            while True:
                print(f"Apa yang akan {nama} lakukan?")
                print("1. Melawannya dengan tangan kosong")
                print("2. Melarikan diri dengan Lily")

                pilih_lanjutan = input("Pilih sesuai logikamu: ")

                if pilih_lanjutan == "1":
                    print(f"{nama} mencoba melawan zombie dengan tangan kosong.")
                    print(f"{nama} kalah dan meninggal.")
                    simpan_ending("Bad End 2 (Die)")
                    return nama   # ✅ FIX BUG

                elif pilih_lanjutan == "2":
                    print(f"{nama} memilih melarikan diri dengan Lily.")
                    
                    while True:
                        print("Tim penyelamat muncul. Apa yang kamu lakukan?")
                        print("1. Membuat obor api")
                        print("2. Berteriak")

                        pilih_ketiga = input("Tentukan: ")

                        if pilih_ketiga == "1":
                            print("Tim penyelamat melihat kalian dan menyelamatkan kalian.")
                            simpan_ending("Good End (Safe In Chaos)")
                            return nama   # ✅ FIX BUG

                        elif pilih_ketiga == "2":
                            print("Zombie menemukan kalian.")
                            simpan_ending("Bad End (Exposed)")
                            return nama   # ✅ FIX BUG

                        else:
                            print("Pilihan tidak ada.")

                else:
                    print("Pilihan tidak ada.")

        elif pilih_awal == "2":
            print(f"{nama} menolong orang tersebut.")
            print("Orang itu berubah menjadi zombie.")
            print(f"{nama} terluka dan akhirnya berubah.")
            simpan_ending("Bad End (Die)")
            return nama   # ✅ FIX BUG

        else:
            print("Cepat tentukan!")

def simpan_ending(teks):
    try:
        with open("ending.txt", "r") as file:
            if teks in file.read():
                return
    except FileNotFoundError:
        pass

    with open("ending.txt", "a") as file:
        file.write(teks + "\n")

def daftar_ending():
    print("=== DAFTAR ENDING ===")

    try:
        with open("ending.txt", "r") as file:
            isi = file.read()
            if isi == "":
                print("Belum ada ending.")
            else:
                print(isi)
    except FileNotFoundError:
        print("Belum ada ending.")

    input("")

nama_pemain = ""

while True:
    print("\nMenu")
    print("1. Mulai Game")
    print("2. Daftar Ending")
    print("0. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        nama_pemain = mulai_game(nama_pemain)

    elif pilih == "2":
        daftar_ending()

    elif pilih == "0":
        break

    else:
        print("Pilihan tidak ada di menu.")
