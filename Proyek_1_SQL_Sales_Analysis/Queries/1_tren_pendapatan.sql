-- Query untuk menghitung total pendapatan bulanan
SELECT 
    DATE_FORMAT(tanggal_transaksi, '%Y-%m') AS bulan,
    SUM(jumlah_terjual) AS total_produk_terjual,
    SUM(jumlah_terjual * harga_satuan) AS total_pendapatan
FROM 
    transaksi_penjualan
GROUP BY 
    DATE_FORMAT(tanggal_transaksi, '%Y-%m')
ORDER BY 
    bulan ASC;