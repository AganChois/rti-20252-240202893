# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : ____________________
Metrik Utama      : ____________________

Tabel Hasil:
| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
|          |                      |                      |   |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 |             |             |        |
| 2 |             |             |        |

Bias Check:
  [ ] Y-axis mulai dari 0 (atau dijustifikasi)
  [ ] Error bar/CI ditampilkan
  [ ] Semua data disertakan (tidak cherry-picked)
  [ ] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda berdasarkan data yang direncanakan. Data skor di bawah ini adalah simulasi untuk tujuan perencanaan.

*Tabel 1: Hasil Evaluasi Kualitas Sistem Berdasarkan ISO 25010*
| Karakteristik Kualitas | Skor Rata-rata (%) (mean ± std) | n |
|-----------------------|---------------------------------|---|
| Functionality | 90.5 ± 5.2 | 24 |
| Usability | 88.1 ± 8.5 | 24 |
| Portability | 85.5 ± 7.8 | 24 |
| Maintainability | 82.0 ± 10.1 | 24 |

**Checklist tabel:**
- [✓] Self-contained (judul jelas, satuan ada, N tercantum)
- [✓] Mean ± std (bukan single number)
- [✓] Diurutkan berdasarkan metrik utama (Functionality)
- [✓] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar chart + error bar | Perbandingan skor rata-rata antar karakteristik kualitas untuk melihat kekuatan dan kelemahan sistem secara umum. | Skor rata-rata (mean) dan standar deviasi (std) dari Tabel 1. |
| 2 | Box plot | Menunjukkan distribusi, median, dan outlier dari skor Usability yang diberikan oleh 24 responden. | Data skor Usability mentah dari setiap responden. |
| 3 | Pie chart | Menampilkan komposisi responden berdasarkan peran (Petani vs. Masyarakat Umum) untuk memberikan konteks demografi sampel. | Jumlah responden per kategori. |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya. Perbedaan 0.4% terlihat sangat besar (A tampak 2x lebih tinggi dari B), padahal secara absolut perbedaannya sangat kecil. Ini adalah bias "truncated axis". |
| Apakah error bar ditampilkan? | Tidak disebutkan. Jika tidak, ini menyembunyikan variabilitas dan ketidakpastian, yang bisa jadi menunjukkan perbedaan tidak signifikan. |
| Apakah semua kondisi ditampilkan? | Ya, kondisi A dan B ditampilkan. |
| Apa solusinya? | Mulai Y-axis dari 0. Selalu sertakan error bar untuk menunjukkan rentang kepercayaan atau standar deviasi. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [✓] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: Tidak ada, dengan catatan:
  - Grafik bar chart (1) harus menggunakan Y-axis yang dimulai dari 0 dan menyertakan error bar.
  - Grafik pie chart (3) hanya akan digunakan jika jumlah kategori sedikit (2-4 kategori) agar tetap mudah dibaca.

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

Tabel dan grafik melayani tujuan yang berbeda namun saling melengkapi. **Tabel** memberikan **presisi**; menyajikan angka-angka eksak (misal: skor 88.1 ± 8.5) yang dibutuhkan untuk verifikasi dan analisis detail. **Grafik**, di sisi lain, memberikan **pola dan insight visual**; perbandingan antar item atau distribusi data jauh lebih cepat dipahami melalui bar chart atau box plot. Grafik menceritakan "kisah" dari data, sementara tabel menyediakan bukti numerik yang mendukung kisah tersebut.

Ya, saya pernah tanpa sengaja membuat grafik yang menyesatkan. Kesalahan paling umum adalah menggunakan bar chart di Excel yang secara default memotong sumbu Y (tidak mulai dari 0) untuk menonjolkan perbedaan. Hal ini membuat perbedaan kecil terlihat sangat signifikan, yang merupakan bentuk misrepresentasi data. Sejak itu, saya selalu memastikan sumbu Y dimulai dari nol untuk perbandingan yang adil.
