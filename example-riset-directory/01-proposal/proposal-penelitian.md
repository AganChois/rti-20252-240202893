# Proposal Penelitian

---

## Judul Penelitian

Peningkatan Kualitas Sistem Pemasaran Pertanian Berbasis Web Menggunakan Metode Prototyping Berdasarkan Standar Kualitas ISO 25010.

## 1. Latar Belakang

Digitalisasi dalam sektor pertanian menawarkan potensi besar untuk meningkatkan efisiensi dan jangkauan pasar bagi para petani. Sejumlah sistem pemasaran berbasis web telah dikembangkan untuk menjembatani produsen dengan konsumen. Namun, banyak dari sistem yang ada dibangun tanpa evaluasi kualitas yang sistematis dan terstandar. Akibatnya, aspek-aspek krusial seperti *usability*, fungsionalitas, dan keandalan seringkali tidak terjamin, yang dapat menghambat adopsi oleh pengguna.

Terdapat kesenjangan (gap) dalam literatur mengenai penerapan standar kualitas perangkat lunak yang formal, seperti ISO 25010, dalam konteks pengembangan sistem informasi agrikultur. Penelitian ini bertujuan untuk mengisi kesenjangan tersebut dengan menerapkan metode pengembangan yang berorientasi pada pengguna (prototyping) dan mengukurnya dengan metrik kualitas yang jelas.

## 2. Rumusan Masalah dan Pertanyaan Penelitian

Berdasarkan latar belakang di atas, pertanyaan penelitian utama (Research Question/RQ) yang ingin dijawab adalah:

> **RQ: Bagaimana kualitas sistem pemasaran pertanian berbasis web yang dikembangkan dengan metode prototyping, jika diukur berdasarkan standar ISO 25010?**

Untuk menjawab pertanyaan tersebut secara kuantitatif, penelitian ini akan menguji hipotesis berikut, khususnya pada aspek *usability* yang merupakan salah satu faktor kunci penerimaan pengguna:

> **H1: Skor rata-rata *usability* sistem yang dikembangkan akan secara signifikan melampaui ambang batas kelayakan umum sebesar 70%.**

## 3. Tujuan dan Kontribusi Penelitian

### Tujuan

1.  Membangun sebuah prototipe fungsional sistem pemasaran pertanian berbasis web.
2.  Mengevaluasi kualitas prototipe tersebut secara empiris menggunakan delapan karakteristik kualitas dari standar ISO 25010.
3.  Menguji secara statistik apakah tingkat *usability* sistem memenuhi standar kelayakan yang telah ditetapkan.

### Kontribusi

Penelitian ini diharapkan dapat memberikan kontribusi berikut:
1.  **Kontribusi Praktis:** Menghasilkan sebuah model sistem pemasaran pertanian yang telah teruji kualitasnya dan dapat menjadi acuan bagi pengembangan serupa.
2.  **Kontribusi Akademis:** Memberikan validasi empiris mengenai efektivitas metode prototyping untuk menghasilkan sistem dengan kualitas terukur (berdasarkan ISO 25010) dalam domain spesifik sistem informasi agrikultur.

## 4. Tinjauan Pustaka

Penelitian ini didasarkan pada tiga pilar literatur utama. Pertama, studi-studi sebelumnya mengenai pengembangan sistem informasi pertanian (misalnya, Tandirerung et al., 2020) akan dianalisis untuk memahami fitur umum dan tantangan yang ada. Kedua, literatur mengenai metode pengembangan perangkat lunak, khususnya *prototyping*, akan ditinjau untuk membangun kerangka kerja proses pengembangan. Ketiga, standar evaluasi perangkat lunak ISO 25010 akan dibedah untuk mendefinisikan metrik-metrik pengukuran kualitas yang akan digunakan.

Posisi penelitian ini adalah sebagai studi yang pertama kali mengintegrasikan ketiga pilar tersebut untuk mengevaluasi kualitas sistem pemasaran pertanian secara formal dan sistematis.

## 5. Metodologi Penelitian

### 5.1. Desain Sistem dan Variabel Penelitian

Penelitian ini menggunakan desain eksperimental di mana sebuah artefak (sistem) dibangun untuk menguji hipotesis. Variabel penelitian diidentifikasi sebagai berikut:

| Variabel | Tipe | Deskripsi | Cara Manipulasi/Pengukuran |
|---|---|---|---|
| **Metode Prototyping** | Independent (IV) | Proses pengembangan iteratif yang melibatkan pengguna. | Diterapkan sebagai metode pengembangan sistem dari awal hingga akhir. |
| **Kualitas Sistem** | Dependent (DV) | Tingkat pemenuhan sistem terhadap standar kualitas ISO 25010. | Diukur melalui kuesioner yang diisi oleh responden setelah menggunakan sistem. |
| **Responden & Lingkungan** | Control (CV) | Karakteristik pengguna dan perangkat yang digunakan. | Dibatasi pada 24 responden dengan profil serupa dan menggunakan browser standar. |

### 5.2. Prosedur Eksperimen

1.  **Fase 1 - Pengembangan Prototipe:** Sistem akan dikembangkan menggunakan framework Laravel dan Vue.js mengikuti siklus metode prototyping.
2.  **Fase 2 - Rekrutmen Responden:** Sebanyak 24 responden yang sesuai dengan target pengguna akan direkrut untuk berpartisipasi dalam pengujian.
3.  **Fase 3 - Pelaksanaan Pengujian:** Setiap responden akan diberikan serangkaian tugas untuk diselesaikan menggunakan sistem.
4.  **Fase 4 - Pengumpulan Data:** Setelah sesi pengujian, responden akan mengisi kuesioner evaluasi kualitas berbasis ISO 25010.

### 5.3. Instrumen dan Metrik Pengukuran

Instrumen utama adalah kuesioner yang dirancang berdasarkan 8 karakteristik kualitas ISO 25010 (*Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability*). Jawaban akan menggunakan skala Likert yang kemudian dikonversi menjadi skor persentase (0-100%).

### 5.4. Rencana Analisis Data

Data skor yang terkumpul akan dianalisis menggunakan statistik deskriptif (mean, median, standar deviasi) untuk setiap karakteristik kualitas. Untuk menguji hipotesis H1, akan dilakukan uji statistik **One-Sample T-test** untuk membandingkan skor rata-rata *usability* yang diperoleh dengan nilai acuan 70%. Tingkat signifikansi (α) ditetapkan sebesar 0.05.