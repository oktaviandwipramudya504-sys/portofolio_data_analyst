import pandas as pd
import matplotlib.pyplot as plt

# DATA MENTAH YANG DIJAMIN BERSIH 100%
isi_csv_bersih = """id_transaksi,tanggal_transaksi,nama_produk,kategori,jumlah_terjual,harga_satuan,biaya_produksi_satuan,wilayah
TRX001,2026-01-10,Kamera Mirrorless A,Elektronik,2,7000000,5500000,Jakarta
TRX002,2026-01-15,Lampu Studio X,Lighting,5,1200000,800000,Bandung
TRX003,2026-01-22,Tripod Profesional,Aksesoris,10,500000,300000,Jakarta
TRX004,2026-02-02,Lensa Kamera B,Elektronik,1,4500000,3800000,Surabaya
TRX005,2026-02-18,Tripod Profesional,Aksesoris,8,500000,300000,Bandung
TRX006,2026-02-25,Lampu Studio X,Lighting,3,1200000,800000,Jakarta
TRX007,2026-03-05,Kamera Mirrorless A,Elektronik,3,7000000,5500000,Medan
TRX008,2026-03-12,Lensa Kamera B,Elektronik,2,4500000,3800000,Jakarta
TRX009,2026-03-29,Lampu Studio X,Lighting,4,1200000,800000,Surabaya
TRX010,2026-04-04,Tripod Profesional,Aksesoris,15,500000,300000,Medan
TRX011,2026-04-19,Kamera Mirrorless A,Elektronik,1,7000000,5500000,Bandung
TRX012,2026-05-02,Lensa Kamera B,Elektronik,4,4500000,3800000,Jakarta
TRX013,2026-05-14,Lampu Studio X,Lighting,6,1200000,800000,Medan"""

# LANGKAH AMAN: Menulis ulang dataset.csv agar pasti bersih & rapi
with open('dataset.csv', 'w', encoding='utf-8') as f:
    f.write(isi_csv_bersih.strip())

print("[INFO] File dataset.csv berhasil dibuat ulang secara otomatis!")

# 1. Membaca data menggunakan Pandas
df = pd.read_csv('dataset.csv')

# 2. Menghitung Kolom Baru
df['total_pendapatan'] = df['jumlah_terjual'] * df['harga_satuan']
df['total_profit'] = df['jumlah_terjual'] * (df['harga_satuan'] - df['biaya_produksi_satuan'])

# 3. Mengatur Tanggal dan Bulan
df['tanggal_transaksi'] = pd.to_datetime(df['tanggal_transaksi'])
df['bulan'] = df['tanggal_transaksi'].dt.to_period('M').astype(str)

# 4. Mengelompokkan data berdasarkan Bulan
tren_bulanan = df.groupby('bulan')['total_pendapatan'].sum().reset_index()

# 5. Menampilkan ringkasan data di terminal
print("\n=== DATA BERHASIL DIOLAH PYTHON! ===")
print("-------------------------------------")
print(tren_bulanan.to_string(index=False))
print("-------------------------------------")

# 6. Membuat GRAFIK BATANG
plt.figure(figsize=(10, 6))
plt.bar(tren_bulanan['bulan'], tren_bulanan['total_pendapatan'], color='#FFD700', edgecolor='black')

plt.title('Tren Total Pendapatan Bulanan (Januari - Mei 2026)', fontsize=14, fontweight='bold')
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Total Pendapatan (Rupiah)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
print("\n[INFO] Menampilkan grafik batang tren pendapatan...")
plt.show()