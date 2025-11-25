import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def set_style():
    """Set style untuk grafik"""
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 10

def plot_harga_medium():
    """Grafik harga beras medium per tahun"""
    try:
        df = pd.read_csv('harga_beras_medium_tahun.csv')

        plt.figure(figsize=(12, 6))
        plt.plot(df['tahun'], df['harga_per_kg'],
                marker='o', linewidth=2, markersize=8,
                color='orange', label='Beras Medium')

        plt.title('Rata-rata Harga Beras Medium per Tahun', fontsize=16, fontweight='bold')
        plt.xlabel('Tahun')
        plt.ylabel('Harga per Kg (Rp)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.xticks(df['tahun'].astype(int))

        # Add value labels
        for i, v in enumerate(df['harga_per_kg']):
            plt.annotate(f'{v:,.0f}', (df['tahun'].iloc[i], v),
                        textcoords="offset points", xytext=(0,10), ha='center')

        plt.tight_layout()
        plt.savefig('grafik_harga_medium.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("[OK] Grafik harga medium berhasil dibuat: grafik_harga_medium.png")

    except FileNotFoundError:
        print("[ERROR] File harga_beras_medium_tahun.csv tidak ditemukan. Jalankan analisis_data.py dulu.")

def plot_harga_premium():
    """Grafik harga beras premium per tahun"""
    try:
        df = pd.read_csv('harga_beras_premium_tahun.csv')

        plt.figure(figsize=(12, 6))
        plt.plot(df['tahun'], df['harga_per_kg'],
                marker='o', linewidth=2, markersize=8,
                color='green', label='Beras Premium')

        plt.title('Rata-rata Harga Beras Premium per Tahun', fontsize=16, fontweight='bold')
        plt.xlabel('Tahun')
        plt.ylabel('Harga per Kg (Rp)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.xticks(df['tahun'].astype(int))

        # Add value labels
        for i, v in enumerate(df['harga_per_kg']):
            plt.annotate(f'{v:,.0f}', (df['tahun'].iloc[i], v),
                        textcoords="offset points", xytext=(0,10), ha='center')

        plt.tight_layout()
        plt.savefig('grafik_harga_premium.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("[OK] Grafik harga premium berhasil dibuat: grafik_harga_premium.png")

    except FileNotFoundError:
        print("[ERROR] File harga_beras_premium_tahun.csv tidak ditemukan. Jalankan analisis_data.py dulu.")

def plot_top10_kabupaten():
    """Grafik top 10 kabupaten harga premium tertinggi"""
    try:
        df = pd.read_csv('top10_kabupaten_harga_premium.csv')

        plt.figure(figsize=(14, 8))

        # Create horizontal bar chart
        bars = plt.barh(range(len(df)), df['Rata-rata Harga/Kg'],
                       color='gold', edgecolor='darkgoldenrod', linewidth=2)

        # Add value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width + 100, bar.get_y() + bar.get_height()/2,
                    f'{width:,.0f}', ha='left', va='center', fontweight='bold')

        plt.yticks(range(len(df)), df['Kabupaten'])
        plt.xlabel('Rata-rata Harga per Kg (Rp)')
        plt.title('Top 10 Kabupaten dengan Harga Beras Premium Tertinggi',
                 fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3, axis='x')
        plt.gca().invert_yaxis()

        plt.tight_layout()
        plt.savefig('grafik_top10_kabupaten.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("[OK] Grafik top 10 kabupaten berhasil dibuat: grafik_top10_kabupaten.png")

    except FileNotFoundError:
        print("[ERROR] File top10_kabupaten_harga_premium.csv tidak ditemukan. Jalankan analisis_data.py dulu.")

def plot_perbandingan():
    """Grafik perbandingan harga medium vs premium"""
    try:
        df = pd.read_csv('perbandingan_harga_beras.csv')

        plt.figure(figsize=(14, 8))

        x = np.arange(len(df))
        width = 0.35

        # Create grouped bar chart
        bars1 = plt.bar(x - width/2, df['Medium'], width,
                       label='Beras Medium', color='orange', alpha=0.8)
        bars2 = plt.bar(x + width/2, df['Premium'], width,
                       label='Beras Premium', color='green', alpha=0.8)

        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                plt.annotate(f'{height:,.0f}',
                           (bar.get_x() + bar.get_width()/2, height),
                           textcoords="offset points", xytext=(0,3), ha='center', va='bottom')

        plt.xlabel('Tahun')
        plt.ylabel('Harga per Kg (Rp)')
        plt.title('Perbandingan Harga Beras Medium vs Premium',
                 fontsize=16, fontweight='bold')
        plt.xticks(x, df['Tahun'].astype(int))
        plt.legend()
        plt.grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        plt.savefig('grafik_perbandingan.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("[OK] Grafik perbandingan berhasil dibuat: grafik_perbandingan.png")

    except FileNotFoundError:
        print("[ERROR] File perbandingan_harga_beras.csv tidak ditemukan. Jalankan analisis_data.py dulu.")

def create_combined_chart():
    """Grafik kombinasi medium dan premium dalam satu chart"""
    try:
        df_medium = pd.read_csv('harga_beras_medium_tahun.csv')
        df_premium = pd.read_csv('harga_beras_premium_tahun.csv')

        plt.figure(figsize=(14, 8))

        # Plot both lines
        plt.plot(df_medium['tahun'], df_medium['harga_per_kg'],
                marker='o', linewidth=2, markersize=8,
                color='orange', label='Beras Medium')

        plt.plot(df_premium['tahun'], df_premium['harga_per_kg'],
                marker='s', linewidth=2, markersize=8,
                color='green', label='Beras Premium')

        plt.title('Tren Harga Beras Medium vs Premium (2020-2025)',
                 fontsize=16, fontweight='bold')
        plt.xlabel('Tahun')
        plt.ylabel('Harga per Kg (Rp)')
        plt.grid(True, alpha=0.3)
        plt.legend()

        # Set x-axis to show all years
        all_years = sorted(list(set(df_medium['tahun']) | set(df_premium['tahun'])))
        plt.xticks(all_years)

        # Add value labels for both lines
        for df, marker in [(df_medium, 'o'), (df_premium, 's')]:
            for i, v in enumerate(df['harga_per_kg']):
                plt.annotate(f'{v:,.0f}', (df['tahun'].iloc[i], v),
                           textcoords="offset points", xytext=(0,10 if marker == 'o' else -20),
                           ha='center')

        plt.tight_layout()
        plt.savefig('grafik_kombinasi.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("[OK] Grafik kombinasi berhasil dibuat: grafik_kombinasi.png")

    except FileNotFoundError:
        print("[ERROR] File harga medium/premium tidak ditemukan. Jalankan analisis_data.py dulu.")

def main():
    print("=== VISUALISASI DATA HARGA BERAS ===\n")
    print("Membuat grafik dari data yang telah dianalisis...\n")

    set_style()

    # Buat semua grafik
    plot_harga_medium()
    plot_harga_premium()
    plot_top10_kabupaten()
    plot_perbandingan()
    create_combined_chart()

    print("\n=== SEMUA GRAFIK SELESAI ===")
    print("File grafik yang dihasilkan:")
    print("- grafik_harga_medium.png")
    print("- grafik_harga_premium.png")
    print("- grafik_top10_kabupaten.png")
    print("- grafik_perbandingan.png")
    print("- grafik_kombinasi.png")

if __name__ == "__main__":
    main()