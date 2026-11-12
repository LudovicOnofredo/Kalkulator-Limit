# Kalkulator-Limit
================================================================================

⚡ Kalkulator Limit: Advanced Symbolic Limit & L'Hôpital Web Engine

================================================================================



Kalkulator limit matematika berbasis web interaktif dengan analisis simbolik 

penuh, otomatisasi Aturan L'Hôpital, ekspansi deret Taylor, uji kontinuitas, 

dan visualisasi grafik real-time.



--------------------------------------------------------------------------------

🚀 FITUR UNGGULAN

--------------------------------------------------------------------------------

* Kalkulasi Simbolik Eksak (SymPy): 

  Mengeluarkan hasil nilai limit dalam bentuk aljabar presisi (pecahan, bentuk 

  akar, atau konstanta e) tanpa pembulatan numerik.



* Otomatisasi Aturan L'Hôpital: 

  Mendeteksi bentuk tak tentu (0/0 atau tak hingga/tak hingga) dan melakukan 

  iterasi turunan pembilang serta penyebut secara otomatis hingga 4 iterasi.



* Langkah Penyelesaian Step-by-Step: 

  Menampilkan rincian pengerjaan analitik menggunakan komponen accordion 

  interaktif dan format matematika LaTeX.



* Analisis Tambahan: 

  Menyertakan penyederhanaan aljabar otomatis, uji kontinuitas fungsi di titik 

  limit, dan ekspansi deret Taylor (orde ke-4).



* Grafik Interaktif Berbasis Plotly: 

  Kurva fungsi responsif yang mendukung fitur zoom, pan, dan hover tooltip untuk 

  melihat koordinat presisi di sekitar titik pendekatan, lengkap dengan penanda 

  asimtot dan titik limit.



* Preset Soal Cepat: 

  Dilengkapi tombol pintasan di sidebar untuk menguji kasus-kasus limit populer 

  secara instan.



--------------------------------------------------------------------------------

🛠️ TECH STACK

--------------------------------------------------------------------------------

* Frontend & UI           : Streamlit (Dark Glassmorphism UI & Custom CSS)

* Symbolic Math Engine    : SymPy

* Interactive Visualizer  : Plotly Graph Objects

* Numerical Processing    : NumPy



--------------------------------------------------------------------------------

📦 PANDUAN INSTALASI & MENJALANKAN LOKAL

--------------------------------------------------------------------------------

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di komputer lokal:



1. Clone repository ini:

   git clone https://github.com/username/kalkulator-limit.git

   cd kalkulator-limit



2. Buat dan aktifkan virtual environment (opsional tapi disarankan):

   python -m venv venv

   

   # Windows:

   venv\Scripts\activate

   

   # Mac/Linux:

   source venv/bin/activate



3. Instal seluruh pustaka yang dibutuhkan:

   pip install streamlit sympy plotly numpy



4. Jalankan aplikasi Streamlit:

   streamlit run kalkulator-limit.py

   

   (Catatan: Gunakan perintah "python -m streamlit run kalkulator-limit.py" 

   jika terjadi kendala pada environment PATH).



--------------------------------------------------------------------------------

📖 PANDUAN PENULISAN SINTAKS FUNGSI

--------------------------------------------------------------------------------

Gunakan format penulisan matematika standar Python/SymPy:

* Pangkat            : x**2 atau x^2

* Perkalian          : 2*x (Wajib menggunakan tanda bintang * secara eksplisit)

* Akar Kuadrat       : sqrt(x)

* Trigonometri       : sin(x), cos(x), tan(x)

* Logaritma Natural  : log(x)

* Tak Hingga         : oo atau -oo



--------------------------------------------------------------------------------

💡 CONTOH KASUS YANG BISA DICOBA

--------------------------------------------------------------------------------

1. Bentuk Tak Tentu 0/0 (L'Hôpital)

   - Fungsi : (sin(x) - x) / x**3

   - Titik  : 0



2. Bilangan Euler (e)

   - Fungsi : (1 + 1/x)**x

   - Titik  : oo



3. Fungsi Diskontinu

   - Fungsi : abs(x) / x

   - Titik  : 0



--------------------------------------------------------------------------------

📜 LISENSI

--------------------------------------------------------------------------------

Proyek ini bersifat open-source di bawah lisensi MIT. Silakan gunakan, 

kembangkan, atau modifikasi untuk keperluan akademik maupun pribadi.
