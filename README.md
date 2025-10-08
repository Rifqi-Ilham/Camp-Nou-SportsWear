
Nama: Muhammad Rifqi Ilham  
NPM: 2406495483  
Kelas: PBP-E  
Link penugasan: https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-6
Link Deployment: https://muhammad-rifqi411-campnousportswear.pbp.cs.ui.ac.id/

# Tugas 6: Javascript dan AJAX
## 1.  Apa perbedaan antara synchronous request dan asynchronous request?
Perbedaannya adalah synchronous request menahan DOM atau browser untuk mengeksekusi suatu kode sampai server mengirim response, sedangkan asynchronous request tidak memperhatikan hal tersebut, sehingga DOM atau browser langsung mengeksekusi kode.

## 2.  Bagaimana AJAX bekerja di Django (alur request–response)?
Saat user mengirim request, misal submit sebuah data, maka akan ada sebuah XMLHttpRequest atau fetch yang dibuat oleh Javascript. Lalu, objek XMLHttpRequest atau fetch mengirimkan request ke server, dan server akan memproses request tersebut. Nantinya, server akan mengembalikan kembali response kepada web dan dibaca oleh javascript. Dan akhirnya, DOM melakukan dynamic rendering untuk mengubah sebagian tampilan di browser.

## 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Dengan menggunakan AJAX, kita dapat melakukan partial update pada halaman web, dimana halaman tidak perlu di reload sepenuhnya. Karena proses ini juga, dimana AJAX hanya melakukan fetching dan mengupdate sebagian halaman, proses interaksi akan menjadi lebih cepat.

## 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Memastikan keamanan di fitur login dan register django menggunakan ajax dilakukan dengan melindungi website dari Cross Site Scripting (XSS), dimana developer menambahkan strip tags pada entry yang akan dimasukan oleh pengguna. Sehingga data yang disimpan dalam database adalah data yang sudah "bersih"

## 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX dapat membuat pengalaman pengguna menjadi lebih interaktif, cepat dan seamless dengan mengeliminasi keperluan untuk melakukan reload page saat mengupdate sebagian halaman. Sehingga, penggunaan website bisa menjadi lebih nyaman.


# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
Link penugasan: https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-5
Link Deployment: https://muhammad-rifqi411-campnousportswear.pbp.cs.ui.ac.id/
## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan secara hirearki pada css selector adalah:
1. inline style, yang langsung mempengaruhi ke style attribute HTML
2. id selector
3. Class, attribute, pseudo-class selector
4. Tag/element selector
5. Universal selector

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Karena dengan menerapkan responsive design, aplikasi web yang kita kembangkan dapat diakses di berbagai platform ukuran bebeda dengan nyaman. Contoh aplikasi yang sudah menerapkan responsive design adalah youtube. Di youtube, tampilan akan berubah sesuai dengan gadget apa yang kita gunakan untuk mengakses youtube tersebut. Sedangkan, ada juga website yang belum menerapkan responsive design, misalnya, saya menemukan
[website](https://dequeuniversity.com/library/responsive/1-non-responsive) ini sebagai contoh website yang tidak responsif. Apabila kita coba buka website dari laptop, dan juga dari handphone, kita dapat melihat dengan jelas bahwa tidak ada penyesuaian, sehingga website ini tidak menerapkan design yg responsive.

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin, border dan padding merupakan bagian dari layout CSS, dimana margin merupakan bagian terluar, dan tiap bagian akan wrap terus ke bagian dalam. Sebagai definisi:
1. Margin merupakan ruang diluar yang memisahkan elemen dengan elemen lain. 
2. Border merupakan garis atau frame terlihat yang membungkus elemen di padding.
3. Padding merupakan ruang luar antara elemen dengan elemen lain, diantara border dan content.
Kita bisa mengimplementasikan ketiga elemen tersebut dengan taiilwind css, misal:
```
<div class="m-5 border-2 border-[#FDB913] p-4">
```
Disini kita memberikan jarak di luar elemen menggunakan margin, yaitu 5 spacing jarak dari elemen ke elemen lain. Lalu, disini kita membuat garis pinggir dan mengubah warna dengan border, dimana border di set ke 2px, dan warna diatur ke warna hex #FDB913. Selanjutnya, disini kiita memberikan jarak di dalam elemen menggunakan padding sebanyak 4 spacing unit. 

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan grid layout merupakan CSS layut modules yang sering digunakan untuk membuat website responsif.
1. Flexbox biasanya digunakan untuk layout 1 dimensi, dimana dapat menyusun item di satu arah, baik sebagai baris atau kolom, sehingga cocok untuk align item atau justify.
2. CSS Grid layout biasanya digunakan untuk layout 2 dimensi, dimana dapat dapat menyusun item di dua arah (baris dan kolom secara bersamaan), sehingga cocok untuk grid elemen.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Secara garis besar, berikut langkah-langkah saya dalam mengiimplementasikan aplikasi:
1. memikirkan terlebih dahulu, design web akan seperti apa, lalu mendownload source statis, misal image yang akan dibutuhkan.
2. menyambungkan django dengan tailwind di base.html dengan CDN
3. menambahkan fungsi edit product & delete product di views.py
4. melakukan routing fungsi-fungsi yang baru dibuat di urls.py
5. menerapkan fungsi-fungsi tersebut di main.html
6. membuat navigation bar dengan navbar.html di templates/
7. melakukan konfigurasi pada pengaturan di settings.py
8. membuat file global css di dir static, stylying global css, include source statis yang tadi didownload, lalu hubungkan ke tailwind
9. melakukan styling sesuai konsep website untuk navbar, login, register, home, create news dan detail news
10. membuat card untuk product, lalu tambahkan di main.html
11. push ke gihub dan pws








Nama: Muhammad Rifqi Ilham  
NPM: 2406495483  
Kelas: PBP-E  
Link penugasan: https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-4
# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm merupakan fitur yang telah disediakan oleh django untuk form login pengguna, sehingga developer tidak perlu membuat login form dari nol. 
Kelebihan dari Django AuthenticationForm:
1. tidak perlu menulis validasi email dan password manual.
2. Otomatis handling validasi pengguna yang aktif.
3. Relatif simple & Bisa langsung dipakai.

Kekurangan dari Django AuthenticationForm:
1. Kurang fleksibel, misal jika developer ingin menambahkan field baru
2. Penampilannnya masih default, sehingga perlu dibuat tampilan HTML/CSS agar lebih selaras dengan website yang dibuat.

## 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi merupakan proses verifikasi data pengguna, sedangkan otorisasi menentukan hak akses yang dapat dilakukan oleh pengguna setelah login. Pada django, developer diberikan model bawaaan user, AuthenticationForm, serta fungsi login() dan juga logout() untuk proses autentikasi. Sedangkan untuk otorisasi, developer  dapat menggunakan decorator seperti @login_requiered sebelum fungsi di views untuk membatasi akses halaman sehingga hanya bisa diakses untuk yang sudah login.

## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan Session:
1. Data tersimpan di server sehingga lebih aman.
2. bisa menampung data besar.

Kekurangan Session:
1. Membutuhkan penyimpanan server
2. Membutuhkan mekanisme garbage collection untuk session lama

Kelebihan Cookies:
1. Bisa diakses di client-side
2. Tidak butuh storage server, karena lebih ringan.

Kekurangan Cookies:
1. Ukuran terbatas (~4KB)
2. Adanya risiko keamanan yang harus diperhatikan (XSS, CSRF)

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies relatif aman dalam pengembangan web, walaupun memiliki beberapa risiko keamanan yang harus diperhatikan. Misal, adanya cookies memungkinkan serangan dimana session cookie bisa dicuri lewat jaringan, namun Django telah menangani hal ini dengan mencegah javascript membaca cookie melalui pengaktifan HTTPOnly untuk session cookie. Selain itu, bisa juga ada serangan dimana hacker memanfaatkan CSRF yang ada di session cookies untuk melakukan hal yang tidak diinginkan user, namun Django juga telah mengatasi ini dengan penerapan CSRF token sehingga apabila token terjadi mismatch, request akan ditolak. Jadi, Penggunaan cookies secara default dalam pengembanan web relatif aman karena beberapa hal sudah di handle oleh Django, namun pada tahap produksi akan lebih baik jika developer menerapkan keamanan tambahan, misal seperti HTTPS.


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Secara garis besar, berikut langkah saya dalam mengimplementasikan checklist tugas:
1. membuat fungsi form register di views.py, dan menambahkan templates register.html
2. membuat fungsi form login di views.py, dan juga menambahkan templates login.html
3. membuat fungsi logout di views.py, dan menambahkan button logout di main.html
5. melakukan routing untuk register, login dan logout di urls.py level aplikasi
6. menerapkan otorisasi dengan menambahkan @login_required pada fungsi show_main dan show_product di views.py
7. modifikasi fungsi login user dan menerapkan cookies di views.py
8. modifikasi model Product dengan menambahkan attribute bawaan django yaitu User, lalu melakukan migrate
9. memodifikasi create_product dan show_main di views.py untuk menambahkan validasi dan filtering, tombol filtering juga ditambahkan di main.html
10. Menampilkan nama author di news detail melalui attribute user yang tadi sudah ditambahkan
11. testing membuat produk di akun berbeda saat di local
12. Push ke github dan pws


# Tugas 3: Implementasi Form dan Data Delivery pada Django
Nama: Muhammad Rifqi Ilham  
NPM: 2406495483  
Kelas: PBP-E  
Link penugasan: https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-3 
## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery agar bisa ada komunikasi data antara client dengan server, sehingga platform nantinya bisa menampilkan data secara real-time, juga menerima input user agar platform bisa interaktif.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dibandingkan XML, karena saya merasa JSON lebih mudah dibaca oleh manusia dan lebih ringkas dibandingkan XML, JSON juga lebih mudah untuk diolah di banyak bahasa pemrograman, hal-hal inilah yang menyebabkan JSON lebih populer dibandingkan XML.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
method is_valid pada form django berfungsi sebagai validasi data yang dimasukan user saat input ke form (misal tipe datanya, constrains, etc), tanpa hal tersebut, ada risiko bahwa data yang disimpan user tidak sesuai dengan database, sehingga bisa merusak program.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF Token (Cross-Site Request Forgery) adalah token unik yang dibutuhkan sebagai proteks dari hacker yang mengirim request palsu yang pura-pura bertindak sebagai user, sehingga bisa saja hal ini dimanfaatkan untuk melakukan hal berbahaya yang tidak dinginkan user, misal mengubah data user tanpa sepengetahuan mereka. Dengan adanya CSRF, server dapat memverifikasi bahwa request yang datang benar-benar dari form user, sehingga hal ini bisa dicegah.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Secara garis besar, berikut langkah-langkah yang saya lakukan dalam mengerjakan tugas ini:
1. Menambahkan forms.py untuk memasukan model product
2. Membuat fungsi untuk proses delivery data seperti create product, show product dan juga show melalui XML, JSON, XML by ID dan JSON by ID
3. Melakukan routing di urls.py untuk fungsi-fungsi baru yang dibuat di views.pyh
4. Membuat templates baru untuk halaman utama (main.html) membuat product (create_product.html) dan melihat detail product (product_detal.html), serta  
5. testing terlebih dahulu di server local, apakah form sudah berhasil, dan apakah data bisa dilihat melalui XML, JSON, XML by ID dan JSON by ID
6. mencoba untuk mengakses data melalui postman
7. menambahkan domain di PWS sebagai CSRF trusted domain
8. push ke github dan PWS

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
tidak ada

## 7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![hasil postman xml](assets/xml.png)
![hasil postman json](assets/json.png)
![hasil postman xml by id](assets/xml_id.png)
![hasil postman json by id](assets/json_id.png)


# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Nama: Muhammad Rifqi Ilham  
NPM: 2406495483  
Kelas: PBP-E  
Link penugasan: https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-2  


## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Selain mengikuti tutorial, saya juga bereksperimen dalam membuat website agar terlihat lebih kreatif dengan menggunakan CSS. Walaupun, saya menemukan masalah bahwa PWS gagal menemukan CSS saya, padahal pada server local Django CSS berhasil ditemukan. Saya mencoba menggunakan collectstatic, tapi masih belum mengatasi masalah. Namun, Secara garis besar, saya berhasil mengerjakan yang diminta tutorial dengan langkah berikut:
1. Membuat environment python baru
2. Membuat proyek Django dan aplikasi main
3. Menambahkan konfigurasi pada settings.py untuk menambahkan nama app
4. membuat model product, dengan atribut yang diminta.
5. Melakukan migrasi database.
6. Konfigurasi pada views.py, dan mengatur routing di urls.py
7. Membuat tampilan website html dan css
8. Push ke PWS



## 2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Diagram Django antara urls.py, views.py, models.py, dan html](assets/diagram.png)
Penjelasan:
1. User mengirim HTTP request, Django lanjutkan ke urls.py
2. Jika request cocok, urls.py akan melanjutkan ke views.py (suatu fungsi atau class tertentu)
3. views.py meminta/mengubah data ke models.py (apabila dibutuhkan)
4. hasil data dikembalikan ke views.py
5. merender data ke templates html
6. template html jadi produk final, dikirim sebagai HTTP response

## 3. Jelaskan peran settings.py dalam proyek Django!
Settings.py dalam proyek Django berfungsi sebagai tempat penyimpanan semua pengaturan penting dalam proyek.
Hal-hal tersebut meliputi:
1. Pengaturan Database
2. Installed apps
3. Allowed Host
4. Templates
5. Keamanan & Autentikasi
Dan masih ada beberapa hal yang diatur di settings.py, pada dasarnya file ini adalah pusat penyimpanan konfigurasi penting proyek Django yang dibuat.




## 4. Bagaimana cara kerja migrasi database di Django?
1. Membuat / Mengubah models.py terlebih dahulu.
2. Melakukan migrations dengan menjalankan command:
`python manage.py makemigrations`
3. Setelah command dijalankan, Django akan membaca perubahan database dan membuat migrasi.
4. Lakukan migrasi dengan menjalankan command:
`python manage.py migrate`
5. Django akan mengeksekusi file menjadi query SQL, maka Migrasi database berhasil dilakukan.



## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
1. Karena mahasiswa sudah mempelajari Python di DDP-1, sehingga akan lebih mudah dipahami.
2. Banyak fitur bawaan yang diberikan (ORM, Autentikasi, Middleware, Unit test, etc)
3. Lebih aman dan stabil, jika dibandingkan dengan bahasa lain (misal PHP)
4. kita bisa membaca dokumentasi lengkap dan Django yang popular memberikan komunitas yang kuat. 
5. Django dapat digunakan secara cepat untuk membangun prototype.

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tutorial sangat seru !
