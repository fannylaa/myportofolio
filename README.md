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

* **5. Tutorial 07 dan Individual Assignment 6 (Django REST Framework):**
    Untuk Tutorial 07 dan Tugas 6 saya memakai Claude (Anthropic) lewat Claude Code, bukan Gemini. Strateginya: saya memberikan PDF instruksi dan folder proyek, lalu Claude menyusun draf `serializers.py`, `permissions.py`, `api_views.py`, `api_urls.py`, JavaScript halaman Projects dan Experience, serta test `APITestCase`. Karena model saya berbeda dari contoh tutorial, kode harus disesuaikan: primary key `Project` berupa integer (bukan UUID), kolom `technology` dipetakan ke `tech_stack` lewat `source=`, dan `Experience` perlu relasi `starred_by` baru beserta migrasi `0006`. Selain itu, tujuh test lama di `main/tests.py` sudah gagal sejak halaman memuat data lewat AJAX, sehingga assertion-nya diperbarui mengikuti kontrak API yang baru (tidak dihapus). Hasilnya diuji dengan menjalankan `python manage.py test main` dan mencoba halaman di browser untuk keempat peran (pengunjung, pengguna biasa, Editor, pemilik). Keterbatasan AI di sini: contoh tutorial tidak otomatis cocok dengan model milik sendiri, sehingga hasilnya perlu dibaca dan diuji, bukan dipakai begitu saja.


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

### Tugas 3

## Reflective Questions (Week 3)
### 1. Alur Penggunaan ModelForm vs. Form HTML Manual serta Esensi `{% csrf_token %}`

- **Keunggulan Arsitektural `ModelForm`**: Pembuatan form secara manual dengan elemen HTML mentah (`<form>`, `<input>`, dll.) memaksa pengembang untuk menduplikasi logika validasi yang sebenarnya sudah didefinisikan secara deklaratif di dalam *layer* `models.py`. `ModelForm` menjembatani lapisan basis data dan antarmuka web secara otomatis (*meta-programming*), di mana Django melakukan *auto-generation fields*, pemetaan tipe data secara presisi, serta menangani proses *clean and validation data* sebelum objek disimpan (`form.save()`). Hal ini meminimalisir *human error* dan menjaga prinsip DRY (*Don't Repeat Yourself*).
- **Mekanisme Keamanan `{% csrf_token %}`**: Token CSRF (*Cross-Site Request Forgery*) bekerja dengan cara menyisipkan nilai *cryptographic token* yang unik, rahasia, dan terikat pada sesi pengguna (*user session*) saat halaman form dirender. Ketika form disubmit via metode POST, Django memvalidasi apakah token pada *payload* request cocok dengan token di server. Jika seorang penyerang mencoba mengeksploitasi sesi autentikasi korban melalui *malicious site* eksternal, penyerang tersebut tidak akan bisa menebak atau memalsukan nilai token rahasia ini, sehingga server dapat menolak request ilegal tersebut secara preventif.

### 2. Paradigma JSON vs. XML dalam Ekosistem Web Modern
Alasan utama JSON mendominasi pengembangan web modern ketimbang XML terletak pada efisiensi *parsing*, ukuran *payload*, dan keselarasan dengan paradigma bahasa pemrograman. 
- **Struktur dan Bandwidth**: XML menggunakan pendekatan dokumen bertingkat dengan *tag* pembuka dan penutup yang redundan (`<item>...</item>`), yang menyebabkan *overhead* ukuran *payload* jaringan menjadi besar. Sebaliknya, JSON merepresentasikan data melalui pasangan kunci-nilai (*key-value pairs*) yang sangat ringkas.
- **Kesesuaian Eksekusi (*Runtime Compatibility*)**: JSON pada dasarnya adalah bagian dari sintaks objek JavaScript. Dalam arsitektur web modern yang berbasis asinkron (seperti AJAX atau Fetch API di sisi *front-end*), data JSON dapat langsung dievaluasi dan diubah menjadi objek JavaScript siap pakai melalui fungsi bawaan `JSON.parse()` tanpa memerlukan *DOM parser* yang kompleks seperti halnya XML.

### 3. Anatomi Alur View JSON dan Kritisnya Proses *Serialization*
- **Alur Kerja Pengembalian JSON**: Ketika klien mengakses *endpoint* URL JSON, fungsi *view* memicu *database query* via ORM untuk mengambil sekumpulan objek model (berbentuk *QuerySet*). Objek-objek Python ini kemudian melewati modul `serializers.serialize()`, dikemas ke dalam objek `HttpResponse` dengan *MIME type* eksplisit `application/json`, dan dikirim kembali melalui protokol HTTP ke peramban atau klien eksternal.
- **Mengapa Harus Melalui *Serialization*?**: Django ORM mengembalikan data dalam bentuk objek Python tingkat tinggi (*native Python objects/QuerySet*) yang penuh dengan metode, relasi basis data, dan atribut internal yang hanya dimengerti oleh lingkungan *runtime* Django. Protokol HTTP murni hanya mentransfer aliran biner atau teks mentah (seperti *string*). Tanpa proses *serialization*—yang menerjemahkan struktur objek kompleks tersebut menjadi representasi string universal berformat JSON—server tidak akan memiliki cara untuk mengubah struktur data relasional internal menjadi format universal yang agnostik terhadap bahasa pemrograman apa pun di sisi penerima.

### Tugas 4

Tugas 4 tidak memiliki pertanyaan reflektif.

### Tugas 5

## Reflective Questions (Week 5)
### 1. Debouncing pada pencarian AJAX

1. Debouncing adalah teknik menunda pemanggilan sebuah fungsi sampai pengguna berhenti memicu event selama jeda waktu tertentu. Setiap event baru me-reset timer, sehingga fungsi hanya dijalankan sekali setelah jeda terakhir. Di halaman Experience saya, setiap event `input` pada kolom pencarian memanggil `clearTimeout(searchDebounceTimer)` lalu memasang `setTimeout` baru selama 300 ms (`SEARCH_DEBOUNCE_DELAY`). Jadi, jika saya mengetik "dosen" dengan cepat, request baru dikirim satu kali, 300 ms setelah huruf terakhir, bukan lima kali untuk "d", "do", "dos", dan seterusnya.
    - Teknik ini penting untuk pencarian AJAX karena tanpa debouncing setiap ketukan tombol langsung mengirim request ke server. Akibatnya server dan database menerima banyak query yang hasilnya langsung tidak terpakai, bandwidth terbuang, dan tampilan bisa "berkedip" karena hasil berganti terus-menerus.
    - Ada juga risiko *race condition*: response untuk "do" bisa datang setelah response untuk "dosen", sehingga hasil lama menimpa hasil terbaru. Debouncing mengurangi jumlah request, dan di kode saya `AbortController` membatalkan request sebelumnya yang belum selesai sehingga hanya hasil pencarian terakhir yang ditampilkan.

### 2. Fungsi `await` pada `fetch()`

2. `fetch()` bersifat asinkron: fungsi ini tidak langsung mengembalikan data, tetapi sebuah `Promise` yang baru terpenuhi setelah server membalas. `await` (yang hanya bisa dipakai di dalam fungsi `async`) membuat fungsi menunggu sampai `Promise` itu selesai, lalu memberikan hasilnya, tanpa membekukan halaman. Selama menunggu, browser tetap bisa merespons scroll, klik, dan ketikan pengguna. Di `fetchExperiences()` saya, `const response = await fetch(url, ...)` menunggu objek `Response`, lalu `response.ok` diperiksa, dan `await response.json()` menunggu lagi karena membaca isi body juga asinkron.
    - Jika `await` tidak dipakai, variabel `response` berisi `Promise`, bukan objek `Response`. Akibatnya `response.ok` bernilai `undefined` sehingga pengecekan status tidak berjalan, `response.json()` gagal dengan error karena `Promise` tidak punya method itu, dan baris berikutnya (misalnya `gridContainer.replaceChildren(...)`) langsung dijalankan sebelum data datang sehingga daftar tidak pernah terisi dengan benar.
    - Selain itu, error dari request yang gagal tidak tertangkap oleh blok `try...catch`, karena `catch` hanya menangkap kegagalan `Promise` yang di-`await`. Alternatif tanpa `await` adalah merangkai `.then()` dan `.catch()`, tetapi `async/await` membuat alurnya terbaca berurutan seperti kode sinkron.

### 3. Serangan XSS dan kerentanan data AJAX

3. XSS (*Cross-Site Scripting*) adalah serangan di mana penyerang menyisipkan kode berbahaya, biasanya JavaScript, ke dalam data yang nanti ditampilkan di halaman pengguna lain. Contohnya, judul pengalaman diisi `<img src="x" onerror="alert(document.cookie)">`. Jika data itu ditampilkan apa adanya, kode tersebut ikut berjalan di browser setiap pengunjung, sehingga penyerang bisa mencuri cookie atau session, melakukan aksi atas nama korban, atau mengubah tampilan halaman.
    - Template Django secara default melakukan *auto-escaping*: saat menulis `{{ experience.title }}`, karakter seperti `<`, `>`, `"`, dan `&` otomatis diubah menjadi `&lt;`, `&gt;`, dan seterusnya, sehingga input jahat tampil sebagai teks biasa dan tidak dijalankan. Perlindungan ini aktif tanpa perlu kita ingat, kecuali sengaja dimatikan dengan filter `|safe`.
    - Saat data diambil lewat AJAX, kartu disusun di sisi klien oleh JavaScript, dan perlindungan template Django tidak ikut berlaku. Jika string dari JSON dimasukkan ke `innerHTML`, browser akan mem-parse dan menjalankan tag di dalamnya. Tanggung jawab escaping berpindah ke developer, sehingga satu field yang lupa di-escape sudah cukup membuka celah XSS.
    - Di proyek saya, pertahanannya berlapis: di server, input dibersihkan dengan `strip_tags` (di `clean_<field>` pada form dan sekarang `validate_<field>` di serializer); di klien, setiap nilai teks yang disisipkan ke `innerHTML` melewati fungsi `escapeHtml()`. Lapisan klien tetap diperlukan karena `strip_tags` hanya membuang tag dan tidak menjamin data aman, serta data lama atau data yang masuk lewat admin bisa belum dibersihkan.

### Tugas 6

## Reflective Questions (Week 6)
### 1. REST, JSON saja belum cukup, serta PUT vs PATCH

1. REST (*Representational State Transfer*) adalah gaya arsitektur untuk merancang web API, bukan library atau format data. Tiga gagasan utamanya yang saya praktikkan: data diperlakukan sebagai *resource* yang punya URL (misalnya `/api/v1/experiences/<uuid>/`), HTTP method menyatakan tindakannya (`GET` membaca, `POST` membuat, `PUT`/`PATCH` mengubah, `DELETE` menghapus, sehingga tindakan tidak ditulis di URL seperti `/projects/delete/3/`), dan klien serta server bertukar representasi data (JSON), bersifat *stateless*, dengan status HTTP yang bermakna (201, 204, 400, 403, 404, 405). Mengembalikan JSON saja belum cukup karena endpoint seperti `/experience/json/` atau `/projects/add-ajax/` di Tutorial 05 memakai JSON tetapi tindakan tetap ditaruh di URL, hampir semuanya lewat `POST`, dan kontraknya tidak konsisten (`item.pk` dan `item.fields`). Itu API yang mengembalikan JSON, belum RESTful.
    - `PUT` mengganti seluruh representasi resource, sehingga semua field wajib dikirim. Contoh: menulis ulang satu entri Experience sekaligus dari form lengkap; jika hanya `title` yang dikirim, API menjawab 400 karena `description` dan `category` wajib.
    - `PATCH` hanya mengubah field yang dikirim (`partial=True` pada serializer). Contoh: Editor hanya memperbaiki judul pengalaman, atau menambahkan tanggal selesai, tanpa mengirim ulang deskripsi.

### 2. Peran serializer di DRF dan keuntungannya dibanding `JsonResponse`

2. Serializer berperan dua arah. Saat `GET` ia mengubah objek model menjadi tipe data Python yang bisa di-*render* ke JSON (*serialization*). Saat `POST`/`PUT`/`PATCH` ia mengubah input klien menjadi data yang sudah divalidasi dan siap disimpan (*deserialization*), lalu `.save()` memanggil `create()` atau `update()`. Pada Tutorial 05 saya merakit dictionary satu per satu dalam perulangan, memeriksa input lewat `ModelForm`, dan menulis `JsonResponse` serta status HTTP sendiri. Dengan `ExperienceSerializer`, (a) bentuk data didefinisikan sekali di `Meta.fields` (eksplisit, bukan `__all__`, sehingga data akun sensitif tidak ikut), (b) validasi ada di tempat yang sama dengan bentuk datanya (`validate_title` dengan `strip_tags`, pilihan `category` dari model, URL dari `URLField`) dan kegagalan otomatis menjadi 400 beserta pesan error per field lewat `is_valid(raise_exception=True)`, (c) field hasil perhitungan seperti `star_count`, `is_starred`, dan `is_ongoing` bersifat *read-only* sehingga tidak bisa dipalsukan klien (diuji di `test_computed_fields_are_read_only`), dan (d) view menjadi pendek karena tidak perlu `json.dumps`, `content_type`, maupun merakit dictionary manual.

### 3. Autentikasi vs otorisasi, dan mengapa hak akses harus di server

3. Autentikasi menjawab *siapa kamu*: `SessionAuthentication` membaca cookie session dan mengisi `request.user`. Otorisasi menjawab *apa yang boleh kamu lakukan*: *permission class* (`IsPortfolioOwnerOrEditorOrReadOnly`) memutuskan apakah request boleh diteruskan berdasarkan method dan peran (pengunjung hanya membaca, pengguna biasa boleh `star`, Editor boleh `PUT`/`PATCH`, pemilik boleh semuanya). Dalam DRF keduanya dipisahkan, dan urutannya autentikasi, permission, baru isi view. Itu sebabnya pengguna yang mengubah data yang tidak ada mendapat 403, bukan 404, karena permission diperiksa sebelum objek dicari. Hak akses harus diperiksa di server, bukan hanya dengan menyembunyikan tombol di template, karena tombol hanya mengatur tampilan. Siapa pun dapat membuka DevTools Console atau memakai `curl` untuk mengirim `DELETE` langsung ke URL API tanpa pernah melihat tombolnya. Hanya pemeriksaan di server yang benar-benar menolak request itu (diuji di `test_guest_and_regular_user_cannot_write`, yang juga memeriksa isi database tidak berubah). Menyembunyikan tombol tetap berguna untuk pengalaman pengguna, tetapi bukan pengaman.

### 4. CSRF pada `SessionAuthentication`, dan batas `force_authenticate`

4. Dengan `SessionAuthentication`, browser otomatis mengirim cookie session pada setiap request ke origin yang sama, termasuk request yang dipicu halaman jahat dari situs lain. Karena itu request yang mengubah data (`POST`, `PUT`, `PATCH`, `DELETE`) dari pengguna yang sudah login wajib menyertakan token CSRF (header `X-CSRFToken` yang dibaca dari cookie `csrftoken`), sehingga situs lain yang tidak bisa membaca token itu tidak dapat memalsukan permintaan atas nama korban. Saya tidak memakai `@csrf_exempt` untuk "menyelesaikan" error 403. Di halaman saya, `{% csrf_token %}` menyetel cookie dan fungsi `writeExperience()` mengirim headernya pada setiap tulis. `force_authenticate` tidak cukup untuk membuktikan perlindungan CSRF berjalan karena ia melewati proses login dan autentikasi session, sehingga pemeriksaan CSRF tidak pernah dijalankan. Test seperti itu tetap hijau walaupun CSRF dimatikan. Untuk membuktikannya saya memakai `APIClient(enforce_csrf_checks=True)` dengan `.login()`: `test_session_write_without_csrf_is_rejected` membuktikan `POST`/`DELETE` tanpa token ditolak (403) dan database tidak berubah, sedangkan `test_session_write_with_csrf_succeeds` membuktikan request yang sama dengan token berhasil (201).
