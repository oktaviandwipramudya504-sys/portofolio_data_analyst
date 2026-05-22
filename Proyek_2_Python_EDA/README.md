Proyek 2: Analisis Eksplorasi Data (EDA) & Visualisasi Tren Penjualan (Python)

1. Latar Belakang Proyek
Setelah berhasil menarik data transaksi menggunakan SQL pada proyek sebelumnya, langkah selanjutnya adalah membangun sistem otomatisasi analisis menggunakan Python. Proyek ini berfokus pada **Exploratory Data Analysis (EDA)** untuk membaca berkas data penjualan format `.csv`, mengolah trennya secara dinamis, dan menyajikan grafik visual yang interaktif bagi tim manajemen.

**Tujuan Proyek:**
- Mengotomatisasi perhitungan total pendapatan dan keuntungan bersih (*profit*) per transaksi.
- Mentransformasi data tanggal mentah menjadi pengelompokkan berbasis bulan.
- Membuat visualisasi grafik batang (*bar chart*) yang informatif untuk presentasi bisnis.



2. Kebutuhan Pustaka (Libraries)
Proyek Python ini menggunakan dua pustaka utama dalam ekosistem *data science*:
 1. **Pandas**: Digunakan untuk manipulasi tabel data (*Dataframe*) dan perhitungan matematika.
 2. **Matplotlib**: Digunakan untuk merancang dan memunculkan grafik visualisasi data.



3. Alur Kerja Kode Python
Seluruh proses analisis ditulis di dalam berkas `analisis_performa.py` dengan tahapan berikut:

1. **Data Ingestion**: Membaca file data mentah `dataset.csv` ke dalam bentuk *Dataframe* Pandas.
2. **Feature Engineering**: Membuat kolom kalkulasi baru untuk `total_pendapatan` serta `total_profit` bersih.
3. **Time Series Grouping**: Mengubah teks tanggal menjadi objek waktu (*datetime*) untuk dikelompokkan berdasarkan bulan transaksi.
4. **Data Visualization**: Menggambar grafik batang pendapatan menggunakan skema warna emas (`#FFD700`) yang elegan dengan grid bantuan agar data mudah dibaca oleh direksi.



4. Hasil Analisis Visual
Ketika program dijalankan, Python akan otomatis menampilkan grafik tren yang menunjukkan fluktuasi penjualan dari bulan Januari hingga Mei 2026 secara rapi, membantu pemangku kebijakan melihat performa bisnis hanya dalam satu kali klik.
