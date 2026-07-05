# Laporan Akhir Penelitian

**Judul:** Peningkatan Kualitas Sistem Pemasaran Pertanian Berbasis Web Menggunakan Metode Prototyping Berdasarkan Standar Kualitas ISO 25010

**Peneliti:** Agan Chois
**Institusi:** Universitas Putra Bangsa
**Tanggal:** 3 Juli 2026

---

## 1. Ringkasan Eksekutif

Penelitian ini merancang, mengimplementasikan, dan mengevaluasi secara empiris sebuah sistem pemasaran pertanian berbasis web. Latar belakang penelitian adalah banyaknya sistem serupa yang dikembangkan tanpa evaluasi kualitas yang terstandar, sehingga aspek penting seperti *usability* dan keandalan sering terabaikan. Untuk mengatasi kesenjangan ini, penelitian menerapkan **metode pengembangan prototyping** dan mengevaluasi artefak yang dihasilkan secara kuantitatif menggunakan **standar kualitas perangkat lunak ISO 25010**.

Evaluasi dilakukan melalui kuesioner yang diisi oleh **24 responden** yang sesuai dengan target pengguna. Data yang terkumpul dianalisis menggunakan statistik deskriptif dan uji hipotesis (One-Sample T-test).

**Temuan utama:**
- Sistem yang dikembangkan menunjukkan skor kualitas yang tinggi di seluruh delapan karakteristik ISO 25010.
- Skor rata-rata *usability* mencapai **90.92%**, secara statistik signifikan melampaui ambang batas kelayakan umum 70% (p < 0.0001).
- Hasil ini memberikan bukti empiris yang kuat bahwa metode prototyping merupakan pendekatan yang efektif untuk menghasilkan sistem informasi pertanian dengan kualitas yang terukur dan terjamin.

Seluruh artefak penelitian, termasuk kode sumber, data mentah, skrip analisis, dan naskah ilmiah, didokumentasikan secara sistematis dalam repositori ini untuk memastikan reprodusibilitas.

---

## 2. Latar Belakang dan Rumusan Masalah

Digitalisasi sektor pertanian telah mendorong munculnya berbagai platform pemasaran online. Namun, pengembangan platform ini seringkali lebih fokus pada penyelesaian fungsionalitas tanpa disertai evaluasi kualitas non-fungsional yang sistematis. Hal ini menciptakan kesenjangan (gap) di mana banyak sistem yang ada mungkin sulit digunakan, tidak andal, atau tidak aman, yang pada akhirnya menghambat adopsi oleh petani dan konsumen.

Penelitian ini bertujuan untuk mengisi kesenjangan tersebut dengan menjawab pertanyaan penelitian (RQ) berikut:

> **RQ: Bagaimana kualitas sistem pemasaran pertanian berbasis web yang dikembangkan dengan metode prototyping, jika diukur berdasarkan standar ISO 25010?**

Untuk menjawabnya, sebuah hipotesis spesifik terkait *usability*—salah satu faktor adopsi terpenting—juga diuji:

> **H1: Skor rata-rata *usability* sistem akan secara signifikan melampaui ambang batas kelayakan umum sebesar 70%.**

Detail lengkap mengenai tujuan dan kontribusi penelitian dapat dilihat pada dokumen proposal di `01-proposal/proposal-penelitian.md`.

---

## 3. Metodologi dan Pelaksanaan per Tahap

Penelitian dilaksanakan dalam beberapa tahap yang terstruktur, di mana output dari satu tahap menjadi input untuk tahap berikutnya.

### Tahap 1: Perancangan Eksperimen dan Proposal
**Status: Selesai.** Tahap ini berfokus pada perancangan kerangka kerja penelitian. Berdasarkan `ws-06-system-experiment.md`, variabel penelitian didefinisikan (IV: Metode Prototyping, DV: Kualitas Sistem, CV: Responden & Lingkungan). Hasil dari tahap ini adalah dokumen proposal komprehensif yang menjadi panduan seluruh penelitian.
*Artefak: `01-proposal/proposal-penelitian.md`*

### Tahap 2: Tinjauan Pustaka
**Status: Selesai.** Tinjauan literatur dilakukan pada tiga pilar utama: sistem informasi pertanian, metode prototyping, dan standar ISO 25010. Hasilnya disusun dalam matriks literatur dan daftar pustaka BibTeX.
*Artefak: `02-literatur/matriks-literatur.md`, `02-literatur/daftar-pustaka.bib`*

### Tahap 3: Desain Arsitektur Sistem
**Status: Selesai.** Arsitektur sistem dirancang dengan pendekatan 3-Tier (Presentation, Application, Data) untuk mendukung modularitas. Teknologi yang dipilih adalah Vue.js (frontend), Laravel (backend), dan MySQL (database). Desain ini memastikan bahwa artefak yang dibangun dapat diuji sesuai dengan variabel penelitian.
*Artefak: `03-teori/arsitektur-dan-skema.md`*

### Tahap 4: Implementasi dan Pengumpulan Data
**Status: Selesai.** Sistem dikembangkan mengikuti desain arsitektur dan metode prototyping. Setelah prototipe fungsional siap, dilakukan pengumpulan data dengan melibatkan 24 responden. Data dikumpulkan melalui kuesioner dan disimpan dalam format CSV. Proses validasi data (sesuai `ws-11-data-validation.md`) mengonfirmasi kelengkapan data sebesar 96% dan mengidentifikasi satu outlier statistik.
*Artefak: `04-data/hasil-kuesioner-mentah.csv`*

### Tahap 5: Analisis Data
**Status: Selesai.** Sebuah skrip Python dikembangkan untuk mengotomatisasi analisis data. Skrip ini membaca data mentah, menghitung statistik deskriptif (mean, median, std), dan melakukan uji hipotesis (One-Sample T-test) pada skor *usability*.
*Artefak: `05-kode/analysis/analisis-data-kuesioner.py`, `06-output/`*

### Tahap 6: Penulisan Naskah
**Status: Selesai.** Hasil analisis disusun menjadi sebuah naskah ilmiah dengan struktur IMRAD. Konsistensi klaim di seluruh bagian naskah dipastikan menggunakan dokumen outline.
*Artefak: `07-manuskrip/naskah-jurnal.md`, `07-manuskrip/00-outline.md`*

---

## 4. Hasil Penelitian

Analisis data dari 24 responden menghasilkan temuan kuantitatif berikut.

### 4.1. Statistik Deskriptif Kualitas Sistem
Skor rata-rata untuk semua karakteristik kualitas berada di atas 85, menunjukkan persepsi kualitas yang sangat positif dari pengguna. *Reliability* (94.42) dan *Functional Suitability* (92.42) menjadi dua aspek dengan skor tertinggi.

**Tabel 1. Statistik Deskriptif Skor Kualitas Sistem (n=24)**
| Metrik | Mean | Median | Std. Dev. |
|---|---|---|---|
| Functional Suitability | 92.42 | 92.5 | 2.53 |
| Performance Efficiency | 88.42 | 88.5 | 2.53 |
| Compatibility | 90.42 | 90.5 | 2.28 |
| **Usability** | **90.92** | **92.0** | **11.83** |
| Reliability | 94.42 | 94.5 | 1.93 |
| Security | 86.17 | 86.0 | 2.60 |
| Maintainability | 88.42 | 88.5 | 2.53 |
| Portability | 92.25 | 92.5 | 2.27 |

### 4.2. Hasil Uji Hipotesis
Uji T-test satu sampel dilakukan untuk membandingkan skor rata-rata *usability* (90.92) dengan nilai acuan 70%.
- **T-statistic:** 8.685
- **P-value (one-tailed):** < 0.0001

Hasil p-value yang sangat kecil (< 0.05) menunjukkan bahwa hipotesis nol (H0: μ ≤ 70) ditolak. Dengan kata lain, **terdapat bukti statistik yang sangat kuat untuk menyatakan bahwa skor *usability* sistem secara signifikan lebih tinggi dari 70%.**

---

## 5. Kendala dan Catatan Lingkungan

- **Kendala Pengumpulan Data:** Satu dari 25 responden yang direncanakan tidak menyelesaikan kuesioner, sehingga analisis dilakukan dengan n=24. Satu outlier statistik (skor usability 35) terdeteksi. Setelah investigasi, diputuskan untuk mempertahankan data tersebut karena tidak ditemukan kesalahan teknis, dan anomali ini dianggap sebagai cerminan pengalaman pengguna yang valid.
- **Lingkungan Pengembangan:** Spesifikasi lingkungan telah didokumentasikan dalam `ws-09-implementation.md` untuk memastikan reprodusibilitas.
  - **Hardware:** Intel Core i5-10400F, 16 GB RAM, CPU-only.
  - **Software:** Windows 11, PHP 8.1, Node.js 18.x, Laravel 9.x, Vue.js 3.x, MySQL 8.0.

---

## 6. Kesimpulan dan Saran

Penelitian ini berhasil menunjukkan bahwa sistem pemasaran pertanian yang dikembangkan dengan metode prototyping memiliki kualitas yang sangat baik menurut standar ISO 25010. Jawaban untuk RQ adalah bahwa sistem mencapai skor rata-rata tinggi di semua aspek kualitas. Hipotesis H1 juga terbukti, di mana skor *usability* secara signifikan melampaui ambang batas kelayakan.

Kontribusi utama penelitian adalah memberikan validasi empiris bahwa metode prototyping, yang berpusat pada pengguna, merupakan pendekatan yang efektif dan cocok untuk menghasilkan sistem informasi berkualitas tinggi dalam domain agrikultur.

Untuk penelitian selanjutnya, disarankan untuk melakukan evaluasi dengan sampel yang lebih besar dan lebih beragam untuk meningkatkan generalisasi hasil.

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|---|---|---|
| `00-admin/` | Berkas administratif, catatan bimbingan, dan log penelitian. | Selesai |
| `01-proposal/` | Proposal penelitian final. | Selesai |
| `02-literatur/` | Matriks tinjauan pustaka dan daftar pustaka BibTeX. | Selesai |
| `03-teori/` | Dokumen arsitektur sistem dan skema database. | Selesai |
| `04-data/` | Data mentah hasil kuesioner dari 24 responden. | Selesai |
| `05-kode/` | Kode sumber aplikasi (backend/frontend) dan skrip analisis. | Selesai |
| `06-output/` | Hasil olahan data (tabel statistik dan teks hasil uji hipotesis). | Selesai |
| `07-manuskrip/` | Draf naskah ilmiah lengkap dan outline. | Selesai |
| `08-laporan/` | Laporan penelitian komprehensif (dokumen ini). | Selesai |
| `09-docs/` | Dokumen perencanaan dan panduan kerja (tidak ada di struktur ini). | - |
| `worksheets/` | Lembar kerja yang memandu setiap langkah penelitian. | Selesai |