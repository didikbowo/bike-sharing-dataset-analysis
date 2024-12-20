import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
@st.cache_data
def load_data():
    try:
        day_data = pd.read_csv('data/day.csv')
        hour_data = pd.read_csv('data/hour.csv')
        return day_data, hour_data
    except FileNotFoundError as e:
        st.error(f"File tidak ditemukan: {e.filename}. Pastikan file berada di folder 'data'.")
        return pd.DataFrame(), pd.DataFrame()

day_data, hour_data = load_data()

# Title and description
st.title('Dashboard Analisis Bike Sharing Dataset')
st.markdown('Dashboard ini menampilkan hasil analisis data penyewaan sepeda untuk menjawab dua pertanyaan bisnis utama:')
st.markdown('1. Apa waktu terbaik untuk memaksimalkan penggunaan sepeda?')
st.markdown('2. Bagaimana pengaruh cuaca terhadap jumlah penyewaan sepeda?')

# Dataset selection
dataset_choice = st.radio("Pilih Dataset", ("Data Harian", "Data Per Jam"))
if dataset_choice == "Data Harian":
    data = day_data
    st.markdown("### Visualisasi untuk Data Harian")
else:
    data = hour_data
    st.markdown("### Visualisasi untuk Data Per Jam")

if not data.empty:
    # Sidebar for filtering
    if 'hr' in data.columns:
        time_filter = st.sidebar.multiselect('Pilih Jam (0-23)', sorted(data['hr'].unique()), default=sorted(data['hr'].unique()))
        data = data[data['hr'].isin(time_filter)]

    weather_filter = st.sidebar.multiselect(
        'Pilih Kondisi Cuaca',
        options=[1, 2, 3, 4],
        default=[1, 2, 3, 4],
        format_func=lambda x: {1: 'Clear/Partly Cloudy', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}[x]
    )
    data = data[data['weathersit'].isin(weather_filter)]

    # Visualizations
    st.subheader('Jumlah Penyewaan Sepeda')
    if 'hr' in data.columns:
        hourly_counts = data.groupby('hr')['cnt'].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(hourly_counts.index, hourly_counts.values, marker='o', label='Rata-rata Penyewaan')
        plt.title('Rata-rata Penyewaan Sepeda per Jam')
        plt.xlabel('Jam')
        plt.ylabel('Jumlah Penyewaan')
        plt.grid()
        plt.legend()
        st.pyplot(plt)
    else:
        monthly_counts = data.groupby('mnth')['cnt'].mean()
        plt.figure(figsize=(10, 6))
        monthly_counts.plot(kind='bar', color='orange', label='Rata-rata Penyewaan')
        plt.title('Rata-rata Penyewaan Sepeda per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Jumlah Penyewaan')
        plt.legend()
        st.pyplot(plt)

    st.subheader('Pengaruh Cuaca terhadap Penyewaan Sepeda')
    weather_counts = data.groupby('weathersit')['cnt'].mean().reindex([1, 2, 3, 4], fill_value=0)
    weather_labels = ['Clear/Partly Cloudy', 'Mist/Cloudy', 'Light Snow/Rain', 'Heavy Rain/Snow']
    plt.figure(figsize=(8, 6))
    plt.bar(weather_labels, weather_counts, color='skyblue')
    plt.title('Rata-rata Penyewaan Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Penyewaan')
    plt.grid()
    st.pyplot(plt)

    # Data preview
    st.subheader('Preview Data')
    st.write(data.head())
else:
    st.warning("Data tidak tersedia untuk ditampilkan. Pastikan file CSV tersedia dan dapat dibaca.")

st.markdown('---')
st.markdown('Gunakan filter di sidebar untuk menyesuaikan visualisasi.')
