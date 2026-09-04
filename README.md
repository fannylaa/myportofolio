Nama : Stephanie Revalina Tamus

NPM : 2506547153

Kelas : PBP C

### Tugas 1

### 1. Penggunaan Elemen Semantik HTML5
Ya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<section>`, `<article>`, dan `<footer>` dalam merancang struktur website portofolio ini.

Elemen semantik membantu pembuatan *static web* dalam beberapa hal:
- Struktur Kode Lebih Terorganisir: Memudahkan pembacaan kode (readability) baik untuk pengembangan pribadi maupun kolaborasi tim, karena fungsi tiap area web terdefinisi dengan jelas dibanding hanya menggunakan `<div>` generik.
- Aksesibilitas (Accessibility/a11y): Membantu *screen reader* membaca navigasi dan konten website secara logis untuk pengguna berkebutuhan khusus.
- Optimasi SEO: Mesin pencari dapat memahami hierarki informasi dengan lebih baik (misalnya membedakan bagian navigasi utama, konten artikel, dan informasi *footer*).

### 2. Responsivitas CSS & Evaluasi Tampilan Mobile
Saat mengatur CSS agar responsif, tantangan tata letak utama yang dihadapi adalah:
- Penyesuaian Grid/Flexbox Multi-Kolom: Mengubah tata letak samping-ke-samping (*side-by-side*) pada layar *desktop* menjadi tumpukan vertikal (*vertical stack*) pada layar *mobile* agar tidak terjadi *overflow* horizontal.
- Skala Tipografi dan *Spacing*: Menjaga rasio *font-size*, *margin*, dan *padding* agar tetap proporsional dan tidak memakan terlalu banyak ruang pada layar kecil.

**Cara Evaluasi & Prioritasi Elemen:**
- Prioritas Konten (Content Hierarchy):Elemen penting seperti nama, perkenalan singkat, dan *call-to-action* (CTA) diprioritaskan muncul di bagian atas pada tampilan *mobile*. Elemen dekoratif atau pendukung digeser ke bawah.
- Prinsip Mobile-First / Breakpoints: Menggunakan *media queries* `@media (max-width: ...)` untuk memantau titik di mana tata letak mulai terlihat sesak. Pada titik tersebut, elemen `flex-direction` diubah menjadi `column` dan ukuran kontainer disesuaikan menggunakan unit relatif (`%`, `vw`, atau `rem`).

### 3. Batasan Static Web & Rencana Fungsionalitas Dinamis
Saat menyajikan informasi pada portofolio *static web* murni, terdapat beberapa batasan utama:
- Data bersifat Statis (*Hardcoded*): Setiap perubahan daftar proyek, keahlian, atau pengalaman memerlukan suntingan langsung pada file `.html`.
- Tidak Ada Interaksi Data Dua Arah: Pengunjung tidak dapat mengirim pesan langsung lewat *Contact Form*, meninggalkan komentar, atau berinteraksi secara real-time.

**Fungsionalitas Dinamis yang Ingin Ditambahkan pada Iterasi Selanjutnya:**
- Manajemen Konten via Database (Django Models): Menggunakan *database* untuk menyimpan data proyek, sertifikat, dan *experience*, sehingga konten dapat ditambah atau diubah secara dinamis melalui Django Admin tanpa menyentuh kode HTML.
- Formulir Kontak Dinamis (*Contact Form*): Menambahkan logika *backend* untuk menangani *submit* formulir kontak, menyimpan pesan pengguna ke *database*, atau mengirimkan notifikasi email secara otomatis.
- Sistem Autentikasi: Menyiapkan akses khusus pengguna/admin untuk mengelola portofolio secara dinamis langsung dari antarmuka web.