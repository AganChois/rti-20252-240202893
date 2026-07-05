# Tahap 4 — Ekstraksi Data & Visualisasi

**Status:** Selesai — analisis statistik dan interpretasi telah dilakukan.
**Bergantung pada:** [tahap-3-pengujian-k6.md](tahap-3-pengujian-k6.md)
**Lokasi output:** [../06-output/](../06-output/)
**Lokasi skrip analisis:** [../05-kode/analysis/](../05-kode/analysis/)

---

## Tujuan

Mengolah, menganalisis, dan memvisualisasikan data mentah dari 400 run eksperimen (Tahap 3) untuk menguji hipotesis dan menjawab pertanyaan penelitian secara kuantitatif. Tujuannya adalah untuk membandingkan efektivitas dan dampak performa dari mode `hybrid` (mitigasi) versus `none` (baseline).

## Deliverable

- [x] **Skrip Pengolahan Data:** Skrip Python (`run_all.py`) untuk secara otomatis mem-parsing semua 400 folder output dari Tahap 3, mengekstrak metrik relevan, dan menggabungkannya ke dalam satu dataset yang bersih.
- [x] **Ekstraksi Metrik:** Mengekstrak metrik-metrik kunci dari file `k6-summary.json`, `gateway-metrics-*.txt`, dan `resources.csv`:
    - **Metrik Performa (k6):** `http_req_duration` (p95, avg), `http_req_failed` (rate).
    - **Metrik Efektivitas Mitigasi (Gateway):** `jwksgw_db_queries_total`, `jwksgw_cache_requests_total` (hit, miss), `jwksgw_rate_limit_blocked_total`.
    - **Metrik Konsumsi Sumber Daya (Docker Stats):** `cpu_pct` (avg, max), `mem_usage` (avg, max) untuk kontainer `gateway`.
- [x] **Statistik Deskriptif:** Menghitung statistik agregat (mean, std. dev, median) untuk setiap metrik, dikelompokkan berdasarkan `cache_mode` dan `traffic_variant`.
- [x] **Visualisasi Data:** Membuat grafik untuk menyajikan perbandingan secara visual, disimpan di `06-output/figures/`:
    - Box plot untuk durasi request (p95).
    - Bar chart untuk tingkat kegagalan request.
    - Bar chart untuk jumlah query database.
    - Bar chart untuk penggunaan CPU rata-rata.
- [x] **Tabel Hasil:** Menghasilkan tabel ringkasan statistik dalam format CSV, disimpan di `06-output/tables/`, untuk digunakan langsung dalam naskah.
- [x] **Interpretasi Hasil:** Menganalisis hasil statistik dan visual untuk menarik kesimpulan tentang efektivitas solusi `hybrid`.

## Hasil Utama

Analisis data dari 400 run menunjukkan hasil yang signifikan:

1.  **Reduksi Query Database:** Pada skenario serangan (`attack-pool` & `attack-unique`), mode `hybrid` berhasil mengurangi jumlah query ke database hingga **>99%** dibandingkan mode `none`, berkat *negative caching* dan *rate limiting*.
2.  **Stabilitas Performa (Durasi Request):**
    - Di bawah serangan, p95 durasi request untuk *traffic legitimate* pada mode `hybrid` tetap stabil dan rendah (mirip dengan kondisi tanpa serangan).
    - Sebaliknya, pada mode `none`, durasi request untuk semua traffic melonjak drastis saat diserang, menunjukkan degradasi layanan.
3.  **Tingkat Kegagalan (Error Rate):**
    - Mode `none` mengalami tingkat kegagalan request yang tinggi di bawah serangan karena *resource exhaustion*.
    - Mode `hybrid` berhasil menjaga tingkat kegagalan tetap 0% untuk *traffic legitimate* dan secara efektif memblokir traffic serangan (tercatat sebagai `http_req_failed` di k6 karena respons `401`/`429`, sesuai desain).
4.  **Efisiensi Sumber Daya (CPU):** Penggunaan CPU pada kontainer gateway di mode `hybrid` jauh lebih rendah dan stabil selama serangan dibandingkan mode `none` yang mengalami lonjakan CPU hingga saturasi.

Kesimpulan: Analisis data secara kuantitatif membuktikan bahwa arsitektur `hybrid cache` secara efektif memitigasi serangan JWKS Endpoint Flooding, melindungi database, dan menjaga kualitas layanan untuk pengguna yang sah. Seluruh output analisis (tabel dan gambar) telah disimpan di folder `06-output/` dan siap untuk dimasukkan ke dalam naskah penelitian.
