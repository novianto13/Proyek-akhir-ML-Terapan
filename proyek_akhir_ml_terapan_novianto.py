# -*- coding: utf-8 -*-
"""Proyek akhir ML Terapan Novianto.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/187hrCS7CWfmt67QiaOl4JaqGz-cKn4jq

# Proyek akhir ML Terapan: Rekomendasi makanan

# Nama: Novianto

Proyek ini akan membuat sistem rekomendasi untuk makanan.

**Business Understanding**

Dalam konteks makanan, banyak pengguna sering merasa kewalahan dengan banyaknya pilihan yang tersedia. Mereka kesulitan menemukan makanan yang sesuai dengan preferensi mereka, baik karena keterbatasan informasi, waktu, maupun pengalaman. Hal ini menyebabkan pengalaman pengguna yang kurang optimal, penurunan loyalitas, dan potensi kehilangan pendapatan bagi platform makanan atau restoran.

**Problem Statements**
1. Makanan apa yang  sesuai dengan preferensi mereka di antara banyaknya pilihan?
2. Makanan apa yang direkomendasikan berdasarkan rating pengguna?

**Goals**

Pengguna mendapatkan rekomendasi makanan yang relevan dan dipersonalisasi oleh pengguna.
Pengguna mendapatkan rekomendasi data seperti nama makanan, jenis makanan, deskripsi, dan rating untuk memahami preferensi pengguna.


Berikut ini adalah langkah yang diperlukan untuk membuat sistem rekomendasi.

# 1. Pemahaman data

Berikut adalah import  library yang diperlukan dalam pembuatan rekomendasi sistem.
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

import re
import string

"""Sistem rekomendasi yang akan dibuat adalah sistem yang akan memberikan rekomendasi makanan berdasarkan rating makanan dalam dataset. Berikut adalah data makanan yang digunakan.

Datase pada proyek ini diambil dari Kaggle
https://www.kaggle.com/datasets/schemersays/food-recommendation-system
"""

food = pd.read_csv('https://raw.githubusercontent.com/novianto13/Proyek-akhir-ML-Terapan/main/Food.csv')
food.head()

food.info()

"""Data makanan terdiri dari 5 kolom. yaitu:
1. food_ID yang merupakan ID makanan
2. Nama makanan
3. C_Type yang menunjukkan jenis makanan
4. Veg_Non yang menunjukkan kategori makanan
5. Deskrisi makanan.

Dari info data menunjukkan bahwa terdapat 400 data dengan satu baris data yang nol atau kosong

Berikutnya adalah data rating yang menunjukkan peringkat makanan.
"""

rating = pd.read_csv('https://raw.githubusercontent.com/novianto13/Proyek-akhir-ML-Terapan/main/ratings.csv')
rating.head()

"""Data rating terdiri dari tiga kolom yaitu:
1. user ID yang menunjukkan ID konsumen
2. Food ID atau kode/ID makanan yang di review
3. Rating yang meunjukkan peringkat makanan
"""

rating.info()

"""Info  data menunjukkan bahsa ada 512 data dengan satu data nol.

## 1.1 Pemahaman Data food

Setelah load data, maka tahap ini kita akan memahami data lebih lanjut dengan visualisasi dan analisa data awal.
"""

sns.countplot(x='C_Type', data=food)
plt.title('Distribusi C_Type')
plt.xlabel('C_Type')
plt.ylabel('Jumlah')
plt.xticks(rotation=45, ha='right') # Rotasi label sumbu x jika diperlukan
plt.show()

"""Grafik di atas menunjukkan jumlah makanan dalam dataset berdasarkan jenis makanan.  Dari grafik tersebut maka dapat dipahami bahwa jenis makanan indian/india merupakan makanan yang paling banyak dalam menu."""

sns.countplot(x='Veg_Non', data=food)
plt.title('Distribusi Veg_Non')
plt.xlabel('Veg_Non')
plt.ylabel('Jumlah')
plt.show()

"""Grafik di atas adalah perbandingan jumlah kategori makanan vegan dan non vegan. grafik menunjukkan bahwa makanan yang masuk dalam kategori vegan lebih banyak dari pada non vegan."""

c_type_counts = food['C_Type'].value_counts()
veg_non_counts = food['Veg_Non'].value_counts()

print("Jumlah data pada C_Type:\n", c_type_counts)
print("\nJumlah data pada Veg_Non:\n", veg_non_counts)

"""Secara jelas, data di atas menunjukkan bahwa terdapat 88 jenis makanan India yang paling banyak dari pada jenis makanan yang lain."""

pd.crosstab(food['C_Type'], food['Veg_Non']).plot(kind='bar', stacked=True)
plt.title('Hubungan antara C_Type dan Veg_Non')
plt.xlabel('C_Type')
plt.ylabel('Jumlah')
plt.xticks(rotation=45, ha='right') # Rotasi label sumbu x jika diperlukan
plt.legend(title='Veg_Non')
plt.show()

"""Grafik di atas menunjukkan perbandingan kategori makanan pada setiap jenis makanan. Rincian data dapat dilihat pada keterangan berikut ini"""

cross_tab = pd.crosstab(food['C_Type'], food['Veg_Non'])
print(cross_tab)

"""Dari informasi di atas, dapat dipahami bahwa makanan india yang paling banyak adalah masuk kategori Non vegan, sedangkan makanan yang masuk kategori vegan yang paling banyak adalah masuk dalam jenis healty food.

## 1.2. Pemahaman data rating

Berikutnya adalah memahami data rating.
"""

rating.describe()

"""Data rating meruapakn data yang bersifat angka sehingga bisa dilihat statistik deskriptif. Statistik deskriptif menunjukkan bahwa rata-rata rating yang diberikan olejh pangguna adalah 5.4, sedangkan rating tertinggi adalah 10 dan terendah adalah 1."""

print('Jumlah user ID: ', len(rating.User_ID.unique()))
print('Jumlah food ID: ', len(rating.Food_ID.unique()))
print('Jumlah data rating: ', len(rating))

"""Informasi di atas menunjukkan bahwa  terdapat 512 data, namun ada 1 data yang memiliki nilai 0.

## 1.3. Penggabungan data

tahap ini dilakukan untuk mempersiapkan data yang akan digunakan dalam sistem rekomendasi.
"""

# Menggabungkan dataset food dan rating berdasarkan Food_ID
food_rating = pd.merge(food, rating, on='Food_ID', how='left')

# Menampilkan 5 baris pertama dari dataset yang sudah digabungkan
print(food_rating.head())

"""Kode di atas ditujukan untuk dapat menggabungkan data rating dan data food sehinga informasi yang diperoleh lebih lengkap."""

# Mengelompokkan data berdasarkan 'Food_Name' dan menghitung rata-rata rating
food_ratings = food_rating.groupby('Name')['Rating'].mean().reset_index()

# Mengurutkan data berdasarkan rating rata-rata secara descending dan mengambil 10 teratas
top_10_foods = food_ratings.sort_values(by=['Rating'], ascending=False).head(10)

# Menampilkan 10 nama makanan dengan rating tertinggi
print("10 Nama Makanan dengan Rating Tertinggi:\n", top_10_foods)

"""pada contoh di atas ini, kita dapat informasi makanan yang mendapatkan reting 10."""

# Mengelompokkan data berdasarkan 'Food_Name' dan menghitung rata-rata rating
food_ratings = food_rating.groupby('Name')['Rating'].mean().reset_index()

# Mengurutkan data berdasarkan rating rata-rata secara descending
sorted_ratings = food_ratings.sort_values(by=['Rating'], ascending=False)

# Mengambil 5 nama makanan dengan rating tertinggi
top_5_foods = sorted_ratings.head(5)

# Mengambil 5 nama makanan dengan rating terendah
bottom_5_foods = sorted_ratings.tail(5)

# Menampilkan hasil
print("5 Nama Makanan dengan Rating Tertinggi:\n", top_5_foods)
print("\n5 Nama Makanan dengan Rating Terendah:\n", bottom_5_foods)

"""Kita dapat melihat data makanan dengan rating tinggi dan rendah"""

# Menghitung jumlah data untuk setiap rating
rating_counts = food_rating['Rating'].value_counts()

# Menghitung jumlah total data
total_data = len(food_rating)

# Menampilkan hasil
print("Jumlah data berdasarkan rating:")
print(rating_counts)
print("\nJumlah total data:", total_data)

"""Hasil kode di atas menunjukkan barapa jumlah pengunjung atau konsumen yang memberikan review untuk setiap ratingnya. Dari informasi tersebut, mayoritas konsumen memmberikan raview pada rating 3, 5, 10."""

# Menghitung jumlah data untuk setiap rating
rating_counts = food_rating['Rating'].value_counts()

# Membuat grafik batang
plt.bar(rating_counts.index, rating_counts.values)

# Menambahkan label dan judul
plt.xlabel("Rating")
plt.ylabel("Jumlah Data")
plt.title("Jumlah Data Berdasarkan Rating")

# Menampilkan grafik
plt.show()

"""Grafik diatas menunjukkan visualisasi jumlah rating yang diberikan dari setiap konsumen."""

# manampilkan tabel rating dan jenis makanan

# Kelompokkan data dan hitung jumlah data
rating_food_counts = food_rating.groupby(['Rating', 'C_Type']).size().unstack(fill_value=0)

# Hitung total per kolom
total_per_column = rating_food_counts.sum()

# Buat baris baru untuk total
total_row = pd.DataFrame(data=[total_per_column.values], columns=total_per_column.index, index=['Total'])

# Gabungkan baris total dengan DataFrame asli
rating_food_counts = pd.concat([rating_food_counts, total_row])

# Hitung total per baris dan tambahkan kolom 'Jumlah'
rating_food_counts['Jumlah'] = rating_food_counts.sum(axis=1)

# Tampilkan tabel
print("Jumlah Data Berdasarkan Rating dan Jenis Makanan:")
display(rating_food_counts)

"""Dengan penggabungna dataset, maka kita dapat informasi yang lebih rinci untuk setiap jenis makanan dan hasil ratingnya.
DAri informasi tersebut, dapat diperoleh informasi bahwa makanan india merupakan makanan yang paling banyak mendapatkan rating tertinggi sekaligus yang paling banyak mendapatkan rating terendah.
Hal ini mungkin karena jenis makanan india adalah makanan yang paling banyak jumlahnya.
"""

# Mengambil data dari tabel rating_food_counts
rating_food_counts = food_rating.groupby(['Rating', 'C_Type']).size().unstack(fill_value=0)

# Membuat grafik batang bertumpuk
rating_food_counts.plot(kind='bar', stacked=True, figsize=(10, 6))

# Menambahkan label dan judul
plt.xlabel("Jenis Makanan (C_Type)")
plt.ylabel("Jumlah Data")
plt.title("Jumlah Data Berdasarkan Rating dan Jenis Makanan")
plt.xticks(rotation=45, ha='right')  # Rotasi label sumbu x agar mudah dibaca
plt.legend(title='Rating')

# Menampilkan grafik
plt.show()

"""Berikut adalah visualisasi yang menunjukkan jumlah rating pada setiap jenis makanan.

## 1.4. Cek data duplikat
"""

food_rating.duplicated().sum()

"""Hasil cek data duplikasi menunjukkan tidak ada data duplikat."""

# Pindahkan kolom 'User_ID' ke posisi paling kiri
food_rating = food_rating[['User_ID'] + [col for col in food_rating.columns if col != 'User_ID']]

# Menampilkan 5 baris pertama dari dataset yang sudah diubah
print(food_rating.head())

food_rating.info()

"""## 1.5. Cek data Kosong dan Nan"""

# Mengecek keberadaan nilai NaN di setiap kolom
print(food_rating.isna().any())

# Mengecek jumlah nilai NaN di setiap kolom
print(food_rating.isna().sum())

# Mengecek keberadaan data kosong di kolom bertipe object (string)
for col in food_rating.select_dtypes(include=['object']).columns:
    print(f"Kolom '{col}':")
    num_empty = food_rating[col].apply(lambda x: x.strip() == '').sum()
    print(f"  Jumlah data kosong: {num_empty}")

# Mengecek keberadaan nilai 0 di kolom numerik
for col in food_rating.select_dtypes(include=['number']).columns:
    print(f"Kolom '{col}':")
    num_zeros = (food_rating[col] == 0).sum()
    print(f"  Jumlah nilai 0: {num_zeros}")

# Menghitung jumlah data NaN di setiap kolom
na_counts = food_rating.isna().sum()

# Menampilkan jumlah total data NaN di seluruh dataset
total_na = na_counts.sum()

# Menampilkan hasil
print("Jumlah data NaN di setiap kolom:\n", na_counts)
print("\nTotal data NaN di seluruh dataset:", total_na)

"""# 2. Data Preprocessing dan Preparation

Tahapan ini dilakukan untuk mempersiapkan data supaya dapat dibbuat model dan proses lebih lanjut.

## 2.1. Cleaning data

Pada tahap ini, membersihkan data dari nilai-nilai yang hilang, duplikat. Langkah ini penting untuk memastikan kualitas data yang akan dianalisis lebih lanjut.

Hasil pemahaman data menunjukkan bahwa masalah data adalah hanya data NAN, yang terdapat pada kolom rating dan user id.

Oleh karena itu, langkah perbaikan data dilakukan dengan menghapus data NAN.
"""

# Menghapus baris yang mengandung nilai NaN
food_rating = food_rating.dropna()

# Menampilkan jumlah baris dan kolom setelah menghapus data NaN
print("Ukuran dataset setelah menghapus data NaN:", food_rating.shape)

"""Setelah data Nan dibapus, maka terdapat 511 data yang siap proses lanjut.

## 2.2. Perbaikan tipe data

Perbaikan tipe data ini supaya data angka dapat diperose lebih lanjut.
"""

# Mengubah tipe data kolom 'User_ID' dan 'Rating' menjadi int
food_rating['User_ID'] = food_rating['User_ID'].astype(int)
food_rating['Rating'] = food_rating['Rating'].astype(int)

# Menampilkan informasi tipe data dari dataset food_rating
print(food_rating.info())

"""Data yang diubah adalah User_ID, Food_D, dan Rating"""

# hasil gabungan data
food_rating.head(5)

"""## 2.3. Content Based Filtering

Membuat rekomendasi berdasarkan konten

### 2.3.1. TF-IDF Vectorizer

Pada tahap ini, kita akan membangun sistem rekomendasi sederhana berdasarkan jenis masakan yang disediakan restoran. Teknik ini juga akan digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap kategori masakan.
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data cuisine
tf.fit(food['C_Type'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(food['C_Type'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama resto

num_cols_to_sample = min(22, tfidf_matrix.shape[1])  # Ensure sample size doesn't exceed columns
num_rows_to_sample = min(10, tfidf_matrix.shape[0])  # Ensure sample size doesn't exceed rows

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=food.Name
).sample(num_cols_to_sample, axis=1, replace=False).sample(num_rows_to_sample, axis=0, replace=False)

"""### 2.3.2. Cosine similraity

Pada tahap sebelumnya, kita telah berhasil mengidentifikasi korelasi antara restoran dengan kategori masakannya. Sekarang, kita akan menghitung derajat kesamaan (similarity degree) antar restoran dengan teknik cosine similarity. Di sini, kita menggunakan fungsi cosine_similarity dari library sklearn.
"""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama resto
cosine_sim_df = pd.DataFrame(cosine_sim, index=food['Name'], columns=food['Name'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""### 2.3.3. Mendapatkan Rekomendasi

Sebelumnya, kita telah memiliki data similarity (kesamaan) antar makanan. selanjutnya adalah menhasilkan sejumlah makanan yang akan direkomendasikan kepada pengguna.


Di sini, kita membuat fungsi resto_recommendations dengan beberapa parameter sebagai berikut:

Nama_makanan : Nama restoran (index kemiripan dataframe).

Similarity_data : Dataframe mengenai similarity yang telah kita definisikan sebelumnya.

Items : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah ‘Name’ dan ‘C_Type’.

k : Banyak rekomendasi yang ingin diberikan.


Sebelum mulai menulis kodenya, ingatlah kembali definisi sistem rekomendasi yang menyatakan bahwa keluaran sistem ini adalah berupa top-N recommendation. Oleh karena itu, kita akan memberikan sejumlah rekomendasi restoran pada pengguna yang diatur dalam parameter k.
"""

def food_recommendations(nama_makanan, similarity_data=cosine_sim_df, items=food[['Name', 'C_Type']], k=5):
    """
    Rekomendasi Resto berdasarkan kemiripan dataframe

    Parameter:
    ---
    nama_food : tipe data string (str)
                Nama Restoran (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan resto sebagai
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_makanan].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_makanan, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""Dengan menggunakan argpartition, kita mengambil sejumlah nilai k tertinggi dari similarity data (dalam kasus ini: dataframe cosine_sim_df). Kemudian, kita mengambil data dari bobot (tingkat kesamaan) tertinggi ke terendah. Data ini dimasukkan ke dalam variabel closest. Berikutnya, kita perlu menghapus nama_resto yang yang dicari agar tidak muncul dalam daftar rekomendasi. Dalam kasus ini, nanti kita akan mencari resto yang mirip dengan christmas cake, sehingga kita perlu drop nama_makanan christmas cake agar tidak muncul dalam daftar rekomendasi yang diberikan nanti.  """

food[food.Name.eq('christmas cake')]

# Mendapatkan rekomendasi restoran yang mirip dengan chrismas cake
food_recommendations('christmas cake')

"""Berikut di atas adalah hasil dari sistem rekomendasi. Karena Christmas cake termasuk dalam dessert maka rekomenasi memunculkan menu dessert.

## 2.4. Collaborative Filtering

Collaborative filtering bergantung pada pendapat komunitas pengguna. Ia tidak memerlukan atribut untuk setiap itemnya seperti pada sistem berbasis konten. Collaborative filtering dibagi lagi menjadi dua kategori, yaitu: model based (metode berbasis model machine learning) dan memory based (metode berbasis memori).

### 2.4.1. Data preparation

Pertama, jangan lupa import semua library yang dibutuhkan. Seperti yang telah kita bahas sebelumnya, impor library di awal merupakan kebiasaan yang umum dilakukan oleh para praktisi data. Hal ini karena praktisi data kadang menggunakan IDE, tools, maupun lingkungan cloud lainnya. Sehingga, library perlu didefinisikan di awal.
"""

# Import library
import pandas as pd
import numpy as np
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt

# menunjukkan data yang akan diolah
rating.head()

#Checking the shape
rating.shape

# Checking for null values
rating.isnull().sum()

rating.info()

rating.tail()

# Removing the last row
rating = rating[:511]
rating.tail()

rating.head()

"""### 2.4.2. Encode Label

Pada tahap ini, Anda perlu melakukan persiapan data untuk menyandikan (encode) fitur ‘User_ID’ dan 'Food_ID' ke dalam indeks integer. Terapkan kode berikut.
"""

# Mengubah userID menjadi list tanpa nilai yang sama
user_ids = rating['User_ID'].unique().tolist()
print('list userID: ', user_ids)

# Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

"""Berikut adalah untuk Food_ID"""

# # Mengubah Food_ID menjadi list tanpa nilai yang sama
food_ids = rating['Food_ID'].unique().tolist()

# # Proses encoding placeID
food_to_food_encoded = {x: i for i, x in enumerate(food_ids)}

# # Proses decoding angka ke placeID
food_encoded_to_food = {i: x for i, x in enumerate(food_ids)}

"""---

Pemetaan User_ID dan Food_ID ke dataframe yang berkaitan.
"""

# Mapping Food ID ke dataframe food
rating['food'] = rating['Food_ID'].map(food_to_food_encoded)

# Cek apakah ada nilai NaN setelah mapping
if rating['food'].isnull().sum() > 0:
    print("Ada nilai NaN dalam kolom 'food' setelah mapping.")

# Cek jumlah unique Food_IDs
print("Unique Food_IDs:", len(rating['Food_ID'].unique()))

# Cek panjang mapping
print("Food to Food Encoded Length:", len(food_to_food_encoded))

# Cek apakah ada nilai Food_ID yang tidak termapping
unmapped_food_ids = set(rating['Food_ID']) - set(food_to_food_encoded.keys())
if unmapped_food_ids:
    print("Unmapped Food_IDs:", unmapped_food_ids)
else:
    print("All Food_IDs are mapped correctly.")

# Cek nilai NaN pada kolom food
print("Jumlah NaN pada kolom 'food':", rating['food'].isnull().sum())

# Tampilkan baris dengan nilai NaN
if rating['food'].isnull().sum() > 0:
    print("Baris dengan NaN di kolom 'food':")
    print(rating[rating['food'].isnull()])

# Proses encoding yang benar
food_to_food_encoded = {x: i for i, x in enumerate(food_ids)}
food_encoded_to_food = {i: x for i, x in enumerate(food_ids)}

# Mapping kolom 'Food_ID' ke 'food'
rating['food'] = rating['Food_ID'].map(food_to_food_encoded)

# Validasi nilai maksimum
# print("Max value in 'food':", rating['food'].max())
# assert rating['food'].max() < num_food, "Food ID encoding out of range!"

"""---

### 2.4.3. Mapping
"""

# Mapping userID ke dataframe user
rating['user'] = rating['User_ID'].map(user_to_user_encoded)

# Mapping placeID ke dataframe resto
rating['food'] = rating['Food_ID'].map(food_to_food_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah resto
num_food = len(food_to_food_encoded)
print(num_food)

# Mengubah rating menjadi nilai float
rating['Rating'] = rating['Rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(rating['Rating'])

# Nilai maksimal rating
max_rating = max(rating['Rating'])

print('Number of User: {}, Number of Food: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_food, min_rating, max_rating
))

"""Tahap persiapan telah selesai. Berikut adalah hal-hal yang telah kita lakukan pada tahap ini:

Memahami data rating yang kita miliki.
Menyandikan (encode) fitur ‘User_ID’ dan ‘placeID’ ke dalam indeks integer.
Memetakan ‘User_ID’ dan ‘pl 'Food_ID’ ke dataframe yang berkaitan.
Mengecek beberapa hal dalam data seperti jumlah user, jumlah makanan, kemudian mengubah nilai rating menjadi float.

### 2.4.4. Validasi

Membuat data random dari data rating
"""

# Mengacak dataset
rating = rating.sample(frac=1, random_state=42)
rating

"""---
### 2.4.5. Split data

kita bagi data train dan validasi dengan komposisi 80:20. Namun sebelumnya, kita perlu memetakan (mapping) data user dan makanan menjadi satu value terlebih dahulu. Lalu, buatlah rating dalam skala 0 sampai 1 agar mudah dalam melakukan proses training.
"""

# Membuat ulang x dan y
x = rating[['user', 'food']].values
y = rating['Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi dataset
train_indices = int(0.8 * rating.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

# Cek nilai di x_train[:, 1] yang lebih besar dari num_food - 1
invalid_food_ids = x_train[:, 1][x_train[:, 1] >= num_food]
print("Invalid Food IDs in x_train:", invalid_food_ids)

"""---"""

# # Membuat variabel x untuk mencocokkan data user dan resto menjadi satu value
# x = rating[['user', 'food']].values

# # Membuat variabel y untuk membuat rating dari hasil
# y = rating['Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# # Membagi menjadi 80% data train dan 20% data validasi
# train_indices = int(0.8 * rating.shape[0])
# x_train, x_val, y_train, y_val = (
#     x[:train_indices],
#     x[train_indices:],
#     y[:train_indices],
#     y[train_indices:]
# )

# print(x, y)

"""###  2.4.6. Training

Pada tahap ini, model menghitung skor kecocokan antara pengguna dan makanan dengan teknik embedding. Pertama, kita melakukan proses embedding terhadap data user dan resto. Selanjutnya, lakukan operasi perkalian dot product antara embedding user dan food. Selain itu, kita juga dapat menambahkan bias untuk setiap user dan food. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid.

Di sini, kita membuat class RecommenderNet dengan keras Model class. Kode class RecommenderNet ini terinspirasi dari tutorial dalam situs Keras dengan beberapa adaptasi sesuai kasus yang sedang kita selesaikan. Terapkan kode berikut.
"""

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_food, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_food = num_food
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.food_embedding = layers.Embedding( # layer embeddings food
        num_food,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.food_bias = layers.Embedding(num_food, 1) # layer embedding resto bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    food_vector = self.food_embedding(inputs[:, -1]) # memanggil layer embedding 3
    food_bias = self.food_bias(inputs[:, -1]) # memanggil layer embedding 4

    dot_user_food = tf.tensordot(user_vector, food_vector, 2)

    x = dot_user_food + user_bias + food_bias

    return tf.nn.sigmoid(x) # activation sigmoid

"""# 3. Modeling

Model ini menggunakan Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer, dan root mean squared error (RMSE) sebagai metrics evaluation.
"""

model = RecommenderNet(num_users, num_food, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Proses training adalah sebagai berikut"""

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

"""### Visualisasi Metrik

Untuk melihat visualisasi proses training, mari kita plot metrik evaluasi dengan matplotlib. Terapkan kode berikut.
"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""proses training model cukup smooth dan model konvergen pada epochs sekitar 100. Dari proses ini, kita memperoleh nilai error akhir sebesar sekitar 0.19 dan error pada data validasi di atas 0.34.

## Mendapatkan Rekomendasi makanan

Untuk mendapatkan rekomendasi makanan, pertama kita ambil sampel user secara acak dan definisikan variabel food_not_reviewed yang merupakan daftar resto yang belum pernah dikunjungi oleh pengguna, menentukan daftar resto_not_revies perlu karena Hal ini karena daftar food_not_review inilah yang akan menjadi resto yang kita rekomendasikan.
"""

food_df = food_rating
df = rating

# Mengambil sample user
user_id = df.User_ID.sample(1).iloc[0]
food_review_by_user = df[df.Food_ID == user_id]


# Operator bitwise (~), bisa diketahui di sini https://docs.python.org/3/reference/expressions.html
# Mengganti 'id' dengan 'Food_ID'
food_not_review = food_df[~food_df['Food_ID'].isin(food_review_by_user.Food_ID.values)]['Food_ID']
food_not_review = list(
    set(food_not_review)
    .intersection(set(food_to_food_encoded.keys()))
)

# Mengganti 'review_not_review' dengan 'food_not_review' dan 'User_ID' dengan 'user_id'
food_not_review = [[food_to_food_encoded.get(x)] for x in food_not_review]
user_encoder = user_to_user_encoded.get(user_id)
user_food_array = np.hstack(
    ([[user_encoder]] * len(food_not_review), food_not_review)
)

"""Selanjutnya, untuk memperoleh rekomendasi restoran, gunakan fungsi model.predict() dari library Keras dengan menerapkan kode berikut."""

ratings = model.predict(user_food_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_food_ids = [
    food_encoded_to_food.get(food_not_review[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Food with high ratings from user')
print('----' * 8)

top_food_user = (
    food_review_by_user.sort_values(
        by='Rating',
        ascending=False
    )
    .head(5)
    .Food_ID.values
)

food_df_rows = food_df[food_df['Food_ID'].isin(top_food_user)]
# Remove duplicate rows based on 'Name' and 'C_Type'
food_df_rows = food_df_rows.drop_duplicates(subset=['Name', 'C_Type'])

for row in food_df_rows.itertuples():
    print(row.Name, ':', row.C_Type)

print('----' * 8)
print('Top 10 food recommendation')
print('----' * 8)

recommended_food = food_df[food_df['Food_ID'].isin(recommended_food_ids)]
# Remove duplicate rows based on 'Name' and 'C_Type'
recommended_food = recommended_food.drop_duplicates(subset=['Name', 'C_Type'])

for row in recommended_food.itertuples():
    print(row.Name, ':', row.C_Type)

"""# Evaluasi"""