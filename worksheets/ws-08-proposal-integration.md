# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [ ] Problem → Gap: masalah terdokumentasi di literatur
  [ ] Gap → RQ: pertanyaan menjawab gap spesifik
  [ ] RQ → Hypothesis: hipotesis memprediksi jawaban
  [ ] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [ ] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [ ] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [ ] Istilah sama di semua bagian
  [ ] Variabel di RQ = variabel di hipotesis = metrik di desain
  [ ] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [ ] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [ ] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [ ] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [ ] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [ ] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        |      |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   |      |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail |      |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Kurangnya sistem monitoring kualitas air limbah rumah tangga yang real-time dan terjangkau menyebabkan keterlambatan deteksi pencemaran, yang berisiko bagi lingkungan. |
| Gap | WS-03 | Studi yang ada cenderung fokus pada skala industri atau sungai, dan belum ada yang spesifik menguji sistem untuk konteks limbah rumah tangga dengan biaya terjangkau (Method & Context Gap). |
| RQ | WS-04 | Apakah sistem monitoring kualitas air berbasis IoT yang dirancang dengan sensor berbiaya rendah (pH, TDS, Suhu) mampu mendeteksi anomali kualitas air limbah rumah tangga dengan akurasi ≥90% dibandingkan hasil uji laboratorium? |
| Hipotesis | WS-04 | H₁: Sistem monitoring kualitas air berbasis IoT dengan sensor berbiaya rendah mampu mendeteksi anomali kualitas air limbah rumah tangga dengan akurasi ≥90%. |
| Variabel & Metrik | WS-05 | IV: Konfigurasi sistem IoT. DV: Akurasi deteksi anomali (%), diukur dengan membandingkan pembacaan sensor dengan hasil uji laboratorium (gold standard). CV: Sampel air limbah, kondisi lingkungan. |
| Sistem | WS-06 | Sistem terdiri dari node sensor (ESP32, sensor pH, TDS, Suhu), gateway, dan backend/dashboard. Komponen pengukuran (DV) adalah modul analisis yang membandingkan data sensor dengan data lab. |
| Desain Eksperimen | WS-07 | Desain eksperimen perbandingan (Comparison) antara data yang dihasilkan oleh sistem IoT (treatment) dengan data hasil uji laboratorium (kontrol/gold standard) pada sampel air yang sama. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Masalah kurangnya sistem monitoring di level rumah tangga didukung oleh analisis literatur di WS-03 yang menunjukkan fokus riset pada konteks industri/sungai. |
| Gap → RQ | ✅ | RQ secara langsung bertujuan untuk menjawab gap dengan menguji kelayakan sistem berbiaya rendah pada konteks rumah tangga yang belum banyak dieksplorasi. |
| RQ → Hypothesis | ✅ | Hipotesis secara langsung memberikan prediksi terukur (akurasi ≥90%) sebagai jawaban yang diharapkan untuk RQ. |
| Hypothesis → Metric | ✅ | Hipotesis tentang "akurasi ≥90%" secara eksplisit mendefinisikan metrik utama (Akurasi deteksi anomali) yang akan diukur seperti yang didefinisikan di WS-05. |
| Metric → System | ✅ | Metrik akurasi (DV) diukur dengan membandingkan output sistem IoT dengan data eksternal (lab), di mana sistem IoT adalah artefak utama yang dibangun (WS-06). |
| System → Experiment | ✅ | Desain eksperimen di WS-07 secara eksplisit menggunakan data dari sistem yang dibangun sebagai kondisi "treatment" untuk divalidasi terhadap "kontrol" (uji lab). |

**Koneksi mana yang paling lemah?** Tidak ada koneksi yang secara fundamental lemah.
**Bagaimana cara memperkuatnya?**
> Semua koneksi sudah membentuk alur yang logis. Penguatan bisa dilakukan pada detail, misalnya dengan memperjelas justifikasi pemilihan threshold akurasi 90% pada hipotesis.

> Jika tidak, di bagian mana terjadi inkonsistensi? _________
**Konsistensi horizontal — apakah istilah dan scope konsisten?** [✓] Ya
> Jika tidak, di bagian mana terjadi inkonsistensi? Istilah kunci seperti "sistem monitoring IoT", "kualitas air", "akurasi", dan "konteks rumah tangga" digunakan secara konsisten di semua bagian.

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Semua 6 koneksi vertikal terhubung dengan baik, membentuk argumen "benang merah" yang utuh dari masalah hingga desain eksperimen. |
| Specificity | 3 | Metrik utama (akurasi deteksi anomali) dan threshold keberhasilan (≥90%) sudah terdefinisi secara numerik dan jelas. |
| Feasibility | 2 | Lingkup (membangun prototipe IoT dan melakukan uji lab) terdengar realistis untuk 3-6 bulan, namun membutuhkan akses ke laboratorium pengujian air yang mungkin menjadi kendala. |
| Rigor | 2 | Baseline sudah sangat kuat (uji laboratorium sebagai gold standard), namun justifikasi pemilihan sensor spesifik (misalnya tipe sensor pH/TDS) dibandingkan alternatif lain belum dijelaskan secara mendalam. |

**Skor total:** 10 / 12

**Apakah proposal siap untuk fase eksekusi?** [✓] Ya
> Jika belum, apa yang perlu diperbaiki? Proposal secara fundamental sudah solid. Langkah berikutnya adalah memastikan ketersediaan sumber daya (akses lab, komponen sensor) dan membuat rencana implementasi serta eksekusi yang detail.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mengidentifikasi masalah dan gap awal (WS-02 & WS-03), karena isunya cukup nyata dan didukung oleh observasi umum serta tinjauan literatur awal.
**Bagian tersulit:** Merumuskan Research Question (RQ) yang spesifik, terukur, dan benar-benar bisa diuji (WS-04). Mengubah masalah umum menjadi pertanyaan riset yang tajam membutuhkan beberapa kali iterasi.
**Yang akan dilakukan berbeda:**

> Jika mengulang dari awal, saya akan menghabiskan lebih banyak waktu di WS-04 untuk memastikan RQ sudah benar-benar solid sebelum melanjutkan ke metodologi. Ini akan mencegah "problem drift" dan memastikan semua bagian metodologi (WS-05 hingga WS-07) langsung selaras sejak awal.
