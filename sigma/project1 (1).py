print("==== Welcome To Refiuse ====")

menu = ["Mulai Game", "Daftar Ending Yang ditemukan"]

def mulai_game(nama):
    if nama == "":
        nama = input("Masukkan nama kamu disini: ")

    print(f"""
Suatu hari {nama} sedang bersekolah,
akan tetapi ada berita yang muncul di sosial media
tentang seseorang mencoba menyerang orang lain
dengan keadaan digigit.""")
    input("")

    print(f"""{nama} terkejut dan langsung pergi dari kelas
Semuanya panik dan terjadi kekacauan di sekolah tersebut.
""")

    print(f"""{nama} pun bertemu dengan seseorang yang bejalan dengan sempoyongan, 
{nama} mencoba membantu dia tetapi {nama} melihat tangan dia tergigit.""")
    input("")

    while True:
        print(f"Apa yang akan {nama} lakukan terhadap seseorang tersebut?")
        print("1. Meninggalkannya lalu pergi dari sana")
        print("2. Menolongnya walaupun ia tergigit")

        pilih_awal = input("tentukan sekarang: ")

        if pilih_awal == "1":
            print(f"{nama} Pergi dari sana lalu ia menuju keatap sekolah dengan tergesa gesa,ia merasa kesal dengan dirinya, tetapi ia juga tidak bisa membantu orang tadi")
            print(f"dan setibanya {nama} diatap ia melihat keadaan kota dengan penuh asap dimana mana, terjadi keributan dan kebakaran")

            input("")
            print(f"Lily: Kakak {nama}! kamu baik baik saja!? aku tidak tahu apa yang terjadi mereka menjadi gila!")
            print(f"{nama} terkejut ada yang memanggilnya dari gedung sebelah ia langsung menengok kesana dan ia melihat adiknya sedang berada diruang lab.")
            print(f"{nama}: Kakak tidak apa apa lily! kamu tetap disana nanti aku selamatkan!")
            print(f"Lily: kakak.. aku takut...")
            print(f"{nama}: tenang ajaa.. ada aku disini")
            print(f"secara tiba tiba ada zombie datang dan menemukan mereka berdua")
            while True:
                print(f"apa yang {nama} akan lakukan jika zombie mulai menyerang")
                print(f"1. melawannya dengan tangan kosong")
                print(f"2. melarikan diri dengan Lily")

                pilih_lanjutan = input("pilih sesuai logika: ")
            
                if pilih_lanjutan == "1":
                    print(f"{nama} mencoba melawan melawan zombie dengan tangan kosong")
                    print(f"perkelahian antara zombie dan {nama} terjadi")
                    print(f"{nama} ternyata gabisa berkelahi dan meninggal karena zombie")
                    simpan_ending("bad end 2 (die)")
                    return

                elif pilih_lanjutan == "2":
                     print(f"{nama} memilih melarikan diri dengan Lily")  
  

        elif pilih_awal == "2":
            print(f"{nama} menghampirinya dan langsung menggendongnya lalu pergi menuju atap sekolah, akan tetapi {nama} ketakutan dengan keadaan orang tersebut.")
            print(f"setibanya diatap sekolah {nama} menoleh kesana kesini, dan ia menemukan adiknya yang sedang berada dilab ipa bersama anak anak yang lainnya")
            
            input("")
            print(f"{nama}: Lily! kamu baik baik saja!? kakak akan kesana membantumu! jadi tolong untuk menjaga dirimu Lily!")
            print(f"Lily: Kakak! dibelakangmu! Kakak!")
            input("")
            print(f"{nama} menoleh kebelakangnya dan tiba tiba orang yang tergigit berubah menjadi Zombie, lalu ia menerkam ke {nama} sampai terluka tetapi {nama} mencoba melawan sehingga mendorongnya dan orang tersebut terjatuh dari atap")
            print(f"{nama}: Si-sial... aku malah lengah, Ma-maafkan aku Lily...")
            input("")
            print(f"Lily: Ka-kakak... Tidak!")
            print(f"{nama} akhirnya berubah menjadi zombie dan terjatuh dari atap, Lily hanya bisa melihatnya dengan tatapan kesedihan ketika kakaknya jatuh dari atap sekaligus berubah jadi zombie")
            
            simpan_ending ("Bad End (Die)")
            break

        else:
            print("Cepat Tentukan!")

    input("")
    return nama


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
    print("=== DAFTAR ENDING YANG DITEMUKAN ===")

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
