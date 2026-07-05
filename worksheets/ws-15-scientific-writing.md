# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : ____________________
Target  : [ ] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [ ] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [ ] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [ ] Related Work — concept-centric, gap positioning
  [ ] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [ ] Results — tabel + grafik + observasi (tanpa interpretasi)
  [ ] Discussion — interpretasi, perbandingan, implikasi, limitation
  [ ] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [ ] RQ di Introduction = RQ di Method = RQ di Conclusion
  [ ] Variabel di Method = variabel di Results
  [ ] Klaim di Discussion didukung data di Results
  [ ] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [ ] Clarity — mudah dipahami tanpa re-read
  [ ] Precision — tidak ada istilah ambigu
  [ ] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Sistem pemasaran pertanian berbasis web banyak dikembangkan, namun evaluasi kualitasnya seringkali tidak terstandar. Penelitian ini menerapkan metode prototyping untuk membangun sistem dan mengevaluasinya menggunakan standar ISO 25010 dengan 24 responden. Hasil menunjukkan skor usability rata-rata 88.1%, yang secara signifikan melampaui ambang batas kelayakan 70%, membuktikan bahwa metode prototyping efektif untuk menghasilkan sistem berkualitas tinggi. | 200-250 |
| Introduction | Digitalisasi pemasaran pertanian penting, namun banyak sistem yang ada tidak dievaluasi secara sistematis. Terdapat kesenjangan (gap) dalam penerapan standar kualitas seperti ISO 25010 pada konteks ini. RQ: Bagaimana kualitas sistem pemasaran pertanian berbasis web yang dikembangkan dengan metode prototyping berdasarkan standar ISO 25010? | 500-700 |
| Related Work | Meringkas studi sebelumnya tentang sistem informasi pertanian (misal: Tandirerung et al., 2020), penggunaan metode prototyping dalam pengembangan sistem, dan penerapan standar ISO untuk evaluasi perangkat lunak. Memposisikan riset ini sebagai yang pertama menggabungkan ketiganya dalam konteks pemasaran pertanian. | 700-1000 |
| Method | Menjelaskan desain sistem (WS-06), proses pengembangan dengan prototyping, desain eksperimen (WS-07) dengan 24 responden, instrumen kuesioner berbasis ISO 25010 (WS-05), dan prosedur pengumpulan data (WS-10). Menyebutkan rencana analisis statistik (One-Sample t-test) (WS-14). | 800-1200 |
| Results | Menyajikan data demografi responden dan statistik deskriptif skor kualitas (Functionality, Usability, dll.) dalam bentuk tabel (WS-12). Menampilkan hasil uji hipotesis (p=0.001, Cohen's d=2.1) dan visualisasi utama seperti bar chart skor kualitas (WS-12). | 500-800 |
| Discussion | Menginterpretasikan hasil: skor usability 88.1% menunjukkan penerimaan pengguna yang sangat baik dan secara praktis signifikan. Membandingkan hasil dengan literatur (skor sebanding dengan Tandirerung et al.). Mendiskusikan implikasi bahwa prototyping adalah metode yang cocok. Mengakui limitasi (sampel kecil, kurang beragam) (WS-14). | 600-900 |
| Conclusion | Menjawab RQ secara langsung: sistem memiliki kualitas yang sangat baik menurut standar ISO 25010. Menyatakan kontribusi utama: validasi empiris metode prototyping untuk domain ini. Memberikan saran untuk penelitian selanjutnya (menguji pada skala lebih besar, menambah fitur). | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

| Elemen | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ Kualitas Sistem | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metode Prototyping (IV) | ✓ | ✓ | ✗ | ✓ | ✓ |
| Kualitas Sistem (DV) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik ISO 25010 | ✓ | ✓ | ✓ | ✓ | ✓ |
| Hipotesis (Usability ≥ 70%) | ✗ | ✓ | ✓ | ✓ | ✓ |
| Kontribusi (Validasi metode) | ✓ | ✗ | ✗ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> 1.  **Hipotesis (Usability ≥ 70%)** tidak disebutkan di Introduction, padahal ini adalah inti dari pengujian kuantitatif.
> 2.  **Kontribusi** (validasi metode prototyping) tidak secara eksplisit terhubung dengan bagian Method dan Result, hanya muncul di awal dan akhir.

**Tindakan perbaikan:**
> 1.  Menambahkan kalimat di akhir Introduction yang menyatakan hipotesis yang akan diuji, yaitu kualitas sistem (khususnya usability) diharapkan melampaui standar kelayakan umum (≥70%).
> 2.  Di bagian Discussion, secara eksplisit hubungkan hasil (skor tinggi) dengan metode yang digunakan (prototyping) untuk memperkuat argumen bahwa metode tersebut berkontribusi pada hasil yang baik.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Hasil pengujian usability menunjukkan skor yang sangat bagus. Rata-rata skor yang didapat dari responden adalah 88.1%. Angka ini menunjukkan bahwa sistem yang dibuat sangat bisa diterima oleh pengguna dan mudah untuk digunakan. Hasil ini juga signifikan.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | "Sangat bagus" dan "sangat bisa diterima" adalah frasa subjektif dan tidak informatif. | Ganti dengan interpretasi yang lebih konkret terkait persepsi pengguna (efektif, efisien, memuaskan). |
| Precision | "Signifikan" adalah istilah ambigu. Harus dijelaskan apakah signifikan secara statistik (dengan p-value) atau praktis (dengan effect size). | Tambahkan nilai p-value, standar deviasi (SD), dan Cohen's d untuk memberikan makna yang presisi. |
| Conciseness | Kalimat "Angka ini menunjukkan bahwa..." dapat digabung dengan kalimat sebelumnya untuk alur yang lebih padat. | Gabungkan beberapa kalimat menjadi satu alur argumen yang ringkas. |

**Paragraf setelah perbaikan:**
> Sistem mencapai skor usability rata-rata 88.1% (SD = 8.5). Hasil ini tidak hanya secara statistik signifikan lebih tinggi dari ambang batas kelayakan 70% (p = 0.001), tetapi juga menunjukkan effect size yang sangat besar (Cohen's d = 2.1). Skor ini mengindikasikan bahwa sistem dinilai sangat efektif, efisien, dan memuaskan oleh pengguna target, serta sebanding dengan temuan pada studi relevan sebelumnya.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis **"tentang" riset** bersifat deskriptif, seperti melaporkan kronologi ("pertama kami melakukan A, lalu kami menemukan B"). Sebaliknya, menulis sebagai **"argumen" riset** bersifat persuasif; setiap bagian (Introduction, Method, Results, Discussion) disusun secara logis untuk membangun sebuah klaim utama (kontribusi). Paper menjadi satu kesatuan argumen yang koheren, bukan sekadar kumpulan fakta.
> Urutan penulisan **Method → Discussion → Introduction** secara drastis meningkatkan kualitas tulisan karena memastikan argumen dibangun di atas fondasi yang kokoh. Menulis Method dan Results terlebih dahulu memaksa kita untuk berpegang pada fakta konkret. Berdasarkan fakta tersebut, Discussion dapat menginterpretasi makna dan implikasinya secara mendalam. Terakhir, Introduction ditulis untuk membingkai "cerita" yang paling sesuai dengan temuan yang ada, memastikan tidak ada klaim berlebihan dan "benang merah" dari masalah hingga kesimpulan terjaga dengan sempurna.
