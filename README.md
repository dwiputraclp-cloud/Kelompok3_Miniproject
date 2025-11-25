# 📊 Analisis Harga Beras Indonesia

Analisis data harga beras medium dan premium di Indonesia tahun 2020-2025.

## 🚀 Cara Penggunaan

### Cara Cepat (Rekomendasi):
```bash
python main.py
```
Pilih opsi 3 untuk menjalankan analisis dan visualisasi lengkap.

### Cara Manual:
```bash
# 1. Analisis data
python analisis_data.py

# 2. Buat grafik
python visualisasi_data.py
```

## 📁 File yang Dihasilkan

### 📄 Data CSV:
- `harga_beras_medium_tahun.csv` - Harga beras medium per tahun
- `harga_beras_premium_tahun.csv` - Harga beras premium per tahun
- `top10_kabupaten_harga_premium.csv` - 10 kabupaten harga tertinggi
- `perbandingan_harga_beras.csv` - Perbandingan medium vs premium

### 📊 Grafik PNG:
- `grafik_harga_medium.png` - Tren harga beras medium
- `grafik_harga_premium.png` - Tren harga beras premium
- `grafik_top10_kabupaten.png` - Top 10 kabupaten harga premium
- `grafik_perbandingan.png` - Perbandingan medium vs premium
- `grafik_kombinasi.png` - Gabungan harga medium dan premium

## 📋 Hasil Utama

### Rata-rata Harga Beras Medium (2020-2025):
- 2020: Rp 8,959/kg
- 2024: Rp 12,420/kg (puncak)

### Rata-rata Harga Beras Premium (2020-2025):
- 2020: Rp 10,198/kg
- 2024: Rp 13,679/kg (puncak)

### Top 5 Kabupaten Harga Premium Tertinggi:
1. Kota Surabaya: Rp 12,330/kg
2. Bangkalan: Rp 12,141/kg
3. Bondowoso: Rp 11,862/kg
4. Jember: Rp 11,827/kg
5. Ngawi: Rp 11,811/kg

## 🔧 Persyaratan
```bash
pip install pandas matplotlib numpy
```

## 📈 Insight Utama:
- Harga beras naik signifikan 2023-2024
- Gap harga premium-medium: 16% (2021) → 10% (2024)
- Jawa Timur dominasi harga premium tertinggi

---
*Dibuat dengan Python | Data: Harga_Pertanian.xlsx*