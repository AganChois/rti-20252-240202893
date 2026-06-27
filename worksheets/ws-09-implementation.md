# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : ____________________
  RAM     : ____________________
  GPU     : ____________________
  Storage : ____________________

Software:
  OS        : ____________________
  Runtime   : ____________________
  Framework : ____________________

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
|         |         |        |               |
|         |         |        |               |

Konfigurasi:
  Config file     : ____________________
  Random seed     : ____________________
  Hyperparameters : ____________________

Reproducibility Check:
  [ ] Dependency terdokumentasi (requirements.txt / lock file)
  [ ] Seed ditetapkan di semua level (Python, NumPy, framework)
  [ ] Config di version control
  [ ] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel Core i5-10400F |
| RAM | 16 GB DDR4 |
| GPU | CPU-only |
| OS | Windows 11 |
| Runtime | PHP 8.1, Node.js 18.x |
| Framework | Laravel 9.x, Vue.js 3.x |
| Random Seed | Tidak berlaku untuk eksekusi sistem utama, namun urutan pertanyaan dalam kuesioner dibuat konsisten untuk semua responden. |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| laravel/framework | 9.52.16 | Core framework untuk membangun aplikasi web. |
| mysql | 8.0 | Database untuk menyimpan data produk, pengguna, dan transaksi. |
| vite | 4.0 | Frontend build tool untuk kompilasi aset (CSS, JS). |
| vue | 3.2.37 | Framework JavaScript untuk membangun antarmuka pengguna interaktif. |
| composer | 2.5.8 | Manajer dependensi untuk library PHP. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | | | [ ] Ya / [ ] Tidak |
| 2 | | | [ ] Ya / [ ] Tidak |
> Karena eksperimen melibatkan interaksi manusia (kuesioner), repeatability test difokuskan pada aspek teknis sistem. Tes otomatis menggunakan browser (misal: Selenium/Cypress) akan dijalankan untuk memastikan perilaku sistem konsisten.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | Database di-reset | Waktu eksekusi skrip otomatis (detik) | [ ] Ya / [✓] Tidak |
| 2 | Database di-reset | Waktu eksekusi skrip otomatis (detik) | [ ] Ya / [✓] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**

> Penyebab umum non-repeatability:
> - **Thermal throttling** — CPU/GPU overheating pada run berturut-turut → clock speed turun → waktu eksekusi berubah
> - **Background process** — antivirus scan, update OS, atau cloud sync aktif saat run berlangsung
> - **Cache dari run sebelumnya** — hasil tersimpan di memori/disk sehingga run berikutnya tidak menjalankan komputasi penuh
> - **Random state tidak dikontrol di semua level** — Python seed di-set, tapi NumPy/PyTorch/TensorFlow punya seed independen

**Cache aplikasi dan database:** Run pertama mungkin lebih lambat karena query belum di-cache oleh database atau view belum di-compile oleh Laravel.
-**Proses latar belakang OS:** Aktivitas lain di komputer (misalnya, update, antivirus) dapat memengaruhi performa secara tidak konsisten.
Hasil waktu eksekusi tidak akan identik 100% karena jitter pada OS dan jaringan, namun perbedaannya harus sangat kecil (<5%). Penyebab utama variasi adalah:
1.  **Caching (Aplikasi & Database):** Run pertama bisa lebih lambat. Mitigasinya adalah membersihkan cache (`php artisan cache:clear`) dan me-restart service database sebelum setiap run.
2.  **Proses Latar Belakang OS:** Antivirus atau proses update dapat berjalan tiba-tiba. Mitigasinya adalah meminimalkan aplikasi lain yang berjalan selama pengujian.

**Checklist kontrol yang sudah diterapkan:**
- [✓] Random seed di-set di semua level (tidak relevan untuk kasus ini)
- [✓] Tidak ada background process yang mengganggu (diminimalkan secara manual)
- [✓] Cache dibersihkan antar-run (dengan `php artisan cache:clear`)
- [✓] Config file yang sama untuk semua run (file `.env` tidak diubah)

---

