# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : ____ (target: 10-12 konten + title/closing)
  Time per slide : ~2 min
  Total time     : ____ menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title       |        | 30s   |
| 2 | Problem     |        | 2min  |
| 3 | Gap + RQ    |        | 2min  |
| ..|             |        |       |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  |                     |               |
| Gap      |                     |               |
| Method   |                     |               |
| Results  |                     |               |
| Generalization |               |               |

Latihan:
  Latihan 1: [tanggal] — [catatan timing & feedback]
  Latihan 2: [tanggal] — [catatan timing & feedback]
  Latihan 3: [tanggal] — [catatan timing & feedback]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul, Nama, Konteks: Evaluasi Kualitas Sistem Pemasaran Pertanian | Screenshot homepage sistem | 1 min |
| 2 | Problem: Petani sulit memasarkan produk, sementara sistem yang ada seringkali tidak dievaluasi kualitasnya secara sistematis. | Diagram alur masalah vs. alur ideal dengan sistem | 2 min |
| 3 | Gap & RQ: Ada kesenjangan dalam evaluasi sistem pertanian menggunakan standar ISO. RQ: Bagaimana kualitas sistem yang dibangun dengan prototyping menurut ISO 25010? | Tabel ringkas literature gap (dari WS-03) | 1.5 min |
| 4 | Metode: Prototyping → Sistem Web → Evaluasi Kuesioner (n=24) → Analisis Statistik (One-Sample t-test vs threshold 70%). | Diagram alur metodologi | 2 min |
| 5 | Hasil Utama (Tabel): Rangkuman skor rata-rata untuk Functionality, Usability, dll. | Tabel hasil dari WS-12 | 2 min |
| 6 | Hasil Utama (Grafik): Skor Usability (88.1%) jauh di atas threshold 70%. | Bar chart skor kualitas dengan error bar (dari WS-12) | 2 min |
| 7 | Interpretasi: Hasil signifikan secara statistik (p=0.001) dan praktis (Cohen's d=2.1), menunjukkan penerimaan pengguna yang sangat baik. | Angka p-value dan Cohen's d ditampilkan di samping grafik | 2 min |
| 8 | Limitasi & Arah Selanjutnya: Sampel kecil (n=24) dan kurang beragam. Perlu pengujian skala besar dan penambahan fitur cerdas. | Bullet points | 1.5 min |
| 9 | Kesimpulan & Kontribusi: Metode prototyping terbukti efektif untuk membangun sistem berkualitas tinggi di domain ini. | Ringkasan 2-3 poin utama | 1 min |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Generalization | "Dengan hanya 24 responden, seberapa yakin Anda hasil ini bisa digeneralisasi?" | Hasil ini adalah indikasi awal yang kuat, namun generalisasi penuh memerlukan studi lanjutan. | Kami secara eksplisit menyatakan ini sebagai limitasi utama di slide ke-8. | Tujuan riset ini adalah studi kelayakan. Efek yang sangat besar (d=2.1) pada sampel kecil menunjukkan sinyal yang kuat, namun validasi eksternal butuh sampel lebih besar. |
| 2 | Method | "Mengapa memilih threshold 70%? Apakah ada standar baku untuk angka itu?" | 70% adalah standar kelayakan umum dalam praktik evaluasi usability. | Angka ini sering diasosiasikan dengan skor "pass" atau "above average" pada skala seperti SUS (System Usability Scale). | Karena tidak ada threshold resmi untuk domain ini, kami mengadopsi praktik umum dari bidang HCI sebagai baseline yang masuk akal untuk menguji kelayakan sistem. |
| 3 | Contribution | "Studi Tandirerung et al. (2020) mendapat hasil yang hampir identik. Apa kebaruan riset Anda?" | Kontribusi kami adalah replikasi dan konfirmasi temuan tersebut, yang memperkuat validitas eksternal dari metode prototyping. | Studi Tandirerung fokus pada UMKM umum, riset kami pada konteks spesifik pemasaran pertanian dengan audiens campuran (petani & masyarakat). | Replikasi adalah kontribusi ilmiah yang berharga. Hasil yang konsisten menunjukkan bahwa efektivitas metode ini bukanlah kebetulan, melainkan pola yang robust. |
| 4 | Construct Validity | "Mengapa analisis utama hanya pada Usability, padahal ISO 25010 punya banyak karakteristik lain?" | Kami fokus pada Usability karena itu yang paling relevan dengan interaksi pengguna, yang merupakan inti dari metode prototyping. | Hipotesis utama kami (WS-04) secara spesifik menargetkan usability. Karakteristik lain tetap disajikan di Tabel 1 (slide 5). | Tujuan utama adalah memastikan sistem mudah digunakan oleh target audiens. Aspek lain seperti efisiensi performa kami sarankan untuk penelitian teknis selanjutnya. |
| 5 | Results | "Ada satu outlier dengan skor rendah. Mengapa tidak dibuang? Apakah hasilnya akan tetap signifikan?" | Outlier tidak dibuang karena merupakan data valid. Hasil tetap sangat signifikan. | Protokol penanganan anomali kami (WS-11) melarang penghapusan tanpa bukti error. Perhitungan ulang tanpa outlier justru akan membuat p-value lebih kecil. | Mempertahankan outlier adalah praktik riset yang jujur dan memberikan gambaran yang lebih realistis tentang penerimaan sistem oleh pengguna. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | "Metode prototyping dikenal cepat tapi sering menghasilkan kode yang tidak maintainable. Apakah Anda mengukur aspek Maintainability?" | "Ya, kami mengukurnya. Berdasarkan Tabel 1 di slide 5, skor Maintainability adalah 82.0%, yang juga merupakan skor yang baik. Ini menunjukkan sistem yang dihasilkan tetap memiliki tingkat maintainability yang layak." | [✓] Direct [✓] Data-based [✓] Honest |
| 2 | "Bagaimana Anda memastikan responden memahami pertanyaan kuesioner ISO 25010 yang bisa jadi cukup teknis?" | "Sebelum pengisian, kami memberikan sesi demo dan briefing singkat. Selama sesi tersebut, kami menjelaskan setiap bagian kuesioner dengan bahasa yang lebih sederhana dan mendampingi responden." | [✓] Direct [✓] Data-based [✓] Honest |
| 3 | "Selain prototyping, metode pengembangan apa lagi yang Anda pertimbangkan, dan mengapa prototyping yang dipilih?" | "Kami mempertimbangkan Waterfall, namun kurang cocok karena butuh semua requirement di awal. Prototyping dipilih karena memungkinkan feedback iteratif dari pengguna, yang sangat krusial untuk memastikan produk akhir sesuai kebutuhan mereka." | [✓] Direct [✓] Data-based [✓] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Pertanyaan tentang kebaruan riset (nomor 3 di Latihan 2), karena membutuhkan argumen yang kuat untuk meyakinkan bahwa sebuah studi replikasi memiliki nilai kontribusi yang signifikan.

**Apa yang perlu disiapkan lebih baik:**
> Justifikasi yang lebih mendalam tentang pentingnya studi konfirmasi (replication study) dalam sains untuk membangun pengetahuan yang lebih robust dan tidak bergantung pada satu temuan tunggal.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Insight terbesar adalah perbedaan fundamental antara *engineering* (membangun sesuatu yang berfungsi) dan *research* (membangun sesuatu untuk membuktikan sebuah klaim). Seluruh proses, terutama WS-06 (System-Experiment Mapping) dan WS-07 (Experimental Design), secara sistematis mengubah mindset dari "membuat aplikasi" menjadi "merancang eksperimen yang terkontrol".

**Yang akan selalu diterapkan:**
> Prinsip "Benang Merah" (Red Thread) dari WS-08. Saya akan selalu memastikan ada alur logis yang koheren dari Masalah → Gap → RQ → Metode → Hasil → Kesimpulan. Ini adalah alat paling ampuh untuk menjaga agar riset tetap fokus dan argumennya utuh.
