# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question:
Bagaimana peningkatan kualitas sistem pemasaran pertanian berbasis web menggunakan metode prototyping berdasarkan ISO 9126?

| Variabel            | Tipe | Konsep                     | Metrik                                   | Skala     | Satuan | Cara Mengukur                          | Justifikasi |
|---------------------|------|-----------------------------|-------------------------------------------|------------|---------|----------------------------------------|-------------|
| Metode prototyping  | IV   | Metode pengembangan sistem  | Penggunaan model prototyping              | Nominal    | -       | Implementasi model pengembangan        | Menentukan proses pengembangan sistem |
| Kualitas sistem     | DV   | Kualitas aplikasi           | Functionality, usability, maintainability, portability | Interval | % / skor | Pengujian ISO 9126 & kuesioner         | Mengukur kelayakan dan kualitas sistem |
| Responden & perangkat uji | CV | Kondisi pengujian tetap | Jumlah responden & browser yang digunakan | Nominal | Orang/browser | Menyamakan kondisi pengujian | Agar hasil pengujian konsisten |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [✓] Setiap langkah terdokumentasi
  [✓] Tidak ada "lompatan logis"
  [✓] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Bagaimana mengembangkan sistem informasi pemasaran produk pertanian berbasis web yang layak digunakan oleh petani dan masyarakat?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Metode prototyping | IV | Metode pengembangan sistem | Prototyping |Nominal | — |
|Kualitas sistem | DV |Kelayakan & kualitas aplikasi |Functionality, usability, maintainability, portability |Interval |% / skor |
|Responden & perangkat uji | CV |Kondisi pengujian |Jumlah responden & browser |Nominal |Orang / browser |

**Apakah ada lompatan logis dalam rantai?** Ya 
> RQ menyebut “layak digunakan” tanpa menjelaskan metrik pengukurannya, yaitu ISO 9126.
---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 4 | ISO 9126 cukup mewakili kualitas sistem|
| Sensitive | 4| Nilai usability dan functionality dapat menunjukkan perubahan kualitas sistem|
| Feasible | 5| Mudah diukur menggunakan kuesioner dan pengujian sistem|

**Apakah perlu secondary metric?** Ya 
> Efficiency dan reliability, karena kedua aspek belum diuji optimal pada penelitian.

**Contoh kasus ceiling effect untuk metrik ini:**
> Nilai usability terlalu tinggi (misalnya semua responden memberi nilai bagus) sehingga sulit melihat peningkatan kualitas lebih lanjut.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Tidak semua responden mungkin mengisi lengkap| Cek ulang kuesioner sebelum dianalisis|
| Consistency | Apakah ada kontradiksi internal? | Bisa ada jawaban pengguna yang tidak konsisten| Validasi & pemeriksaan data|
| Validity | Apakah benar-benar mengukur yang dimaksud? | Ya, menggunakan standar ISO 9126| Gunakan instrumen sesuai standar|
| Representativeness | Apakah sampel mewakili populasi target? | Belum sepenuhnya karena hanya 25 responden| Tambah jumlah dan variasi responden|

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
>Memilih metrik setelah melihat hasil data disebut p-hacking karena metrik dipilih agar hasil terlihat bagus atau signifikan. Berbeda dengan eksplorasi data yang sah, karena eksplorasi bertujuan memahami pola data tanpa mengubah tujuan penelitian awal.