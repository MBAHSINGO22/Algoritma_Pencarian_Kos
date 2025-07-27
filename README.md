# 📝 Algoritma Pencarian Kos

**Implementasi Algoritma Backtracking dan Greedy untuk Pencarian Kos Terbaik**  
Proyek pembelajaran Python yang menerapkan algoritma Backtracking dan Greedy untuk memilih kos terbaik berdasarkan harga dan jarak dari data yang diberikan.

---

## 📖 Deskripsi Proyek

**Algoritma_Pencarian_Kos** adalah proyek pembelajaran Python yang mengimplementasikan dua pendekatan algoritma untuk memilih kos terbaik dari dataset `data_kos.docx`:

- 📊 **Algoritma Backtracking**: Mengeksplorasi semua kemungkinan kombinasi kos dengan batasan harga maksimum Rp500.000 dan jarak maksimum 450 meter, memilih kos dengan harga termurah dan jarak terdekat jika ada konflik.
- 🔍 **Algoritma Greedy**: Memilih kos terbaik dengan pendekatan greedy berdasarkan harga termurah dari kandidat yang memenuhi batasan harga maksimum Rp500.000 dan jarak maksimum 450 meter.
- 📋 **Data Kos**: Menggunakan file Word (`data_kos.docx`) yang berisi daftar kos dengan nama, harga per bulan, dan jarak dalam meter.

Proyek ini terdiri dari dua skrip Python (`Backtracking.py`, `Greedy.py`) dan file data (`data_kos.docx`). Cocok untuk pemula yang ingin mempelajari algoritma pencarian dan pemrograman Python. 🟢

---

## 🧠 Teknologi

- Python 3.x  
- python-docx

---

## 📂 Struktur File

```
Algoritma_Pencarian_Kos/
├── Backtracking.py                # 📊 Skrip untuk algoritma backtracking
├── Greedy.py                      # 🔍 Skrip untuk algoritma greedy
├── data_kos.docx                  # 📋 Dataset kos dalam format Word
├── README.md                      # 📖 Dokumentasi proyek
├── requirements.txt               # ⚙️ Daftar dependensi Python
```

---

## ▶️ Menjalankan Program

### 1. Kloning Repositori:

```bash
git clone https://github.com/MBAHSINGO22/Algoritma_Pencarian_Kos.git
cd Algoritma_Pencarian_Kos
```

### 2. Pastikan Python Terinstal:

Periksa versi Python:

```bash
python --version
```

Jika belum terinstal, unduh dari [python.org](https://www.python.org/).

### 3. Instal Dependensi:

Instal pustaka yang diperlukan dari `requirements.txt`:

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:

```
python-docx
```

### 4. Jalankan Skrip Python:

Untuk algoritma **Backtracking**:

```bash
python Backtracking.py
```

Untuk algoritma **Greedy**:

```bash
python Greedy.py
```

> Pastikan file `data_kos.docx` berada di direktori yang sama dengan skrip atau sesuaikan `file_path` dalam kode.

---

## 🟢 Catatan:

- File `data_kos.docx` harus ada di direktori yang sama dengan skrip atau sesuaikan path di kode.
- Algoritma **Backtracking** mengevaluasi semua kemungkinan untuk menemukan kos terbaik.
- Algoritma **Greedy** memilih solusi pertama yang valid berdasarkan harga termurah.
- Dataset harus berupa tabel Word dengan kolom **Nama Kos**, **Harga/bulan**, dan **Jarak (m)**.

---

## 📈 Contoh Output

### **Backtracking.py**
```
=== Mulai Pencarian Kos Terbaik ===
Memeriksa: Pak Mushofa Depok Sleman (Harga: 500000, Jarak: 550)
  => Tidak valid
...
Memeriksa: Bu Santini (Harga: 500000, Jarak: 400)
  => Valid
  => Menjadi kandidat terbaik sementara
Memeriksa: Putri Sekar Ayu (Harga: 585000, Jarak: 280)
  => Valid
  => Menjadi kandidat terbaik sementara
...
=== Selesai ===

Kos yang dipilih: Nama=Putri Sekar Ayu, Harga=585000, Jarak=280
```

### **Greedy.py**
```
=== Filter Kos yang Valid (harga ≤ 500000 dan jarak ≤ 450) ===
Memeriksa: Bu Santini (Harga: 500000, Jarak: 400)
  => VALID, ditambahkan ke kandidat

=== Pemilihan Kos Terbaik Berdasarkan Harga Termurah ===
Memeriksa kandidat: Bu Santini (Harga: 500000, Jarak: 400)
  => Dipilih sebagai kos terbaik (greedy)

=== Hasil Akhir ===
Kos yang dipilih: Nama=Bu Santini, Harga=500000, Jarak=400
```

---

## 👨‍💻 Pengembang

**MBAHSINGO22**  
🔗 [GitHub](https://github.com/MBAHSINGO22)
