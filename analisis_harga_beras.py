import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Set style untuk visualisasi
plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)

# Membaca data
print("Membaca data...")
df = pd.read_excel("harga_pertanian_fix.xlsx")

# Filter data untuk beras saja
beras_data = df[df['kategori_utama'] == 'BERAS'].copy()

# Filter untuk beras medium dan premium
beras_medium = beras_data[beras_data['kategori'] == 'BERAS MEDIUM'].copy()
beras_premium = beras_data[beras_data['kategori'] == 'BERAS PREMIUM'].copy()

print(f"\nJumlah data BERAS: {len(beras_data)}")
print(f"Jumlah data BERAS MEDIUM: {len(beras_medium)}")
print(f"Jumlah data BERAS PREMIUM: {len(beras_premium)}")

# Menampilkan rentang tahun
tahun_min = df['tahun'].min()
tahun_max = df['tahun'].max()
print(f"\nRentang tahun: {tahun_min} - {tahun_max}")

# 1. RATA-RATA HARGA BERAS MEDIUM PER TAHUN
print("\n" + "="*60)
print("1. RATA-RATA HARGA BERAS MEDIUM PER TAHUN")
print("="*60)

if len(beras_medium) > 0:
    # Konversi harga dari per ton ke per kg (untuk readability)
    beras_medium['harga_per_kg'] = beras_medium['harga_per_ton'] / 1000

    # Group by tahun dan hitung rata-rata
    rata_rata_medium_tahun = beras_medium.groupby('tahun').agg({
        'harga_per_kg': 'mean',
        'harga_per_ton': 'mean',
        'jumlah': 'mean'
    }).reset_index()

    # Sort by tahun
    rata_rata_medium_tahun = rata_rata_medium_tahun.sort_values('tahun')

    print("\nTabel Rata-rata Harga Beras Medium per Tahun:")
    print("------------------------------------------------")
    print(f"{'Tahun':<6} {'Harga/Kg (Rp)':<15} {'Harga/Ton (Rp)':<15} {'Jumlah Data':<12}")
    print("------------------------------------------------")

    for _, row in rata_rata_medium_tahun.iterrows():
        print(f"{row['tahun']:<6} {row['harga_per_kg']:>13,.0f} {row['harga_per_ton']:>15,.0f} {len(beras_medium[beras_medium['tahun'] == row['tahun']]):>12}")

    # Visualisasi
    plt.figure(figsize=(12, 6))
    plt.plot(rata_rata_medium_tahun['tahun'], rata_rata_medium_tahun['harga_per_kg'],
             marker='o', linewidth=2, markersize=8, color='orange', label='Beras Medium')
    plt.title('Rata-rata Harga Beras Medium per Tahun', fontsize=16, fontweight='bold')
    plt.xlabel('Tahun', fontsize=12)
    plt.ylabel('Harga per Kg (Rp)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rata_rata_medium_tahun['tahun'].astype(int))
    plt.tight_layout()
    plt.savefig('rata_rata_harga_beras_medium_tahun.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n[SELESAI] Grafik rata-rata harga beras medium per tahun tersimpan sebagai 'rata_rata_harga_beras_medium_tahun.png'")
else:
    print("[ERROR] Tidak ada data untuk beras medium")

# 2. HARGA BERAS PREMIUM PER TAHUN
print("\n" + "="*60)
print("2. HARGA BERAS PREMIUM PER TAHUN")
print("="*60)

if len(beras_premium) > 0:
    # Konversi harga dari per ton ke per kg
    beras_premium['harga_per_kg'] = beras_premium['harga_per_ton'] / 1000

    # Group by tahun dan hitung rata-rata
    rata_rata_premium_tahun = beras_premium.groupby('tahun').agg({
        'harga_per_kg': 'mean',
        'harga_per_ton': 'mean',
        'jumlah': 'mean'
    }).reset_index()

    # Sort by tahun
    rata_rata_premium_tahun = rata_rata_premium_tahun.sort_values('tahun')

    print("\nTabel Rata-rata Harga Beras Premium per Tahun:")
    print("------------------------------------------------")
    print(f"{'Tahun':<6} {'Harga/Kg (Rp)':<15} {'Harga/Ton (Rp)':<15} {'Jumlah Data':<12}")
    print("------------------------------------------------")

    for _, row in rata_rata_premium_tahun.iterrows():
        print(f"{row['tahun']:<6} {row['harga_per_kg']:>13,.0f} {row['harga_per_ton']:>15,.0f} {len(beras_premium[beras_premium['tahun'] == row['tahun']]):>12}")

    # Visualisasi
    plt.figure(figsize=(12, 6))
    plt.plot(rata_rata_premium_tahun['tahun'], rata_rata_premium_tahun['harga_per_kg'],
             marker='o', linewidth=2, markersize=8, color='green', label='Beras Premium')
    plt.title('Rata-rata Harga Beras Premium per Tahun', fontsize=16, fontweight='bold')
    plt.xlabel('Tahun', fontsize=12)
    plt.ylabel('Harga per Kg (Rp)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rata_rata_premium_tahun['tahun'].astype(int))
    plt.tight_layout()
    plt.savefig('rata_rata_harga_beras_premium_tahun.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\n[SELESAI] Grafik rata-rata harga beras premium per tahun tersimpan sebagai 'rata_rata_harga_beras_premium_tahun.png'")
else:
    print("[ERROR] Tidak ada data untuk beras premium")

# 3. TOP 10 KABUPATEN DENGAN HARGA BERAS PREMIUM TERTINGGI DALAM 6 TAHUN
print("\n" + "="*60)
print("3. TOP 10 KABUPATEN DENGAN HARGA BERAS PREMIUM TERTINGGI")
print("   DALAM 6 TAHUN TERAKHIR")
print("="*60)

if len(beras_premium) > 0:
    # Filter data untuk 6 tahun terakhir
    tahun_terakhir = df['tahun'].max()
    tahun_6_kebelakang = tahun_terakhir - 5  # 6 tahun termasuk tahun terakhir

    beras_premium_6tahun = beras_premium[beras_premium['tahun'] >= tahun_6_kebelakang].copy()

    print(f"\nData yang dianalisis: tahun {tahun_6_kebelakang} - {tahun_terakhir}")
    print(f"Jumlah data: {len(beras_premium_6tahun)}")

    if len(beras_premium_6tahun) > 0:
        # Group by kabupaten dan hitung rata-rata harga
        rata_rata_kabupaten = beras_premium_6tahun.groupby('nama_kabupaten_kota').agg({
            'harga_per_kg': 'mean',
            'harga_per_ton': 'mean',
            'tahun': ['count', 'min', 'max']
        }).reset_index()

        # Flatten column names
        rata_rata_kabupaten.columns = ['Kabupaten/Kota', 'Rata-rata Harga/Kg', 'Rata-rata Harga/Ton',
                                      'Jumlah Data', 'Tahun Awal', 'Tahun Akhir']

        # Sort by harga descending
        top_10_kabupaten = rata_rata_kabupaten.sort_values('Rata-rata Harga/Kg', ascending=False).head(10)

        print("\nTop 10 Kabupaten/Kota dengan Harga Beras Premium Tertinggi:")
        print("="*70)
        print(f"{'No':<3} {'Kabupaten/Kota':<25} {'Harga/Kg (Rp)':<15} {'Jumlah Data':<12} {'Tahun':<10}")
        print("="*70)

        for idx, (_, row) in enumerate(top_10_kabupaten.iterrows(), 1):
            tahun_range = f"{row['Tahun Awal']}-{row['Tahun Akhir']}"
            print(f"{idx:<3} {row['Kabupaten/Kota'][:24]:<25} {row['Rata-rata Harga/Kg']:>13,.0f} {row['Jumlah Data']:>12} {tahun_range:<10}")

        # Visualisasi
        plt.figure(figsize=(14, 8))
        bars = plt.barh(range(len(top_10_kabupaten)), top_10_kabupaten['Rata-rata Harga/Kg'],
                       color='gold', edgecolor='darkgoldenrod', linewidth=2)

        # Add value labels on bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width + 100, bar.get_y() + bar.get_height()/2,
                    f'{width:,.0f}', ha='left', va='center', fontweight='bold')

        plt.yticks(range(len(top_10_kabupaten)), top_10_kabupaten['Kabupaten/Kota'])
        plt.xlabel('Rata-rata Harga per Kg (Rp)', fontsize=12)
        plt.title(f'Top 10 Kabupaten dengan Harga Beras Premium Tertinggi\n({tahun_6_kebelakang}-{tahun_terakhir})',
                 fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3, axis='x')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig('top_10_kabupaten_harga_beras_premium.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n[SELESAI] Grafik top 10 kabupaten tersimpan sebagai 'top_10_kabupaten_harga_beras_premium.png'")
    else:
        print("[ERROR] Tidak ada data untuk 6 tahun terakhir")
else:
    print("[ERROR] Tidak ada data untuk beras premium")

# 4. PERBANDINGAN HARGA BERAS MEDIUM VS PREMIUM
print("\n" + "="*60)
print("4. PERBANDINGAN HARGA BERAS MEDIUM VS PREMIUM")
print("="*60)

if len(beras_medium) > 0 and len(beras_premium) > 0:
    # Gabungkan data medium dan premium
    comparison_data = []

    for tahun in sorted(df['tahun'].unique()):
        medium_tahun = beras_medium[beras_medium['tahun'] == tahun]
        premium_tahun = beras_premium[beras_premium['tahun'] == tahun]

        if len(medium_tahun) > 0 and len(premium_tahun) > 0:
            comparison_data.append({
                'Tahun': tahun,
                'Medium': medium_tahun['harga_per_kg'].mean(),
                'Premium': premium_tahun['harga_per_kg'].mean()
            })

    comparison_df = pd.DataFrame(comparison_data)

    if len(comparison_df) > 0:
        print("\nPerbandingan Harga Beras Medium vs Premium per Tahun:")
        print("="*65)
        print(f"{'Tahun':<6} {'Medium (Rp)':<15} {'Premium (Rp)':<15} {'Selisih (Rp)':<15} {'%':<8}")
        print("="*65)

        for _, row in comparison_df.iterrows():
            selisih = row['Premium'] - row['Medium']
            persentase = (selisih / row['Medium']) * 100
            print(f"{row['Tahun']:<6} {row['Medium']:>13,.0f} {row['Premium']:>15,.0f} {selisih:>13,.0f} {persentase:>7.1f}%")

        # Visualisasi perbandingan
        plt.figure(figsize=(14, 8))

        x = np.arange(len(comparison_df))
        width = 0.35

        plt.bar(x - width/2, comparison_df['Medium'], width, label='Beras Medium', color='orange', alpha=0.8)
        plt.bar(x + width/2, comparison_df['Premium'], width, label='Beras Premium', color='green', alpha=0.8)

        plt.xlabel('Tahun', fontsize=12)
        plt.ylabel('Harga per Kg (Rp)', fontsize=12)
        plt.title('Perbandingan Harga Beras Medium vs Premium per Tahun', fontsize=16, fontweight='bold')
        plt.xticks(x, comparison_df['Tahun'])
        plt.legend()
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig('perbandingan_harga_beras_medium_premium.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n[SELESAI] Grafik perbandingan tersimpan sebagai 'perbandingan_harga_beras_medium_premium.png'")
    else:
        print("[ERROR] Tidak ada data yang bisa dibandingkan")
else:
    print("[ERROR] Data medium atau premium tidak lengkap")

print("\n" + "="*60)
print("ANALISIS SELESAI")
print("="*60)
print("\nSemua grafik telah disimpan dalam format PNG")