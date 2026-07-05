# Outline, Peta Sumber, dan Klaim Kunci Naskah

Dokumen ini adalah "peta" untuk `naskah-jurnal.md`. Tujuannya adalah untuk memastikan konsistensi internal dari argumen penelitian di seluruh bagian naskah dan dokumen-dokumen terkait.

---

## 1. Outline Naskah (Struktur IMRAD)

1.  **Abstrak:** Ringkasan masalah (evaluasi kualitas tidak standar), metode (prototyping, ISO 25010, n=24), hasil utama (usability 90.92%, p < 0.0001), dan kontribusi (validasi metode prototyping).
2.  **Pendahuluan:** Konteks (digitalisasi pertanian), gap (kurangnya evaluasi kualitas formal), RQ, tujuan, dan kontribusi.
3.  **Tinjauan Pustaka:** Sintesis dari 3 pilar: sistem informasi pertanian (Tandirerung, 2020), metode prototyping (Wijaya, 2018), dan standar kualitas ISO 25010 (Hartono, 2022).
4.  **Metodologi:** Desain eksperimen, arsitektur sistem, prosedur pengujian, instrumen kuesioner, dan rencana analisis data (T-test).
5.  **Hasil dan Analisis:** Penyajian statistik deskriptif (Tabel 1) dan hasil uji hipotesis.
6.  **Pembahasan:** Interpretasi hasil (makna skor 90.92%), perbandingan dengan literatur, diskusi tentang outlier, dan limitasi penelitian.
7.  **Kesimpulan:** Jawaban langsung untuk RQ, penegasan kontribusi, dan saran untuk penelitian selanjutnya.

---

## 2. Peta Sumber Konten

| Bagian Naskah | Sumber Utama |
|---|---|
| **Pendahuluan** | `01-proposal/proposal-penelitian.md` (Bagian 1-3) |
| **Tinjauan Pustaka** | `02-literatur/matriks-literatur.md`, `02-literatur/daftar-pustaka.bib` |
| **Metodologi** | `01-proposal/proposal-penelitian.md` (Bagian 5), `03-teori/arsitektur-dan-skema.md` |
| **Hasil dan Analisis** | `06-output/tables/descriptive_stats.csv`, `06-output/text/hasil-uji-hipotesis.txt` |
| **Pembahasan** | `ws-15-scientific-writing.md` (Latihan 3), `catatan-bimbingan-dan-progres.md` (Sesi 2) |
| **Kesimpulan** | `ws-15-scientific-writing.md` (Latihan 1) |

---

## 3. Daftar Klaim Kunci (Checklist Konsistensi)

Nilai dan klaim berikut harus **identik** di semua tempat (abstrak, isi, tabel, gambar, kesimpulan).

### 3.1. Desain Penelitian

| Klaim | Nilai | Sumber |
|---|---|---|
| Pertanyaan Penelitian (RQ) | "Bagaimana kualitas sistem... jika diukur berdasarkan standar ISO 25010?" | `proposal-penelitian.md` |
| Hipotesis (H1) | Skor rata-rata usability > 70% | `proposal-penelitian.md` |
| Jumlah Responden (n) | 24 | `hasil-kuesioner-mentah.csv` |
| Standar Evaluasi | ISO/IEC 25010:2011 | `proposal-penelitian.md` |
| Metode Pengembangan | Prototyping | `proposal-penelitian.md` |

### 3.2. Hasil Numerik Utama

| Klaim | Nilai | Sumber |
|---|---|---|
| **Skor Usability (Mean)** | **90.92** | `descriptive_stats.csv` |
| Skor Usability (Median) | 92.0 | `descriptive_stats.csv` |
| Skor Usability (Std. Dev.) | 11.83 | `descriptive_stats.csv` |
| Outlier Usability | 1 kasus (nilai 35) | `catatan-bimbingan-dan-progres.md` |
| **T-statistic** | **8.685** | `hasil-uji-hipotesis.txt` |
| **P-value** | **< 0.0001** | `hasil-uji-hipotesis.txt` |
| Skor Reliability (Mean) | 94.42 | `descriptive_stats.csv` |
| Skor Security (Mean) | 86.17 | `descriptive_stats.csv` |

### 3.3. Klaim Kualitatif Utama

| Klaim | Sumber |
|---|---|
| Hipotesis **terbukti** / H0 **ditolak**. | `hasil-uji-hipotesis.txt` |
| Hasil **signifikan secara statistik**. | `hasil-uji-hipotesis.txt` |
| Kontribusi utama adalah **validasi empiris** metode prototyping untuk domain agrikultur. | `proposal-penelitian.md` |
| Metode prototyping **efektif** untuk menghasilkan sistem berkualitas tinggi. | Kesimpulan Naskah |