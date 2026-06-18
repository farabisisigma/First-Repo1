Berikut README yang menjelaskan setiap fungsi (function) dan cara kerja programmu secara profesional.

README - Refiuse (Text Adventure Game)

Deskripsi Program

Refiuse adalah game petualangan berbasis teks (text adventure) dengan tema wabah zombie. Pemain akan membuat keputusan yang menentukan akhir cerita (ending) yang diperoleh.

Program juga memiliki sistem penyimpanan ending menggunakan file ending.txt sehingga ending yang sudah ditemukan dapat dilihat kembali.


---

Struktur Program

1. Variabel Menu

menu = ["Mulai Game", "Daftar Ending Yang Ditemukan"]

Fungsi

Menyimpan daftar menu yang tersedia.

Catatan

Pada versi program saat ini, variabel ini sebenarnya belum digunakan secara langsung karena menu ditampilkan menggunakan print().


---

2. Function mulai_game()

def mulai_game(nama):

Fungsi

Menjalankan seluruh alur cerita game.

Parameter

Parameter	Keterangan

nama	Nama pemain


Cara Kerja

A. Meminta Nama Pemain

if nama == "":
    nama = input("Masukkan nama kamu disini: ")

Jika pemain belum memiliki nama, program akan meminta nama.


---

B. Menampilkan Cerita Awal

print(...)

Program menampilkan latar belakang cerita mengenai wabah zombie.


---

C. Pilihan Pertama

1. Meninggalkannya lalu pergi dari sana
2. Menolongnya walaupun ia tergigit

Jika memilih 1

Pemain pergi ke atap sekolah dan melanjutkan cerita.

Jika memilih 2

Pemain tertular zombie.

simpan_ending("Bad End (Die)")

Ending disimpan ke file.


---

D. Pilihan Kedua

1. Melawannya dengan tangan kosong
2. Melarikan diri dengan Lily

Pilihan 1

Bad End 2 (Die)

Pemain kalah melawan zombie.

Pilihan 2

Lanjut ke pilihan ketiga.


---

E. Pilihan Ketiga

1. Membuat obor api
2. Berteriak

Pilihan 1

Good End (Safe In Chaos)

Tim penyelamat melihat pemain.

Pilihan 2

Bad End (Exposed)

Zombie menemukan pemain.


---

Return Value

return nama

Mengembalikan nama pemain agar tidak perlu memasukkan nama lagi saat bermain ulang.


---

3. Function simpan_ending()

def simpan_ending(teks):

Fungsi

Menyimpan ending yang berhasil ditemukan ke dalam file.

Parameter

Parameter	Keterangan

teks	Nama ending



---

Cara Kerja

Membuka File

with open("ending.txt", "r")

Membaca isi file ending.


---

Mengecek Duplikat

if teks in file.read():
    return

Jika ending sudah pernah disimpan, function langsung berhenti.

Tujuannya agar ending tidak tersimpan dua kali.


---

Menangani Error

except FileNotFoundError:

Jika file belum ada, program tidak error dan langsung membuat file baru.


---

Menyimpan Ending

with open("ending.txt", "a")

Mode "a" berarti append, yaitu menambahkan data di akhir file.

Contoh isi file:

Bad End (Die)
Bad End (Exposed)
Good End (Safe In Chaos)


---

4. Function daftar_ending()

def daftar_ending():

Fungsi

Menampilkan semua ending yang sudah ditemukan.


---

Cara Kerja

Membaca File

with open("ending.txt", "r")

Program membuka file ending.


---

Menampilkan Isi File

print(isi)

Jika ada ending yang tersimpan, semuanya akan ditampilkan.

Contoh:

Bad End (Die)
Good End (Safe In Chaos)


---

Jika File Belum Ada

except FileNotFoundError:

Program menampilkan:

Belum ada ending.


---

5. Sistem Save (Penyimpanan)

Program menggunakan file:

ending.txt

Kapan Save Dilakukan?

Saat pemain mencapai ending.

Contoh:

simpan_ending("Good End (Safe In Chaos)")


---

Apa yang Disimpan?

Hanya nama ending.

Contoh:

Good End (Safe In Chaos)


---

Apa yang Tidak Disimpan?

Nama pemain

Posisi permainan

Progress cerita


Jadi sistem save di sini hanya untuk koleksi ending.


---

6. Main Program (Menu Utama)

while True:

Fungsi

Menjalankan menu utama terus-menerus sampai pemain memilih keluar.


---

Menu

1. Mulai Game
2. Daftar Ending
0. Keluar


---

Pilihan 1

nama_pemain = mulai_game(nama_pemain)

Memulai permainan.


---

Pilihan 2

daftar_ending()

Menampilkan ending yang ditemukan.


---

Pilihan 0

break

Menghentikan program.


---

Diagram Alur Sederhana

Menu
 │
 ├── Mulai Game
 │      │
 │      ├── Tinggalkan Korban
 │      │       │
 │      │       ├── Lawan Zombie
 │      │       │      └── Bad End 2
 │      │       │
 │      │       └── Kabur Dengan Lily
 │      │              │
 │      │              ├── Buat Obor
 │      │              │      └── Good End
 │      │              │
 │      │              └── Berteriak
 │      │                     └── Bad End
 │      │
 │      └── Menolong Korban
 │              └── Bad End
 │
 ├── Daftar Ending
 │      └── Membaca ending.txt
 │
 └── Keluar

Ringkasan Function

Function	Fungsi

mulai_game()	Menjalankan seluruh cerita game
simpan_ending()	Menyimpan ending ke file ending.txt
daftar_ending()	Menampilkan ending yang sudah ditemukan
while True (main menu)	Mengontrol menu utama program


Program ini sudah menerapkan konsep function, percabangan (if-else), perulangan (while), file handling (load & save), dan return value dengan cukup baik untuk proyek game teks sederhana.
