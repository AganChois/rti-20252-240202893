# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Sistem Informasi Pemasaran Produk Pertanian Berbasis Web
Database   : Google Scholar
Query      : ("agricultural marketing information system" OR "sistem informasi pemasaran pertanian") AND ("web" OR "e-commerce") NOT ("medical")
Tahun      : 2017–2024
Hasil awal : ±25 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|Tandirerung et al.|2020|Prototype + ISO 9126|Data petani & UMKM|Usability 88,13%|Belum uji efficiency & reliability|
|Apriadi & Saputra|2017|Marketplace E-commerce|Produk pertanian|Distribusi lebih pendek|Tidak fokus UX|

Pola yang ditemukan:
  Metode dominan     : Sistem berbasis web & e-commerce + pendekatan prototype
  Dataset umum       : Data produk pertanian, petani, transaksi penjualan
  Limitasi berulang  : 
                      -Kurangnya interaksi user (penjual–pembeli)
                      -Belum optimal di aspek efficiency & reliability
                      -Sistem masih sederhana (belum intelligent/AI)

GAP IDENTIFICATION

Gap 1: Method + Performance Gap
  Deskripsi    : Sistem masih berbasis web sederhana, belum menggunakan teknologi cerdas (AI/rekomendasi)
  Bukti        : Semua penelitian hanya fokus pada sistem informasi & transaksi, tanpa fitur pintar
  Signifikansi : Tanpa AI, sistem tidak bisa memberi rekomendasi produk → potensi penjualan kurang maksimal

Gap 2: Context + Data Gap
  Deskripsi    : Sistem belum diuji secara luas di berbagai daerah atau skala besar
  Bukti        : Studi hanya dilakukan di daerah tertentu (contoh: Desa Kanreapia)
  Signifikansi : Belum diketahui apakah sistem efektif untuk kondisi berbeda (daerah lain / skala nasional)

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|Sistem Web Prototype (Tandirerung et al.)|Sama-sama pemasaran pertanian|Banyak digunakan|Jurnal utama|
|Marketplace E-commerce (Apriadi & Saputra)|Sama domain distribusi|Umum dipakai|Jurnal RESTI|
```

---

## Latihan 1 — Concept-Centric Literature Table

Topik riset dari WS-02 : Sistem IoT untuk Monitoring Kualitas Air Limbah

**Topik riset:**Sistem IoT untuk Monitoring Kualitas Air Limbah
**Query pencarian:** ("IoT" OR "Internet of Things") AND ("water quality monitoring" OR "wastewater") AND ("real-time")
**Database:** Google Scholar, IEEE, Springer, MDPI

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Sugiharto et al. | 2023 | IoT + cloud + multi-sensor | 4,833 data points (river test) | Akurasi pH 96.85%, TDS 98.10% | Hanya 4 parameter |
| 2 | Geetha & Gouthami| 2017| IoT real-time sensor network| Water sample pipeline| Real-time alert monitoring|Sistem lama, sensor terbatas |
| 3 | Choong & Chia| 2026| ESP32 + Blynk| Sampel limbah tekstil Akurasi pH 93.28%| Fokus industri tekstil|
| 4 | Dhruba et al.| 2023| IoT + mobile app| Industrial wastewater| Monitoring pH, TDS, turbidity| Tidak bahas efisiensi daya|
| 5 | HydroSense Framework| 2026| Dual microcontroller + edge processing| Uji 90 hari| Reliabilitas cloud 99.8%| Biaya masih relatif tinggi|

**Pola yang terlihat — Metode dominan:** ESP32 / Arduino + sensor pH, TDS, turbidity + cloud monitoring
**Limitasi yang berulang:** Akurasi sensor, stabilitas jaringan, keterbatasan parameter kualitas air

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [☑] Ya /  | Akurasi sensor menurun pada lingkungan limbah nyata yang kompleks |
| Method Gap | [☑ ] Ya /  |Sebagian besar studi masih menggunakan threshold sederhana, belum banyak edge analytics / AI |
| Data Gap | [ ☑] Ya / | Dataset jangka panjang dan multi-lokasi masih terbatas|
| Context Gap | [ ☑] Ya |Banyak penelitian fokus sungai / industri, belum spesifik rumah tangga |

**Gap utama yang dipilih:** Method Gap + Context Gap
**Mengapa gap ini penting ?**
> Karena sistem monitoring limbah rumah tangga membutuhkan solusi murah, real-time, dan akurat. Sebagian besar paper masih fokus pada industri atau sungai, sehingga belum sepenuhnya sesuai untuk konteks rumah tangga dan UMKM.
---

## Latihan 3 — Baseline Selection

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|1|IoT + mobile alert system|Sama-sama monitoring limbah|Banyak dipakai pada sistem praktis|Bukan|Dhruba et al., 2023|
| 2 | ESP32 + pH/TDS sensor + cloud dashboard | Task sama: monitoring air real-time | Dipakai banyak paper | Bukan, tapi common practice| Sugiharto et al., 2023|

**Apakah pemilihan baseline ini bisa dianggap straw man?** Tidak
> Justifikasi: baseline diambil dari metode yang memang umum digunakan dalam literatur, bukan metode yang sengaja dibuat lemah.
---
## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
“Belum ada yang meneliti ini” adalah klaim tanpa bukti jika tidak didukung literature review.
Research gap yang valid harus dibuktikan dari beberapa paper yang menunjukkan keterbatasan, pola limitasi, atau konteks yang belum terjangkau. Cara membuktikannya adalah dengan membandingkan minimal 5 paper dan menemukan pola gap yang berulang.