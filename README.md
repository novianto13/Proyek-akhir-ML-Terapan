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
### 1. Data food

Dari data makanan yang akan ada dapat ditampilakn makanan berdasarkan jenis kategorinya, sebagai berikut:

![image](https://github.com/user-attachments/assets/5ad6c437-d142-493b-8523-174691ac2424)

Hasil visualisasi data makanan berdasarkan jenis makanan, dapat dipahami bahwa jumlah makanan tiga tertinggi dalam dataset adalah jenis makanan Indian (India), healty food, dan dessert. Sedangkan jumlah makanan yang yang terendah adalah jenis makanan korea dan spanyol. 
Berikut adalah rincian datanya:

![image](https://github.com/user-attachments/assets/d316499f-56a3-4850-b416-60396aad2773)

Dari data makan yang direview, makanan juga dibagi ke dalam dua kelompok, yaitu vegan dan non-vegan.

![image](https://github.com/user-attachments/assets/2052f23a-3994-4288-adb1-99de3728d553)

Dari gambar tersebut di atas, diperoleh informasi bahwa makanan vegan merupakan jenis makanan yang jumlahnya lebih banyak tersedia dari makanan yang non vegan.

Hubungan antara jenis makanan dan kategori makanan dapat ditunjukkan sebagai berikut:

![image](https://github.com/user-attachments/assets/628208c2-38ff-4e7f-832e-ea800cd5b8e8)

Dari gambar di atas dapat dimaknai sebagai berikut:
1. Dari jenis makanan non vegan, kategori makanan tiga terbanyak adalah makanan indian, chinese, dan thai.
3. Dari jenis makanan vegan, kategori makanan tiga terbanyak adalah makanan dessert, healty food, dan indian.

### 2 Data rating
Berikut adalah gambaran data rating dalam dataset:

![image](https://github.com/user-attachments/assets/96732922-7ff4-4f6f-b6e0-321fc4fd6449)


Dari data rating tersebut, terdapat tiga kolom atau variabel. yaitu
1. User_ID. Data ini adalah data terkait dengan ID pengguna yang memberikan rating pada makana yang ada.
2. Food_ID. Data ini berisi kode atau ID makanan yang ada dalam set
3. Rating. Berisi peringkat yang diberikan oleh konsumen terhadap makanan yang ada.

Deskripsi data rating adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/a4335dcd-197b-469a-90f5-5e9e9dabea22)

Poin utama dalam data tersebut adalah pada bagian rating, yang dapat dimaknai sebagai berikut:
1. Rata-rata nilai rating pada makanan adalah 5,4. Nilai ini adalah nilai tengah dimana rating nilai adalah 1 sampai 10.
2. Nilai terendah yang diberikan oleh konsumen pada makana adalah 1
3. Nilai tertinggi yang diberikan oleh konsumen adalah 10.

Untuk dapat melihat rating makanan, maka data dapat dikelompokkan berdasarkan jenis manakan dan ratingnya. Kaitan antara jenis makanan dan rating dapat dilihat pada gambar berikut

![image](https://github.com/user-attachments/assets/1e488f5e-4acf-419c-9bd2-6d701ad9c9ff)

![image](https://github.com/user-attachments/assets/c6e8a52c-3062-42ee-a4d7-1415fac8cd2f)

Gambar tersebut diperoleh dari tabel berikut ini:

![image](https://github.com/user-attachments/assets/affcd1cb-d358-4f8c-8e8d-aba80c260b46)

Dari rating jemis makan tersebut dapat dimaknai sebagai berikut:
1. Total konsumen yang memberikan review ada 511 orang.
2. Konsumen yang memberikan review 3 terbanyak adalah rating 3 (63 konsumen), kemudian rating 5 dan rating 10 yang masing-masing 61 konsumen. Kondisi ini menunjukkan orang 
3. Banyaknya makanan yang review adalah makanan indian, dan sekaligus makanan yang mendapatkan jumlah rating 10 terbanyak dibandingkan makanan lainnya, yaitu 14 konsumen dari 61 konsumen yang memberikan rating 10. Sekaligus jenis makanan yang paling banyak mendapatkan nilai terendah dari konsumen, yaitu 12 konsumen dari total 48 konnsumen yang memberikan nilai rating 1.

Kesimpulan dari data ini:

Makanan Indian merupakan jenis makanan yang paling banyak dipesan konsumen. Jenis makanan ini juga merupakan jenis kelompok yang mendapatkan penilaian tertinggi dan terendah paling banyak dari konsumen. 

# Data prepocessing
Tahapan data preprocessing dilakukan untuk mempersiapkan data yang akan diolah. tahapan dilakukan dengan:

Menggambungkan dua data set, yaitu data food dan data rating. penggambungan data ini didasarkan pada Food_ID, supaya hasilnya diurutkan berdasarkan Food_ID.

![image](https://github.com/user-attachments/assets/6cdbaf4d-ae50-485d-a2e1-5d7abee0739c)

Hasilnya adalah sebagai sebagai berikut

![image](https://github.com/user-attachments/assets/3feb02fe-9677-4371-b501-58bfb532b6a4)

# Data Preparation
Tahapan ini merupakan lanjutan dari tahap prepocessing yang dilakukan untuk mempersiapakn data 


