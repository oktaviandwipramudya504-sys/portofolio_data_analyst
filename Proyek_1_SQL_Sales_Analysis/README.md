# Proyek 1: Analisis Performa Penjualan & Profit Toko (SQL)

## 📌 1. Latar Belakang & Masalah Bisnis
Manajemen perusahaan retail menghadapi tantangan dalam memantau tren pendapatan bulanan serta menentukan produk mana yang memberikan keuntungan bersih (*profit*) paling besar. Selama ini, keputusan bisnis sering diambil hanya berdasarkan insting dan total pendapatan kotor (*revenue*), tanpa memperhitungkan biaya operasional produksi.

**Tujuan Analisis:**
- Menemukan tren total pendapatan (*revenue*) dari bulan ke bulan (Januari - Mei 2026).
- Mengidentifikasi produk dengan performa penjualan tertinggi berdasarkan keuntungan bersih (*profit*).
- Memberikan rekomendasi bisnis berbasis data untuk strategi kuartal berikutnya.

---

## 🛠️ 2. Struktur Proyek
Proyek ini diatur dengan struktur folder yang bersih dan terstandarisasi sebagai berikut:
- `data/` : Berisi file data mentah berupa skema tabel dan sampel data transaksi.
- `queries/` : Berisi kueri SQL tingkat lanjut yang digunakan untuk menarik *insight* dari database.

---

## 💻 3. Analisis & Kode SQL

### A. Analisis Tren Pendapatan Bulanan
Kueri ini digunakan untuk melihat total kuantitas produk yang terjual dan total uang masuk dari bulan ke bulan.
- **File Kode:** `queries/1_tren_pendapatan.sql`
- **Hasil Kueri (Output):**
  - **Maret 2026** merupakan bulan dengan pendapatan tertinggi mencapai **Rp 33.800.000**.
  - Terjadi penurunan pendapatan yang cukup signifikan di bulan Februari dan April.

### B. Analisis Performa & Profit Produk
Kueri ini digunakan untuk menghitung keuntungan bersih per produk (`Harga Jual - Biaya Produksi`) untuk mengetahui produk mana yang paling mendatangkan keuntungan.
- **File Kode:** `queries/2_performa_produk.sql`
- **Hasil Kueri (Output):**
  - **Kamera Mirrorless A** menghasilkan total profit terbesar bagi toko, yaitu **Rp 9.000.000** dari total 6 unit yang terjual.
  - **Lensa Kamera B** memiliki margin profit yang tipis namun stabil.

---

## 💡 4. Rekomendasi Bisnis
1. **Fokus pada Produk High-Profit:** Manajemen disarankan untuk meningkatkan anggaran pemasaran pada produk **Kamera Mirrorless A** karena produk ini memberikan kontribusi keuntungan bersih terbesar meskipun volume penjualannya bukan yang terbanyak.
2. **Evaluasi Biaya Operasional:** Lakukan peninjauan kembali terhadap biaya produksi produk yang memiliki margin keuntungan kecil untuk mengoptimalkan profitabilitas di bulan-bulan mendatang.