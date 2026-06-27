# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [ ] Semua skenario tercakup
  [ ] Jumlah run sesuai rencana
  [ ] Tidak ada file output hilang
  Missing: ____ dari ____ data points

Format Consistency:
  [ ] Semua file format sama (CSV/JSON/...)
  [ ] Header konsisten
  [ ] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [ ] Nilai dalam range masuk akal
  [ ] Tidak ada waktu negatif
  [ ] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: ____________________

Cross-Validation:
  [ ] Run identik → hasil mendekati
  [ ] Trend konsisten dengan ekspektasi teori

Keputusan:
  [ ] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Evaluasi Sistem Web v1.0 | 25 | 24 | 1 | Satu responden tidak menyelesaikan pengisian kuesioner hingga akhir. |

**Total expected:** 25 | **Total actual:** 24 | **Missing:** 1

**Keputusan untuk data missing:**
> Data dari responden yang tidak lengkap tidak akan diikutsertakan dalam analisis kuantitatif (perhitungan skor rata-rata). Namun, feedback kualitatif parsial yang mungkin sudah diberikan akan tetap dicatat sebagai data observasi.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (data `Usability_Score` dari 7 responden):**

| Run | Usability_Score (%) |
|-----|-------------|
| resp-001 | 88 |
| resp-002 | 92 |
| resp-003 | 85 |
| resp-004 | 95 |
| resp-005 | 35 |
| resp-006 | 90 |
| resp-007 | 87 |

**Deteksi outlier:**
- Data terurut: `[35, 85, 87, 88, 90, 92, 95]`
- Q1 = 85 | Q3 = 92 | IQR = 7
- Batas bawah (Q1 - 1.5×IQR) = 74.5
- Batas atas (Q3 + 1.5×IQR) = 102.5
- Outlier terdeteksi: `35` (karena < 74.5)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| resp-005 | 35% | Sesuai protokol di WS-10: bisa jadi responden mengalami kesulitan teknis, salah paham instruksi, atau ini adalah feedback asli yang sangat negatif. | Data tidak dihapus. Periksa feedback kualitatif dari `resp-005` untuk konteks. Laporkan median sebagai tambahan dari mean dalam analisis untuk mengurangi dampak outlier. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 96% data terkumpul (24 dari 25 responden).
**2. Format:** [✓] Konsisten. Semua data dari database diekspor ke CSV dengan skema kolom yang sama.
**3. Range check (anomali):** Satu outlier terdeteksi pada `Usability_Score` (nilai 35%, di luar batas bawah IQR). Metrik lain (`Functionality_Score`, `Task_Completion_Time_s`) berada dalam range yang valid.
**4. Logic check:** [✓] Parameter sesuai plan. Semua data tercatat menggunakan `System_Version: v1.0` dan `Instrument_Version: Kuesioner ISO 25010 v1`.

**Kesimpulan:** [✓] Data siap dianalisis, dengan catatan untuk menangani 1 record yang hilang dan 1 outlier selama analisis sesuai keputusan yang telah dibuat.

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

**Data yang benar (correct data)** adalah data yang valid secara format dan tipe, misalnya skor adalah angka numerik dalam rentang 0-100. **Data yang dipercaya (trusted data)** adalah data yang tidak hanya benar, tetapi juga telah melewati serangkaian pemeriksaan (kelengkapan, konsistensi, anomali) dan diyakini secara akurat merepresentasikan fenomena yang diukur.

Proses validasi formal tetap diperlukan karena pengumpulan otomatis tidak kebal terhadap error. Bug pada kode logger, masalah koneksi jaringan, atau kondisi tak terduga di sisi klien (misalnya, browser crash) dapat menghasilkan data yang "benar" secara format tetapi tidak "dipercaya" secara kontekstual. Validasi adalah jaring pengaman untuk memastikan integritas data sebelum menarik kesimpulan.
