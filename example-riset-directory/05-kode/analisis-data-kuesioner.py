import pandas as pd
from scipy import stats
import numpy as np

# Path ke file data mentah
DATA_FILE_PATH = '../04-data/hasil-kuesioner-mentah.csv'

def analyze_data(file_path):
    """
    Membaca data kuesioner, menghitung statistik deskriptif,
    dan melakukan uji hipotesis.
    """
    try:
        # 1. Membaca data dari file CSV
        df = pd.read_csv(file_path)
        print("Analisis Data Kuesioner Kualitas Sistem")
        print("="*40)
        print(f"Data berhasil dibaca dari: {file_path}")
        print(f"Jumlah responden: {len(df)}")
        print("-" * 40)

        # 2. Menghitung Statistik Deskriptif
        # Mengambil kolom-kolom metrik kualitas
        quality_metrics = df.columns.drop('respondent_id')
        
        print("Statistik Deskriptif Skor Kualitas (0-100):")
        
        # Menghitung mean, median, dan std dev untuk setiap metrik
        descriptive_stats = df[quality_metrics].agg(['mean', 'median', 'std']).round(2)
        
        print(descriptive_stats)
        print("-" * 40)
        
        # Catatan khusus untuk Usability karena adanya outlier
        usability_mean = descriptive_stats.loc['mean', 'usability']
        usability_median = descriptive_stats.loc['median', 'usability']
        print(f"Catatan: Skor 'usability' memiliki outlier. Mean ({usability_mean}) "
              f"terpengaruh, sedangkan Median ({usability_median}) lebih representatif.")
        print("-" * 40)

        # 3. Uji Hipotesis untuk Usability
        # H0: Rata-rata skor usability <= 70
        # H1: Rata-rata skor usability > 70 (one-tailed test)
        print("Uji Hipotesis: Skor Rata-rata Usability > 70%")
        
        usability_scores = df['usability']
        population_mean = 70
        
        # Melakukan One-Sample T-test
        t_statistic, p_value = stats.ttest_1samp(
            a=usability_scores,
            popmean=population_mean,
            alternative='greater'  # Menguji apakah rata-rata sampel > popmean
        )
        
        print(f"Skor rata-rata (Mean): {usability_scores.mean():.2f}")
        print(f"T-statistic: {t_statistic:.3f}")
        print(f"P-value (one-tailed): {p_value:.4f}")
        
        # Interpretasi hasil
        alpha = 0.05
        if p_value < alpha:
            print(f"\nKesimpulan: Karena p-value ({p_value:.4f}) < {alpha}, kita menolak hipotesis nol (H0).")
            print("Terdapat bukti statistik yang signifikan untuk menyatakan bahwa skor rata-rata usability lebih tinggi dari 70%.")
        else:
            print(f"\nKesimpulan: Karena p-value ({p_value:.4f}) >= {alpha}, kita gagal menolak hipotesis nol (H0).")
            print("Tidak terdapat bukti statistik yang cukup untuk menyatakan bahwa skor rata-rata usability lebih tinggi dari 70%.")
            
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di path '{file_path}'.")
        print("Pastikan file 'hasil-kuesioner-mentah.csv' ada di direktori '04-data'.")
    except Exception as e:
        print(f"Terjadi error saat analisis: {e}")

if __name__ == "__main__":
    analyze_data(DATA_FILE_PATH)