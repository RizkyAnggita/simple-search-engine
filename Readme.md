# Algeo02-19033
> Sebuah mesin pencari sederhana yang menggunakan Cosine Similarity dalam proses perhitungan tingkat kemiripan.
> Dibangun menggunakan Python dengan Flask, library Sastrawi, dan Bootstrap 4.

## Daftar Isi
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Contact](#contact)

## General Info
Hampir semua orang pernah menggunakan search engine, seperti google, bing dan yahoo! search. Setiap hari, bahkan untuk sesuatu yang sederhana orang-orang menggunakan mesin pencarian. Pada tugas besar Aljabar Linear dan Geometri kali ini penulis akan menjelaskan bagaimana cara search engine tersebut mendapatkan semua dokumen kita berdasarkan apa yang ingin pengguna cari.

Sebagaimana yang telah diajarkan di dalam kuliah pada materi vektor di ruang Euclidean, temu-balik informasi (information retrieval) merupakan proses menemukan kembali (retrieval) informasi yang relevan terhadap kebutuhan pengguna dari suatu kumpulan informasi secara otomatis. Biasanya, sistem temu balik informasi ini digunakan untuk mencari informasi pada informasi yang tidak terstruktur, seperti laman web atau dokumen.
## Screenshots
<a href="https://ibb.co/zfghYrf"><img src="https://i.ibb.co/ryhGSmy/Snip20201115-5.png" alt="Snip20201115-5" border="0"></a>

## Technologies
Menggunakan Flask with Python untuk bagian backend, library Sastrawi untuk text-processing, dan Bootstrap 4 untuk bagian tampilan web:
```
Python 3.8.5
Flask 1.1.2
Werkzeug 1.0.1
Sastrawi 1.0.1

```

## Setup
Terdapat beberapa hal yang harus di-install sebelum menjalankan program ini.
Kami menggunakan text-editor Visual Studio Code pada proses pengembangan, berikut merupakan instalasi yang dilakukan untuk menjalankan program melalui VSCode

1. Install Python versi 3.8 atau yang lebih baru, melalui VSCode.
   Link: https://code.visualstudio.com/docs/python/python-tutorial
2. Install Flask dan ikuti seluruh langkah yang ada, termasuk persiapan Virtual Environment untuk program ini.
   Link: https://code.visualstudio.com/docs/python/tutorial-flask
3. Install Sastrawi melalui virtual environment terminal pada VSCode
   Command: pip3 install Sastrawi
4. Semua prerequisite terpenuhi.

## Features
Fitur yang sudah ada:
- [x] Program mampu menerima search query. Search query dapat berupa kata dasar maupun berimbuhan.
- [x] Hasil pencarian terurut berdasarkan similaritas tertinggi dari hasil teratas hingga hasil terbawah berupa judul dokumen, nilai similaritas, dan  kalimat pertama dari    dokumen tersebut.
- [x] Adanya pembersihan dokumen dengan cara stemming dan penghapusan stopword.
- [x] Dapat menerima input hingga 15 dokumen.

Saran pengembangan
- [] Memperindah desain website supaya lebih menarik bagi pengguna. Beberapa diantaranya adalah desain tombol, typography, color pallete, dan membuat tampilan yang responsif.
- [] Membuat kode lebih rapi dan memberikan komentar yang lebih detail serta mudah dipahami.
- [] Memberikan konvensi dalam menentukan standar nama fungsi atau variabel.
- [] Menerapkan web scraping agar bisa menerima input html.
## Code Examples
<p>Setelah semua prerequisite terpasang, jalankan program melalui app.py.
  Terdapat 2 cara untuk menjalankan nya pada local server.
  <br>Cara pertama dengan menekan tombol run pada VSCode.
  <br>Cara kedua ialah menggunakan terminal dan mengetik command berikut: `python3 app.py`
  
  <br>Kemudian akan muncul link local server pada project ini, klik link tersebut dan program berhasil dijalankan.
</p>

<p align="center">
  <a href="https://ibb.co/wJ9HY2V"><img src="https://i.ibb.co/1sDVb41/Snip20201115-4.png" alt="Snip20201115-4" border="0"></a>
</p>

## Contact
<p> Created by JAF <br>
Teknik Informatika <br>
Institut Teknologi Bandung <br>
2020
</p>
