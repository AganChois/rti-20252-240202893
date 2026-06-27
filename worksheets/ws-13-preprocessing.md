# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : ____________________
Jumlah data awal  : ____________________

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing |             |            |             |
| Duplikat|             |            |             |
| Error   |             |            |             |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
|             |          |        |        |

Normalization:
  Metode    : ____________________
  Alasan    : ____________________
  Parameter : (dihitung dari: training set / seluruh data)

Leakage Check:
  [ ] Parameter normalisasi dari training set saja
  [ ] Tidak ada informasi test set dalam preprocessing
  [ ] Cross-validation dilakukan setelah split

Jumlah data akhir : ____________________
Script tersedia   : [ ] Ya → path: ____ | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Berdasarkan hasil validasi data dari WS-11, dokumentasikan rencana pembersihan data.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing values | 1 dari 25 (4%) | Listwise deletion | Data responden tidak lengkap (tidak menyelesaikan kuesioner). Karena persentasenya kecil (<5%) dan tidak bisa diimputasi, data ini dikecualikan dari analisis kuantitatif. |
| Duplikat | 0 | - | Tidak ditemukan data responden yang duplikat berdasarkan ID. |
| Error format | 0 | - | Semua data skor dan waktu tercatat dalam format numerik yang konsisten sesuai skema. |

**Jumlah data sebelum cleaning:** 25
**Jumlah data setelah cleaning:** 24
**Persentase data yang hilang/berubah:** 4%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Usability_Score | 0 – 100 | Cenderung left-skewed | Ya (1) | Tidak perlu | Analisis deskriptif tidak memerlukan normalisasi. Skor sudah dalam skala persentase yang dapat diinterpretasikan langsung. |
| Functionality_Score | 0 – 100 | Cenderung left-skewed | Tidak | Tidak perlu | Sama seperti Usability_Score, skala sudah konsisten dan mudah diinterpretasikan. |
| Task_Completion_Time_s | > 0 | Cenderung right-skewed | Ya (potensial) | Tidak perlu | Metrik ini akan dianalisis secara terpisah (misal: menggunakan median) dan tidak digabungkan dengan metrik skor dalam satu model. |

**Apakah normalisasi diperlukan?** [ ] Ya / [✓] Tidak
**Justifikasi:**
> Normalisasi tidak diperlukan karena analisis utama yang akan dilakukan adalah statistik deskriptif (mean, median, std) dan penyajian visual (bar chart, box plot). Semua metrik skor utama (Functionality, Usability) sudah berada pada skala yang sama dan dapat dibandingkan (0-100%). Metode analisis yang digunakan tidak sensitif terhadap skala fitur.

**Leakage check:**
- [✓] Parameter dihitung dari training set saja (tidak relevan)
- [✓] Normalisasi diterapkan setelah train-test split (tidak relevan)

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: Hasil Kuesioner Evaluasi Kualitas Sistem (ISO 25010)
2. Data awal: 25 records, 4 features
3. Cleaning:
   - Missing values: 1 kasus, metode: Listwise deletion
   - Duplikat: 0 kasus, tindakan: -
   - Error: 0 kasus, tindakan: -
4. Transformation: Tidak ada transformasi yang dilakukan.
5. Normalisasi: Tidak dilakukan.
6. Data akhir: 24 records, 4 features
7. Leakage check:  Lulus (Tidak relevan karena tidak ada train-test split atau normalisasi)
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, terutama pada proyek-proyek awal machine learning, saya sering langsung menerapkan `StandardScaler` atau `MinMaxScaler` pada semua fitur numerik sebagai bagian dari "ritual" preprocessing, tanpa mempertimbangkan apakah model yang digunakan (misalnya, Decision Tree atau Random Forest) memang sensitif terhadap skala fitur.
Risiko **over-preprocessing** (pemrosesan berlebihan) adalah:
1.  **Distorsi Informasi:** Mengubah distribusi asli data secara tidak perlu dapat mempersulit interpretasi hasil dan menghilangkan wawasan penting.
2.  **Kehilangan Makna Asli:** Mengubah data dari skala aslinya (misalnya, suhu dalam Celsius) ke skala [0, 1] dapat membuat nilai-nilai tersebut kehilangan makna intuitifnya bagi analis.
3.  **Kompleksitas yang Tidak Perlu:** Setiap langkah preprocessing menambah kerumitan pada pipeline, yang harus didokumentasikan, di-debug, dan direplikasi, yang meningkatkan potensi kesalahan.
