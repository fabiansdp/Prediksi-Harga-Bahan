## Tugas Akhir II4042 Kecerdasan Buatan Untuk Bisnis

> ### Dibuat Oleh
> 1. Fabian Savero Diaz P (13519140)
> 2. Fadel Ananda Dotty (13519146)
> 3. Muhammad Fawwaz N. (13519206)

### Deskripsi Permasalahan
--- 

Permasalahan yang ingin diselesaikan oleh model ini berkaitan dengan proses procurement yang terjadi pada perusahaan seperti misalnya Super Indo. Terkadang terjadi fluktuasi harga secara tiba-tiba pada bahan pokok yang dipasok sehingga diperlukan sebuah solusi untuk dapat memprediksi harga sehingga proses procurement dapat direncanakan dan kenaikan harga secara tiba-tiba dapat diantisipasi.

### Solusi
---

Salah satu solusi data science untuk mengatasi permasalahan ini adalah membuat model yang dapat memprediksi harga bahan pokok di suatu waktu di masa depan. Analitik yang dipilih adalah regresi karena berkaitan dengan prediksi sesuatu. Metrik yang digunakan adalah Mean Root Square Error (MRSE). 

Kami membuat model dengan tiga buah algoritma yaitu Decission Tree, Linear Regression, dan Random Forest.

Proses yang dilakukan untuk tugas ini meliputi:

1. Business understanding
2. Data understanding
3. Data preparation
4. Modeling
5. Model Evaluation
6. Deployment

Dengan adanya model yang dapat memprediksi harga, diharapkan permasalahan yang dihadapi dapat diselesaikan.


### Cara Menggunakan Web
---
1. Membuka https://prediksi-bahan-baku.herokuapp.com/
2. Mengisi input field yang disediakan dengan input yang sesuai
3. Menekan tombol submit

### Test Case yang Dapat Digunakan
---
1. Memilih model prediksi
2. Memasukkan bulan dan tahun sebagai "Juli 2021"
3. Pilih kategori "Vegetables and fruits"
4. Pilih komoditas "Cabe"
5. Pilih unit "Kilogram"
6. Pilih price type "Actual"
7. Tekan tombol submit
