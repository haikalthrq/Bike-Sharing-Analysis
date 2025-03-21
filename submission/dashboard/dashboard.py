import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# ===============================
# STEP 1: Load & Persiapkan Data
# ===============================
# Asumsi data sudah melalui proses cleaning seperti pada instruksi analisis
# dan disimpan sebagai cleaned_hourData.csv.

base_path = os.path.dirname(__file__)  # Lokasi file dashboard.py
file_path = os.path.join(base_path, 'cleaned_hourData.csv')
hour_data = pd.read_csv(file_path)

# ===============================
# STEP 2: Membuat Grafik Utama
# ===============================
# Grafik utama: Line chart aktivitas peminjaman sepeda sepanjang hari.
hourly_activity = hour_data.groupby('hr').agg({'casual': 'sum', 'registered': 'sum'}).reset_index()

fig_main, ax_main = plt.subplots(figsize=(14, 6))
ax_main.plot(hourly_activity['hr'], hourly_activity['casual'], label='Peminjaman Casual', marker='o')
ax_main.plot(hourly_activity['hr'], hourly_activity['registered'], label='Peminjaman Registered', marker='o')
ax_main.set_title('Pola Aktivitas Penggunaan Sepeda Sepanjang Hari')
ax_main.set_xlabel('Jam')
ax_main.set_ylabel('Jumlah Peminjaman')
ax_main.legend()
ax_main.grid(True)
ax_main.set_xticks(np.arange(0, 24, 1))

# ===============================
# STEP 3: Menyusun Tampilan Dashboard
# ===============================
st.title("Analisis Data Bike Sharing")
st.pyplot(fig_main)

# ------------------------------------------------
# Pertanyaan 1: Pola Aktivitas Penggunaan Sepeda
# ------------------------------------------------
st.markdown("## Pertanyaan 1")
st.markdown("**Bagaimana pola aktivitas penggunaan sepeda dalam satu hari berdasarkan data waktu (hourly data)?**")

# Grafik untuk pertanyaan 1 (menggunakan line chart yang sama)
fig_q1, ax_q1 = plt.subplots(figsize=(14, 6))
ax_q1.plot(hourly_activity['hr'], hourly_activity['casual'], label='Peminjaman Casual', marker='o')
ax_q1.plot(hourly_activity['hr'], hourly_activity['registered'], label='Peminjaman Registered', marker='o')
ax_q1.set_title('Pola Aktivitas Penggunaan Sepeda Sepanjang Hari')
ax_q1.set_xlabel('Jam')
ax_q1.set_ylabel('Jumlah Peminjaman')
ax_q1.legend()
ax_q1.grid(True)
ax_q1.set_xticks(np.arange(0, 24, 1))
st.pyplot(fig_q1)

st.markdown("""
Grafik menunjukkan bahwa peminjaman sepeda mengalami peningkatan pada jam sibuk, khususnya pada pagi (misalnya 6-9) dan sore hari (misalnya 17-19).  
Pengguna casual dan registered menunjukkan pola yang mirip, meskipun pengguna registered cenderung memiliki jumlah peminjaman yang lebih tinggi.
""")

# ------------------------------------------------
# Pertanyaan 2: Pengaruh Cuaca Terhadap Peminjaman
# ------------------------------------------------
st.markdown("## Pertanyaan 2")
st.markdown("**Bagaimana cuaca mempengaruhi jumlah penyewaan sepeda?**")


# Grafik untuk pertanyaan 2: Stacked Bar Chart berdasarkan cuaca
weather_activity = hour_data.groupby('weathersit').agg({'casual': 'sum', 'registered': 'sum'}).reset_index()

fig_q2, ax_q2 = plt.subplots(figsize=(10, 6))
# Membuat stacked bar chart
weather_activity.set_index('weathersit')[['casual', 'registered']].plot(kind='bar', stacked=True, ax=ax_q2, legend=True)
ax_q2.set_title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
ax_q2.set_xlabel('Jenis Cuaca')
ax_q2.set_ylabel('Jumlah Peminjaman')
ax_q2.legend(title='Tipe Pengguna', labels=['Casual', 'Registered'])
ax_q2.tick_params(axis='x', rotation=45)
st.pyplot(fig_q2)

st.markdown(""" 
Analisis menunjukkan bahwa cuaca yang cerah (Clear) memberikan jumlah penyewaan tertinggi, sedangkan kondisi cuaca yang kurang mendukung seperti Mist/Cloudy atau Light Rain/Light Snow mengurangi aktivitas penyewaan.  
Pada kondisi cuaca ekstrem (Heavy Rain/Heavy Snow), hampir tidak terjadi penyewaan.
""")

# ------------------------------------------------
# Pertanyaan 3: Pengaruh Musim Terhadap Peminjaman
# ------------------------------------------------
st.markdown("## Pertanyaan 3")
st.markdown("**Bagaimana musim mempengaruhi jumlah penyewaan sepeda?**")

# Grafik untuk pertanyaan 3: Grouped Bar Chart berdasarkan musim
season_activity = hour_data.groupby('season').agg({'casual': 'sum', 'registered': 'sum'}).reset_index()

fig_q3, ax_q3 = plt.subplots(figsize=(10, 6))
season_activity.set_index('season')[['casual', 'registered']].plot(kind='bar', ax=ax_q3, legend=True)
ax_q3.set_title('Pengaruh Musim terhadap Jumlah Peminjaman Sepeda')
ax_q3.set_xlabel('Musim')
ax_q3.set_ylabel('Jumlah Peminjaman')
ax_q3.legend(title='Tipe Pengguna', labels=['Casual', 'Registered'])
ax_q3.tick_params(axis='x', rotation=45)
st.pyplot(fig_q3)

st.markdown(""" 
Grafik mengungkapkan bahwa musim gugur (Fall) mencatat jumlah peminjaman tertinggi, sedangkan musim semi (Spring) menunjukkan angka peminjaman yang paling rendah.  
Hal ini dapat menjadi dasar bagi strategi operasional dan pemasaran untuk menyesuaikan penawaran sesuai musim.
""")