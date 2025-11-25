import pandas as pd

# Load file
df = pd.read_excel("data_bersih.xlsx")

# 1. Tambah kolom harga per ton (konversi dari harga per KG → Ton)
df["harga_per_ton"] = df["jumlah"] * 1000

# 2. Tambah kolom kategori utama (ambil kata pertama dari kolom kategori)
df["kategori_utama"] = df["kategori"].apply(lambda x: str(x).split()[0])

# 3. Tambah kolom status harga (murah / normal / mahal)
def status(x):
    if x < 6000:
        return "Murah"
    elif x < 10000:
        return "Normal"
    else:
        return "Mahal"

df["status_harga"] = df["jumlah"].apply(status)

# Simpan ke file baru
df.to_excel("harga_pertanian_fix.xlsx", index=False)

print("✔ File baru berhasil dibuat: harga_pertanian_fix.xlsx")