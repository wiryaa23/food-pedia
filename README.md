# Food Pedia

**Nama**: Wirya Dharma Kurnia <br />
**NPM**: 2306152115 <br />
**Kelas**: PBP C

**Link Web:** [http://wirya-dharma-foodpedia.pbp.cs.ui.ac.id/](http://wirya-dharma-foodpedia.pbp.cs.ui.ac.id/)

# Jawaban Soal Tugas 2


## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Cara yang saya lakukan dalam tugas kali ini adalah sebagai berikut.
- Membuat repositori baru di github bernama “food-pedia” dengan visibility public.
- Membuat direktori lokal baru dengan nama “food-pedia” dan melakukan inisiasi git dengan perintah `git init`.
- Membuat branch utama dan menghubungkannya ke repositori GitHub.
- Membuat virtual environment dengan perintah `python -m venv env` dan mengaktifkannya dengan perintah `env\Scripts\activate`.
- Membuat file requirements.txt dan menginstall dependencies.
- Buat progek django dengan nama food_pedia menggunakan perintah `django-admin startproject food_pedia .`.
- Membuat app main dengan perintah `python manage.py startapp main`.
- Melakukan routing dengan konfigurasi URL pada app main.
- Melakukan konfigurasi pada `urls.py`.
- Membuat model dan menambahkan atribut wajib (name dengan tipe data CharField, price dengan tipe data IntegerField, dan description dengan tipe data TextField).
- Menambahkan atribut tambahan (quantity dengan tipe data IntegerField dan rating dengan tipe data FloatField).
- Menambahkan URL deployment PWS di bagian `ALLOWED_HOSTS` pada `settings.py`.
- Membuat migrasi model dengan perintah `python manage.py makemigrations`.
- Menerapkan migrasi ke dalam basis data lokal dengan perintah `python manage.py migrate`.
- Mengedit `main.html` untuk menyesuaikan layout informasi pada web.
- Mengatur function pada `views.py` sesuai tampilan yang diinginkan.
- Melakukan push perubahan ke GitHub dan PWS.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src="pictures/bagan_tugas2pbp.png">
Request dari user akan diproses melalui Django Web Server ke urls.py terlebih dahulu. Kemudian, urls.py akan meneruskannya ke view yang sesuai. View lalu akan membaca/menulis data pada model, dan mengggunakan template untuk menunjkkan respon pada user. Berkas .html juga akan dirender sehingga views.py dapat mengembalikan respons yang diinginkan kembali kepada user.

## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git merupakan sistem version control terdistribusi yang luas digunakan dalam pengembangan perangkat lunak. Git digunakan untuk membantu tim developer dalam bekerja, sehingga dapat bekerja secara kolaboratif dan memastikan setiap perubahan telah dicatat. Fungsinya antara lain adalah:
- Memonitor dan melacak setiap perubahan yang dibuat pada kode sumber
- Memungkinkan lebih dari satu developer untuk bekerja secara bersamaan pada proyek yang sama tanpa mengganggu pekerjaan satu sama lain
- Memungkinkan developer untuk membuat cabang baru dari kode utama dengan adanya branching, agar dapat mengerjakan fitur baru, memperbaiki bug, atau bereksperimen tanpa memengaruhi kode yang stabil.
- Menyediakan mekanisme backup untuk setiap proyek.
- Menyediakan fasilitas praktik code review sehingga developer lain dapat meninjau dan memberikan masukan sebelum kode digabungkan ke kode utama.

## 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena mudah digunakan dan memiliki fitur yang lengkap, misalnya ORM. Bahasa yang digunakan adalah Python, yaitu bahasa yang memang sudah dipelajari sebelumnya. Django juga memiliki struktur MVT (Model-View-Template), sehingga strukturnya mudah diapahami dan pelajar baru dapat memahami alur pengembangan web secara mendalam. Keamanan bawaan dari framework ini pun tergolong baik.

## 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object Relational Mapping) karena menyediakan suatu lapisan abstraksi untuk interaksi dengan basis data  menggunakan Python, tanpa harus menulis query SQL secara langsung. ORM akan memetakan objek ke tabel dalam kelas Python, sehingga dapat memudahkan developer dalam melakukan operasi basis data seperti menambah, mengubah, ataupun menghapus data.


# Jawaban Soal Tugas 3


## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform!
Data delivery merupakan salah satu aspek terpenting dalam pengimplementasian sebuah platform. Alasannya adalah karena sebagai berikut.
- Akses data secara real-time:  Dalam platform digital, seringkali developer maupun pengguna membutuhkan data secara real-time, baik untuk pengembangan aplikasi maupun untuk kebutuhan konsumen. Misalnya dalam aplikasi e-commerce, konsumen harus dapat melihat stok barang yang tersisa sebelum memesan barang tersebut.
- Integrasi data antar komponen: Ada berbagai komponen dalam platform digital, di mana seluruh komponen tersebut memerlukan pertukaran data yang konsisten agar platform dapat berjalan dengan baik. Data delivery berperan untuk melakukan integrasi data secara efisien antar komponen-komponen tersebut sehingga pertukaran data dapat terjadi di lingkungan platform tersebut.
- Optimisasi performa platform: Data delivery sebagai aspek terpenting tentunya akan sangat memengaruhi performa suatu platform. Mengoptimalisasi data delivery tentunya akan meningkatkan kinerja platform secara keseluruhan, khususnya jika skala platform sudah berkembang luas dan memiliki banyak pengguna.
- Keamanan data: Dalam proses data delivery, seringkali data dilindungi dengan melibatkan protokol keamanan seperti enkripsi. Proses data delivery yang terstruktur tentunya akan mempermudah pengelolaan data secara aman, sehingga data yang bersifat rahasia dapat tetap terjaga kerahasiaan dan integritasnya.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya pribadi, di era platform digital yang bersifat modern ini JSON cenderung lebih baik jika dibandingkan dengan XML. Alasan yang mendukung pendapat saya adalah sebagai berikut.
- Kompleksitas yang rendah dan mudah dibaca: JSON memiliki struktur yang lebih sederhana dan ringkas dibandingkan XML. Hal ini dikarenakan JSON lebih berfokus pada pengiriman dan pertukaran data, sehingga lebih mudah digunakan untuk mengembangkan API, aplikasi, dan layanan web modern. JSON juga memiliki format penyajian data yang cenderung lebih mudah dibaca oleh manusia.
- Ukuran data yang lebih kecil: Ukuran data JSON lebih kecil dibandingkan XML, karena JSON tidak menggunakan banyak markup seperti XML dalam membungkus data. Hal ini menyebabkan penyimpanan yang digunakan menjadi lebih sedikit sehingga program dapat berjalan dengan lebih cepat dan efisien.
- Kecepatan pemrosesan data: Karena ukurannya lebih kecil, pemrosesan data dengan JSON juga mengalami peningkatan jika dibandingkan dengan XML. Karena itu, JSON lebih cocok digunakan untuk program yang membutuhkan respon yang cepat dengan pertukaran data yang sederhana.
Karena alasan-alasan di atas, JSON lebih populer dibandingkan XML untuk kebanyakan aplikasi modern saat ini.

## 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django berfungsi untuk melakukan validasi terhadap data yang masuk ke dalam form. Hal ini penting untuk memastikan semua data yang masuk ke dalam form telah memenuhi aturan validasi yang ditentukan. Alasan method ini penting dan dibutuhkan adalah sebagai berikut.
- Validasi data: Ini merupakan tujuan utama dari method `is_valid()`, yaitu memastikan bahwa semua field data yang dibutuhkan telah terisi sesuai dengan tipe data yang diminta, dan memenuhi aturan validasi yang berlaku (seperti nilai minimum dari integer atau panjang minimum dari string).
- Feedback kepada user: Django dapat memberikan pesan error tertentu kepada user jika data yang dimasukkan tidak sesuai. Hal ini memudahkan user untuk memperbaiki input yang dimasukkan.
- Meningkatkan keamanan: Validasi data menyebabkan input yang diterima oleh program cenderung aman. Dalam beberapa kasus, ada kemungkinan input yang dimasukkan berbahaya dan dapat memicu serangan seperti injection. Hal ini dicegah dengan validasi data yang dilakukan method `is_valid()`.

## 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` pada Django berfungsi sebagai salah satu mekanisme perlindungan untuk keamanan platform, khususnya dalam perlindungan serangan Cross-Site Request Forgery (CSRF). CSRF merupakan serangan di mana penyerang melakukan eksploitsi kredensial pengguna lain untuk membuat mereka mengirim request yang tidak sah ke situs web tertentu tanpa sepengetahuan atau izin pengguna tersebut. Dalam hal ini, `csrf_token` berguna untuk memverifikasi request yang dikirim berasal dari pengguna yang sah.

Jika kita tidak menambahkan `csrf_token` pada form Django, aplikasi akan rentan terhadap serangan CSRF. Ini memberikan kesempatan kepada penyerang untuk melakukan aksi dengan memanfaatkan kredensial pengguna lain. Hal tersebut dimanfaatkan penyerang dengan cara sebagai berikut.
- Penyerang bisa saja membuat request HTTP palsu dengan formulir HTML atau script JavaScript, yang secara otomatis mengirim reuqest yang tidak diinginkan.
- Ketika pengguna yang sah mengunjungi halaman penyerang dalam sesi aplikasi yang sedang berlangsung, browser dapat menyertakan cookie sesi yang valid sehingga server akan menganggap request tersebut bersifat sah.
- Jika hal ini terjadi, penyerang dapat memanfaatkannya untuk melakukan tindakan kriminal seperti pencurian data, transaksi yang tidak sah, dan masih banyak lagi.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Cara yang saya lakukan dalam tugas kali ini adalah sebagai berikut.
- Membuat direktori `templates` pada root folder dan mengisinya dengan `base.html`, yang berfungsi sebagai template dasar/kerangka views dari web.
- Menambahkan `templates` yang telah dibuat pada `settings.py`.
- Mengubah `main.html` pada subdirektori `main/templates` dengan menggunakan `base.html` sebagai template utama.
- Menghapus berkas `db.sqlite3` untuk mengosongkan objek pada model. Kemudian melakukan `import uuid` pada `models.py` dan dilanjutkan dengan melakukan migrasi perubahan tersebut.
- Membuat berkas `forms.py` pada direktori `main` dan mengisinya sesuai model yang telah dibuat sebelumnya. 
- Menambahkan import redirect pada `views.py` di direktori `main`, lalu membuat fungsi `create_food_entry` yang menerima parameter request. Fungsi ini melakukan redirect ke fungsi `show_main`.
- Mengubah fungsi `show_main` sesuai kebutuhan web. Dalam web saya, fungsi ini mengambil data entri makanan yang sudah default dan yang dari database, kemudian menampilkannya pada halaman web. Context pada fungsi ini akan berubah sehingga berupa gabungan entri default dan database.
- Menambahkan import `create_mood_entry` dan path fungsi ke berkas `urls.py`.
- Membuat berkas HTML baru dengan nama `create_food_entry.html` pada direktori `main/templates` dan mengubah isinya sesuai kebutuhan web Food Pedia. Berkas ini berfungsi untuk menandakan block dengan metode POST, meningkatkan security terhadap serangan CSRF, menampilkan fields `forms.py` sebagai table, dan mengirim request ke view `create_food_entry(request)` dengan tombol submit.
- Mengedit `main.html` untuk menambahkan tombol "Add New Food".
- Pada berkas `views.py`, lakukan import `HttpResponse`, `Serializer`, dan membuat 4 fungsi baru untuk menampilkan data pada JSON dan XML. Fungsi tersebut adalah `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`.
- Menambahkan fungsi baru yaitu `delete_item` yang menerima parameter request dan pk, yang berfungsi untuk menghapus data tertentu pada database. Path kelima fungsi baru ini juga ditambahkan pada bagian `urlpatterns` di berkas `urls.py`.
- Membuat berkas `deploy.yml` pada direktori `.github/workflows/` agar dapat melakukan push ke GitHub sekaligus PWS.
- Melakukan push perubahan ke GitHub, yang secara otomatis akan meneruskannya ke PWS dengan GitHub actions.

## Dokumentasi URL Postman
`show_json`: <img src="pictures/show_json.png">
`show_xml`: <img src="pictures/show_xml.png">
`show_json_by_id`: <img src="pictures/show_json_by_id.png">
`show_xml_by_id`: <img src="pictures/show_xml_by_id.png">


# Jawaban Soal Tugas 4


## 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?


## 2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!


## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.


## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Cara yang saya lakukan dalam tugas kali ini adalah sebagai berikut.
- Melakukan import `UserCreationForm` dan `messages`, serta menambahkan fungsi `register` pada `views.py`.
- Membuat `register.html` di `main/templates` sebagai template tampilan halaman register.
- Melakukan import fungsi `register` dan menambahkan pathnya di `urls.py` direktori `main`.
- Melakukan import `authenticate`, `login`, dan `AuthenticationForm`, serta menambahkan fungsi `login_user` pada `views.py`. Semua ini berfungsi untuk melakukan autentikasi dan jika berhasil akan melakukan login.
- Membuat `login.html` di `main/templates/` sebagai template tampilan halaman login.
- Melakukan import fungsi `login_user` dan menambahkan pathnya di `urls.py` direktori `main`.
- Membuat fitur logout dengan cara yang sama persis dengan pembuatan fitur login. Hanya saja, tampilannya diimplementasikan langsung di main.html karena hanya memerlukan tombol logout saja (tidak memerlukan halaman khusus).
- Menggunakan data dari cookies, yaitu awalnya dengan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada `views.py`.
- Menambahkan fungsionalitas cookie untuk melihat waktu terakhir login pengguna pada fungsi `login_user`. Setelah perubahan, cookie last_login user akan ditambahkan ke dalam response yang diberikan server.
- Menambahkan `'last_login': request.COOKIES['last_login']` ke `context` pada fungsi `show_main`.
- Mengubah fungsi `logout_user` sehingga cookie `last_login` dihapus saat user logout.
- Menambahkan informasi data sesi terakhir login pada `main.html`.
- Menghubungkan model dengan user, yaitu pertama dengan melakukan import model pada `models.py` di `main`.'
- Selanjutnya, hubungkan model dengan satu user melalui sebuah relationship.
- Mengubah fungsi `create_food_entry` pada `views.py` untuk memungkinkan modifikasi objek sebelum disimpan di database.
- Mengubah value dari `food_entries` dan `context` pada fungsi `show_main`. Hal ini dilakukan agar program dapat menampilkan objek Food Entry dari user yang sedang login saja.
- Melakukan migrasi model untuk mengimplementasikan perubahan.