"""
Program Pendaftaran Mahasiswa Baru
Menggunakan dictionary untuk menyimpan data mahasiswa
"""

def tampilkan_menu():
    """Menampilkan menu utama program"""
    print("\n" + "="*50)
    print("   SISTEM PENDAFTARAN MAHASISWA BARU")
    print("="*50)
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa berdasarkan NIM")
    print("4. Hapus Mahasiswa berdasarkan NIM")
    print("5. Keluar")
    print("="*50)


def tambah_mahasiswa(data_mahasiswa):
    """Menambahkan mahasiswa baru ke dalam database"""
    print("\n--- TAMBAH MAHASISWA BARU ---")
    
    try:
        # Input NIM
        nim = input("Masukkan NIM: ").strip()
        
        # Validasi NIM kosong
        if not nim:
            print("Error: NIM tidak boleh kosong!")
            return
        
        # Validasi NIM duplikat
        if nim in data_mahasiswa:
            print(f"Error: NIM {nim} sudah terdaftar!")
            return
        
        # Input Nama
        nama = input("Masukkan Nama: ").strip()
        if not nama:
            print("Error: Nama tidak boleh kosong!")
            return
        
        # Input Prodi
        prodi = input("Masukkan Program Studi: ").strip()
        if not prodi:
            print("Error: Program Studi tidak boleh kosong!")
            return
        
        # Input IPK dengan validasi
        while True:
            try:
                ipk = float(input("Masukkan IPK (0.00 - 4.00): "))
                if 0.0 <= ipk <= 4.0:
                    break
                else:
                    print("Error: IPK harus dalam rentang 0.00 - 4.00!")
            except ValueError:
                print("Error: IPK harus berupa angka!")
        
        # Simpan data mahasiswa
        data_mahasiswa[nim] = {
            'nama': nama,
            'prodi': prodi,
            'ipk': ipk
        }
        
        print(f"Mahasiswa dengan NIM {nim} berhasil ditambahkan!")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def tampilkan_semua_mahasiswa(data_mahasiswa):
    """Menampilkan semua data mahasiswa"""
    print("\n--- DAFTAR SEMUA MAHASISWA ---")
    
    if not data_mahasiswa:
        print("Belum ada data mahasiswa yang terdaftar.")
        return
    
    print(f"\nTotal mahasiswa terdaftar: {len(data_mahasiswa)}")
    print("-" * 80)
    print(f"{'NIM':<15} {'Nama':<25} {'Prodi':<20} {'IPK':<10}")
    print("-" * 80)
    
    for nim, data in data_mahasiswa.items():
        print(f"{nim:<15} {data['nama']:<25} {data['prodi']:<20} {data['ipk']:<10.2f}")
    
    print("-" * 80)


def cari_mahasiswa(data_mahasiswa):
    """Mencari mahasiswa berdasarkan NIM"""
    print("\n--- CARI MAHASISWA ---")
    
    nim = input("Masukkan NIM yang dicari: ").strip()
    
    if not nim:
        print("Error: NIM tidak boleh kosong!")
        return
    
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print("\nMahasiswa ditemukan!")
        print("-" * 50)
        print(f"NIM         : {nim}")
        print(f"Nama        : {data['nama']}")
        print(f"Prodi       : {data['prodi']}")
        print(f"IPK         : {data['ipk']:.2f}")
        print("-" * 50)
    else:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")


def hapus_mahasiswa(data_mahasiswa):
    """Menghapus mahasiswa berdasarkan NIM"""
    print("\n--- HAPUS MAHASISWA ---")
    
    nim = input("Masukkan NIM yang akan dihapus: ").strip()
    
    if not nim:
        print("Error: NIM tidak boleh kosong!")
        return
    
    if nim in data_mahasiswa:
        # Konfirmasi sebelum menghapus
        nama = data_mahasiswa[nim]['nama']
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus mahasiswa {nama} (NIM: {nim})? (y/n): ").strip().lower()
        
        if konfirmasi == 'y':
            del data_mahasiswa[nim]
            print(f"Mahasiswa dengan NIM {nim} berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")


def main():
    """Fungsi utama program"""
    # Dictionary untuk menyimpan data mahasiswa
    data_mahasiswa = {}
    
    print("\nSelamat datang di Sistem Pendaftaran Mahasiswa Baru!")
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input("\nPilih menu (1-5): ").strip()
            
            if pilihan == '1':
                tambah_mahasiswa(data_mahasiswa)
            elif pilihan == '2':
                tampilkan_semua_mahasiswa(data_mahasiswa)
            elif pilihan == '3':
                cari_mahasiswa(data_mahasiswa)
            elif pilihan == '4':
                hapus_mahasiswa(data_mahasiswa)
            elif pilihan == '5':
                print("\nTerima kasih telah menggunakan sistem ini!")
                print("Program selesai.\n")
                break
            else:
                print("Pilihan tidak valid! Silakan pilih menu 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


# Menjalankan program
if __name__ == "__main__":
    main()
