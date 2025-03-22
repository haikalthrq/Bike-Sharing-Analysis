# 🚴‍♂️ Analisis Data Bike Sharing 🚴‍♀️

Proyek ini merupakan analisis data menggunakan dataset **Bike Sharing**. Analisis dilakukan untuk memahami pola penggunaan sepeda di kota, dengan fokus pada beberapa pertanyaan bisnis yang telah ditetapkan. Dashboard interaktif juga disediakan menggunakan **Streamlit** untuk memvisualisasikan insight dari data.

Bisa diakses disini:

[Bike Sharing Analysis](https://bike-sharing-analysis-bdzuubcatjd4x6kw4vjzta.streamlit.app/)

---

## 📖 Latar Belakang

Bike Sharing merupakan salah satu solusi transportasi alternatif di perkotaan yang kini semakin populer. Proyek ini bertujuan untuk menganalisis pola penggunaan sepeda melalui dataset yang mencakup informasi harian dan per jam, serta memberikan insight yang berguna bagi penyedia layanan untuk melakukan perencanaan operasional dan strategi pemasaran.

---

## 🎯 Tujuan Proyek

- **Memahami pola aktivitas penggunaan sepeda**: Menjawab pertanyaan mengenai kapan sepeda paling banyak disewa dalam satu hari.
- **Menganalisis pengaruh cuaca**: Mengetahui bagaimana kondisi cuaca memengaruhi jumlah penyewaan sepeda.
- **Menganalisis pengaruh musim**: Mengidentifikasi tren penyewaan sepeda berdasarkan musim.

---

## ❓ Pertanyaan Bisnis

1. **Pola Aktivitas Penggunaan Sepeda (Hourly Data)**: Bagaimana pola aktivitas penggunaan sepeda dalam satu hari berdasarkan data waktu?
2. **Pengaruh Cuaca**: Bagaimana cuaca mempengaruhi jumlah penyewaan sepeda?
3. **Pengaruh Musim**: Bagaimana musim mempengaruhi jumlah penyewaan sepeda?

---

## 📊 Data & Preprocessing

Dataset yang digunakan adalah:

- `hour.csv`: Data dengan resolusi per jam.

### Proses Preprocessing

- Pengecekan missing values dan duplikasi.
- Konversi tipe data (misalnya, kolom tanggal, mapping kategori untuk season, weekday, month, dan weathersit).
- Normalisasi variabel numerik seperti `temp`, `atemp`, `hum`, dan `windspeed`.

### Hasil Data yang Telah Dibersihkan

- `cleaned_hourData.csv`

---

## 🔍 Eksplorasi dan Visualisasi Data

Analisis eksploratif (EDA) dilakukan dengan menggunakan library seperti **Pandas**, **NumPy**, **Matplotlib**, dan **Seaborn**. Beberapa visualisasi utama yang dibuat meliputi:

- **Distribusi variabel numerik**: Untuk memahami sebaran data.
- **Line Chart**: Menampilkan aktivitas penyewaan per jam.
- **Stacked Bar Chart**: Menganalisis pengaruh cuaca terhadap penyewaan.
- **Grouped Bar Chart**: Mengungkap pengaruh musim terhadap penyewaan.

---

## 📈 Dashboard Interaktif

Dashboard dibuat menggunakan **Streamlit** dengan fitur:

- **Judul dan Grafik Utama**: Menampilkan tren penyewaan sepanjang hari.
- **Pertanyaan 1**: Menampilkan grafik aktivitas peminjaman per jam.
- **Pertanyaan 2**: Menampilkan stacked bar chart pengaruh cuaca.
- **Pertanyaan 3**: Menampilkan grouped bar chart pengaruh musim.

---

## 🛠️ Teknologi yang Digunakan

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Streamlit**

---

## 🚀 Cara Menjalankan Proyek

1. Clone repository ini:
   ```bash
   git clone https://github.com/haikalthrq/Bike-Sharing-Analysis.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Jalankan dashboard Streamlit:
   ```bash
   streamlit run dashboard.py
