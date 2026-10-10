# Praktikum 01 - Pengenalan Sistem Terdistribusi dan Terdesentralisasi - Git dan GitHub 

---

Mata Kuliah : Praktikum Sistem Terdistribusi dan Terdesentralisasi<br>
Judul Topik : Git dan GitHub


## 🎯 Tujuan Praktikum 

1. Memahami cara untuk menginstal Git

2. Mengetahui cara menggunakan GitHub seperti membuat repositori baru

3. Mengetahui cara untuk mengkonfigurasi Git

4. Mengetahui cara melakukan berbagai perintah Git

5. Mengetahui cara mengelola repositori, baik untuk pribadi maupun organisasi

## 📖 Dasar Teori 

**1. Instalasi Git**
Git merupakan sistem pengendali versi (Version Control System) yang digunakan untuk merekam dan memantau setiap perubahan pada file atau proyek. Git memudahkan pengguna dalam menelusuri perubahan yang telah dilakukan, mengetahui siapa yang melakukan perubahan, serta kapan perubahan tersebut terjadi Pemasangan Git pada komputer menjadi tahap awal untuk memanfaatkan berbagai fitur yang tersedia. Proses instalasi relatif sederhana, tetapi terdapat beberapa opsi pengaturan yang perlu dipahami agar Git dapat berfungsi sesuai kebutuhan.

**2. Github**
GitHub merupakan platform berbasis web yang digunakan untuk menyimpan dan mengelola repositori Git secara daring. GitHub menyediakan berbagai fitur, seperti repository, branch, commit, pull request, dan Issues. Repository digunakan untuk menyimpan file proyek beserta riwayat perubahannya.

**3. Konfigurasi Git**
Konfigurasi Git merupakan proses pengaturan awal agar Git dapat digunakan sesuai kebutuhan pengguna. Konfigurasi ini mencakup identitas pengguna, editor teks, nama cabang utama, dan pengaturan lainnya. Identitas pengguna biasanya diatur melalui parameter user.name dan user.email. Informasi tersebut akan tercatat pada setiap commit yang dibuat.

---

# 📝Pembahasan Praktikum

## Praktik 01 - Menginstal GIt

### 1. Melakukan download Git dari website resmi

<img src="../images/Instal GIt_0.png"

#### Pembahasan :

Langkah awal yang dilakukan adalah dengan cara mengunduh installer Git yang ada pada website resmi _git-scm.com_. Tunggu instal aplikasi sampai dengan selesai. Jika sudah cek file Git pada lokasi awal mengunduh dimuat. 

### 2. Setelah Git diunduh, klik sebanyak dua kali untuk membuka hasil filr yang sudah di dowmload yang akan memunculkan lisensi aplikasi

<img src="../images/Install Git_01.png" 

### Pembahasan :

Setelah berhasil diunduh, lakukan klik pada file Git sampai muncul halaman lisensi dari Git. Halaman informasi berisi lisensi GNU General Public License versi 2. Lisensi ini menjelaskan bahwa Git adalah perangkat lunak bebas yang boleh digunakan, disalin, dan didistribusikan sesuai ketentuan yang tertera. Lalu klik tulisan Install untuk melanjutkan pemasangan Git pada perangkat.

### 3. Menentukan tempat untuk menyimpan Git pada SSD atau lokasi lainnya

<img src="../images/Install Git_02.png"

### Pembahasan :

Pada tahap ini installer menanyakan di folder mana Git akan dipasang. Lokasi bawaannya adalah C:\Program Files\Git, dan lokasi ini sebaiknya dibiarkan agar tidak ada masalah saat program lain mencari Git. Installer juga menampilkan kebutuhan ruang kosong minimal sekitar 329,3 MB, jadi pastikan penyimpanan masih cukup. Kalau ingin memilih folder lain, tombol Browse bisa dipakai, tetapi untuk praktikum pengaturan default sudah memadai.

### 4. Memilih komponen yang ingin diinstal, gunakan pilihan default, lalu klik next

<img src="../images/Install Git_3.png" 

### Pembahasan :
Di halaman ini kita memilih komponen apa saja yang ikut terpasang. Beberapa yang tercentang adalah Windows Explorer integration (menu “Open Git Bash here” dan “Open Git GUI here” saat klik kanan folder), Git LFS untuk file berukuran besar, asosiasi file .git* dan .sh, serta Scalar. Opsi seperti ikon tambahan di desktop, pengecekan pembaruan harian, dan profil Git Bash di Windows Terminal dibiarkan kosong. Kebutuhan ruang untuk pilihan ini sekitar 329,0 MB, lalu lanjut dengan Next.

### 5. Membuat shortcut pada menu start, dengan nama Git (default)

<img src="../images/Install Git_04.png" 

### Pembahasan :
Tahap ini mengatur di mana shortcut Git diletakkan pada Start Menu. Nama folder bawaannya adalah “Git”, sehingga nanti Git Bash atau Git GUI mudah dicari lewat menu Start. Ada juga opsi “Don’t create a Start Menu folder” bagi yang tidak ingin shortcut dibuat, tetapi di sini opsi itu tidak dicentang. Karena tidak ada yang perlu diubah, langsung klik Next.

### 6. Memilih editor yang akan digunakan dengan Git

<img src="../images/Install Git_05.png" 

### Pembahasan :
Halaman ini menanyakan editor teks yang akan dipakai Git, misalnya saat menulis pesan commit. Pilihan yang tampil adalah Vim, yang disebut powerful tetapi cukup sulit digunakan karena tampilan dan tombol-tombolnya kurang intuitif. Installer sendiri menyarankan untuk beralih ke editor GUI modern bagi pengguna yang belum terbiasa. Jadi, kalau belum akrab dengan Vim, ada baiknya memilih editor lain lewat menu dropdown yang dibahas di dua gambar berikutnya.

### 7. Menentukan Nama Branch Awal

<img src="../images/Instal Git_06.png" 

### Pembahasan :
Halaman ini mengatur nama branch awal setiap kali kita membuat repositori baru dengan git init. Pilihan yang dipakai adalah “Override the default branch name for new repositories” dengan nama main, bukan master yang menjadi bawaan lama Git. Nama main sekarang lebih umum digunakan, termasuk oleh GitHub. Perlu diingat bahwa pengaturan ini tidak mengubah repositori yang sudah ada, jadi aman untuk dilanjutkan dengan Next.

### 8. Mengatur Lingkungan PATH

<img src="../images/Install Git_07.png" 

### Pembahasan :
Tahap ini menentukan bagaimana Git dapat dipanggil dari command line. Pilihan yang dipakai adalah “Git from the command line and also from 3rd-party software”, yang ditandai sebagai rekomendasi. Dengan opsi ini, Git bisa dijalankan dari Git Bash, Command Prompt, PowerShell, maupun aplikasi lain yang membutuhkan Git. Opsi ini juga hanya menambahkan sedikit perintah ke PATH sehingga tidak mengganggu perintah bawaan Windows seperti find dan sort.

### 9. Memilih Pustaka HTTPS Transport

<img src="../images/Install Git_8.png" 

### Pembahasan :
Halaman ini memilih pustaka SSL/TLS yang dipakai Git untuk koneksi HTTPS. Pilihan yang aktif adalah “Use the native Windows Secure Channel library”, yaitu pustaka bawaan Windows. Sertifikat server akan divalidasi menggunakan Windows Certificate Stores, sehingga lebih sesuai dengan lingkungan Windows, termasuk jaringan kantor atau kampus yang memakai sertifikat internal. Kita biarkan pilihan ini, lalu klik Next.

### 10. Mengatur Konversi Akhiran Baris

<img src="../images/Install Git_9.png" 

### Pembahasan :
Pada tahap ini kita mengatur cara Git memperlakukan akhiran baris (line endings) pada berkas teks. Pilihan yang dipakai adalah “Checkout Windows-style, commit Unix-style line endings”, yaitu Git mengubah LF menjadi CRLF saat checkout dan mengembalikannya ke LF saat commit. Pengaturan ini adalah yang direkomendasikan untuk pengguna Windows (core.autocrlf bernilai true). Manfaatnya, proyek yang dikerjakan bersama pengguna Linux atau macOS tetap konsisten.

### 11. Memilih Emulator Terminal untuk Git Bash

<img src="../images/Install Git_10.png" 

### Pembahasan :
Halaman ini memilih emulator terminal untuk Git Bash. Pilihan yang aktif adalah MinTTY, terminal bawaan MSYS2, yang jendelanya bisa diubah ukurannya, mendukung seleksi teks non-persegi, dan memiliki font Unicode. Alternatifnya adalah console window bawaan Windows (cmd.exe) yang lebih terbatas dalam hal scroll-back dan tampilan karakter non-ASCII. Karena MinTTY lebih nyaman dipakai, kita biarkan pilihan ini dan klik Next.

### 12. Mengatur Perilaku Bawaan Git Pull

<img src="../images/Install Git_11.png" 

### Pembahasan :
Tahap ini mengatur perilaku bawaan perintah git pull. Pilihan yang dipakai adalah “Fast-forward or merge”, yaitu Git akan melakukan fast-forward jika memungkinkan, dan jika tidak, membuat merge commit. Dua pilihan lainnya adalah Rebase dan “Only ever fast-forward”. Opsi pertama paling aman untuk pemula karena cara kerjanya mudah dipahami dan jarang menimbulkan kebingungan.

### 13. Memilih Credential Helper

<img src="../images/Install Git_12.png" 

### Pembahasan :
Halaman ini memilih credential helper, yaitu alat yang menyimpan kredensial login agar kita tidak perlu mengetik ulang akun setiap kali berinteraksi dengan repositori remote. Pilihan yang aktif adalah Git Credential Manager, yang bisa dipakai lintas platform. Alat ini sangat membantu saat kita login ke layanan seperti GitHub. Pilihan “None” tidak kita pakai karena kita akan sering terhubung ke repositori online.

### 14. Mengatur Opsi Tambahan

<img src="../images/Install Git_13.png" 

### Pembahasan :
Pada halaman ini terdapat dua opsi tambahan. Opsi “Enable file system caching” dicentang karena membuat data sistem berkas dibaca dan disimpan sementara di memori sekaligus, sehingga kinerja Git meningkat. Opsi “Enable symbolic links” dibiarkan kosong karena membutuhkan izin khusus (SeCreateSymbolicLink) dan jarang diperlukan. Setelah itu kita klik Install untuk memulai pemasangan.

### 15. Proses Instalasi Berlangsung

<img src="../images/Install Git_14.png"

### Pembahasan :
Proses instalasi sedang berjalan pada tahap ini. Setup mengekstrak berkas-berkas Git ke folder tujuan, dan pada gambar terlihat berkas yang sedang diproses berada di C:\Program Files\Git\mingw64\bin. Progress bar menunjukkan kemajuan pemasangan, sehingga kita hanya perlu menunggu sampai selesai. Selama proses ini kita tidak boleh menutup jendela agar instalasi tidak rusak.

### 16. Menyelesaikan Instalasi Git

<img src="../images/Install Git_15.png" 

### Pembahasan :
Halaman terakhir menandakan bahwa Git Setup Wizard telah selesai dan Git berhasil terpasang. Terdapat dua opsi, yaitu “Launch Git Bash” yang tidak dicentang dan “View Release Notes” yang dicentang. Opsi pertama bisa dicentang jika kita ingin langsung membuka Git Bash, sedangkan opsi kedua akan membuka catatan rilis versi 2.53.0. Kita menutup wizard dengan klik Finish, dan Git siap digunakan.

### 17. Memeriksa versi Git yang telah terpasang

<img src="../images/Check versi.png" 

### Pembahasan :
Setelah proses instalasi selesai, langkah berikutnya adalah memastikan bahwa Git benar-benar sudah terpasang dan bisa dikenali oleh sistem. Untuk itu kita membuka Command Prompt, lalu mengetikkan perintah git --version dan menekan Enter. Perintah ini berfungsi untuk menampilkan versi Git yang saat ini terpasang di komputer. Pada gambar terlihat bahwa Command Prompt berada di direktori C:\Users\Ezraapra, dan hasil keluarannya adalah git version 2.56.0.windows.2. Munculnya nomor versi tersebut menandakan bahwa Git sudah berhasil terpasang dan PATH-nya sudah terkonfigurasi dengan benar, sehingga Git dapat dipanggil dari Command Prompt. Kalau yang muncul justru pesan bahwa perintah tidak dikenali, biasanya instalasinya belum sempurna atau Command Prompt perlu ditutup lalu dibuka kembali.

---

## Praktik 02 - Konfigurasi Git

### 1. Mengatur Identitas Pengguna Global

<img src="images/Konfigurasi Git.png" 

### Pembahasan :
Pada langkah pertama, perintah git config --global user.name "Ezraapra8" dan git config --global user.email ezraapra@gmail.com dijalankan di terminal Git Bash. Kedua perintah ini berfungsi untuk mendaftarkan nama dan alamat email yang akan menjadi identitas penulis setiap kali kita membuat commit. Opsi --global berarti pengaturan ini berlaku untuk semua repositori di komputer tersebut, jadi kita tidak perlu mengulanginya di setiap proyek. Identitas ini penting karena Git selalu mencatat siapa yang membuat perubahan, sehingga riwayat kerja dalam sebuah proyek bisa dilacak dengan jelas.

### 2. Memeriksa File Konfigurasi Global

<img src="../images/Konfigurasi Git_1.png" 

### Pemabahasan :
Setelah identitas diatur, langkah berikutnya adalah memastikan pengaturan tadi benar-benar tersimpan dengan menampilkan isi file .gitconfig memakai perintah cat ~/.gitconfig di PowerShell. File ini terletak di direktori home pengguna dan menjadi tempat Git menyimpan konfigurasi global. Dari tampilannya, terlihat bagian [user] yang berisi email dan nama sesuai yang kita masukkan, serta bagian [init] yang menetapkan defaultBranch = main. Dengan begitu, kita tahu bahwa setiap repositori baru nantinya akan otomatis memakai branch bernama main, bukan master.

### 3.Menampilkan Konfigurasi Git Sistem dan Bawaan Instalasi

<img src="../images/Konfigurasi Git_2.png" 

### Pemabahasan :
Pada langkah ini, perintah git config --list dijalankan di PowerShell dari direktori C:\Users\Ezraapra, yaitu di luar folder repositori mana pun. Karena itu, hasil yang muncul adalah konfigurasi tingkat sistem dan bawaan instalasi Git, bukan pengaturan milik satu proyek tertentu. Terlihat beberapa pengaturan seperti core.autocrlf=true, yang membuat Git otomatis menyesuaikan karakter akhir baris antara Windows dan sistem lain, serta core.symlinks=false dan core.fscache=true yang mengatur cara Git bekerja dengan sistem file Windows. Ada juga http.sslbackend=schannel, yang berarti Git memakai layanan keamanan bawaan Windows untuk koneksi HTTPS.

Selain itu, daftar ini memperlihatkan beberapa komponen tambahan yang ikut terpasang saat instalasi. Bagian filter.lfs menandakan bahwa Git LFS sudah aktif untuk mengelola file berukuran besar, sedangkan credential.helper=manager berarti Git Credential Manager dipakai untuk menyimpan kredensial login supaya tidak perlu mengetik ulang setiap kali melakukan push atau pull. Pengaturan pull.rebase=false menetapkan bahwa perintah pull akan memakai strategi merge, dan init.defaultbranch=main kembali menegaskan bahwa repositori baru akan otomatis bernama main. Dengan begitu, langkah ini berguna sebagai pemeriksaan bahwa instalasi Git di komputer sudah lengkap dan siap dipakai sebelum mulai mengelola repositori.


### 4. Menampilkan Seluruh Konfigurasi Git di Repositori

<img src="../images/Konfigurasi Git_3.png" 

### Pembahasan :
Pada langkah terakhir, perintah git config --list dijalankan di dalam folder repositori prak-disc-dec untuk melihat semua konfigurasi yang sedang aktif. Hasilnya menggabungkan pengaturan global yang sudah dibuat sebelumnya, seperti user.name, user.email, dan init.defaultbranch, dengan pengaturan bawaan tingkat repositori seperti core.filemode, core.bare, dan core.ignorecase. Perintah ini sangat berguna sebagai pemeriksaan akhir, karena kita bisa memastikan tidak ada pengaturan yang keliru sebelum mulai bekerja. Selain itu, tampilnya nilai core.bare=false menandakan bahwa folder tersebut adalah repositori kerja biasa yang memiliki working directory, bukan repositori kosong untuk penyimpanan saja.






































