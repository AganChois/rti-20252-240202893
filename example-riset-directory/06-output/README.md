# 06-output

Hasil olahan data, statistik, dan visualisasi dari analisis data kuesioner.

Dihasilkan oleh skrip di `05-kode/analysis/` dari data mentah di `04-data/hasil-kuesioner-mentah.csv`.

## tables/

| File | Isi |
|---|---|
| `descriptive_stats.csv` | Statistik deskriptif (mean, median, std) untuk setiap 8 karakteristik kualitas ISO 25010. |

## text/

| File | Isi |
|---|---|
| `hasil-uji-hipotesis.txt` | Ringkasan hasil dan kesimpulan dari uji hipotesis (One-Sample T-test) untuk skor usability. |

## figures/

*(Direktori ini akan berisi visualisasi data, seperti bar chart skor rata-rata kualitas atau box plot untuk distribusi skor usability).*

## Acuan

- Skrip Analisis: `../05-kode/analysis/analisis-data-kuesioner.py`
- Data Mentah: `../04-data/hasil-kuesioner-mentah.csv`
