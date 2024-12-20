# Dashboard Analisis Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda dan menjawab dua pertanyaan bisnis utama:
1. Apa waktu terbaik untuk memaksimalkan penggunaan sepeda?
2. Bagaimana pengaruh cuaca terhadap jumlah penyewaan sepeda?

Hasil analisis divisualisasikan dalam sebuah dashboard interaktif yang dibuat menggunakan **Streamlit**.

---

## Struktur Folder Proyek
```
submission
├───dashboard
│     ├───dashboard.py
│     ├───day.csv
│     └───hour.csv
├───data
│     ├───day.csv
│     └───hour.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```
- **dashboard/dashboard.py**: Script utama untuk menjalankan dashboard.
- **dashboard/day.csv**: Dataset penyewaan sepeda harian yang diolah.
- **dashboard/hour.csv**: Dataset penyewaan sepeda per jam yang diolah.
- **data/day.csv**: Dataset penyewaan sepeda harian.
- **data/hour.csv**: Dataset penyewaan sepeda per jam.
- **notebook.ipynb**: Notebook analisis data.
- **README.md**: Dokumentasi proyek.
- **requirements.txt**: Daftar library Python yang digunakan.
- **url.txt**: Tautan untuk dashboard jika dideploy.

---

## Cara Menjalankan Proyek

1. **Persiapan Lingkungan**:
   - Pastikan Python 3.8 atau versi lebih baru telah terinstal.
   - Install library yang diperlukan dengan menjalankan:
     ```bash
     pip install -r requirements.txt
     ```

2. **Menjalankan Dashboard**:
   - Pastikan file `day.csv` dan `hour.csv` berada di dalam folder `data`.
   - Jalankan script Streamlit dengan perintah:
     ```bash
     streamlit run dashboard/dashboard.py
     ```

3. **Mengakses Dashboard**:
   - Dashboard dapat diakses melalui browser di alamat:
     ```
     http://localhost:8501
     ```

---

## Fitur Dashboard

- **Pemilihan Dataset**: Pengguna dapat memilih dataset harian atau per jam untuk divisualisasikan.
- **Visualisasi Waktu Terbaik**:
  - Grafik rata-rata penyewaan per jam untuk menemukan waktu puncak penyewaan.
  - Grafik rata-rata penyewaan per bulan untuk analisis musiman.
- **Pengaruh Cuaca**:
  - Grafik rata-rata penyewaan berdasarkan kondisi cuaca.
- **Filter Interaktif**:
  - Filter jam (`hour`) dan kondisi cuaca (`weather`) melalui sidebar.
- **Preview Data**: Tabel untuk melihat sampel data yang sedang dianalisis.

---

## Insight

### 1. Waktu Terbaik untuk Penyewaan Sepeda
- Puncak penyewaan terjadi pada pagi (07:00-09:00) dan sore (17:00-19:00).
- Bulan dengan cuaca hangat (musim panas) mencatatkan penyewaan tertinggi.

### 2. Pengaruh Cuaca terhadap Penyewaan Sepeda
- Cuaca cerah atau sebagian berawan memiliki jumlah penyewaan tertinggi.
- Cuaca ekstrem (hujan deras atau salju) menyebabkan penurunan signifikan dalam penyewaan.

---

## Library yang Digunakan
- **Streamlit**: Untuk membuat dashboard interaktif.
- **Pandas**: Untuk manipulasi dan analisis data.
- **Matplotlib**: Untuk visualisasi data.

---

## Catatan Tambahan
- Data berasal dari Bike Sharing Dataset.
- Pastikan semua file dan struktur direktori sesuai dengan panduan di atas agar dashboard berjalan dengan baik.

---

Jika ada kendala atau pertanyaan, jangan ragu untuk menghubungi pengembang proyek.
