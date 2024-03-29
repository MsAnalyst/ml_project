# Klasifikasi Gambar Stroke Menggunakan CNN dan Deployment Menggunakan Flask
Hallo, saya Dewi Astuti (dewi-I4Zs)

Ini adalah Final Project dari kelas Machine Learning Process pada Sekolah Data Pacmann. 

## Deskripsi
Project ini bertujuan untuk membuat sistem klasifikasi gambar stroke menggunakan Convolutional Neural Network (CNN) dan deployment sistem tersebut menggunakan Flask sebagai websitenya. Project ini memiliki tujuan untuk mempermudah proses deteksi stroke pada gambar MRI dan CT-Scan serta mempermudah akses informasi bagi para dokter dan pasien.

## Instalasi
Untuk menjalankan project ini, pastikan komputer anda sudah terinstall Python dan beberapa library pendukung seperti:
1. Tensorflow
2. Keras
3. Flask
4. Numpy
5. Matplotlib

Untuk menginstall library tersebut, bisa menjalankan perintah berikut pada terminal atau Command Prompt:
<blockquote> pip install tensorflow </blockquote>
<blockquote> pip install keras </blockquote>
<blockquote> pip install flask </blockquote>
<blockquote> pip install numpy </blockquote>
<blockquote> pip install matplotlib  </blockquote>

## Penggunaan
- Clone repository ini pada komputer anda.
- Jalankan file app.py pada terminal atau Command Prompt. Contoh : python app.py
- Buka browser anda dan masukkan URL http://localhost:5000/ untuk mengakses websitenya.
- Pilih gambar yang ingin diklasifikasi dan klik tombol Upload Image.
- Hasil klasifikasi akan ditampilkan pada halaman websitenya.

## Klasifikasi Gambar Stroke
    |-- app.py
    |-- model
    |   `-- model.h5
    |-- static
    |   |-- css
    |   |   `-- styles.css
    |   `-- uploads
    |-- templates
    |    `-- index.html
    |-- training.ipynb
    |-- LICENSE
    `-- README.md
