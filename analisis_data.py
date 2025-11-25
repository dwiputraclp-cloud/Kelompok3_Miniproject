import pandas as pd
import numpy as np

def main():
    print("=== ANALISIS HARGA BERAS INDONESIA ===\n")

    # Load data
    df = pd.read_excel("harga_pertanian_fix.xlsx")

    # Filter data beras
    beras_data = df[df['kategori_utama'] == 'BERAS'].copy()
    beras_medium = beras_data[beras_data['kategori'] == 'BERAS MEDIUM']
    beras_premium = beras_data[beras_data['kategori'] == 'BERAS PREMIUM']

    print(f"Data Overview:")
    print(f"- Total data BERAS: {len(beras_data):,}")
    print(f"- BERAS MEDIUM: {len(beras_medium):,}")
    print(f"- BERAS PREMIUM: {len(beras_premium):,}")
    print(f"- Rentang tahun: {df['tahun'].min()} - {df['tahun'].max()}")
    print()

    # 1. Rata-rata harga beras medium per tahun
    print("1. RATA-RATA HARGA BERAS MEDIUM PER TAHUN")
    print("-" * 50)

    if len(beras_medium) > 0:
        beras_medium['harga_per_kg'] = beras_medium['harga_per_ton'] / 1000
        medium_tahun = beras_medium.groupby('tahun')['harga_per_kg'].mean().reset_index()
        medium_tahun = medium_tahun.sort_values('tahun')

        print(f"{'Tahun':<6} {'Harga/Kg (Rp)':<15} {'Jumlah Data':<12}")
        print("-" * 45)

        for _, row in medium_tahun.iterrows():
            count = len(beras_medium[beras_medium['tahun'] == row['tahun']])
            print(f"{int(row['tahun']):<6} {row['harga_per_kg']:>13,.0f} {count:>12}")

        # Simpan hasil
        medium_tahun.to_csv('harga_beras_medium_tahun.csv', index=False)
        print(f"\nData tersimpan: harga_beras_medium_tahun.csv")
    else:
        print("Tidak ada data untuk beras medium")

    print()

    # 2. Rata-rata harga beras premium per tahun
    print("2. RATA-RATA HARGA BERAS PREMIUM PER TAHUN")
    print("-" * 50)

    if len(beras_premium) > 0:
        beras_premium['harga_per_kg'] = beras_premium['harga_per_ton'] / 1000
        premium_tahun = beras_premium.groupby('tahun')['harga_per_kg'].mean().reset_index()
        premium_tahun = premium_tahun.sort_values('tahun')

        print(f"{'Tahun':<6} {'Harga/Kg (Rp)':<15} {'Jumlah Data':<12}")
        print("-" * 45)

        for _, row in premium_tahun.iterrows():
            count = len(beras_premium[beras_premium['tahun'] == row['tahun']])
            print(f"{int(row['tahun']):<6} {row['harga_per_kg']:>13,.0f} {count:>12}")

        # Simpan hasil
        premium_tahun.to_csv('harga_beras_premium_tahun.csv', index=False)
        print(f"\nData tersimpan: harga_beras_premium_tahun.csv")
    else:
        print("Tidak ada data untuk beras premium")

    print()

    # 3. Top 10 kabupaten harga premium tertinggi (6 tahun terakhir)
    print("3. TOP 10 KABUPATEN HARGA BERAS PREMIUM TERTINGGI")
    print("-" * 50)

    if len(beras_premium) > 0:
        # Filter 6 tahun terakhir
        tahun_max = df['tahun'].max()
        tahun_min = tahun_max - 5

        premium_6tahun = beras_premium[beras_premium['tahun'] >= tahun_min].copy()
        premium_6tahun['harga_per_kg'] = premium_6tahun['harga_per_ton'] / 1000

        # Group by kabupaten
        kabupaten_stats = premium_6tahun.groupby('nama_kabupaten_kota').agg({
            'harga_per_kg': 'mean',
            'tahun': 'count'
        }).reset_index()
        kabupaten_stats.columns = ['Kabupaten', 'Rata-rata Harga/Kg', 'Jumlah Data']

        # Top 10
        top10 = kabupaten_stats.sort_values('Rata-rata Harga/Kg', ascending=False).head(10)

        print(f"Analisis: {tahun_min}-{tahun_max} (Total data: {len(premium_6tahun)})")
        print(f"{'No':<3} {'Kabupaten':<25} {'Harga/Kg (Rp)':<15} {'Jumlah':<8}")
        print("-" * 60)

        for idx, (_, row) in enumerate(top10.iterrows(), 1):
            kab = row['Kabupaten'][:24]  # Truncate if too long
            print(f"{idx:<3} {kab:<25} {row['Rata-rata Harga/Kg']:>13,.0f} {row['Jumlah Data']:>8}")

        # Simpan hasil
        top10.to_csv('top10_kabupaten_harga_premium.csv', index=False)
        print(f"\nData tersimpan: top10_kabupaten_harga_premium.csv")
    else:
        print("Tidak ada data untuk beras premium")

    print()

    # 4. Perbandingan harga medium vs premium
    print("4. PERBANDINGAN HARGA MEDIUM VS PREMIUM")
    print("-" * 40)

    if len(beras_medium) > 0 and len(beras_premium) > 0:
        comparison = []

        for tahun in sorted(df['tahun'].unique()):
            medium_year = beras_medium[beras_medium['tahun'] == tahun]
            premium_year = beras_premium[beras_premium['tahun'] == tahun]

            if len(medium_year) > 0 and len(premium_year) > 0:
                comparison.append({
                    'Tahun': tahun,
                    'Medium': medium_year['harga_per_ton'].mean() / 1000,
                    'Premium': premium_year['harga_per_ton'].mean() / 1000
                })

        comp_df = pd.DataFrame(comparison)

        print(f"{'Tahun':<6} {'Medium (Rp)':<12} {'Premium (Rp)':<13} {'Selisih (Rp)':<13} {'%':<6}")
        print("-" * 60)

        for _, row in comp_df.iterrows():
            selisih = row['Premium'] - row['Medium']
            persen = (selisih / row['Medium']) * 100
            print(f"{int(row['Tahun']):<6} {row['Medium']:>10,.0f} {row['Premium']:>13,.0f} {selisih:>11,.0f} {persen:>5.1f}%")

        # Simpan hasil
        comp_df.to_csv('perbandingan_harga_beras.csv', index=False)
        print(f"\nData tersimpan: perbandingan_harga_beras.csv")
    else:
        print("Data medium atau premium tidak lengkap")

    print("\n=== ANALISIS SELESAI ===")
    print("File CSV yang dihasilkan:")
    print("- harga_beras_medium_tahun.csv")
    print("- harga_beras_premium_tahun.csv")
    print("- top10_kabupaten_harga_premium.csv")
    print("- perbandingan_harga_beras.csv")

if __name__ == "__main__":
    main()