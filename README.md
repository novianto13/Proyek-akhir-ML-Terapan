# Proyek-akhir-ML-Terapan
### Proyek akhir: Novianto

# Project Overview
## Latar Belakang Masalah
Sistem rekomendasi telah menjadi alat penting dalam membantu pengguna membuat keputusan yang tepat dalam berbagai sektor, termasuk e-commerce, streaming, dan makanan. Dalam konteks makanan, pengguna sering dihadapkan dengan banyaknya pilihan makanan yang tersedia, baik di restoran maupun dalam layanan pesan antar. Hal ini dapat menyebabkan kebingungan dan membuat mereka kesulitan memilih makanan yang sesuai dengan preferensi pribadi.

Sistem rekomendasi makanan dirancang untuk memanfaatkan data seperti nama makanan, jenis makanan, deskripsi, dan rating pengguna untuk menawarkan rekomendasi yang relevan dan dipersonalisasi. Dengan memanfaatkan algoritma seperti collaborative filtering, content-based filtering, atau pendekatan hybrid, sistem ini dapat meningkatkan pengalaman pengguna dengan memberikan saran makanan yang paling mungkin mereka nikmati.

### Contoh Kasus
Misalnya, pengguna yang menyukai makanan pedas dapat menerima rekomendasi untuk menu lain dengan karakteristik serupa, bahkan dari restoran berbeda. Sebaliknya, seorang vegetarian dapat diarahkan hanya pada pilihan yang sesuai dengan kebutuhannya.

## 2. Pentingnya Proyek
1. Meningkatkan Pengalaman Pengguna: Dengan memberikan rekomendasi yang relevan, pengguna tidak perlu lagi membuang waktu untuk mencari makanan yang mereka sukai. Ini meningkatkan kepuasan mereka dan loyalitas terhadap platform atau restoran.
2. Meningkatkan Pendapatan Layanan Makanan: Rekomendasi yang akurat dapat mendorong pengguna untuk mencoba lebih banyak item, meningkatkan transaksi, dan menciptakan peluang upselling (misalnya, menyarankan makanan pendamping).
3. Personalisasi yang Lebih Baik: Penggunaan data historis dan preferensi memungkinkan sistem untuk menyediakan layanan yang dipersonalisasi, yang kini menjadi ekspektasi pengguna di era digital.
4. Mengurangi Pilihan yang Berlebihan (Choice Overload): Dengan banyaknya opsi makanan yang tersedia, rekomendasi dapat menyederhanakan proses pengambilan keputusan dan mencegah kelelahan keputusan.
5. Potensi Pengembangan Bisnis: Restoran dan platform makanan dapat menggunakan wawasan dari sistem ini untuk mengidentifikasi tren makanan, merancang menu baru, atau meningkatkan strategi pemasaran.

# Business Understanding
Dalam konteks makanan, banyak pengguna sering merasa kewalahan dengan banyaknya pilihan yang tersedia. Mereka kesulitan menemukan makanan yang sesuai dengan preferensi mereka, baik karena keterbatasan informasi, waktu, maupun pengalaman. Hal ini menyebabkan pengalaman pengguna yang kurang optimal, penurunan loyalitas, dan potensi kehilangan pendapatan bagi platform makanan atau restoran.

## Problem Statements
1. Makanan apa yang  sesuai dengan preferensi mereka di antara banyaknya pilihan?
2. Makanan apa yang direkomendasikan berdasarkan rating pengguna.

## Goals
Pengguna mendapatkan rekomendasi makanan yang relevan dan dipersonalisasi oleh pengguna.
Pengguna mendapatkan rekomendasi data seperti nama makanan, jenis makanan, deskripsi, dan rating untuk memahami preferensi pengguna.

## Solution Approach
1. Content-Based Filtering

Deskripsi: Pendekatan ini menggunakan atribut makanan (seperti jenis makanan, deskripsi, bahan utama) untuk merekomendasikan makanan yang mirip dengan makanan yang telah disukai atau diberi rating tinggi oleh pengguna.
Cara Kerja: Menggunakan data fitur makanan, sistem menghitung tingkat kesamaan (misalnya, menggunakan cosine similarity) antara makanan yang pernah disukai pengguna dan makanan lainnya.
Keunggulan:
Tidak memerlukan data pengguna lain sehingga efektif untuk pengguna baru.
Rekomendasi sangat relevan karena didasarkan pada preferensi eksplisit pengguna.

2. Collaborative Filtering

Deskripsi: Pendekatan ini merekomendasikan makanan berdasarkan preferensi pengguna lain yang memiliki pola atau kesamaan preferensi dengan pengguna saat ini.
Cara Kerja:
User-based collaborative filtering: Sistem mencari pengguna lain yang memiliki pola rating yang mirip dengan pengguna saat ini dan merekomendasikan makanan yang mereka sukai.
Item-based collaborative filtering: Sistem mencari makanan yang sering diberi rating tinggi bersama oleh pengguna yang sama.
Keunggulan:
Tidak bergantung pada atribut makanan.
Dapat menemukan rekomendasi "non-tradisional" (makanan yang berbeda dari kebiasaan pengguna).

# Data Understanding
Untuk mencapai tujuannya, sistem rekomendasi ini dibuat dengan menggunakan data yang diambil dari https://www.kaggle.com/datasets/schemersays/food-recommendation-system. Data ini berisi dua data, yaitu makanan dan rating. Berikut ini data makana (food):

![image](https://github.com/user-attachments/assets/0a245946-19a5-48f2-887f-be0a439a9580)


Dengan rincian kolom atau variabel adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/22aeddad-a1d4-417b-a27a-274e034842fb)

Terdapat 5 kolom atau variabel dalam data makanan. yaitu
1. Food_ID. Data ini adalah data kode makanan dalam data.
2. Name. Data ini berisi nama makanan
3. C_Type. Data ini berisi kategori atau jenis makanan.
4. Veg_Non. Data ini menjelaskan kategori makanan yang dikategori vegan atau non vegan.
5. Describe. Data ini berisi penjelasan rici komposisi makanan atau masakan.

Data rating adalah seperti berikut:

![image](https://github.com/user-attachments/assets/73437fda-0f8c-4fbc-9dd6-192a7ffa381e)


Data rating meliputi berikut ini

![image](https://github.com/user-attachments/assets/67ba40ec-9b6d-46dc-a487-2eaf676e48be)

Terdapat tiga variabel pada dataset ini, yaitu:
1. User_ID. Data ini berisi ID dari pengguna atau konsumen yang memberikan peringkat makanan.
2. Food_ID. Data ini berisi ID atau kode makanan yang di review
3. Rating. Data ini berisi nilai peringkat atau review dari konsumen.

### Berikut ini adalah penjelasan data yang digunakan dalam sistem rekomendasi
Dari data makanan yang akan ada dapat ditampilakn makanan berdasarkan jenis kategorinya, sebagai berikut:

![image](https://github.com/user-attachments/assets/5ad6c437-d142-493b-8523-174691ac2424)

Hasil visualisasi data makanan berdasarkan jenis makanan, dapat dipahami bahwa jumlah makanan tertinggi dalam dataset adalah jenis makanan Indian (India). Sedangkan jumlah makanan yang yang terendah adalah jenis makanan korea dan spanyol. 
Berikut adalah rincian datanya:

![image](https://github.com/user-attachments/assets/d316499f-56a3-4850-b416-60396aad2773)

