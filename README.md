# Petra Cookies

**Aplikasi Web UMKM untuk memperkenalkan Petra Cookies di kalangan masyarakat**

Petra Cookies adalah aplikasi web e-commerce berbasis **Python Flask** yang dikembangkan untuk memenuhi tugas mata kuliah **Pemrograman Web**. Aplikasi ini dikhususkan untuk UMKM Petra Cookies yang bergerak di bidang kuliner dan penjualan berbagai macam aneka kue sesuai request pelanggan. Aplikasi ini memungkinkan pelanggan untuk melihat produk, melakukan pemesanan melalui WhatsApp, dan menyediakan dashboard admin yang lengkap untuk mengelola produk, kategori, galeri, blog, dan FAQ. 
---

### 🌐 Deployment Link

Aplikasi Petra Cookies telah di-deploy dan dapat diakses secara online melalui tautan berikut:

### 🔗 Link Deployment

**[🔗 Klik di sini untuk mengakses Petra Cookies](https://lanjarmulia.vercel.app/)**

---

## 👥 Anggota Kelompok 

| No | Nama | NIM  |
|----|------|-------------|-------|
| 1 | **Usvatun Khasanah** | l200240162 |
| 2 | **Latifah Puji Lestari** | l200240170 |
| 3 | **Afifa Najwa Azzahra** | l200240174 |
| 4 | **Aqtus Denalia Andriani** | l200240181 |
| 5 | **Avisa Putri Rosyida** | l200240190 |
| 6 | **Woro Nurhaliza Cahyani** | l200240185 |

---

Opsi Backend (BE) yang kami pilih adalah

**Opsi 1 — Python (Flask)**

| Teknologi | Peran |
|-----------|-------|
| **Python (Flask)** | Logika server dan routing |
| **MySQL** | Basis data |

---

# ✅ Fitur Sesuai Ketentuan Tugas

### Fitur Wajib (Umum)

| No | Fitur | Status | Keterangan |
|----|-------|--------|-----------|
| 1 | **Halaman Beranda (Home)** | ✅ | Deskripsi singkat UMKM, produk unggulan, testimoni, alamat lengkap di footer |
| 2 | **Basis Data MySQL** | ✅ | 7 tabel berelasi dengan foreign key dan query JOIN, tanpa ORM |
| 3 | **Halaman Login Admin** | ✅ | Route /admin/login dengan hash password bcrypt, manajemen session Flask |
| 4 | **Panel Admin** | ✅ | Dashboard,  CRUD produk, kategori, galeri, blog, FAQ, manajemen admin, upload gambar |
| 5 | **Kontak via WhatsApp** | ✅ | Tombol WhatsApp di navbar dan footer `https://wa.me/+6281313451583` |

### Fitur Spesifik UMKM (Minimal 3 dari 7)
| No | Fitur | Status | Keterangan |
|----|-------|--------|-----------|
| 1 | **Katalog Produk** | ✅ | Daftar produk lengkap dengan foto, deskripsi, harga, dan kategori |
| 2 | **Galeri & Testimoni** | ✅ | Halaman /galeri menampilkan foto produk dan testimoni yang dapat dilihat oleh user |
| 3 | **Blog / Artikel** | ✅ | Halaman /blog dengan sistem artikel lengkap |
| 4 | **Pencarian & Filter Produk** | ✅ | Filter berdasarkan kategori dan pencarian kata kunci di halaman produk |
| 5 | **WhatsApp Integration** | ✅ | Tombol chat WhatsApp di footer dan header |

---

## ✨ Fitur Utama

### 💻 Sisi Pelanggan (Public)
- **Landing Page** — Halaman utama (`/`) dengan hero section "Kue Homemade untuk Setiap Momen Istimewa", produk unggulan, dan testimoni pelanggan.
- **Katalog Produk** — Halaman `/produk` menampilkan semua produk kue dengan pencarian real-time (`?q=`) dan filter berdasarkan kategori (`?category=`).
- **Detail Produk** — Halaman `/produk/<slug>` dengan informasi lengkap produk, harga, deskripsi, dan tombol "Pesan via WhatsApp".
- **Galeri & Testimoni** — Halaman `/galeri` menampilkan foto-foto produk dan testimoni pelanggan dengan rating bintang.
- **Blog/Artikel** — Halaman `/blog` dengan daftar artikel dan `/blog/<slug>` untuk detail artikel.
- **FAQ** — Halaman `/faq` dengan pertanyaan dan jawaban yang sering ditanyakan.
- **Tentang Kami** — Halaman `/tentang` dengan informasi profil UMKM Petra Cookies.
- **WhatsApp Direct Order** — Tombol WhatsApp di setiap produk dan navbar untuk pemesanan langsung ke `+6281313451583`.

### 👨💼 Sisi Admin
- **Dashboard** — Menampilkan statistik: total produk aktif, total artikel published, total foto galeri, total testimoni.
- **Manajemen Produk** — CRUD produk lengkap dengan upload gambar, pengaturan kategori, harga, dan status aktif/nonaktif.
- **Manajemen Kategori** — CRUD kategori produk dengan modal AJAX untuk pengalaman yang smooth.
- **Manajemen Galeri** — CRUD untuk foto produk dan testimoni pelanggan dengan rating system.
- **Manajemen Blog** — CRUD artikel dengan editor konten, status publish/unpublish, dan upload gambar.
- **Manajemen FAQ** — CRUD pertanyaan dan jawaban dengan pengaturan urutan tampil.
- **Manajemen Admin** — CRUD user admin dengan hash password bcrypt dan validasi email/username unik.
- **Autentikasi** — Login admin dengan session management dan password hashing.
- **Sidebar Responsif** — Navigasi admin dengan toggle untuk perangkat mobile.

### 🎨 UI/UX
- **Bootstrap 5** — Framework CSS responsif dengan grid system dan komponen modern.
- **Google Fonts: Poppins** — Tipografi yang clean dan mudah dibaca.
- **Responsive Design** — Layout yang optimal di desktop, tablet, dan mobile.
- **Flash Messages** — Notifikasi sukses/error dengan styling Bootstrap alerts.
- **Image Upload** — Sistem upload gambar dengan validasi ekstensi file (jpg, jpeg, png).
- **Modal AJAX** — Form kategori dengan modal untuk pengalaman pengguna yang lebih baik.
- **WhatsApp Integration** — Button styling khusus untuk call-to-action WhatsApp.
- **Admin Theme** — Interface admin yang terpisah dengan sidebar navigation dan topbar.
- **SEO Friendly** — Meta tags, Open Graph, dan struktur URL yang SEO-friendly.
- **Back to Top** — Button untuk kembali ke atas halaman.
- **Announcement Bar** — Area untuk pengumuman atau promo di atas footer.

### 🚀 Fitur Teknis Tambahan
- **Secure File Upload** — Menggunakan `secure_filename` dari Werkzeug.
- **Database Connection Pooling** — Koneksi database yang efisien dengan PyMySQL.
- **URL Slugification** — Otomatis generate slug untuk produk dan artikel.
- **Environment Configuration** — Konfigurasi database dan secret key melalui file `.env`.
- **Error Handling** — 404 handling untuk produk dan artikel yang tidak ditemukan.
- **SQL Injection Prevention** — Menggunakan parameterized queries untuk keamanan.

### 📱 Mobile-First Features
- **Responsive Navbar** — Collapse menu untuk mobile dengan Bootstrap.
- **Touch-Friendly Buttons** — Ukuran button yang optimal untuk touchscreen.
- **Mobile-Optimized Images** — Gambar yang responsive di semua ukuran layar.
- **WhatsApp Mobile Integration** — Link WhatsApp yang langsung membuka aplikasi di mobile.

---

## 🛠 Tech Stack
- **Frontend**  HTML, CSS, JavaScript  Struktur halaman, tampilan, dan interaktivitas 
- **Framework CSS**  Bootstrap 5 (CDN)  Framework CSS responsif dengan komponen siap pakai 
- **Typography**  Google Fonts (Poppins)  Tipografi modern dan clean 
- **Backend**  Python 3 + Flask  Framework web untuk logika server dan routing 
- **Database**  MySQL  Basis data relasional untuk menyimpan data aplikasi 
- **Koneksi DB**  PyMySQL (tanpa ORM)  Driver MySQL untuk Python dengan query SQL langsung 
- **Autentikasi**  bcrypt  Library untuk hashing dan verifikasi password admin 
- **Session**  Flask-Session  Manajemen sesi login admin 
- **File Upload**  Werkzeug (secure_filename)  Handling upload file gambar dengan aman 
- **Environment**  python-dotenv  Manajemen konfigurasi environment variables 
- **Web Server**  Flask Development Server  Server untuk development dan testing 

## 📁 Struktur Proyek

membangun-web-umkm-atau-pcm-mbg-mohon-bantuannya-gusti/
├── .env.example                 # Template konfigurasi environment
├── .env                         # Konfigurasi environment (tidak di-commit)
├── .gitignore                   # File yang diabaikan Git
├── README.md                    # Dokumentasi proyek utama
├── README new.md                # Dokumentasi tambahan
├── README 2.md                  # Dokumentasi alternatif
├── laporan.md                   # Laporan pengembangan
├── requirements.txt             # Dependencies Python
├── run.py                       # Entry point aplikasi Flask
├── petra_cookies-7.sql          # Backup database
│
├── .github/                     # GitHub configuration
│   └── .keep                    # Keep folder in Git
│
├── app/                         # Direktori utama aplikasi
│   ├── __init__.py              # Factory function create_app()
│   │
│   ├── models/                  # Layer model/database
│   │   ├── db.py                # Koneksi database PyMySQL dengan DictCursor
│   │   └── helpers.py           # Helper functions dan decorators
│   │
│   ├── routes/                  # Route handlers (controllers)
│   │   ├── __init__.py          # Blueprint registration
│   │   ├── public.py            # Route publik (beranda, produk, galeri, blog, dll.)
│   │   ├── auth.py              # Route autentikasi (login, logout)
│   │   └── admin.py             # Route admin (dashboard, CRUD, manajemen)
│   │
│   ├── templates/               # Template Jinja2
│   │   ├── base.html            # Template dasar (navbar, footer, flash messages)
│   │   ├── index.html           # Halaman beranda
│   │   ├── produk.html          # Katalog produk
│   │   ├── produk_detail.html   # Detail produk
│   │   ├── galeri.html          # Galeri foto dan testimoni
│   │   ├── blog.html            # Daftar artikel blog
│   │   ├── blog_detail.html     # Detail artikel
│   │   ├── blog-detail.html     # Detail artikel (alternatif)
│   │   ├── tentang.html         # Halaman tentang kami
│   │   ├── faq.html             # Halaman FAQ
│   │   │
│   │   └── admin/               # Template khusus admin
│   │       ├── login.html            # Halaman login admin
│   │       ├── dashboard.html        # Dashboard admin
│   │       ├── produk_list.html      # Daftar produk admin
│   │       ├── produk_form.html      # Form tambah/edit produk
│   │       ├── kategori_list.html    # Manajemen kategori
│   │       ├── kategori_form.html    # Form kategori
│   │       ├── galeri_list.html      # Manajemen galeri
│   │       ├── galeri_form.html      # Form galeri
│   │       ├── blog_list.html        # Manajemen blog
│   │       ├── blog_form.html        # Form blog
│   │       ├── faq_list.html         # Manajemen FAQ
│   │       ├── faq_form.html         # Form FAQ
│   │       ├── user_list.html        # Manajemen admin
│   │       └── user_form.html        # Form admin
│   │
│   └── static/                  # File statis
│       ├── css/
│       │   ├── style.css        # CSS utama untuk public pages
│       │   └── admin.css        # CSS khusus untuk admin panel
│       │
│       ├── js/
│       │   ├── public-base.js   # JavaScript untuk halaman publik
│       │   ├── public-index.js  # JavaScript khusus halaman beranda
│       │   └── admin-form.js    # JavaScript untuk form admin
│       │
│       └── images/
│           ├── logo.png              # Logo Petra Cookies
│           ├── halal.png             # Sertifikat halal
│           └── [uploaded-files]      # File gambar yang diupload admin
│
└── database/                    # Skema database
    ├── schema.sql               # DDL (CREATE TABLE) - 7 tabel
    └── seed.sql                 # DML (INSERT data awal)
```
---

## 🚀 Cara Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di lingkungan lokal:

### 1. Clone Repositori

```bash
git clone <url-repo>
cd lanjar-mulia
```

### 2. Buat Virtual Environment (Direkomendasikan)

```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
# atau
venv\Scripts\activate          # Windows
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment

Salin file `.env.example` menjadi `.env`:

```bash
cp .env.example .env
```

Kemudian edit file `.env` dan sesuaikan dengan konfigurasi MySQL Anda:

```env
FLASK_ENV=development
SECRET_KEY=replace-with-your-secret-key

DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=petra_cookies
```

> **Penting:** Jangan commit file `.env` ke repositori. File ini sudah ada di `.gitignore`.

### 5. Setup Database MySQL

Buat database baru di MySQL:

```bash
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS `petra_cookies` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

Import skema tabel (DDL):

```bash
mysql -u root -p petra_cookies< database/schema.sql
```

Import data awal (DML / seed):

```bash
mysql -u root -p lanjar_mulia_db < database/seed.sql
```

### 6. Jalankan Aplikasi

```bash
python run.py
```

Aplikasi akan berjalan di **http://localhost:5000** atau **http://0.0.0.0:5000**.

### Akun Default untuk Testing

| Role | Password |
|------|-------|
| admin| admin123(telah di-hash bcrypt) |

---

## 👥 Role dan Hak Akses
### Customer (Pengunjung)
### 🌐 **Hak Akses Public**
- ✅ **Melihat Halaman Beranda** — Akses ke halaman utama dengan hero section dan produk unggulan
- ✅ **Browse Katalog Produk** — Melihat semua produk kue dengan foto, harga, dan deskripsi
- ✅ **Pencarian & Filter** — Mencari produk berdasarkan nama dan filter kategori
- ✅ **Detail Produk** — Melihat informasi lengkap setiap produk
- ✅ **Galeri & Testimoni** — Melihat foto-foto produk dan testimoni pelanggan
- ✅ **Baca Blog/Artikel** — Akses ke semua artikel yang dipublish
- ✅ **FAQ** — Melihat pertanyaan dan jawaban yang sering ditanyakan
- ✅ **Tentang Kami** — Informasi profil UMKM Petra Cookies
- ✅ **Kontak WhatsApp** — Langsung chat untuk inquiry dan pemesanan

### Admin (Pengelola UMKM)
### 🔐 **Hak Akses Lengkap**
- ✅ **Semua Hak Akses Customer** — Dapat mengakses semua halaman public
- ✅ **Login/Logout** — Autentikasi dengan bcrypt password hashing
- ✅ **Dashboard Admin** — Melihat statistik: total produk, artikel, galeri, testimoni

### 📊 **Manajemen Konten**
- ✅ **CRUD Produk** — Tambah, edit, hapus produk dengan upload gambar
- ✅ **CRUD Kategori** — Manajemen kategori produk dengan modal AJAX
- ✅ **CRUD Galeri** — Upload foto produk dan manajemen testimoni pelanggan
- ✅ **CRUD Blog** — Buat, edit, publish/unpublish artikel
- ✅ **CRUD FAQ** — Manajemen pertanyaan dan jawaban dengan urutan tampil
- ✅ **Upload File** — Upload gambar untuk produk, galeri, dan artikel

### 👨‍💼 **Manajemen Admin**
- ✅ **CRUD Admin** — Tambah, edit, hapus user admin (kecuali diri sendiri)
- ✅ **Ganti Password** — Update password admin dengan hashing bcrypt
- ✅ **Manajemen Session** — Control akses berdasarkan session login

### 🔒 **Proteksi Akses**
- 🛡️ **Decorator @login_required** — Semua route admin dilindungi
- 🛡️ **Session Validation** — Cek `session['admin_id']` di setiap request
- 🛡️ **Auto Redirect** — Redirect ke login jika belum authenticated

---

## 🔒 Fitur Keamanan
## 🔐 **Autentikasi & Otorisasi**
### **Password Security**
- ✅ **Bcrypt Hashing** — Password di-hash dengan `bcrypt.hashpw()` dan salt
- ✅ **Password Verification** — Login menggunakan `bcrypt.checkpw()`
- ✅ **No Plain Text** — Password tidak pernah disimpan dalam bentuk plain text

### **Session Management**
- ✅ **Flask Session** — Menggunakan Flask's secure session dengan secret key
- ✅ **Session Data** — Menyimpan `admin_id` dan `admin_name` untuk identifikasi
- ✅ **Auto Logout** — Session clear saat logout
- ✅ **Login Required Decorator** — Proteksi otomatis untuk semua route admin

## 🛡️ **Database Security**
### **SQL Injection Prevention**
- ✅ **Parameterized Queries** — Semua query menggunakan parameter binding (`%s`)
- ✅ **Input Sanitization** — Form input di-strip dan divalidasi
- ✅ **PyMySQL Driver** — Driver yang secure untuk koneksi MySQL

### **Database Connection**
- ✅ **Environment Variables** — Kredensial database disimpan di `.env`
- ✅ **Connection Pooling** — Koneksi database yang efisien dan aman
- ✅ **Proper Connection Closing** — Koneksi selalu ditutup di `finally` block

## 📁 **File Upload Security**
### **Secure File Handling**
- ✅ **secure_filename()** — Menggunakan Werkzeug untuk sanitize filename
- ✅ **File Extension Validation** — Hanya menerima `.jpg`, `.jpeg`, `.png`
- ✅ **Upload Directory** — File disimpan di direktori yang aman (`/static/images/`)
- ✅ **File Size Control** — Kontrol ukuran file upload

## 🔒 **Access Control**
### **Route Protection**
- ✅ **Blueprint Separation** — Pemisahan route public dan admin
- ✅ **URL Prefix** — Admin routes menggunakan `/admin/*` prefix
- ✅ **Automatic Redirect** — Auto redirect ke login jika belum authenticated
- ✅ **Flash Messages** — Notifikasi error untuk akses yang tidak sah

### **Data Validation**
- ✅ **Form Validation** — Validasi input di server-side
- ✅ **Required Fields** — Validasi field wajib diisi
- ✅ **Duplicate Prevention** — Cek unique constraint untuk username/email admin
- ✅ **XSS Protection** — Jinja2 auto-escape untuk mencegah XSS

## 🌐 **Environment Security**
### **Configuration Management**
- ✅ **Environment Variables** — Konfigurasi sensitif di file `.env`
- ✅ **.gitignore** — File `.env` tidak di-commit ke repository
- ✅ **Secret Key** — Flask secret key untuk session encryption
- ✅ **Development vs Production** — Konfigurasi terpisah untuk berbagai environment

## ⚡ **Error Handling**
### **Graceful Error Management**
- ✅ **Try-Catch Blocks** — Database operations dalam try-catch
- ✅ **Connection Cleanup** — Database connection selalu ditutup
- ✅ **404 Handling** — Proper handling untuk resource yang tidak ditemukan
- ✅ **Flash Messages** — User-friendly error messages

## 🔐 **Additional Security Measures**
### **Anti-Pattern Protection**
- ✅ **No Hardcoded Credentials** — Semua kredensial di environment variables
- ✅ **HTTPS Ready** — Struktur siap untuk deployment dengan HTTPS
- ✅ **CSRF Protection Ready** — Struktur mendukung CSRF token implementation
- ✅ **Input Sanitization** — Form input di-sanitize sebelum disimpan
---



<p align="center">
  <strong>Petra Cookies</strong><br>
  <em>Manis, segar, dan langsung dari petani ke meja makanmu</em><br><br>
  <strong>MBG Team</strong><br>
  Usvatun · Latifah · Dena · Avisa · Haliza · Afifa
</p>