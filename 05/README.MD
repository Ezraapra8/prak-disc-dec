# Praktik 5 - Fault Tolerance

---

Judul Modul : Fault Tolerance  <br>
Mata Kuliah : __Praktikum Sistem Terdistribusi dan Terdesentralisasi__


| Field | Keterangan |
| :--- | :--- |
| **Nama** | Ezra Adyatma Pranantio |
| **NIM** | 255410002 |

---

## 📌 Tujuan Praktikum

1. Memahami konsep Fault Tolerance dalam sistem terdistribusi untuk menjaga ketersediaan dan keandalan aplikasi.

2. Memahami penerapan Load Balancing menggunakan Nginx untuk mendistribusikan permintaan pengguna ke beberapa instance aplikasi.

3. Mempelajari penggunaan Docker dan Docker Compose untuk menjalankan serta mengelola beberapa container aplikasi.

4. Memahami mekanisme Failure Detection menggunakan metode Heartbeat untuk mengetahui kondisi aktif atau tidak aktifnya suatu layanan.

5. Mempelajari penggunaan mekanisme Retry dan Circuit Breaker dalam menangani kegagalan komunikasi serta mencegah terjadinya kegagalan berantai pada sistem.

6. Mengamati dan membandingkan perilaku aplikasi ketika layanan berada dalam kondisi aktif dan tidak aktif.



## 📖 Dasar Teori

<p align ="justify">Fault Tolerance merupakan kemampuan suatu sistem untuk tetap beroperasi ketika terjadi kegagalan pada salah satu komponen. Dalam sistem terdistribusi, Fault Tolerance diperlukan untuk menjaga ketersediaan layanan agar tetap dapat diakses oleh pengguna. Pada modul ini, pembahasan Fault Tolerance mencakup Load Balancing dan Failure Detection sebagai metode untuk meningkatkan keandalan aplikasi.

<p align ="justify">Load Balancing merupakan teknik untuk membagi permintaan pengguna ke beberapa instance aplikasi agar beban kerja tidak terpusat pada satu server. Teknik ini dapat meningkatkan ketersediaan aplikasi dan mengurangi risiko gangguan layanan ketika terjadi peningkatan jumlah permintaan. Pada praktikum ini, Load Balancing menggunakan Nginx sebagai proxy yang mengatur distribusi permintaan ke beberapa instance aplikasi Blacksheep. Docker dan Docker Compose digunakan untuk menjalankan serta mengelola beberapa container aplikasi secara bersamaan.

<p align ="justify">Failure Detection merupakan proses untuk mengetahui apakah suatu komponen dalam sistem mengalami kegagalan atau tidak memberikan respons. Salah satu metode yang digunakan adalah Heartbeat, yaitu protokol pemantauan aktivitas komponen melalui pengiriman sinyal secara berkala. Apabila sinyal tidak diterima dalam jangka waktu tertentu, komponen tersebut dianggap mengalami kegagalan atau tidak responsif.

<p align ="justify">Selain itu, terdapat mekanisme Retry dan Circuit Breaker untuk menangani kegagalan komunikasi antar komponen. Retry digunakan untuk mencoba kembali koneksi ketika permintaan mengalami kegagalan. Sementara itu, Circuit Breaker merupakan pola desain yang mencegah terjadinya kegagalan berantai dengan menghentikan sementara permintaan menuju layanan yang bermasalah. Circuit Breaker memiliki tiga status, yaitu Closed, Open, dan Half-Open, yang mengatur proses permintaan serta pemulihan layanan.



# 📝Pembahasan Praktikum

## 4.1 Load Balancing Aplikasi

---

### 1. Persiapan 

**Instal Docker Dekstop**

Langkah awal untuk memulai praktikum yaitu dengan melakukan instal Docker, dikarenakan praktikum sebelumnya sudah menginstal Docker, maka bisa dilakukan cek versi pada Powershell :

<img src="images/gambar 1.png" width="610">

#### Pembahasan :

<p align ="justify">Proses ini dilakukan untuk memeriksa versi Docker dan Docker Compose yang sudah terpasang pada komputer melalui PowerShell. Perintah docker --version digunakan untuk menampilkan versi Docker, sedangkan docker-compose --version digunakan untuk memeriksa versi Docker Compose. Pemeriksaan ini bertujuan untuk memastikan bahwa kedua perangkat tersebut sudah tersedia dan dapat digunakan sebelum menjalankan proses pembuatan aplikasi berbasis container. Dengan mengetahui versi yang digunakan, pengguna juga dapat memastikan kesiapan lingkungan praktikum.

### 2. Mengatur Execution Policy dan Menginstal UV

<img src="images/gambar 2.png" width="610">

#### Pembahasan :

<p align ="justify">Pada proses ini dilakukan pengaturan Execution Policy menggunakan perintah Set-ExecutionPolicy RemoteSigned -Scope CurrentUser agar PowerShell mengizinkan eksekusi skrip lokal dan skrip yang telah memenuhi ketentuan keamanan. Selanjutnya, perintah powershell -c "irm https://astral.sh/uv/install.ps1 | iex" digunakan untuk mengunduh dan menjalankan installer UV. UV merupakan perangkat yang digunakan untuk mengelola instalasi Python, virtual environment, dan dependensi proyek. Tujuan proses ini adalah mempersiapkan alat pengelolaan lingkungan Python agar proses pengembangan aplikasi dapat dilakukan dengan lebih teratur.

## 3. Membuat Direktori Workspace-05

<img src="images/gambar 3.png" width="610">

#### Pembahasan :

<p align ="justify">Proses ini dilakukan dengan menggunakan perintah mkdir workspace-05 untuk membuat direktori baru bernama workspace-05. Setelah direktori berhasil dibuat, perintah cd workspace-05 digunakan untuk masuk ke dalam direktori tersebut. Direktori ini berfungsi sebagai tempat penyimpanan seluruh kebutuhan praktikum, termasuk lingkungan Python, aplikasi Blacksheep, dan konfigurasi Docker. Tujuan pembuatan direktori ini adalah agar seluruh berkas proyek tersusun dalam satu lokasi sehingga lebih mudah dikelola dan ditemukan.

### 4. Membuat Virtual Environment Menggunakan UV

<img src="images/gambar 4.png" width="610">

#### Pembahasan :

<p align ="justify">Pada tahap ini dilakukan pembuatan virtual environment menggunakan perintah uv venv. Berdasarkan hasil terminal, UV menggunakan Python versi 3.14.7 dan berhasil membuat lingkungan virtual dengan nama .venv. Virtual environment merupakan lingkungan Python terpisah yang memungkinkan suatu proyek memiliki kumpulan pustaka dan dependensi sendiri tanpa mencampuri instalasi Python utama pada komputer. Tujuan proses ini adalah menjaga kebutuhan aplikasi tetap terisolasi sehingga pengelolaan paket dan pengembangan aplikasi dapat berjalan lebih teratur.

### 5. Menginstal Framework Blacksheep

<img src="images/gambar 5.png" width="610">

<img src="images/gambar 6.png" width="610">

#### Pembahasan :

<p align ="justify">Proses ini dilakukan dengan menjalankan perintah uv pip install blacksheep untuk menginstal framework Blacksheep ke dalam lingkungan Python yang telah dibuat sebelumnya. Terminal menampilkan daftar paket yang berhasil diunduh dan dipasang, termasuk paket utama Blacksheep beserta beberapa dependensi pendukungnya. Blacksheep merupakan framework Python yang digunakan untuk membangun aplikasi web berbasis ASGI. Tujuan instalasi ini adalah menyediakan framework yang diperlukan untuk membuat aplikasi web yang nantinya akan digunakan sebagai layanan backend dalam pengujian load balancing.

### 6. Menginstal Blacksheep CLI

<img src="images/gambar 7.png" width="610">

#### Pembahasan :

<p align ="justify">Pada tahap ini dilakukan instalasi Blacksheep CLI menggunakan perintah uv pip install --link-mode=copy blacksheep blacksheep-cli. Perintah tersebut digunakan untuk memasang paket Blacksheep beserta perangkat command-line interface yang menyediakan perintah untuk membantu proses pembuatan dan pengelolaan proyek. Hasil instalasi menunjukkan bahwa paket yang diperlukan berhasil diproses oleh UV. Tujuan proses ini adalah menyediakan fasilitas untuk membuat struktur awal aplikasi Blacksheep tanpa harus menyusun seluruh berkas proyek secara manual.

### 7. Membuat Proyek Aplikasi Blacksheep

<img src="images/gambar 8.png" width="610">

#### Pembahasan :

<p align ="justify">Proses pembuatan aplikasi dilakukan dengan menjalankan perintah blacksheep create. Pada tahap ini ditentukan nama proyek blacksheep_lb, kemudian dipilih template proyek MVC, penggunaan dokumentasi OpenAPI, library konfigurasi, dan format pengaturan TOML. Setelah seluruh pilihan ditentukan, terminal menampilkan informasi bahwa proyek berhasil dibuat di dalam direktori blacksheep_lb. Tujuan proses ini adalah membentuk struktur dasar aplikasi web yang akan dikembangkan dan digunakan sebagai backend dalam penerapan load balancing.

### 8. Menginstal Dependensi Aplikasi dari Requirements.txt

<img src="images/gambar 9.png" width="610">

#### Pembahasan :

<p align ="justify">Pada proses ini dilakukan instalasi seluruh dependensi yang dibutuhkan oleh aplikasi menggunakan perintah uv pip install --link-mode=copy -r requirements.txt. Berkas requirements.txt berisi daftar pustaka Python yang diperlukan agar aplikasi dapat berjalan sesuai dengan konfigurasi proyek. UV akan membaca daftar tersebut, memeriksa paket yang dibutuhkan, kemudian memasang dependensi yang belum tersedia pada lingkungan virtual. Tujuan proses ini adalah memastikan seluruh kebutuhan aplikasi telah terpenuhi sehingga aplikasi dapat dijalankan tanpa mengalami kendala akibat pustaka yang belum terpasang.

### 9. Menjalankan Aplikasi Blacksheep dalam Mode Development

<img src="images/gambar 10.png" width="610">

#### Pembahasan :

<p align ="justify">etelah proses instalasi selesai, aplikasi dijalankan menggunakan perintah python dev.py. Terminal menunjukkan bahwa server berhasil dimulai dan berjalan menggunakan Uvicorn pada alamat http://localhost:44777. Informasi tersebut menunjukkan bahwa proses startup aplikasi telah selesai dan server siap menerima permintaan dari pengguna. Tujuan proses ini adalah mengaktifkan aplikasi Blacksheep pada lingkungan lokal agar fungsionalitas aplikasi dapat diperiksa sebelum diterapkan ke dalam container Docker.

### 10. Mengakses Aplikasi Blacksheep Melalui Browser

<img src="images/gambar 11.png" width="610">

#### Pembahasan :

<p align ="justify">Pada tahap ini dilakukan pengujian aplikasi dengan membuka alamat http://localhost:44777 melalui browser. Hasil yang ditampilkan berupa halaman utama Blacksheep yang menunjukkan bahwa aplikasi berhasil diakses melalui alamat lokal komputer. Tampilan tersebut menjadi bukti bahwa server web telah berjalan dan dapat memberikan respons terhadap permintaan dari browser. Tujuan proses ini adalah memastikan aplikasi dapat diakses dengan baik sebelum dilanjutkan ke tahap konfigurasi dan penerapan load balancing menggunakan Docker dan Nginx.

### 11. Memeriksa Aktivitas Permintaan HTTP pada Server

<img src="images/gambar 12.png" width="610">

#### Pembahasan :

<p align ="justify">Proses ini dilakukan dengan mengamati keluaran terminal ketika aplikasi Blacksheep sedang berjalan dan diakses melalui browser. Terminal menampilkan sejumlah log permintaan HTTP, seperti permintaan terhadap halaman utama, file CSS, JavaScript, gambar, dan beberapa sumber pendukung lainnya. Kode status 200 OK menunjukkan bahwa server berhasil memproses permintaan dan mengirimkan respons kepada browser. Tujuan proses ini adalah memeriksa aktivitas komunikasi antara browser dan server serta memastikan bahwa berbagai sumber daya yang diperlukan oleh halaman web dapat dimuat dengan baik.

### 12. Memeriksa Container yang Sedang Berjalan Menggunakan Docker PS

img src="images/gambar 12.png" width="610">

#### Pembahasan :

<p align ="justify">Pada tahap ini digunakan perintah docker ps --format "{{.Image}} {{.Names}}" untuk menampilkan daftar container yang sedang berjalan beserta nama image dan container-nya. Hasil terminal memperlihatkan beberapa container, termasuk workspace-05-nginx, workspace-05-bs_app-1, dan workspace-05-bs_app-2. Keberadaan dua container bs_app menunjukkan bahwa aplikasi telah memiliki dua instance yang dapat digunakan untuk membagi beban permintaan. Tujuan proses ini adalah memeriksa kondisi container yang aktif serta memastikan bahwa layanan aplikasi dan Nginx telah tersedia dalam lingkungan Docker.




