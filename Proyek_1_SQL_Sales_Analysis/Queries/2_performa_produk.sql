-- Query untuk menganalisis total penjualan dan profit per produk
SELECT 
    nama_produk,
    kategori,
    SUM(jumlah_terjual) AS total_terjual,
    SUM(jumlah_terjual * harga_satuan) AS total_pendapatan,
    SUM(jumlah_terjual * (harga_satuan - biaya_produksi_satuan)) AS total_profit
FROM 
    transaksi_penjualan
GROUP BY 
    nama_produk, kategori
ORDER BY 
    total_profit DESC;