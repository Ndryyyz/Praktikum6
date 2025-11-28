# Program Daftar Nilai Mahasiswa

## Deskripsi
Program sederhana untuk mengelola daftar nilai mahasiswa menggunakan Python. Program ini menyediakan fitur CRUD (Create, Read, Update, Delete) untuk data mahasiswa.

## Fitur Program

### 1. Tambah Data (`tambah()`)
Menambahkan data mahasiswa baru ke dalam sistem dengan memasukkan:
- Nama mahasiswa
- Nilai mahasiswa

### 2. Tampilkan Data (`tapilkan()`)
Menampilkan seluruh daftar mahasiswa beserta nilai mereka dalam format tabel yang rapi.

### 3. Hapus Data (`hapus(nama)`)
Menghapus data mahasiswa berdasarkan nama yang diinputkan.

### 4. Ubah Data (`ubah(nama)`)
Mengubah nilai mahasiswa berdasarkan nama yang diinputkan.

## Struktur Data
Program menggunakan list of dictionary untuk menyimpan data:
```python
data_mahasiswa = [
    {"nama": "Budi", "nilai": 85.5},
    {"nama": "Ani", "nilai": 90.0}
]
```

## Cara Menggunakan

1. **Clone atau Download Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Jalankan Program**
   ```bash
   python Lab6.py
   ```

3. **Pilih Menu**
   - Ketik angka 1-5 untuk memilih menu
   - Ikuti instruksi yang muncul di layar

## Contoh Penggunaan

```
=== MENU PROGRAM ===
1. Tambah data
2. Tampilkan data
3. Hapus data
4. Ubah data
5. Keluar
Pilih menu (1-5): 1

Masukkan nama mahasiswa: Budi
Masukkan nilai: 85.5
Data Budi berhasil ditambahkan!
```

## Flowchart Program

```
┌─────────────────┐
│      START      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tampilkan Menu │
│   1. Tambah     │
│   2. Tampilkan  │
│   3. Hapus      │
│   4. Ubah       │
│   5. Keluar     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Input Pilihan  │
└────────┬────────┘
         │
         ▼
    ┌────┴────┐
    │ Pilihan │
    └──┬──┬──┬──┬──┘
       │  │  │  │
   ┌───┘  │  │  └───┐
   │      │  │      │
   ▼      ▼  ▼      ▼
┌─────┐ ┌──┐ ┌──┐ ┌────┐
│  1  │ │2 │ │3 │ │ 4  │
└──┬──┘ └┬─┘ └┬─┘ └─┬──┘
   │     │    │     │
   ▼     ▼    ▼     ▼
┌──────┐┌────┐┌───┐┌────┐
│Tambah││Show││Del││Edit│
└──┬───┘└─┬──┘└─┬─┘└─┬──┘
   │      │     │    │
   └──────┴─────┴────┘
          │
          ▼
     ┌─────────┐
     │ Keluar? │
     └────┬────┘
       Ya │ │ Tidak
          │ └─────┐
          ▼       │
      ┌──────┐    │
      │ END  │◄───┘
      └──────┘
```

## Flowchart Detail Setiap Fungsi

### Fungsi Tambah
```
START → Input Nama → Input Nilai → 
Simpan ke List → Tampilkan Konfirmasi → END
```

### Fungsi Tampilkan
```
START → Cek Data Kosong? 
├─ Ya → Tampilkan "Belum ada data" → END
└─ Tidak → Loop semua data → Tampilkan → END
```

### Fungsi Hapus
```
START → Input Nama → Cari di List → 
├─ Ditemukan → Hapus → Konfirmasi → END
└─ Tidak Ditemukan → Tampilkan Error → END
```

### Fungsi Ubah
```
START → Input Nama → Cari di List → 
├─ Ditemukan → Input Nilai Baru → Update → Konfirmasi → END
└─ Tidak Ditemukan → Tampilkan Error → END
```

## Tabel Fungsi

| No | Nama Fungsi | Parameter | Return | Deskripsi |
|----|-------------|-----------|--------|-----------|
| 1  | `tambah()`  | -         | None   | Menambah data mahasiswa baru |
| 2  | `tapilkan()`| -         | None   | Menampilkan semua data |
| 3  | `hapus()`   | nama      | None   | Menghapus data berdasarkan nama |
| 4  | `ubah()`    | nama      | None   | Mengubah nilai berdasarkan nama |
| 5  | `main()`    | -         | None   | Fungsi utama program |

## Persyaratan Sistem
- Python 3.6 atau lebih baru
- Tidak memerlukan library eksternal

## Catatan
- Data hanya tersimpan sementara (tidak persisten)
- Data akan hilang saat program ditutup
- Pencarian nama tidak case-sensitive

## Pengembangan Selanjutnya
- [ ] Menyimpan data ke file (JSON/CSV)
- [ ] Validasi input nilai (harus angka 0-100)
- [ ] Fitur pencarian mahasiswa
- [ ] Export data ke Excel
- [ ] Sistem login

## Kontributor
- Nama Anda
- NIM Anda
- Kelas Anda

## Lisensi
MIT License

---
**Tugas Praktikum - Pemrograman Python**
