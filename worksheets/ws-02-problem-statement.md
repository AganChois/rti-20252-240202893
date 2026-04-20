# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Internet of Things (IoT) & Lingkungan
  Konteks  : Monitoring kualitas air limbah rumah tangga secara real-time


System Context
  Input       : Data sensor (pH, suhu, kekeruhan, COD, BOD)
  Process     : Pengambilan data sensor, pengolahan data, dan pengiriman ke sistem monitoring
  Output      : Informasi kualitas air dalam bentuk dashboard
  Outcome     : Peningkatan kontrol terhadap pencemaran air
  Constraints : Keterbatasan biaya, akurasi sensor, konektivitas internet
  Stakeholders: Masyarakat, pemerintah, pengelola limbah, peneliti

Fenomena → Problem
  Fenomena yang diamati             : Banyak limbah rumah tangga dibuang tanpa monitoring kualitas air
  Gejala (symptom) yang terukur     : Tingginya nilai COD/BOD di saluran air
  Masalah yang didiagnosis          : Tidak adanya sistem monitoring kualitas air secara real-time dan terjangkau
  Masalah riset (researchable)      : Bagaimana merancang sistem IoT murah yang mampu memonitor kualitas air limbah secara akurat dan real-time?
  Variabel yang terukur             : pH, suhu, kekeruhan, COD, BOD, latency sistem, akurasi sensor

Problem Quality Check
  [✓] Clarity — Apakah satu orang membaca akan paham?
  [✓] Measurability — Apakah ada metrik kuantitatif?
  [✓] Relevance — Apakah penting untuk domain?
  [✓] Testability — Apakah bisa gagal?
  [✓] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Kurangnya sistem monitoring kualitas air limbah rumah tangga secara real-time menyebabkan sulit mendeteksi pencemaran sejak awal, yang ditunjukkan oleh tingginya nilai parameter seperti COD dan BOD di lingkungan perairan. Penelitian ini bertujuan untuk merancang dan mengevaluasi sistem berbasis IoT yang mampu memonitor kualitas air secara akurat, real-time, dan dengan biaya terjangkau. Sistem ini diharapkan dapat memberikan informasi yang relevan bagi masyarakat dan pemangku kepentingan untuk mengurangi dampak pencemaran air.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Sistem IoT untuk Monitoring Kualitas Air Limbah

| Tahap | Hasil |
|-------|-------|
| Reality | Limbah rumah tangga dibuang ke lingkungan tanpa pemantauan kualitas air secara rutin |
| Observed Issue (Symptom) | Nilai parameter kualitas air (COD, BOD, pH) sering melebihi ambang batas, namun tidak terdeteksi secara cepat |
| Diagnosed Problem (Root Cause) |Tidak adanya sistem monitoring real-time yang terjangkau serta keterbatasan alat ukur konvensional |
| Researchable Problem |Bagaimana merancang dan mengevaluasi sistem IoT yang mampu memonitor kualitas air limbah secara real-time dengan biaya terjangkau dan akurasi yang memadai?|
| Measurable Variable |pH, suhu, kekeruhan, COD, BOD, akurasi sensor (%), delay pengiriman data (detik) |

**Apakah terjebak solution-first thinking?** Tidak

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data dari sensor kualitas air (pH, suhu, kekeruhan, COD, BOD) yang dikumpulkan secara periodik |
| Process | Akuisisi data sensor → filtering/noise reduction → pengiriman data melalui jaringan (WiFi/LoRa) → penyimpanan dan analisis di server/cloud|
| Output | Informasi kualitas air dalam bentuk dashboard (grafik, status aman/tidak)|
| Outcome | Deteksi dini pencemaran air dan peningkatan pengambilan keputusan untuk pengolahan limbah|
| Constraints | Keterbatasan akurasi sensor, biaya perangkat, kestabilan koneksi internet, konsumsi daya|
| Stakeholders | Masyarakat, pemerintah, pengelola limbah, peneliti, industri kecil|

**Komponen mana yang paling relevan dengan masalah riset?** Process
---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 3 | Sudah jelas menjelaskan masalah dan tujuan, namun masih bisa dipertegas pada konteks lingkungan spesifik (misalnya rumah tangga atau industri kecil)|
| Measurability | 3|variable cukup terukur (pH, COD, BOD, akurasi sensor, delay) dan dapat diuji secara kuantitatif |
| Relevance | 4| cukup relevan dengan isu lingkungan dan kebutuhan monitoring limbah yang meningkat|
| Testability | 4| Dapat diuji melalui implementasi sistem IoT dan pengujian performa sensor serta sistem|
| Impact | 3| Memberikan dampak nyata, namun masih bisa ditingkatkan dengan menambahkan aspek skalabilitas atau implementasi luas|

**Skor total:** 17 / 25

**Problem statement versi final (1 paragraf):**
Kurangnya sistem monitoring kualitas air limbah secara real-time pada lingkungan rumah tangga menyebabkan keterlambatan dalam mendeteksi pencemaran, yang ditunjukkan oleh tingginya parameter seperti COD, BOD, dan ketidakseimbangan pH. ini bertujuan untuk merancang sistem berbasis IoT yang mampu memonitor kualitas air secara real-time dengan tingkat akurasi yang memadai dan biaya yang terjangkau. Sistem ini diharapkan dapat memberikan informasi yang cepat dan akurat untuk mendukung pengambilan keputusan dalam pengelolaan limbah serta mengurangi dampak pencemaran lingkungan.
---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
Masalah coding itu jelas , biasanya ada error dan bisa langsung diperbaiki.
Masalah riset lebih kompleks dan tidak selalu jelas, harus dianalisis dulu penyebabnya.
