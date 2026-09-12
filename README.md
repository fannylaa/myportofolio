Nama : Stephanie Revalina Tamus

NPM : 2506547153

Kelas : PBP C

## AI Disclosure & Collaboration Strategy
Dalam pengerjaan proyek portofolio Django ini, saya menggunakan AI (Gemini) sebagai *thought partner* dan asisten dengan pendekatan yang berkembang seiring berjalannya proses pengerjaan:

* **1. Tahap Eksplorasi & Memahami Fondasi:**
    Di awal pengerjaan Tutorial 1, sempat ada banyak kebingungan terkait alur dan sintaks Django. Pada fase ini, saya menggunakan AI secara intensif untuk membedah baris demi baris kode yang berulang atau membingungkan agar saya benar-benar paham fungsi di baliknya secara logis. 
* **2. Transisi ke Delegasi Tugas Repetitif:**
    Seiring bertambahnya pemahaman dan mulai terbiasanya saya dengan pola struktur Django, saya mulai mendelegasikan penulisan kode-kode yang sifatnya repetitif atau boilerplate kepada AI selama saya sudah tahu secara pasti untuk apa kode tersebut dibuat dan bagaimana alurnya bekerja.
* **3. Kontrol Utama & Integrasi Kode:**
    Meskipun AI membantu mempercepat penulisan bagian yang berulang, saya tetap memegang kendali penuh atas pengujian, penyesuaian logika utama, integrasi ke dalam proyek, serta memastikan bahwa seluruh unit test (`TestCase`) berjalan hijau (15/15 *passed*).
* **4. Penggunaan AI:**
    AI digunakan dalam proses debugging pesan error pada database, memvalidasi alur routing urls.py, serta membantu merapikan struktur bahasa pada bagian dokumentasi reflektif agar argumen teknis tersampaikan secara logis dan jelas.


### Tugas 1

## Reflective Questions (Week 1)

### 1. Penggunaan Elemen Semantik HTML5
**Apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Bagaimana elemen tersebut membantu dalam membuat static web?**

Ya, saya menggunakan elemen semantik HTML5 secara penuh dalam merancang struktur web portofolio ini, seperti `<header>`, `<main>`, `<section>`, dan `<article>`. 

Penggunaan elemen semantik sangat membantu dalam membuat static web karena:
- **Kemudahan Navigasi dan Keterbacaan Kode**: Pengelompokan struktur menjadi jauh lebih jelas dibandingkan hanya menggunakan tumpukan `<div>`. Saya dan pengembang lain dapat langsung mengenali bagian mana yang berfungsi sebagai navigasi (`<header>`), konten utama (`<main>`), pengelompokan topik (`<section>`), hingga kartu informasi independen (`<article>`).
- **Aksesibilitas dan SEO**: Elemen semantik membantu screen reader memahami hierarki informasi dengan baik bagi pengguna berkebutuhan khusus, serta memudahkan mesin pencari mengindeks bagian-bagian penting dari portofolio saya.

---

### 2. Responsivitas CSS dan Evaluasi Tata Letak Mobile
**Tantangan tata letak apa yang Anda temukan saat mengatur CSS agar responsive? Bagaimana Anda mengevaluasi elemen yang harus diubah posisinya atau diprioritaskan ukurannya dari desktop ke mobile?**

**Tantangan Tata Letak:**
Tantangan terbesar adalah menjaga keseimbangan visual dan konsistensi proporsi jarak (padding dan gap) saat beralih dari layar lebar ke layar yang lebih sempit, terutama pada bagian grid kartu (Core Values serta Background dan Skills) agar tidak terlihat terlalu padat atau gepeng.

**Strategi Evaluasi dan Prioritas:**
- **CSS Grid dan Flexbox Fluid**: Saya memanfaatkan fitur modern CSS seperti `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));` yang memungkinkan elemen kartu beradaptasi secara otomatis dari banyak kolom di desktop menjadi satu kolom vertikal di layar mobile tanpa perlu membuat banyak media queries manual.
- **Hierarki Konten Mobile**: Saat beralih ke layar mobile, elemen visual sekunder diberi proporsi yang lebih ringkas (misalnya ukuran hero avatar dikecilkan dan jarak padding disesuaikan) agar informasi teks utama seperti bio dan core values tetap menjadi fokus utama yang pertama kali dibaca oleh pengunjung.
- **Penggunaan Typography Fluid**: Menggunakan fungsi `clamp()` pada judul utama agar ukuran teks membesar dan mengecil secara halus sesuai lebar viewport perangkat.

---

### 3. Batasan Static Web dan Rencana Fungsionalitas Dinamis
**Batasan apa yang Anda rasakan saat menyajikan informasi secara static? Fungsionalitas dinamis apa yang ingin Anda tambahkan pada iterasi proyek selanjutnya?**

**Batasan Static Web:**
- **Pengelolaan Konten Manual**: Setiap kali ada penambahan data baru (seperti proyek baru, pengalaman, atau daftar keahlian), saya harus mengubah kode HTML secara langsung dan melakukan commit atau deploy ulang.
- **Kurangnya Interaktivitas Pengunjung**: Website belum dapat menerima masukan atau interaksi dari pengunjung secara langsung, seperti formulir kontak yang mengirimkan pesan nyata atau fitur penyaring (filter) kategori keahlian.

**Rencana Fungsionalitas Dinamis di Iterasi Selanjutnya:**
- **Integrasi Database dan Django ORM**: Mengintegrasikan Model Django untuk menyimpan data proyek, keahlian, dan core values secara terpusat di database SQLite atau PostgreSQL.
- **Dynamic Content Rendering**: Menggunakan Django Views dan Templates untuk melakukan looping data secara dinamis dari database ke template HTML.
- **Interactive Contact Form**: Menyediakan formulir kontak dinamis yang memproses data input pengunjung melalui Django Forms dan menyimpannya ke database atau mengirimkannya via email.

### Tugas 2

## Reflective Questions (Week 2)
### 1. Alur Perjalanan Data (MVT Lifecycle) di Proyek Portofolio

- urls.py Proyek: Titik awal semua request HTTP dari browser masuk. Berdasarkan URL yang diketik, routing utama ini bertugas mengenali area aplikasi mana yang dituju lalu meneruskannya menggunakan include(), persis seperti catatan komentar yang saya tulis di file main/views.py  untuk memetakan seluruh endpoint aplikasi.

- urls.py Aplikasi: Di dalam modul aplikasi, routing ini memecah URL lebih spesifik lagi untuk mencocokkannya dengan fungsi view yang bertanggung jawab menangani halaman tersebut, ini memastikan setiap permintaan langsung mengarah ke fungsi pengolah yang sesuai dengan dokumentasi kodeku.

- View: View menerima request yang masuk, berkoordinasi dengan Model untuk meminta data yang diperlukan, lalu mengkoordinasikan data tersebut ke dalam konteks template sesuai dengan alur logika yang yg saya notes di fungsi view.

- Model: Representasi struktur data berbasis Object-Relational Mapping (ORM). Model menterjemahkan interaksi Python menjadi query SQL yang aman untuk mengambil atau menyimpan data portofolio dari database tanpa perlu menulis query mentah, selaras dengan struktur class yang saya notes di models.py.

- Template: Komponen visual berupa file HTML yang menerima data dari view. Template bertugas merender data tersebut menjadi antarmuka yang siap ditampilkan kembali ke browser pengguna.

### 2. Alur Penyimpanan Data Portofolio pada Model vs. Hardcode di Template
Menyimpan data portofolio melalui Model jauh lebih dianjurkan ketimbang menulisnya langsung (hardcode) di dalam file HTML. Jika data ditulis di dalam template, setiap kali ada penambahan atau perubahan proyek, kita harus selalu mengubah baris kode sumber secara manual, yang tentu sangat tidak efisien dan rentan merusak layout. Dengan memanfaatkan Model dan database, konten portofolio menjadi dinamis dan terpusat. Kita bisa dengan mudah menambah, mengedit, atau menghapus data secara praktis lewat antarmuka Django Admin tanpa perlu menyentuh atau merusak struktur kodenya lagi.

### 3. Perbedaan makemigrations dan migrate

makemigrations: Berfungsi untuk mendeteksi setiap perubahan yang kita buat pada file models.py (seperti menambah model baru atau mengubah field) dan merangkumnya menjadi sebuah file cetak biru atau draf instruksi migrasi. Pada tahap ini, database fisik belum disentuh sama sekali.

migrate: Berfungsi untuk menerjemahkan dan mengeksekusi file draf migrasi tersebut secara nyata ke dalam database fisik (seperti SQLite), sehingga tabel-tabel yang dibutuhkan benar-benar terbentuk atau diperbarui.

Contoh Kasus: Ketika kita mendefinisikan kelas model baru untuk item portofolio di file models.py (seperti yang saya notes dalam dokumentasi model), kita wajib menjalankan python manage.py makemigrations terlebih dahulu agar Django membuat rekam jejak perubahannya, kemudian dilanjutkan dengan python manage.py migrate agar tabel tersebut resmi tercipta di database dan siap dipakai oleh view.