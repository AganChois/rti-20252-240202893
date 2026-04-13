# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Agan Chois
Tanggal          : 13 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Bagaimana metode tersebut diuji dan pada dataset apa tingkat akurasi 95% itu diperoleh?
   - Data yang dibutuhkan untuk verifikasi: Dataset uji (train/test split), ukuran sampel, metode evaluasi (confusion matrix, cross-validation), serta konteks penggunaan metode tersebut.

2. Posisi paradigma:
   - Pendekatan: Positivis 
   - Alasan: Karena penelitian berfokus pada pengukuran objektif (akurasi), menggunakan data kuantitatif dan metode statistik untuk membuktikan kebenaran.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Bahwa angka 95% berlaku umum untuk semua kondisi dan dataset.
   - Sumber bias potensial: Bias dataset (tidak representatif), overfitting, atau pemilihan metrik yang tidak tepat.
   - Langkah mitigasi: Menggunakan dataset yang beragam, melakukan validasi silang (cross-validation), dan membandingkan dengan metode lain.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Hasil eksperimen, nilai akurasi, serta data mentah penelitian.
   - Batasan yang diakui sejak awal: Keterbatasan dataset, kemungkinan bias model, dan bahwa hasil mungkin tidak berlaku di semua situasi.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**

> Judul: Deep Learning-Based Intrusion Detection System Improves Network Security Performance
> Penulis (Tahun): Ahmad et al. (2022)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan dataset trafik jaringan dari dataset publik (misal: KDD Cup / CICIDS) | Dataset tidak merepresentasikan kondisi real-time (data lama / simulasi) |
| Data → Processing |Data dibersihkan, dinormalisasi, dan dibagi train-test | Data leakage atau pembagian data tidak acak|
| Processing → Analysis | Melatih model deep learning dan menghitung akurasi|Overfitting karena model terlalu kompleks |
| Analysis → Inference |Menyimpulkan model lebih baik karena akurasi tinggi |Hanya fokus pada akurasi, abaikan metrik lain (precision, recall) |
| Inference → Knowledge | Mengklaim metode meningkatkan performa keamanan jaringan| Generalisasi berlebihan ke semua sistem jaringan|

**Distorsi paling besar di tahap:** Processing → Analysis

**Dua distorsi spesifik yang teridentifikasi:**
1. Overfitting model sehingga performa tinggi hanya pada dataset uji, bukan kondisi nyata
2. Penggunaan dataset yang tidak representatif terhadap kondisi jaringan real-world

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah |Peneliti harus melaporkan kedua hasil (dengan dan tanpa outlier) serta menjelaskan alasan penghapusan outlier secara metodologis, bukan untuk “memperindah” hasil. |
| Transparansi | Proses identifikasi outlier harus dijelaskan (misalnya menggunakan metode statistik seperti IQR atau Z-score), termasuk dampaknya terhadap hasil analisis.|
| Peer review | Reviewer kemungkinan akan mempertanyakan keputusan menghapus outlier; jika tidak dijelaskan dengan baik, penelitian bisa dianggap bias atau manipulatif.|

**Keputusan akhir dan justifikasi:**
> Data outlier tidak boleh dihapus sembarangan hanya untuk mencapai hasil signifikan. Peneliti sebaiknya menyajikan analisis dengan dan tanpa outlier, disertai justifikasi ilmiah yang jelas. Hal ini menjaga integritas penelitian, menghindari bias, dan memastikan hasil dapat dipercaya serta direplikasi.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Pengembangan Sistem IoT untuk Monitoring Kualitas Air Limbah

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
<<<<<<< HEAD
| Kesesuaian dengan topik (1–5) | 4 | 2 | 5 |
| Jenis data yang dikumpulkan | Data sensor (pH, suhu, COD, BOD) dalam bentuk numerik| Persepsi pengguna terhadap sistem (wawancara/operator)| Data performa sistem + hasil implementasi prototipe|
| Limitasi paradigma | Kurang memahami konteks sosial penggunaan sistem| Tidak fokus pada pengukuran teknis sistem| Fokus pada solusi, kadang kurang generalisasi teoritis|
=======
| Kesesuaian dengan topik (1–5) | *Contoh: 4 — topik kuantitatif, cocok uji hipotesis* | *Contoh: 2 — topik tidak studi makna/konteks* | *Contoh: 5 — membangun artefak untuk uji klaim* |
| Jenis data yang dikumpulkan | *Metrik numerik, log eksperimen* | *Wawancara, observasi kualitatif* | *Hasil uji artefak, komparasi kinerja* |
| Limitasi paradigma | | | |
>>>>>>> c96f0d9a29d432f612b2ee6cca9bc239c291aacf

**Paradigma yang dipilih:** Design Science
**Alasan:** Karena penelitian berfokus pada pembuatan dan evaluasi artefak (sistem IoT), bukan hanya analisis data atau pemahaman sosial. Tujuannya adalah menghasilkan solusi nyata yang dapat diuji performanya.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelumnya saya cenderung langsung percaya pada klaim “95% akurat” tanpa mempertanyakan proses di baliknya.
> Sekarang saya akan bertanya: dataset apa yang digunakan, bagaimana metode evaluasinya, apakah ada bias atau overfitting, dan apakah hasil tersebut bisa digeneralisasi ke kondisi nyata.~
