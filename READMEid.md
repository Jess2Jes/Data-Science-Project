[English](README.md) | Bahasa Indonesia | [中文](READMECN.md)
# TaskMaster CLI: Sistem Manajemen Tugas Berbasis Python

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Sebuah aplikasi manajemen tugas berbasis *command-line* yang komprehensif dan dibangun dengan Python. Alat ini memungkinkan pengguna untuk secara efisien menambah, melacak, memfilter, dan mengelola tugas serta jadwal harian mereka langsung dari terminal. Didesain sebagai proyek tugas sekolah, aplikasi ini mendemonstrasikan konsep inti pemrograman termasuk manipulasi data, desain modular, dan interaksi *command-line* yang ramah pengguna.

## ✨ Fitur Utama

-   **Fungsionalitas CRUD Penuh**: Tambah, lihat, perbarui, dan hapus tugas dengan mudah.
-   **Pengurutan Tingkat Lanjut**: Urutkan tugas berdasarkan **tenggat waktu**, **nama**, **prioritas**, atau **status** dalam urutan menaik (*ascending*) dan menurun (*descending*).
-   **Penyaringan Cerdas**: Filter tugas secara dinamis berdasarkan berbagai periode waktu (`hari ini`, `besok`, `minggu ini`, `bulan ini`), prioritas, atau status.
-   **Prioritas Tugas**: Lihat "3 Tugas Paling Penting" secara instan berdasarkan kombinasi prioritas dan tenggat waktu yang akan datang.
-   **Aksi Cepat**: Tandai tugas sebagai "Selesai" dengan mudah atau hapus semua tugas yang sudah selesai sekaligus.
-   **Laporan Statistik**: Hasilkan laporan terperinci dengan format yang indah, mencakup total tugas, rincian status, dan statistik prioritas.
-   **Antarmuka yang Ramah Pengguna**: Antarmuka berbasis menu yang sederhana dan intuitif untuk navigasi yang lancar.
-   **Format Tabel Dinamis**: Daftar tugas ditampilkan dalam tabel yang diformat dengan rapi dan ukurannya menyesuaikan dengan panjang konten.

## 📸 Demo

Berikut adalah tampilan menu utama baru dan contoh output daftar tugas:

**Menu Utama:**

<img src="assets/MENU_APPEARANCE.png" alt="Menu Appearance" width="300">

**Contoh Output (`Daftar Task`):**
```
──────────────────────────────────────────────────────────────────────────────────
                                   Semua Task
──────────────────────────────────────────────────────────────────────────────────
ID │ Task                      │ Deadline              │ Priority │ Status
──────────────────────────────────────────────────────────────────────────────────
1  │ Kerjakan Tugas Basis Data │ 2025 05 October 13:00 │ High     │ Pending
2  │ Belajar Algoritma         │ 2025 06 October 12:57 │ Medium   │ In Progress
3  │ Buat Slide Presentasi     │ 2025 08 October 16:49 │ High     │ Completed
4  │ Rapat Tim                 │ 2025 04 October 15:00 │ Low      │ Completed
5  │ Kerjakan Tugas Pbo        │ 2025 04 October 15:00 │ High     │ Completed
──────────────────────────────────────────────────────────────────────────────────
```

## 📂 Struktur Proyek

Proyek ini diorganisir ke dalam file-file modular untuk keterbacaan dan pemeliharaan yang lebih baik.

```
nama-proyek-anda/
├── main.py                     # Titik masuk utama aplikasi
└── helpers/
    ├── __init__.py
    ├── addData.py              # Menangani logika untuk menambah tugas baru
    ├── changeData.py           # Fungsi untuk memperbarui, menghapus, dan menandai tugas selesai
    ├── dataFilters.py          # Fungsi untuk memfilter tugas dan menampilkan tabel data
    ├── reports.py              # Menghasilkan dan mencetak laporan statistik
    ├── search.py               # Mengimplementasikan fungsionalitas pencarian tugas
    └── sorter.py               # Berisi semua fungsi untuk pengurutan tugas tingkat lanjut
```

## 🚀 Cara Memulai

Ikuti instruksi berikut untuk menjalankan proyek ini di mesin lokal Anda.

### Prasyarat

-   Python 3.8 atau yang lebih baru

### Instalasi & Menjalankan

1.  **Clone repositori (atau unduh file):**
    ```sh
    git clone [https://github.com/Dendroculus/nama-repo-anda.git](https://github.com/Dendroculus/nama-repo-anda.git)
    ```
2.  **Masuk ke direktori proyek:**
    ```sh
    cd nama-repo-anda
    ```
3.  **Jalankan aplikasi:**
    ```sh
    python main.py
    ```
    Aplikasi akan dimulai, dan Anda dapat menavigasi fitur-fiturnya menggunakan menu di layar.

## 🛠️ Gambaran Umum Modul Kode

-   **`main.py`**: Penggerak utama aplikasi. File ini menampilkan menu utama dan menangani input pengguna untuk memanggil fungsi dari modul-modul pembantu.
-   **`helpers/addData.py`**: Berisi fungsi `tambah_task`. Modul ini meminta detail tugas kepada pengguna, memvalidasi input (misalnya, memeriksa nama duplikat dan tanggal yang valid), dan menambahkan tugas baru ke dalam daftar.
-   **`helpers/changeData.py`**: Sebuah modul untuk memodifikasi tugas. Ini mencakup fungsi untuk memperbarui bidang tertentu dari tugas (`ubah_task`), menghapus tugas tertentu (`hapus_data`), menandai tugas sebagai selesai (`selesaikan_task`), dan membersihkan semua tugas yang telah selesai (`hapus_task_selesai`).
-   **`helpers/dataFilters.py`**: Modul inti yang mencakup fungsi untuk memfilter tugas berdasarkan berbagai rentang waktu, prioritas, dan status. Modul ini juga berisi fungsi penting `data_task` untuk menampilkan semua data dalam tabel yang bersih dengan ukuran dinamis.
-   **`helpers/reports.py`**: Berisi fungsi `laporan_statistik`, yang menghitung dan mencetak laporan ringkasan dalam kotak yang diformat.
-   **`helpers/search.py`**: Mengimplementasikan fungsionalitas `cari_task` untuk menemukan dan menampilkan tugas berdasarkan pencarian kata kunci.
-   **`helpers/sorter.py`**: Menyediakan serangkaian fungsi pengurutan yang komprehensif. Dapat mengurutkan tugas berdasarkan tenggat waktu, nama, prioritas, atau status dalam urutan menaik dan menurun.

## 👤 Kontributor

<table border="0" cellspacing="10" cellpadding="5">
  <tr>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Jess2Jes">
        <img src="https://github.com/Jess2Jes.png" width="100" height="100" alt="Jess2Jes" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Jess2Jes">Jess2Jes</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Dendroculus">
        <img src="https://github.com/Dendroculus.png" width="100" height="100" alt="Hans 展豪" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Dendroculus">Hans 展豪</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Solynixx">
        <img src="https://github.com/Solynixx.png" width="100" height="100" alt="Solynixx" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Solynixx">Solynixx</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/StevNard">
        <img src="https://github.com/StevNard.png" width="100" height="100" alt="StevNard" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/StevNard">StevNard</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Milkdrinker-creator">
        <img src="https://github.com/Milkdrinker-creator.png" width="100" height="100" alt="Milkdrinker-creator" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Milkdrinker-creator">Milkdrinker-creator</a>
    </td>
        <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Azelezasl">
        <img src="https://github.com/Azelezasl.png" width="100" height="100" alt="Azelezasl" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Azelezasl">Azelezasl</a>
    </td>
    
  </tr>
</table>