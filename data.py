import pandas as pd

# Membaca file Excel
df = pd.read_excel("Harga_Pertanian.xlsx")   # ganti dengan nama file Anda

# Menghapus baris yang memiliki jumlah = 0
df = df[df['jumlah'] != 0]

# Menyimpan kembali ke file Excel
df.to_excel("data_bersih.xlsx", index=False)

print("Baris dengan jumlah = 0 berhasil dihapus!")