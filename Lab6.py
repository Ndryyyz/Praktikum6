data_mahasiswa = []

def tambah():
    """Fungsi untuk menambah data mahasiswa"""
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai: "))
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print(f"Data {nama} berhasil ditambahkan!\n")

def tapilkan():
    """Fungsi untuk menampilkan semua data mahasiswa"""
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.\n")
        return
    
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    print("-" * 40)
    for i, mhs in enumerate(data_mahasiswa, 1):
        print(f"{i}. Nama: {mhs['nama']:<20} Nilai: {mhs['nilai']}")
    print("-" * 40 + "\n")

def hapus(nama):
    """Fungsi untuk menghapus data berdasarkan nama"""
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            data_mahasiswa.remove(mhs)
            print(f"Data {nama} berhasil dihapus!\n")
            return
    print(f"Data {nama} tidak ditemukan.\n")

def ubah(nama):
    """Fungsi untuk mengubah data berdasarkan nama"""
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            nilai_baru = float(input(f"Masukkan nilai baru untuk {nama}: "))
            mhs['nilai'] = nilai_baru
            print(f"Data {nama} berhasil diubah!\n")
            return
    print(f"Data {nama} tidak ditemukan.\n")

# Program utama
def main():
    while True:
        print("=== MENU PROGRAM ===")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Hapus data")
        print("4. Ubah data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tapilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama yang akan dihapus: ")
            hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama yang akan diubah: ")
            ubah(nama)
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()
