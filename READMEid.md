[English](README.md) | Bahasa Indonesia | [中文](READMECN.md)
# TaskMaster CLI: Sistem Manajemen Tugas Berbasis Python

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Sebuah aplikasi manajemen tugas berbasis *command-line* yang komprehensif dan dibangun dengan Python. Alat ini memungkinkan pengguna untuk secara efisien menambah, melacak, memfilter, dan mengelola tugas serta jadwal harian mereka langsung dari terminal. Didesain sebagai proyek tugas sekolah, aplikasi ini mendemonstrasikan konsep inti pemrograman termasuk manipulasi data, desain modular, dan interaksi *command-line* yang ramah pengguna.

## ✨ Fitur Utama

-   **Fungsionalitas CRUD Penuh**: Tambah, lihat, perbarui, dan hapus tugas dengan mudah.
-   **Filter Tingkat Lanjut**: Filter tugas secara dinamis berdasarkan **status** (`Tertunda`, `Sedang Dikerjakan`, `Selesai`), **prioritas** (`Tinggi`, `Sedang`, `Rendah`), atau **tenggat waktu** (*deadline*).
-   **Pengurutan Cerdas**: Urutkan tugas secara kronologis secara otomatis untuk menjaga jadwal Anda tetap terorganisir.
-   **Prioritas Tugas**: Lihat "3 Tugas Paling Penting" secara instan berdasarkan kombinasi prioritas dan tenggat waktu yang akan datang.
-   **Pencarian Dinamis**: Temukan tugas apa pun dengan cepat berdasarkan namanya.
-   **Laporan Statistik**: Hasilkan laporan terperinci yang mencakup total tugas, rincian status, dan penugasan pengguna.
-   **Antarmuka yang Ramah Pengguna**: Antarmuka berbasis menu yang sederhana dan intuitif untuk navigasi yang lancar.
-   **Format Tabel Dinamis**: Daftar tugas ditampilkan dalam tabel yang diformat dengan rapi dan ukurannya menyesuaikan dengan panjang konten.

## 📸 Demo

Berikut adalah tampilan menu utama dan contoh output daftar tugas:

**Menu Utama:**
```
────────────────────Menu────────────────────
1. Tambah Task
2. Daftar Task
3. Cari Task
4. Sortir Task
5. Laporan Statistik
6. Filter
7. Keluar
────────────────────────────────────────────
Pilihan : 2
```

**Contoh Output (`Daftar Task`):**
```
──────────────────────────────────────────────────────────────────────────────────────────
                                       Semua Task
──────────────────────────────────────────────────────────────────────────────────────────
ID │ Task                      │ Deadline            │ Priority │ Status
──────────────────────────────────────────────────────────────────────────────────────────
1  │ Kerjakan Tugas Basis Data │ 2025-10-05 13:00 PM │ High     │ Pending
2  │ Belajar Algoritma         │ 2025-10-06 12:57 PM │ Medium   │ In Progress
3  │ Buat Slide Presentasi     │ 2025-10-08 16:49 PM │ High     │ Completed
4  │ Rapat Tim                 │ 2025-10-04 15:00 PM │ Low      │ Completed
5  │ Kerjakan Tugas PBO        │ 2025-10-04 15:00 PM │ High     │ Completed
──────────────────────────────────────────────────────────────────────────────────────────
```

## 📂 Struktur Proyek

Proyek ini diorganisir ke dalam file-file modular untuk keterbacaan dan pemeliharaan yang lebih baik. Disarankan untuk menempatkan skrip-skrip pembantu di dalam direktori `helpers`.

```
nama-proyek-anda/
├── main.py                     # Titik masuk utama aplikasi
└── helpers/
    ├── __init__.py
    ├── addData.py              # Menangani logika untuk menambah tugas baru
    ├── dataFilters.py          # Fungsi untuk memfilter, mengurutkan, dan menampilkan tugas
    ├── searchUpdateTask.py     # Mengelola pencarian dan pembaruan tugas yang ada
    ├── deleteTask.py           # Logika untuk menghapus tugas
    ├── sortTask.py             # Logika inti untuk mengurutkan tugas
    └── reportStats.py          # Menghasilkan dan mencetak statistik tugas
```
*Catatan: Nama file asli seperti `Program Pencarian & Perubahan Data.py` telah diubah menjadi `searchUpdateTask.py` dalam struktur ini untuk mengikuti konvensi penamaan standar Python.*

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

-   **`main.py`**: Penggerak utama aplikasi. File ini menampilkan menu utama dan menangani input pengguna untuk menavigasi ke berbagai fungsionalitas seperti menambah, memfilter, atau melihat tugas.
-   **`helpers/addData.py`**: Berisi fungsi `tambah_task`. Modul ini meminta detail tugas kepada pengguna (nama, tenggat waktu, prioritas, status), memvalidasi input, dan menambahkan tugas baru ke dalam daftar.
-   **`helpers/dataFilters.py`**: Modul inti yang mencakup fungsi untuk:
    -   Memfilter tugas berdasarkan tenggat waktu (`filter_by_deadline`), prioritas (`filter_by_priority`), dan status (`filter_by_status`).
    -   Mengidentifikasi dan mengembalikan tugas-tugas terpenting (`get_top_tasks`).
    -   Menampilkan tugas dalam tabel yang bersih dengan ukuran dinamis (`data_task`).
-   **`helpers/searchUpdateTask.py`**: Mengimplementasikan fungsionalitas pencarian untuk menemukan tugas berdasarkan namanya dan menyediakan antarmuka untuk memperbarui detailnya.
-   **`helpers/deleteTask.py`**: Menyediakan logika untuk menemukan dan menghapus tugas tertentu dari daftar data.
-   **`helpers/sortTask.py`**: Berisi logika untuk mengurutkan daftar tugas, terutama berdasarkan tenggat waktunya.
-   **`helpers/reportStats.py`**: Menghitung dan mencetak laporan ringkasan, termasuk jumlah tugas berdasarkan status, kategori, dan pengguna.

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
  </tr>
</table>

