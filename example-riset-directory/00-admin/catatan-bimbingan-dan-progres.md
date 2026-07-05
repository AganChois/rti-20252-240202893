# Catatan Bimbingan & Progres Penelitian

Dokumen ini merangkum catatan dari sesi bimbingan dan progres penelitian, disarikan dari hasil kerja pada *worksheet* metodologi penelitian.

---

## Sesi 1: Finalisasi Proposal & Kesiapan Eksekusi

**Tanggal:** (diasumsikan setelah WS-08)
**Agenda:** Review integrasi proposal penelitian.
**Referensi:** `ws-08-proposal-integration.md`

### Poin Diskusi:
1.  **Koherensi Proposal:** Proposal mini menunjukkan alur argumen yang solid. Keenam koneksi kritis (Problem → Gap → RQ → Hipotesis → Metrik → Sistem → Eksperimen) telah terverifikasi dan terhubung dengan baik.
2.  **Kesiapan Metodologi:** Metodologi telah dirancang secara spesifik untuk menjawab RQ. Metrik utama (akurasi deteksi anomali ≥90%) sudah terdefinisi secara kuantitatif.
3.  **Penilaian Mandiri:** Skor *self-assessment* (10/12) mengindikasikan proposal memiliki koherensi dan spesifisitas yang tinggi.
4.  **Risiko & Feasibility:** Risiko utama yang teridentifikasi adalah ketersediaan akses ke laboratorium pengujian air untuk validasi *gold standard*.

### Tindak Lanjut:
- [x] Memastikan ketersediaan sumber daya (akses lab, komponen sensor) sebelum memulai fase implementasi.
- [ ] Membuat rencana implementasi detail berdasarkan `ws-09-implementation.md`.

---

## Sesi 2: Validasi Data Hasil Eksperimen

**Tanggal:** (diasumsikan setelah WS-11)
**Agenda:** Review kelengkapan dan integritas data mentah.
**Referensi:** `ws-09-implementation.md`, `ws-11-data-validation.md`

### Poin Diskusi:
1.  **Reproducibility Lingkungan:** Implementasi telah dilakukan dengan memperhatikan kontrol lingkungan (spesifikasi hardware/software, versi dependensi di-lock) sesuai panduan `ws-09`.
2.  **Kelengkapan Data:** Data berhasil dikumpulkan dari 24 dari 25 responden yang direncanakan (tingkat kelengkapan 96%).
3.  **Integritas & Anomali:** Satu *outlier* statistik terdeteksi pada metrik `Usability_Score` (nilai 35%). Investigasi menunjukkan tidak ada kesalahan teknis, sehingga *outlier* dianggap sebagai data valid.

### Tindak Lanjut:
- [x] Melanjutkan ke tahap analisis data.
- [x] Saat menganalisis, laporkan median selain mean untuk metrik `Usability_Score` untuk menunjukkan tendensi sentral yang tidak terlalu terpengaruh oleh *outlier*.
- [x] Anomali dan keputusan penanganannya wajib didokumentasikan pada laporan akhir.

---

## Sesi 3: Penulisan Naskah Ilmiah

**Tanggal:** (diasumsikan setelah WS-15)
**Agenda:** Review struktur dan kualitas penulisan naskah.
**Referensi:** `ws-15-scientific-writing.md`

### Poin Diskusi:
1.  **Struktur Argumen:** Penulisan naskah mengikuti alur IMRAD untuk membangun argumen riset yang utuh.
2.  **Konsistensi Internal:** *Consistency matrix* digunakan untuk memastikan RQ, hipotesis, dan kontribusi terjawab secara konsisten di seluruh bagian naskah.
3.  **Kualitas Penulisan:** Fokus pada tiga pilar: *Clarity* (kejelasan), *Precision* (ketepatan), dan *Conciseness* (keringkasan), seperti contoh perbaikan paragraf hasil usability.

### Tindak Lanjut:
- [x] Terapkan perbaikan kualitas penulisan secara konsisten di seluruh bagian naskah.
- [ ] Finalisasi draf naskah untuk review internal sebelum memilih jurnal tujuan.