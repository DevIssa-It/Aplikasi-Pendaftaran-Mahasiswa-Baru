# Aplikasi Pendaftaran Mahasiswa Baru

Program Python untuk mengelola data pendaftaran mahasiswa baru menggunakan struktur data dictionary.

## Deskripsi

Aplikasi ini memungkinkan pengguna untuk mendaftarkan, menampilkan, mencari, dan menghapus data mahasiswa baru. Data disimpan dalam bentuk dictionary dengan NIM sebagai key dan informasi mahasiswa (Nama, Prodi, IPK) sebagai value.

## Fitur

1. **Tambah Mahasiswa**
   - Memasukkan data mahasiswa baru (NIM, Nama, Prodi, IPK)
   - Validasi NIM duplikat
   - Validasi input kosong
   - Validasi IPK (0.00 - 4.00)

2. **Tampilkan Semua Mahasiswa**
   - Menampilkan daftar semua mahasiswa dalam format tabel
   - Menampilkan total jumlah mahasiswa terdaftar

3. **Cari Mahasiswa berdasarkan NIM**
   - Mencari dan menampilkan detail mahasiswa berdasarkan NIM
   - Validasi NIM tidak ditemukan

4. **Hapus Mahasiswa berdasarkan NIM**
   - Menghapus data mahasiswa dari database
   - Konfirmasi sebelum menghapus

5. **Keluar**
   - Keluar dari program

## Struktur Data

```python
data_mahasiswa = {
    'NIM': {
        'nama': 'Nama Mahasiswa',
        'prodi': 'Program Studi',
        'ipk': 3.75
    }
}
```

## Cara Menjalankan

1. Pastikan Python sudah terinstal di komputer Anda
2. Clone atau download repository ini
3. Buka terminal/command prompt
4. Navigate ke folder program:
   ```bash
   cd "Aplikasi Pendaftaran Mahasiswa Baru"
   ```
5. Jalankan program:
   ```bash
   python pendaftaran_mahasiswa.py
   ```

## Contoh Penggunaan

```
==================================================
   SISTEM PENDAFTARAN MAHASISWA BARU
==================================================
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Cari Mahasiswa berdasarkan NIM
4. Hapus Mahasiswa berdasarkan NIM
5. Keluar
==================================================

Pilih menu (1-5): 1

--- TAMBAH MAHASISWA BARU ---
Masukkan NIM: 123456
Masukkan Nama: Ahmad Fauzi
Masukkan Program Studi: Teknik Informatika
Masukkan IPK (0.00 - 4.00): 3.75
Mahasiswa dengan NIM 123456 berhasil ditambahkan!
```

## Validasi Input

Program ini dilengkapi dengan berbagai validasi untuk memastikan data yang dimasukkan valid:

- **NIM**: Tidak boleh kosong dan harus unik (tidak duplikat)
- **Nama**: Tidak boleh kosong
- **Program Studi**: Tidak boleh kosong
- **IPK**: Harus berupa angka dalam rentang 0.00 - 4.00

## Error Handling

Program menangani berbagai jenis error:
- Input yang tidak valid
- NIM duplikat
- NIM tidak ditemukan
- ValueError untuk input IPK yang bukan angka
- KeyboardInterrupt untuk penghentian program oleh pengguna

## Teknologi yang Digunakan

- Python 3.x
- Built-in Python modules (tidak memerlukan instalasi package tambahan)

## Struktur Program

- `tampilkan_menu()`: Menampilkan menu utama
- `tambah_mahasiswa()`: Menambahkan data mahasiswa baru
- `tampilkan_semua_mahasiswa()`: Menampilkan semua data mahasiswa
- `cari_mahasiswa()`: Mencari mahasiswa berdasarkan NIM
- `hapus_mahasiswa()`: Menghapus data mahasiswa
- `main()`: Fungsi utama program

## Author

A. Issadurrofiq Jaya Utama

## Lisensi

Project ini dibuat untuk keperluan tugas kuliah.
