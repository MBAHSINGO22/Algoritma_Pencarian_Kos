# 📝 Algoritma Pencarian Kos

**Implementasi Algoritma Backtracking dan Greedy untuk Pencarian Kos Terbaik**  
Project yang menerapkan algoritma Backtracking dan Greedy untuk memilih kos terbaik berdasarkan harga dan jarak dari data yang diberikan.

---

## 📖 Deskripsi Proyek

**Algoritma_Pencarian_Kos** adalah project Python yang mengimplementasikan dua pendekatan algoritma untuk memilih kos terbaik dari dataset `data_kos.docx`:

- 📊 **Algoritma Backtracking**: Mengeksplorasi semua kemungkinan kombinasi kos dengan batasan harga maksimum Rp500.000 dan jarak maksimum 450 meter, memilih kos dengan harga termurah dan jarak terdekat jika ada konflik.
- 🔍 **Algoritma Greedy**: Memilih kos terbaik dengan pendekatan greedy berdasarkan harga termurah dari kandidat yang memenuhi batasan harga maksimum Rp500.000 dan jarak maksimum 450 meter.
- 📋 **Data Kos**: Menggunakan file Word (`data_kos.docx`) yang berisi daftar kos dengan nama, harga per bulan, dan jarak dalam meter.

Proyek ini terdiri dari dua skrip Python (`Backtracking.py`, `Greedy.py`) dan file data (`data_kos.docx`).🟢

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
```
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
