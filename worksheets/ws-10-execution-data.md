# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| 3     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : ____
Total runs               : ____

DATA LOG (per run):
  Run ID    : ____________________
  Timestamp : ____________________
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

> "Run" dalam konteks ini adalah satu sesi lengkap dari satu responden, mulai dari penggunaan sistem hingga pengisian kuesioner. "Seed" tidak berlaku, namun konsistensi dijaga dengan skenario tugas dan instrumen yang sama untuk semua responden.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Evaluasi Sistem Web v1.0 | N/A (Urutan tugas & kuesioner konsisten) | Sistem v1.0, Kuesioner ISO 25010 v1 | Planned |
| 2 | Evaluasi Sistem Web v1.0 | N/A (Urutan tugas & kuesioner konsisten) | Sistem v1.0, Kuesioner ISO 25010 v1 | Planned |
| ... | ... | ... | ... | Planned |
| 25 | Evaluasi Sistem Web v1.0 | N/A (Urutan tugas & kuesioner konsisten) | Sistem v1.0, Kuesioner ISO 25010 v1 | Planned |

**Total skenario:** 1
**Run per skenario:** 25 (sesuai jumlah responden)
**Total run keseluruhan:** 25

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | `resp-001` |
| Timestamp | `2026-06-27T10:30:00Z` |
| Respondent_ID | `anon-f2a4` |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| System_Version | `v1.0` |
| Code version | `commit 8f5d3a2` |
| Instrument_Version | `Kuesioner ISO 25010 v1` |
| Browser_Info | `Chrome/125.0.0.0 on Windows 11` |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Usability_Score | float | 0.0 – 100.0 |
| Functionality_Score | float | 0.0 – 100.0 |
| Task_Completion_Time_s | integer | > 0 |
| Qualitative_Feedback | string | - |

**Format output:** [✓] CSV / [ ] JSON / [✓] Database / [ ] Lainnya: ____
> Data mentah dari kuesioner akan disimpan di database, kemudian diekspor ke CSV untuk analisis.

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Responden tidak bisa submit kuesioner karena error 500. | Dokumentasi error, perbaiki bug, data dari sesi tersebut tidak digunakan, dan cari responden pengganti jika memungkinkan. |
| Hasil ekstrem | Satu responden memberi skor 1 untuk semua aspek, sementara 24 lainnya memberi skor 4-5. | Data tidak dihapus. Tandai sebagai outlier, periksa feedback kualitatifnya, dan laporkan dalam analisis (misal, dengan membandingkan mean vs median). |
| Waktu eksekusi anomali | Rata-rata responden butuh 10 menit, satu responden butuh 60 menit. | Catat waktu tersebut. Investigasi dari catatan observasi (jika ada). Gunakan median untuk melaporkan waktu penyelesaian agar tidak terdistorsi oleh outlier. |
| Inkonsistensi dengan run lain | Responden memberi skor usability 5/5 tapi di feedback menulis "sistem sangat sulit digunakan". | Dokumentasikan sebagai temuan. Ini bukan error, melainkan insight tentang persepsi pengguna. Bahas inkonsistensi ini di bagian Diskusi. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya, seringkali dalam tugas atau proyek awal, hasil dilaporkan hanya dari satu kali pengujian. Risikonya adalah hasil tersebut bisa jadi hanya kebetulan (fluke), tidak dapat diandalkan, dan tidak memberikan gambaran tentang variabilitas atau ketidakpastian. Kesimpulan yang ditarik menjadi sangat lemah.
**Yang akan dilakukan berbeda:**
> Dengan melakukan multiple runs (dalam hal ini, pengujian dengan 25 responden), saya dapat menghitung rata-rata, standar deviasi, dan melihat distribusi hasil. Ini mengubah kepercayaan secara fundamental karena kesimpulan tidak lagi didasarkan pada satu titik data, melainkan pada tren yang diamati dari sebuah sampel. Kepercayaan terhadap hasil meningkat karena didukung oleh bukti yang lebih kuat dan terukur.
