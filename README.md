# Proyek-akhir-ML-Terapan
### Proyek akhir: Novianto

# 1. Project Overview
## 1.1. Latar Belakang Masalah
Sistem rekomendasi telah menjadi alat penting dalam membantu pengguna membuat keputusan yang tepat dalam berbagai sektor, termasuk e-commerce, streaming, dan makanan. Dalam konteks makanan, pengguna sering dihadapkan dengan banyaknya pilihan makanan yang tersedia, baik di restoran maupun dalam layanan pesan antar. Hal ini dapat menyebabkan kebingungan dan membuat mereka kesulitan memilih makanan yang sesuai dengan preferensi pribadi.

Sistem rekomendasi makanan dirancang untuk memanfaatkan data seperti nama makanan, jenis makanan, deskripsi, dan rating pengguna untuk menawarkan rekomendasi yang relevan dan dipersonalisasi. Dengan memanfaatkan algoritma seperti collaborative filtering, content-based filtering, atau pendekatan hybrid, sistem ini dapat meningkatkan pengalaman pengguna dengan memberikan saran makanan yang paling mungkin mereka nikmati.

### 1.2. Contoh Kasus
Misalnya, pengguna yang menyukai makanan pedas dapat menerima rekomendasi untuk menu lain dengan karakteristik serupa, bahkan dari restoran berbeda. Sebaliknya, seorang vegetarian dapat diarahkan hanya pada pilihan yang sesuai dengan kebutuhannya.

## 1.3. Pentingnya Proyek 
1. Meningkatkan Pengalaman Pengguna: Dengan memberikan rekomendasi yang relevan, pengguna tidak perlu lagi membuang waktu untuk mencari makanan yang mereka sukai. Ini meningkatkan kepuasan mereka dan loyalitas terhadap platform atau restoran.
2. Meningkatkan Pendapatan Layanan Makanan: Rekomendasi yang akurat dapat mendorong pengguna untuk mencoba lebih banyak item, meningkatkan transaksi, dan menciptakan peluang upselling (misalnya, menyarankan makanan pendamping).
3. Personalisasi yang Lebih Baik: Penggunaan data historis dan preferensi memungkinkan sistem untuk menyediakan layanan yang dipersonalisasi, yang kini menjadi ekspektasi pengguna di era digital.
4. Mengurangi Pilihan yang Berlebihan (Choice Overload): Dengan banyaknya opsi makanan yang tersedia, rekomendasi dapat menyederhanakan proses pengambilan keputusan dan mencegah kelelahan keputusan.
5. Potensi Pengembangan Bisnis: Restoran dan platform makanan dapat menggunakan wawasan dari sistem ini untuk mengidentifikasi tren makanan, merancang menu baru, atau meningkatkan strategi pemasaran.

# 2. Business Understanding
Dalam konteks makanan, banyak pengguna sering merasa kewalahan dengan banyaknya pilihan yang tersedia. Mereka kesulitan menemukan makanan yang sesuai dengan preferensi mereka, baik karena keterbatasan informasi, waktu, maupun pengalaman. Hal ini menyebabkan pengalaman pengguna yang kurang optimal, penurunan loyalitas, dan potensi kehilangan pendapatan bagi platform makanan atau restoran.

## 2.1. Problem Statements
1. Makanan apa yang  sesuai dengan preferensi mereka di antara banyaknya pilihan?
2. Makanan apa yang direkomendasikan berdasarkan rating pengguna?

## 2.2. Goals
Pengguna mendapatkan rekomendasi makanan yang relevan dan dipersonalisasi oleh pengguna.
Pengguna mendapatkan rekomendasi data seperti nama makanan, jenis makanan, deskripsi, dan rating untuk memahami preferensi pengguna.

## 2.3. Solution Approach
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

# 3. Data Understanding
Untuk mencapai tujuannya, sistem rekomendasi ini dibuat dengan menggunakan data yang diambil dari https://www.kaggle.com/datasets/schemersays/food-recommendation-system. 
Data ini berisi dua data, yaitu makanan dan rating. 

Berikut ini data makanan (food):

![image](https://github.com/user-attachments/assets/0a245946-19a5-48f2-887f-be0a439a9580)

Dengan rincian kolom atau variabel adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/22aeddad-a1d4-417b-a27a-274e034842fb)

Terdapat 5 kolom atau variabel dalam data makanan. yaitu
1. Food_ID. Data ini adalah data kode makanan dalam data.
2. Name. Data ini berisi nama makanan
3. C_Type. Data ini berisi kategori atau jenis makanan.
4. Veg_Non. Data ini menjelaskan kategori makanan yang dikategori vegan atau non vegan.
5. Describe. Data ini berisi penjelasan rici komposisi makanan atau masakan.

Dari info data menunjukkan bahwa terdapat 400 data dengan satu baris data yang nol atau kosong

Data rating adalah seperti berikut:

![image](https://github.com/user-attachments/assets/73437fda-0f8c-4fbc-9dd6-192a7ffa381e)


Data rating meliputi berikut ini

![image](https://github.com/user-attachments/assets/67ba40ec-9b6d-46dc-a487-2eaf676e48be)

Terdapat tiga variabel pada dataset ini, yaitu:
1. User_ID. Data ini berisi ID dari pengguna atau konsumen yang memberikan peringkat makanan.
2. Food_ID. Data ini berisi ID atau kode makanan yang di review
3. Rating. Data ini berisi nilai peringkat atau review dari konsumen.

Info data menunjukkan bahsa ada 512 data dengan satu data nol.

## 3.1. Berikut ini adalah penjelasan data yang digunakan dalam sistem rekomendasi
### 3.1.1. Data food

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

### 3.1.2 Data rating
Berikut adalah gambaran data rating dalam dataset:

![image](https://github.com/user-attachments/assets/96732922-7ff4-4f6f-b6e0-321fc4fd6449)


Dari data rating tersebut, terdapat tiga kolom atau variabel. yaitu
1. User_ID. Data ini adalah data terkait dengan ID pengguna yang memberikan rating pada makana yang ada.
2. Food_ID. Data ini berisi kode atau ID makanan yang ada dalam set
3. Rating. Berisi peringkat yang diberikan oleh konsumen terhadap makanan yang ada.

Info data menunjukkan bahwa:
1. Jumlah user ID:  101
2. Jumlah food ID:  310
3. Jumlah data rating:  512
Informasi di atas menunjukkan bahwa terdapat 512 data, namun ada 1 data yang memiliki nilai 0.

Deskripsi statistik data rating adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/a4335dcd-197b-469a-90f5-5e9e9dabea22)

Poin utama dalam data tersebut adalah pada bagian rating, yang dapat dimaknai sebagai berikut:
1. Rata-rata nilai rating pada makanan adalah 5,4. Nilai ini adalah nilai tengah dimana rating nilai adalah 1 sampai 10.
2. Nilai terendah yang diberikan oleh konsumen pada makana adalah 1
3. Nilai tertinggi yang diberikan oleh konsumen adalah 10.

## 3.2. Gabungan data food dan rating

Menggambungkan dua data set, yaitu data food dan data rating. penggambungan data ini didasarkan pada Food_ID, supaya hasilnya diurutkan berdasarkan Food_ID.

![image](https://github.com/user-attachments/assets/6cdbaf4d-ae50-485d-a2e1-5d7abee0739c)

Hasilnya adalah sebagai sebagai berikut

![image](https://github.com/user-attachments/assets/3feb02fe-9677-4371-b501-58bfb532b6a4)

Untuk dapat melihat rating makanan, maka data dapat dikelompokkan berdasarkan jenis manakan dan ratingnya. Kaitan antara jenis makanan dan rating dapat dilihat pada gambar berikut

![image](https://github.com/user-attachments/assets/1e488f5e-4acf-419c-9bd2-6d701ad9c9ff)

![image](https://github.com/user-attachments/assets/c6e8a52c-3062-42ee-a4d7-1415fac8cd2f)

Gambar tersebut diperoleh dari tabel berikut ini:

![image](https://github.com/user-attachments/assets/affcd1cb-d358-4f8c-8e8d-aba80c260b46)

Dari rating jemis makan tersebut dapat dimaknai sebagai berikut:
1. Total konsumen yang memberikan review ada 511 konsumen yang memberikan rating (dari total data 602).
2. Konsumen yang memberikan review 3 terbanyak adalah rating 3 (63 konsumen), kemudian rating 5 dan rating 10 yang masing-masing 61 konsumen. Kondisi ini menunjukkan orang 
3. Banyaknya makanan yang review adalah makanan indian, dan sekaligus makanan yang mendapatkan jumlah rating 10 terbanyak dibandingkan makanan lainnya, yaitu 14 konsumen dari 61 konsumen yang memberikan rating 10. Sekaligus jenis makanan yang paling banyak mendapatkan nilai terendah dari konsumen, yaitu 12 konsumen dari total 48 konnsumen yang memberikan nilai rating 1.

Kesimpulan dari data ini:

Makanan Indian merupakan jenis makanan yang paling banyak dipesan konsumen. Jenis makanan ini juga merupakan jenis kelompok yang mendapatkan penilaian tertinggi dan terendah paling banyak dari konsumen. 

## 3.3. Cek Dataset 
Tahapan ini dilakukan untuk melihat kondisi data:
1. cek data kosong
2. cek data duplikasi

**1. Cek data kosong**
Cek data dilakukan dengan kode sebagia berikut:

![image](https://github.com/user-attachments/assets/e2155ae7-6440-45a4-957a-f36fa5d5cc04)

hasilnya:

![image](https://github.com/user-attachments/assets/50def69c-d17a-4fee-a02b-01fd6c26758f)

Dari hasil tersebut dapat dipahami bahwa terdapat nilai yang mengandung nilai NA adalah 91 dari data User ID dan Rating.

Cek data kosong hasilnya adalah 

![image](https://github.com/user-attachments/assets/b48d865a-47c2-4a8b-8177-01c3f7e568cf)

Dari informasi tersebut maka dapat dimaknai bahwa dapat tidak ada data kosong, namun data yang kosong sudah terisi dengan NAN sebanyak 91. 

**2. Cek data duplikat:**

food_rating.duplicated().sum()

Hasilnya duplikasi data adalah 0. Hal ini, menunjukkan tidak ada data yang duplikat.


# 4. Data Preparation
Tahapan data preprocessing dilakukan untuk mempersiapkan data yang akan diolah. 

## 4.1. Handling Missing value
Pada tahap ini dilakukan membersihkan data dari nilai-nilai yang hilang, duplikat. Langkah ini penting untuk memastikan kualitas data yang akan dianalisis lebih lanjut. Hasil pemahaman data menunjukkan bahwa masalah data adalah hanya data NAN, yang terdapat pada kolom rating dan user id. Oleh karena itu, langkah perbaikan data dilakukan dengan menghapus data NAN.

Data yang kosong atau NAN  dihapus dengan kode berikut:

![image](https://github.com/user-attachments/assets/e4377a1a-749e-4ded-b671-09e6518a1fac)

Setelah data NA dihapus, maka terdapat 511 data yang bisa diolah.

## 4.2. Content Based Filtering

Model pertama yang dibuat untuk sistem rekomendasi adalah membuat model dengan pendekatan Content Based Filtering. Pembuatan model ini dilakukan dengan tahapan:
1. Vektorisasi: TF-IDF Vectorizer
2. Cosine Similarity
3. Membuat rekomendasi

### 4.2.1. Vektorisasi: TF-IDF Vectorizer

Pada tahap ini, kita akan membangun sistem rekomendasi sederhana berdasarkan jenis masakan yang disediakan restoran. Teknik ini juga akan digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap kategori masakan.

a. Vektorisasi dilakukan berdasarkan jenis makanan dari data C_Type. 

![image](https://github.com/user-attachments/assets/02e59832-b0e3-430e-8996-99d9a1e4b9f9)

Berikut penjelasan singkatnya:

Membuat vektor TF IDF: tf = TfidfVectorizer(): Baris ini membuat instance TfidfVectorizer dan menetapkannya ke variabel tf. Anggap saja ini seperti menyiapkan mesin untuk memproses data teks.


Fiting vectorizer adalah dengan kode: tf.fit(food['C_Type']): Baris ini adalah tempat mesin (TfidfVectorizer) mempelajari kosakata kolom 'C_Type' dalam kerangka data makanan. C_Type kemungkinan merujuk pada jenis masakan makanan. Langkah ini penting karena membantu model memahami pentingnya setiap kata dalam konteks masakan yang berbeda.

b. membuat fit tfidf matrix 

![image](https://github.com/user-attachments/assets/55938435-b731-480c-9584-f85385e3a768)

Keterangan:

fit: Mempelajari kosakata dan bobot IDF (Inverse Document Frequency) dari kolom 'C_Type' pada food DataFrame. Kolom ini kemungkinan berisi informasi tentang jenis masakan untuk setiap item makanan.

transform: Mengonversi jenis masakan menjadi representasi numerik yang disebut matriks TF-IDF, di mana setiap baris mewakili item makanan dan setiap kolom mewakili kata unik dalam jenis masakan. Nilai dalam matriks mewakili skor TF-IDF, yang menunjukkan pentingnya setiap kata dalam jenis masakan setiap item makanan.

![image](https://github.com/user-attachments/assets/d855731b-45f5-46fd-927d-a3e24638a6ed)

Untuk dapat melihat matriks dalam data frame yang lebih jelas maka matriks dapat ditampilakn dalam tampilan berikut ini:

![image](https://github.com/user-attachments/assets/c2d646a1-99f7-4154-86c7-d9b3c178e1b4)

Katerangan:

pd.DataFrame(): Ini adalah fungsi dari pustaka pandas yang digunakan untuk membuat DataFrame, yang seperti tabel dalam Python.

tfidf_matrix.todense(): Ini mengonversi matriks TF-IDF (yang disimpan dalam format khusus yang hemat memori) menjadi matriks padat dan teratur yang dapat dilihat dengan mudah.
columns=tf.get_feature_names_out(): Ini menetapkan nama fitur (jenis masakan) yang diekstrak oleh TfidfVectorizer sebagai tajuk kolom DataFrame.

index=food.Name: Ini menetapkan nama item makanan sebagai label baris (indeks) DataFrame

Hasil matrik tersebut menunjukan adanya nilai 1 antar dua data, angka tersebut menunjukkan bahwa kaitan jenis makanan dan nama makannya.

### 4.2.2. Cosine similarity

Pada tahap sebelumnya, kita telah berhasil mengidentifikasi korelasi antara restoran dengan kategori masakannya. Sekarang, kita akan menghitung derajat kesamaan (similarity degree) antar restoran dengan teknik cosine similarity. Di sini, kita menggunakan fungsi cosine_similarity dari library sklearn.

![image](https://github.com/user-attachments/assets/c8397199-c7a5-41ee-970c-58d2b6318538)


![image](https://github.com/user-attachments/assets/65a68e59-852c-4181-8fee-fcac0f7ab149)


### 4.2.3. Mendapatkan rekomendasi
Sebelumnya, kita telah memiliki data similarity (kesamaan) antar makanan. selanjutnya adalah menhasilkan sejumlah makanan yang akan direkomendasikan kepada pengguna. Di sini, kita membuat fungsi resto_recommendations dengan beberapa parameter sebagai berikut:

Nama_makanan : Nama restoran (index kemiripan dataframe).

Similarity_data : Dataframe mengenai similarity yang telah kita definisikan sebelumnya.

Items : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah ‘Name’ dan ‘C_Type’.

k : Banyak rekomendasi yang ingin diberikan.

Sebelum mulai menulis kodenya, ingatlah kembali definisi sistem rekomendasi yang menyatakan bahwa keluaran sistem ini adalah berupa top-N recommendation. Oleh karena itu, kita akan memberikan sejumlah rekomendasi restoran pada pengguna yang diatur dalam parameter k.

Untuk mendapatkan rekomendasi berbasis konten, maka perlu membuat fungsi terlebih dahulu, berikut adalah:

def food_recommendations(nama_makanan, similarity_data=cosine_sim_df, items=food[['Name', 'C_Type']], k=5):

index = similarity_data.loc[:,nama_makanan].to_numpy().argpartition(
        range(-1, -k, -1))

 closest = similarity_data.columns[index[-1:-(k+2):-1]]

closest = closest.drop(nama_makanan, errors='ignore')

return pd.DataFrame(closest).merge(items).head(k)


Keterangan:
Fungsi ini bertujuan untuk memberikan rekomendasi restoran berdasarkan kemiripan dengan restoran yang diberikan.

Parameter:
nama_makanan: Tipe data string (str). Nama restoran yang akan dijadikan acuan untuk mencari kemiripan.

similarity_data: Tipe data pd.DataFrame. Dataframe yang berisi nilai kemiripan antar restoran, simetrik dengan restoran sebagai indeks dan kolom.
items: Tipe data pd.DataFrame. Dataframe yang berisi nama restoran dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan.
k: Tipe data integer (int). Jumlah rekomendasi yang akan diberikan.

Langkah-langkah dalam fungsi:
1. Mengambil indeks restoran dengan kemiripan tertinggi:
- Menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan. Dataframe diubah menjadi numpy array untuk mempermudah proses ini.
- range(-1, -k, -1) digunakan untuk mengambil k nilai terbesar dari kemiripan.

2. Mengambil nama restoran dengan kemiripan tertinggi:
- Menggunakan indeks yang diperoleh dari langkah sebelumnya untuk mendapatkan nama restoran dengan kemiripan tertinggi.
- index[-1:-(k+2):-1] digunakan untuk mengurutkan dan mengambil k nilai terbesar.

3. Menghapus nama restoran yang dicari dari daftar rekomendasi:
- Menggunakan drop untuk memastikan restoran yang dicari tidak muncul dalam daftar rekomendasi.

4. Menggabungkan hasil dengan dataframe items:
- Menggunakan merge untuk menggabungkan hasil rekomendasi dengan dataframe items agar informasi tambahan tentang restoran juga disertakan.
- Menggunakan head(k) untuk memastikan hanya k rekomendasi yang diberikan.


Pada akhirnya kita akan menjalankan fungsi tersebut. 
Pertama kita akan mencoba melihat data. Sebagai contoh kita mengambil data dengan nama makanan chrismas cake dengan kode:

food[food.Name.eq('christmas cake')]

Dengan menggunakan argpartition, kita mengambil sejumlah nilai k tertinggi dari similarity data (dalam kasus ini: dataframe cosine_sim_df). Kemudian, kita mengambil data dari bobot (tingkat kesamaan) tertinggi ke terendah. Data ini dimasukkan ke dalam variabel closest. Berikutnya, kita perlu menghapus nama_resto yang yang dicari agar tidak muncul dalam daftar rekomendasi. Dalam kasus ini, nanti kita akan mencari resto yang mirip dengan christmas cake, sehingga kita perlu drop nama_makanan christmas cake agar tidak muncul dalam daftar rekomendasi yang diberikan nanti.
hasilnya adalah:

![image](https://github.com/user-attachments/assets/b26bb49b-5520-4abe-8b71-24a55b1df05f)

Kedua kita akan meminta rekomendasi makanan yang mirip dengan chrismas cake dengan kode:

food_recommendations('christmas cake')

![image](https://github.com/user-attachments/assets/ca170395-82d6-4c84-b815-1c83a483a210)

Hasilnya adalah makanan yang mirip dengan chrismas cake adalah: 
1. chocolate kaju katli	
2. eggless vanilla cake	
3. sweet potato pie	
4. eggless coffee cupcakes	
5. plum cake	

Semua rekomendasi tersebut adalah masuk dalam kategori dessert yang sama dengan yang kategori chrismas cake

## 4.3. Collaborative Filtering
Collaborative filtering bergantung pada pendapat komunitas pengguna. Ia tidak memerlukan atribut untuk setiap itemnya seperti pada sistem berbasis konten. Collaborative filtering dibagi lagi menjadi dua kategori, yaitu: model based (metode berbasis model machine learning) dan memory based (metode berbasis memori).

Untuk melakukan sistem rekomendasi dengan Collaborative Filtering, kita akan mempersiapkan  data rating. Langkah untuk melakukan collaborative filtering adalah
1. Encode label
2. validasi
3. training data
4. visualisasi metrik
5. rekomendasi makanan

### 4.3.1. Encode label
Pada tahap ini, Anda perlu melakukan persiapan data untuk menyandikan (encode) fitur ‘User_ID’ dan 'Food_ID' ke dalam indeks integer. Terapkan kode berikut.

**1. langkah pertama adalah ini dilakukan dengna membuat kode untuk melakukan encoded pada data rating.** 
Kodenya adalah sebagai berikut

![image](https://github.com/user-attachments/assets/111d0cbd-aed1-41c1-a9da-1e209abe29b2)

Kode ini bertujuan untuk mengubah User_ID menjadi bentuk yang lebih mudah diproses oleh model pembelajaran mesin, yaitu dengan melakukan encoding pada User_ID. Encoding ini mengubah User_ID menjadi angka unik yang sesuai dengan indeksnya.

Keterangan Kode:
- Mengubah User_ID menjadi list tanpa nilai yang sama:

user_ids = rating['User_ID'].unique().tolist()
print('list userID: ', user_ids)
rating['User_ID'].unique() mengambil semua nilai unik dari kolom User_ID dalam dataframe rating.

.tolist() mengubah array hasil dari unique() menjadi list Python.

print digunakan untuk menampilkan list user_ids.

- Melakukan encoding User_ID:

user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

{x: i for i, x in enumerate(user_ids)} adalah dictionary comprehension yang membuat dictionary dengan User_ID sebagai kunci dan indeksnya sebagai nilai.

enumerate(user_ids) memberikan pasangan indeks dan nilai dari user_ids.
print digunakan untuk menampilkan dictionary user_to_user_encoded.

- Melakukan proses encoding angka ke User_ID:

user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

{i: x for i, x in enumerate(user_ids)} adalah dictionary comprehension yang membuat dictionary dengan indeks sebagai kunci dan User_ID sebagai nilai.

print digunakan untuk menampilkan dictionary user_encoded_to_user.

hasilnya

![image](https://github.com/user-attachments/assets/b2f9e90b-40c7-48e1-b039-235bf0983ed5)

Kode ini membantu dalam proses transformasi User_ID menjadi bentuk yang lebih mudah diproses oleh model pembelajaran mesin dengan melakukan encoding dua arah: dari User_ID ke angka dan sebaliknya. Ini sangat berguna dalam sistem rekomendasi atau model lain yang memerlukan representasi numerik dari data kategorikal.

**2. Mempersiapkan data makanan**

Kodenya

![image](https://github.com/user-attachments/assets/1ab14d54-96d1-434e-a637-99d1e572798b)

Kode ini bertujuan untuk mengubah Food_ID menjadi bentuk yang lebih mudah diproses oleh model pembelajaran mesin, yaitu dengan melakukan encoding pada Food_ID. Encoding ini mengubah Food_ID menjadi angka unik yang sesuai dengan indeksnya.

Kode ini membantu dalam proses transformasi Food_ID menjadi bentuk yang lebih mudah diproses oleh model pembelajaran mesin dengan melakukan encoding dua arah: dari Food_ID ke angka dan sebaliknya. Ini sangat berguna dalam sistem rekomendasi atau model lain yang memerlukan representasi numerik dari data kategorikal.

**3. Mapping Food_ID dalam dataframe**

Kodenya

![image](https://github.com/user-attachments/assets/cff6b62b-5491-40c4-bb31-0014ce7a0a11)

Kode ini bertujuan untuk memetakan Food_ID ke dalam dataframe rating menggunakan dictionary food_to_food_encoded, dan kemudian memeriksa apakah ada nilai NaN setelah proses pemetaan.

Kode ini memastikan bahwa setiap Food_ID dalam dataframe rating berhasil dipetakan ke nilai yang telah diencode. Selain itu, kode ini juga memeriksa apakah ada kesalahan dalam proses pemetaan yang menyebabkan nilai NaN.

**4. Cek nilai dari Food_ID yang digunakan dasar mapping rekomendasi**

Kodenya

![image](https://github.com/user-attachments/assets/b6564677-0893-4355-a3e4-8d022749e589)

Kode ini bertujuan untuk memverifikasi bahwa semua Food_ID dalam dataframe rating telah berhasil dipetakan ke nilai yang telah diencode, serta memastikan tidak ada Food_ID yang tidak termapping.

Kode ini memastikan bahwa semua Food_ID dalam dataframe rating telah berhasil dipetakan ke nilai yang telah diencode dan tidak ada Food_ID yang terlewat. Ini penting untuk memastikan integritas data sebelum digunakan dalam model pembelajaran mesin.

Pada akhirnya maping diseiapkan dengan kode berikut ini. Kode ini bertujuan untuk melakukan encoding pada Food_ID dan memetakan hasil encoding tersebut ke dalam kolom baru food di dataframe rating. 

![image](https://github.com/user-attachments/assets/b6c1e9dc-da40-4dfc-bd1f-99a3989a2e22)

Kode ini memastikan bahwa setiap Food_ID dalam dataframe rating berhasil dipetakan ke nilai yang telah diencode, dan hasilnya disimpan dalam kolom baru food. Ini penting untuk mempersiapkan data sebelum digunakan dalam model pembelajaran mesin atau analisis lebih lanjut.

Mapping juga dilakukan pada data rating dengan kode berikut

![image](https://github.com/user-attachments/assets/a59efc6d-5d16-4fad-a857-f2b4a49ee571)

![image](https://github.com/user-attachments/assets/44401c4c-f452-4b02-870f-6481ec0fa1b9)

Kode ini bertujuan untuk:

1. Mendapatkan jumlah unik pengguna dan makanan.
2. Mengubah kolom Rating menjadi tipe data float.
3. Menentukan nilai minimum dan maksimum dari kolom Rating.
4. Menampilkan informasi tersebut.

Hsilnya adalah 

![image](https://github.com/user-attachments/assets/c5c8ff46-b2f3-458f-a47b-3d54d134bc08)

Kode ini membantu dalam mempersiapkan dan memverifikasi data sebelum digunakan dalam analisis atau model pembelajaran mesin. Dengan mengetahui jumlah pengguna dan makanan, serta rentang nilai rating, kita dapat lebih memahami distribusi data yang akan digunakan.

### 4.3.2. Split Data untuk Validasi

untuk validasi maka kita akan mengacak data rating:

![image](https://github.com/user-attachments/assets/a2c3504b-7316-46b2-b043-91b5cf186ab8)

untuk validasi maka data dibagi menjadi x dan y untuk dapat ditraining:

![image](https://github.com/user-attachments/assets/46c0f852-a91f-40e1-8d27-bd89906ce7ca)

Kode ini bertujuan untuk:
1. Membuat ulang variabel x dan y dari dataframe rating.
2. Melakukan normalisasi pada kolom Rating.
3. Membagi dataset menjadi data latih (training) dan data validasi (validation).

Kode ini mempersiapkan data untuk digunakan dalam model pembelajaran mesin dengan melakukan normalisasi pada rating dan membagi dataset menjadi data latih dan data validasi. Ini adalah langkah penting untuk memastikan model dapat dilatih dan divalidasi dengan benar

Keterangan:

kode tersebut diawali dengan membuat ulang variabel x dan y dengan kode:


x = rating[['user', 'food']].values
y = rating['Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

Selanjutnya adalah membagi dataset dengan kode:

train_indices = int(0.8 * rating.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

Cek validasi:

![image](https://github.com/user-attachments/assets/d1f80203-7c86-4046-b2a8-882e2af96ef9)

Kode ini bertujuan untuk memeriksa apakah ada nilai Food_ID dalam data latih (x_train) yang lebih besar atau sama dengan jumlah total makanan (num_food). Nilai Food_ID yang lebih besar dari atau sama dengan num_food dianggap tidak valid karena indeks makanan seharusnya berada dalam rentang 0 hingga num_food - 1.

Kode ini membantu dalam memverifikasi integritas data latih dengan memastikan bahwa semua nilai Food_ID berada dalam rentang yang valid. Jika ada nilai Food_ID yang tidak valid, ini akan ditampilkan sehingga dapat diperbaiki sebelum melanjutkan ke tahap pelatihan model


### 4.3.3. Training data

Pada tahap ini, model menghitung skor kecocokan antara pengguna dan makanan dengan teknik embedding. Pertama, kita melakukan proses embedding terhadap data user dan resto. Selanjutnya, lakukan operasi perkalian dot product antara embedding user dan food. Selain itu, kita juga dapat menambahkan bias untuk setiap user dan food. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid.

Di sini, kita membuat class RecommenderNet dengan keras Model class. Kode class RecommenderNet ini terinspirasi dari tutorial dalam situs Keras dengan beberapa adaptasi sesuai kasus yang sedang kita selesaikan. Terapkan kode berikut.

Pada bagian inim model yang sudah dibuat akan ditrain untuk melihat akurasinya

Pertama kita perlu membuat fungsi terselebih dahulu denga kode berikut:

![image](https://github.com/user-attachments/assets/457ee661-96e0-4d85-87ca-0f91646a01d5)

# 5. Modeling

Kode ini mendefinisikan sebuah model rekomendasi menggunakan TensorFlow dan Keras. Model ini menggunakan embedding untuk merepresentasikan pengguna dan makanan dalam ruang vektor, dan kemudian menghitung skor kecocokan antara pengguna dan makanan.
Model ini menggunakan embedding untuk merepresentasikan pengguna dan makanan dalam ruang vektor, kemudian menghitung skor kecocokan antara pengguna dan makanan dengan menambahkan dot product dari embedding dan bias masing-masing. Fungsi aktivasi sigmoid digunakan untuk menghasilkan output akhir.

![image](https://github.com/user-attachments/assets/19539b93-917c-40b1-8752-1e7c8fea6708)

Kode ini bertujuan untuk menginisialisasi dan meng-compile model rekomendasi (RecommenderNet) dengan parameter yang telah ditentukan. Proses ini mempersiapkan model untuk dilatih dengan data. Tahap ini terdiri dari:
1. Inisiasi model
2. Compile model
Kode ini mempersiapkan model rekomendasi untuk dilatih dengan data. Dengan meng-compile model, kita menentukan fungsi loss, optimizer, dan metrik evaluasi yang akan digunakan selama proses pelatihan. Ini adalah langkah penting sebelum memulai pelatihan model.

![image](https://github.com/user-attachments/assets/d857772a-c257-4da4-8397-685c34600fec)

Kode ini bertujuan untuk menginisialisasi dan meng-compile model rekomendasi (RecommenderNet) dengan parameter yang telah ditentukan. Proses ini mempersiapkan model untuk dilatih dengan data.
Kode ini mempersiapkan model rekomendasi untuk dilatih dengan data. Dengan meng-compile model, kita menentukan fungsi loss, optimizer, dan metrik evaluasi yang akan digunakan selama proses pelatihan. Ini adalah langkah penting sebelum memulai pelatihan model.

Hasilnnya adalah sebagai berikut

![image](https://github.com/user-attachments/assets/828fb7bd-d2a9-4343-8ac2-ed8c6d98f59c)

Berikut adalah keterangannya:

Epoch 97-100: Menunjukkan tahap pelatihan model di epoch ke-97 hingga ke-100 dari total 100 epoch. Setiap epoch mewakili satu kali iterasi lengkap melalui data pelatihan.

Loss: Ini adalah metrik yang dihitung berdasarkan fungsi kehilangan (loss function). Loss mengukur seberapa jauh prediksi model dari nilai sebenarnya dalam data pelatihan. Semakin rendah nilai loss, semakin baik model melakukan pelatihan.

Root Mean Squared Error (RMSE):

Ini adalah akar dari rata-rata kuadrat selisih antara prediksi model dan nilai aktual. RMSE sering digunakan untuk merepresentasikan kesalahan dalam skala yang sama dengan target data.
root_mean_squared_error adalah nilai RMSE untuk data pelatihan.
Val_loss dan val_root_mean_squared_error:

Val_loss: Ini adalah nilai loss yang dihitung pada data validasi, yang digunakan untuk mengevaluasi performa model terhadap data yang belum pernah dilihat sebelumnya selama pelatihan.
val_root_mean_squared_error: Nilai RMSE untuk data validasi. Semakin kecil nilai ini, semakin baik performa model terhadap data validasi.
uared_error: Ini kemungkinan salah satu metrik tambahan yang Anda definisikan (bisa jadi metrik kustom). Nilainya tampaknya konsisten di sekitar 0.346-0.347, yang bisa menunjukkan metrik khusus lain untuk mengevaluasi model.

Progres Pelatihan (ms/step): Waktu pelatihan per step menunjukkan seberapa cepat setiap batch data diproses. Dalam kasus ini, terlihat bahwa pelatihan berlangsung dengan cukup cepat (2-3 ms per step).

Secara keseluruhan, berdasarkan gambar:

Model terus memperbaiki nilai loss dan RMSE pada data pelatihan, namun val_loss dan val_root_mean_squared_error tampak stabil di sekitar 0.74. Perbedaan yang kecil antara RMSE pada data pelatihan dan validasi mengindikasikan model tidak overfitting.


## 5.1. Visualisasi matrik

Berikut ini adalah kode untuk melihat hasil training dalam bentuk visualisasi.

![image](https://github.com/user-attachments/assets/ef270ce7-773d-4dbe-bde9-a88411d626ce)

Hasilnya

![image](https://github.com/user-attachments/assets/95bb363b-a5d4-40fd-91a6-9b5965d3616f)

Gambar tersebut menunjukkan grafik metrik Root Mean Squared Error (RMSE) terhadap jumlah epoch untuk data pelatihan (train) dan data pengujian (test). Berikut adalah analisis hasil training:

Sumbu X: Merepresentasikan jumlah epoch (dari 0 hingga 100), yaitu jumlah iterasi pelatihan model.

Sumbu Y: Merepresentasikan nilai root mean squared error (RMSE), yang mengukur rata-rata kesalahan antara prediksi model dan nilai sebenarnya.

**Observasi**
Kurva Pelatihan (Train - Garis Biru):

1. Nilai RMSE untuk data pelatihan terus menurun seiring bertambahnya epoch.
Ini menunjukkan bahwa model belajar dengan baik dari data pelatihan dan terus memperbaiki performanya.
2. Tidak ada tanda-tanda stagnasi atau peningkatan RMSE, sehingga pelatihan pada data ini tampak efektif.

Kurva Pengujian (Test - Garis Oranye):

Nilai RMSE untuk data pengujian cenderung meningkat seiring bertambahnya epoch.
Hal ini menunjukkan bahwa adanya potensi model mengalami overfitting, yaitu model belajar terlalu spesifik pada data pelatihan sehingga kehilangan kemampuan generalisasi terhadap data pengujian.

**Kesimpulan**
Masalah Overfitting: Model menunjukkan overfitting karena perbedaan yang semakin besar antara RMSE pada data pelatihan dan pengujian. Hal ini dapat disebabkan oleh:
1. Model terlalu kompleks.
2. Tidak cukupnya data untuk melatih model.


## 5.2 Rekomendasi makanan

Tahap rekomendasi ini dimulai dengan membentuk fungsi dari data Food dan rating yang telah disiapkan sebelumnya. Berikut adalah kodenya:

![image](https://github.com/user-attachments/assets/823b9c4b-fb16-44b2-9cf4-033843576ce9)

Kode tersebut bertujuan untuk mempersiapkan data guna membuat prediksi makanan yang belum direview oleh seorang user tertentu dalam sistem rekomendasi makanan. Proses ini melibatkan encoding data dan membentuk pasangan user-food yang dapat digunakan untuk inferensi model.

Keterangan tahapan kode:
1. Ambil satu sampel user (user_id).
2. Identifikasi makanan yang belum direview oleh user tersebut.
3. Encode ID makanan dan ID user ke bentuk numerik.
4. Bentuk pasangan user-makanan yang dapat diproses oleh model untuk prediksi.

Kode ini membantu membuat data input untuk model sistem rekomendasi berbasis collaborative filtering atau neural network, di mana model akan memprediksi rating atau rekomendasi untuk makanan yang belum direview oleh user tertentu.

Selanjutnya sistem akan menunjukkan  rekomendasi makanan terbaik dan makanan yang memiliki kemiripan dengan jenis makanan tersebut. Berikut ini kodenya:

![image](https://github.com/user-attachments/assets/54cd1d3d-2e22-4e9b-a23f-d2abaae46859)


Hasilnya berikut ini

Makanan Favorit User: Daftar makanan dengan rating tertinggi yang telah direview oleh user.
Rekomendasi Makanan: Daftar 10 makanan yang belum direview tetapi diprediksi memiliki rating tinggi untuk user tersebut. Rekomendasi ini bisa digunakan untuk meningkatkan pengalaman user dalam sistem rekomendasi.

![image](https://github.com/user-attachments/assets/21b39659-8078-4532-bcfb-57f69c144e98)

Saat sistem merekomendasikan makanan yang memiliki reting tinggi yaitu: almond pearls yaitu (Snack), Sistem juga memberikan rekomendasi makanan snack yang mirip dari berbagai jenis makanan, seperti berikut ini:

1. corn and raw mango salad : Healthy Food
2. sugar free modak : Japanese
3. andhra pan fried pomfret : Indian
4. steam bunny chicken bao : Japanese
5. hot chocolate : Beverage
6. grilled lemon margarita : Beverage
7. spiced coffee : Beverage
8. filter coffee : Beverage
9. garlic and pinenut soup with burnt butter essence : French
10. roasted spring chicken with root veggies : Healthy Food


# 6. Evaluasi
Sistem rekomendasi ini bertujuan untuk memberikan saran makanan yang relevan bagi pengguna (user) berdasarkan preferensi mereka di masa lalu dan pola perilaku pengguna lainnya. Ini dicapai melalui pendekatan berbasis collaborative filtering atau neural network, di mana sistem mempelajari hubungan antara pengguna dan makanan berdasarkan data historis.

Proses Utama dari sistem rekoemndasi ini adalah berikut:
1. Proses keseluruhan terdiri dari beberapa langkah penting:
Pengumpulan Data: Data rating makanan oleh pengguna digunakan sebagai input utama. Data ini mencakup user ID, food ID, rating, deskripsi makanan, dan jenis makanan.

2. Pemilihan Pengguna dan Makanan:
Sistem secara acak memilih seorang pengguna (user) untuk dianalisis.
Menentukan makanan yang telah direview dan makanan yang belum direview oleh pengguna tersebut.

3. Encoding Data: ID pengguna dan makanan diencode ke format numerik agar dapat diproses oleh model.
Prediksi Rating: Model memprediksi skor/rating untuk makanan yang belum direview oleh pengguna.

4.  Penyaringan Rekomendasi:
Sistem memilih 10 makanan dengan prediksi rating tertinggi sebagai rekomendasi untuk pengguna. Makanan duplikat dihapus berdasarkan nama dan jenisnya.

**Keunggulan Sistem:**
1. Personalisasi: Rekomendasi didasarkan pada preferensi unik setiap pengguna.
2. Efisiensi: Dengan encoding dan prediksi berbasis model, sistem dapat memberikan rekomendasi dengan cepat meskipun ada banyak data.
3. Eksplorasi Baru: Sistem memperkenalkan makanan baru yang kemungkinan akan disukai pengguna, membantu memperluas pilihan mereka.

**Hasil Akhir:**
Walaupun ada potensi overfifting, hasil sistem rekomendasi ini berhasil memberikan hasil dari pertanyaan dan tujuan bisnis yang menjadi tujuan dari proyek ini.

1. Makanan Favorit Pengguna:
Sistem menampilkan 5 makanan yang sudah direview oleh pengguna dengan rating tertinggi. Ini mencerminkan preferensi eksplisit pengguna.

2. Rekomendasi Makanan:
Sistem merekomendasikan 10 makanan baru yang belum direview tetapi diprediksi memiliki rating tinggi oleh model. Rekomendasi ini dirancang untuk memperluas pengalaman pengguna dan mencocokkan preferensi mereka.


**Kesimpulan Akhir:**
Sistem rekomendasi ini menunjukkan kemampuan untuk memprediksi dan menyarankan makanan secara personal bagi pengguna berdasarkan data historis. Dengan cara ini, pengguna tidak hanya mendapatkan pengalaman yang lebih relevan, tetapi juga diperkenalkan ke opsi baru yang sesuai dengan preferensi mereka. Sistem ini dapat terus ditingkatkan dengan lebih banyak data, teknik regulasi yang lebih baik, atau integrasi metode berbasis konten untuk mengatasi kekurangan dalam skenario cold-start.








