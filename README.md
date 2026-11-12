<div align="center">

# ⚡ Kalkulator - Limit: Advanced Symbolic Limit & L'Hôpital Web Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![SymPy](https://img.shields.io/badge/SymPy-Symbolic_Math-orange?style=for-the-badge&logo=sympy&logoColor=white)](https://www.sympy.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3f4f75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

*Kalkulator limit matematika berbasis web interaktif dengan analisis simbolik penuh, otomatisasi Aturan L'Hôpital, ekspansi deret Taylor, uji kontinuitas, dan visualisasi grafik real-time.*

</div>

---

## 🚀 Fitur Unggulan

* **🧮 Kalkulasi Simbolik Eksak (`SymPy`):** Mengeluarkan hasil nilai limit dalam bentuk aljabar presisi (pecahan, bentuk akar, atau konstanta $e$) tanpa pembulatan numerik.
* **🔄 Otomatisasi Aturan L'Hôpital:** Mendeteksi bentuk tak tentu ($\frac{0}{0}$ atau $\frac{\infty}{\infty}$) dan melakukan iterasi turunan pembilang serta penyebut secara otomatis hingga 4 iterasi.
* **📝 Langkah Penyelesaian Step-by-Step:** Menampilkan rincian pengerjaan analitik menggunakan komponen *accordion* interaktif dan format matematika LaTeX.
* **🔬 Analisis Tambahan:** Menyertakan penyederhanaan aljabar otomatis, uji kontinuitas fungsi di titik limit, dan ekspansi deret Taylor (orde ke-4).
* **📉 Grafik Interaktif Berbasis Plotly:** Kurva fungsi responsif yang mendukung fitur *zoom*, *pan*, dan *hover tooltip* untuk melihat koordinat presisi di sekitar titik pendekatan, lengkap dengan penanda asimtot dan titik limit.
* **⚡ Preset Soal Cepat:** Dilengkapi tombol pintasan di *sidebar* untuk menguji kasus-kasus limit populer secara instan.

---

## 🛠️ Tech Stack

* **Frontend & UI:** [Streamlit](https://streamlit.io/) (Dark Glassmorphism UI & Custom CSS)
* **Symbolic Math Engine:** [SymPy](https://www.sympy.org/)
* **Interactive Visualization:** [Plotly Graph Objects](https://plotly.com/)
* **Numerical Processing:** [NumPy](https://numpy.org/)

---

## 📦 Panduan Instalasi & Menjalankan Lokal

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di komputer lokal kamu:

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/LudovicOnofredo/Kalkulator-Limit.git](https://github.com/LudovicOnofredo/Kalkulator-Limit.git)
   cd kalkulator-limit
   python3 kalkulator-limit.py
