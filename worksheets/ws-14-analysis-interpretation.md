# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   |          |      |     |        |     |     |   |

2. Uji Hipotesis:
   Uji yang digunakan  : ____________________
   Justifikasi          : ____________________
   Hasil: p = ____, effect size (d/r/η²) = ____
   CI 95%               : [____, ____]

3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : ____________________
   Practical significance: ____________________
   Perbandingan literatur: ____________________

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   |       |         |        |          |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : ____________________
   Boundary condition   : ____________________
   Insight              : ____________________
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.
| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 1 grup (skor dari 24 responden) yang dibandingkan dengan sebuah nilai standar (threshold). |
| Apakah data berpasangan (paired)? | Tidak, ini adalah desain one-sample. |
| Apakah distribusi normal? (uji normalitas) | Perlu diuji (misal: dengan Shapiro-Wilk). Jika normal, gunakan uji parametrik. Jika tidak, gunakan non-parametrik. |
| **Uji yang dipilih:** | **One-Sample t-test** (jika data terdistribusi normal) atau **Wilcoxon Signed-Rank Test** (jika tidak normal). |
| **Justifikasi:** | Tujuan riset adalah menguji apakah kualitas sistem (misal: skor usability) dari satu sampel (n=24) secara signifikan melampaui sebuah threshold kelayakan yang telah ditentukan (misalnya, 70%), sesuai dengan hipotesis di WS-04. |

**Effect size yang akan dilaporkan:** [✓] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| Sistem Baru | 88.1 ± 8.5 | 24 |
| Threshold | 70.0 | - |

*Asumsikan hasil uji hipotesis (One-Sample t-test) adalah: p = 0.001, Cohen's d = 2.1, CI 95% = [84.5, 91.7]*

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | Dengan p-value = 0.001 (jauh di bawah α=0.05), kita menolak hipotesis nol. Hasil ini menunjukkan bahwa skor usability rata-rata (88.1%) secara statistik signifikan lebih tinggi dari threshold kelayakan 70%. |
| Effect size | Cohen's d = 2.1 menunjukkan effect size yang "sangat besar" (large). Ini berarti perbedaan antara skor yang didapat dan threshold kelayakan tidak hanya signifikan secara statistik, tetapi juga sangat besar secara praktis. |
| Practical significance | Perbedaan yang sangat besar ini memiliki signifikansi praktis yang tinggi. Sistem tidak hanya "lulus" standar kelayakan, tetapi jauh melampauinya, mengindikasikan tingkat penerimaan pengguna yang sangat baik. |
| Hubungan ke RQ | Hasil ini secara langsung menjawab Research Question (WS-04) dengan memberikan bukti kuantitatif bahwa sistem yang dikembangkan menggunakan metode prototyping memang memiliki kualitas (usability) yang sangat baik, melampaui standar umum. |
| Perbandingan literatur | Skor 88.1% sebanding dengan hasil dari studi Tandirerung et al. (2020) yang juga melaporkan usability 88.13% (WS-03). Ini menunjukkan bahwa sistem yang dikembangkan mencapai tingkat kualitas yang setara dengan penelitian relevan sebelumnya. |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Skor usability rata-rata sistem adalah 72%, dengan p-value = 0.15 saat diuji terhadap threshold 70%. Hipotesis H₁ (terdapat peningkatan kualitas) tidak didukung secara signifikan.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan kegagalan riset. Ini adalah temuan valid bahwa sistem yang dikembangkan hanya sedikit di atas standar kelayakan dan peningkatannya tidak signifikan secara statistik. Ini adalah kontribusi yang jujur. |
| Kemungkinan penyebab? | 1. Desain antarmuka mungkin tidak seintuitif yang diharapkan. 2. Responden mungkin mengalami kesulitan teknis minor yang tidak terdeteksi. 3. Variasi jawaban antar responden sangat tinggi, sehingga menutupi efek rata-rata. |
| Boundary condition? | Metode prototyping mungkin efektif untuk pengembangan cepat, tetapi untuk mencapai usability yang sangat tinggi, mungkin diperlukan iterasi desain tambahan atau user testing yang lebih mendalam yang tidak termasuk dalam lingkup saat ini. |
| Insight yang bisa diambil? | Mencapai "kelayakan" (passing grade) relatif mudah, tetapi mencapai "keunggulan" (excellence) membutuhkan usaha lebih. Ada trade-off antara kecepatan pengembangan (via prototyping) dan kualitas UX puncak. |
| Apakah layak dilaporkan? Mengapa? | Sangat layak. Melaporkan hasil ini mencegah klaim berlebihan tentang efektivitas metode prototyping. Ini memberikan gambaran realistis dan mendorong penelitian masa depan untuk menyelidiki cara meningkatkan usability dari "cukup" menjadi "sangat baik". |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical / Conclusion | Ukuran sampel kecil (n=24) | Power statistik rendah, sehingga sulit mendeteksi efek yang sebenarnya ada (risiko Type II error). Perbedaan kecil mungkin tidak akan terdeteksi sebagai signifikan. |
| External Validity | Sampel kurang beragam (dari WS-07) | Hasil mungkin tidak dapat digeneralisasi ke seluruh populasi petani dan masyarakat. Responden yang lebih tech-savvy mungkin memberikan skor lebih tinggi. |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> "Failure" dalam riset, seperti hipotesis yang tidak terdukung, bukanlah kegagalan proyek, melainkan sebuah kontribusi ilmiah yang berharga. Hasil negatif memberikan informasi penting: bahwa sebuah pendekatan tertentu tidak bekerja dalam konteks yang diuji. Ini mencegah peneliti lain membuang waktu dan sumber daya untuk mengejar jalan buntu yang sama.
> Failure analysis mengubah cara saya melihat hasil negatif dari sebuah "kegagalan" menjadi sebuah "temuan". Ia memaksa kita untuk bertanya "mengapa ini tidak berhasil?" yang seringkali menghasilkan pemahaman yang lebih dalam tentang sebuah masalah, asumsi yang salah, atau batasan (boundary condition) dari sebuah metode. Menemukan di mana dan mengapa sebuah metode gagal seringkali lebih mencerahkan daripada sekadar melaporkan bahwa metode tersebut berhasil.
