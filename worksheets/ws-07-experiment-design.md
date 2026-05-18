# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question :
Bagaimana peningkatan kualitas sistem pemasaran pertanian berbasis web menggunakan metode prototyping berdasarkan ISO 25010?

Hypothesis :
H₁ : Sistem berbasis web dengan metode prototyping memiliki kualitas lebih baik dibanding sistem konvensional.

Tipe Eksperimen   : [✓] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Sistem konvensional/non-web | Tanpa prototyping | Responden, browser, dan data sama |
| Treatment | Sistem website pertanian | Metode prototyping | Responden, browser, dan data sama |

Fairness Checklist:
  [✓] Dataset identik untuk semua kondisi
  [✓] Preprocessing setara
  [✓] Tuning effort setara
  [✓] Environment identik
  [✓] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Jawaban responden tidak konsisten | Validasi data & kuesioner |
| External    | Sampel sedikit dan tidak mewakili semua petani | Menambah variasi responden |
| Construct   | Konsep “kualitas” tidak sesuai metrik | Menggunakan ISO 25010 |
| Conclusion  | Hasil kurang kuat karena data terbatas | Menggunakan analisis dan pengujian yang jelas |

Statistical Plan:
  Uji statistik   : Analisis deskriptif persentase
  Justifikasi      : Digunakan untuk menilai kualitas sistem berdasarkan ISO 25010
  Alpha            : 0.05
  Effect size min  : ≥ 70% usability
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana peningkatan kualitas sistem pemasaran pertanian berbasis web menggunakan metode prototyping berdasarkan ISO 25010?
**Tipe eksperimen:** Comparison 

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Sistem pemasaran konvensional/non-web | Tanpa prototyping | Data, responden, browser, dan kondisi uji sama |
| Treatment | Sistem pemasaran pertanian berbasis web| Metode prototyping| Data, responden, browser, dan kondisi uji sama|

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅| Menggunakan data dan responden yang sama|
| Preprocessing setara | ✅| Pengolahan data dilakukan dengan langkah yang sama|
| Tuning effort setara | ✅| Pengembangan dan pengujian dilakukan dengan usaha yang seimbang|
| Environment identik | ✅| Browser, perangkat, dan kondisi uji dibuat sama|
| Metrik evaluasi sama | ✅| Semua kondisi diuji menggunakan ISO 25010|

**Ada yang tidak fair?** Tidak
> Semua kondisi eksperimen sudah menggunakan pengaturan yang sama sehingga hasil lebih adil dan dapat dibandingkan.

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Jawaban responden tidak konsisten | Validasi dan pengecekan data kuesioner |
| External | Jumlah responden sedikit| Menambah variasi dan jumlah responden|
| Construct | Konsep “kualitas sistem” tidak sepenuhnya terwakili| Menggunakan standar ISO 25010|
| Conclusion | Hasil kurang kuat karena data terbatas| Menggunakan analisis dan pengujian yang jelas|

**Ancaman mana yang paling sulit dimitigasi?** External validity
**Mengapa?**
> Karena jumlah responden terbatas sehingga hasil penelitian belum tentu mewakili seluruh pengguna atau petani secara umum.
---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah dataset dan kondisi pengujian sama untuk semua baseline?
2. Apakah metrik evaluasi yang digunakan sudah adil dan jelas?
3. Apakah peningkatan hasil benar-benar signifikan dan dapat dibuktikan secara statistik?
