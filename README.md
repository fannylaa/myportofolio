Nama : Stephanie Revalina Tamus

NPM : 2506547153

Kelas : PBP C

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