# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Belum adanya sistem pemasaran pertanian yang terintegrasi dan dievaluasi secara standar (ISO 9126).

Research Question:
  Tipe         : Improvement 
  Formulasi    : Bagaimana peningkatan kualitas sistem pemasaran pertanian berbasis web dengan metode prototyping berdasarkan ISO 9126 dibanding sistem konvensional?
  Variabel IV  : Metode prototyping
  Variabel DV  : Kualitas sistem
  Metrik       : Functionality, Usability (88,13%), Maintainability, Portability
  Dataset      : 25 responden (petani & masyarakat)
  Baseline     : Sistem pemasaran konvensional (tanpa sistem web)

Quality Check RQ:
  [✓] Variabel spesifik
  [✓] Metrik jelas
  [✓] Baseline ada
  [✓] Konteks disebutkan
  [✓] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Sistem berbasis web dengan prototyping terbukti memiliki kualitas baik berdasarkan ISO 9126
  Jenis kontribusi        : Improvement 
  Gap yang diisi          : Kurangnya sistem terintegrasi dan evaluasi kualitas standar

Hypothesis Pair:
  H₀ : Tidak ada peningkatan kualitas sistem dibanding metode konvensional
  H₁ : Terdapat peningkatan kualitas sistem menggunakan metode prototyping
  Threshold              : Usability ≥ 70%
  Justifikasi threshold  : Standar umum kelayakan usability sistem (di atas rata-rata penerimaan pengguna)
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Method Gap + Context Gap

**RQ versi pertama (tulis bebas):**
> Bagaimana kualitas sistem pemasaran pertanian berbasis web menggunakan metode prototyping?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | YA |Prototyping |
| Metrik terukur |KURANG |(belum disebutkan ISO 9126) |
| Baseline |TIDAK |- |
| Dataset/konteks |KURANG |(belum jelas pengguna) |

**Tipe RQ:** Improvement

**RQ versi revisi (setelah evaluasi):**
> Bagaimana peningkatan kualitas sistem pemasaran pertanian berbasis web menggunakan metode prototyping dibanding sistem konvensional berdasarkan metrik ISO 9126 pada 25 pengguna (petani dan masyarakat)?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada peningkatan kualitas sistem pemasaran pertanian berbasis web menggunakan metode prototyping dibanding sistem konvensional |
| H₁ | Terdapat peningkatan kualitas sistem pemasaran pertanian berbasis web menggunakan metode prototyping dibanding sistem konvensional|
| Metrik | ISO 9126: functionality, usability, maintainability, portability|
| Threshold |Usability ≥ 70% |
| Justifikasi threshold |70% adalah batas umum penerimaan sistem oleh pengguna (layak digunakan) |

**Apakah hipotesis ini falsifiable?** Ya 
> Bagaimana cara membuktikannya salah? Jika hasil pengujian menunjukkan nilai usability < 70% atau tidak ada peningkatan kualitas dibanding sistem konvensional, maka H₁ ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | *Apakah metode prototyping meningkatkan kualitas sistem pemasaran pertanian berbasis web dibanding sistem konvensional berdasarkan ISO 9126? |
| Variable (IV) | Metode pengembangan (prototyping vs konvensional) |
| Variable (DV) | Kualitas sistem|
| Metric |Functionality, Usability (persentase), Maintainability, Portability |
| Data source |25 responden (petani & masyarakat) + hasil pengujian sistem |
| Analysis method |Analisis deskriptif kuantitatif (persentase & uji kelayakan ISO 9126) |

**Apakah rantai lengkap?** Ya 
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Pengembangan Sistem Informasi Pemasaran Produk Pertanian Berbasis Website
**RQ yang diekstrak:** Bagaimana mengembangkan sistem informasi pemasaran produk pertanian berbasis web yang layak digunakan oleh petani dan masyarakat?
**Komponen yang hilang:** 
-Baseline (tidak ada perbandingan dengan sistem lain)
-Metrik eksplisit di RQ (ISO 9126 digunakan, tapi tidak dirumuskan di RQ)
-Metode tidak disebut di RQ (prototyping ada di metode, bukan di RQ)
-Konteks belum spesifik (lokasi & jumlah responden tidak disebut di RQ)
