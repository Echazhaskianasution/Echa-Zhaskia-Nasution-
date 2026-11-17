def program_tiket_bioskop():
    print("==========================================")
    print("   SELAMAT DATANG DI BIOSKOP CINEMA        ")
    print("==========================================")
    
    # Ketentuan Harga Tiket
    # Reguler : Rp35.000
    # VIP     : Rp50.000
    # Premium : Rp75.000
    
    # 5. Proses Berulang (Menggunakan perulangan untuk melayani beberapa pelanggan)
    while True:
        print("\n--- Input Data Pelanggan Baru ---")
        # 1. Input Nama Pelanggan
        nama_pelanggan = input("Masukkan nama pelanggan (atau ketik 'selesai' untuk keluar): ")
        if nama_pelanggan.lower() == 'selesai':
            print("\nTerima kasih telah menggunakan program pemesanan tiket bioskop!")
            break
            
        # 2. Input Jenis dan Jumlah Tiket
        print("Pilih Jenis Tiket:")
        print("1. Reguler (Rp35.000)")
        print("2. VIP (Rp50.000)")
        print("3. Premium (Rp75.000)")
        
        pilihan_jenis = input("Masukkan pilihan jenis tiket (Reguler/VIP/Premium): ").strip().capitalize()
        
        if pilihan_jenis not in ["Reguler", "Vip", "Premium"]:
            print("Maaf, jenis tiket tidak valid. Silakan ulangi pemesanan.")
            continue
            
        try:
            jumlah_tiket = int(input("Masukkan jumlah tiket yang dibeli: "))
            if jumlah_tiket <= 0:
                print("Jumlah tiket harus lebih dari 0.")
                continue
        except ValueError:
            print("Input jumlah tiket harus berupa angka!")
            continue
            
        # 3. Tentukan Harga (Menggunakan percabangan untuk menentukan harga dasar)
        if pilihan_jenis == "Reguler":
            harga_satuan = 35000
        elif pilihan_jenis == "Vip":
            pilihan_jenis = "VIP"  # Menyamakan format tampilan
            harga_satuan = 50000
        elif pilihan_jenis == "Premium":
            harga_satuan = 75000
            
        subtotal = harga_satuan * jumlah_tiket
        
        # 4. Cek Diskon (Percabangan diskon 10% jika beli > 3 tiket)
        diskon = 0
        status_diskon = "Tidak Mendapatkan Diskon"
        
        if jumlah_tiket > 3:
            diskon = 0.10 * subtotal
            status_diskon = "Mendapat Diskon 10%"
        else:
            status_diskon = "Membayar Harga Normal"
            
        total_pembayaran = subtotal - diskon
        
        # Menampilkan Struk / Rincian Pemesanan Pelanggan
        print("\n------------------------------------------")
        print("         STRUK PEMESANAN TIKET            ")
        print("------------------------------------------")
        print(f" Nama Pelanggan   : {nama_pelanggan}")
        print(f" Jenis Tiket      : {pilihan_jenis}")
        print(f" Jumlah Tiket     : {jumlah_tiket}")
        print(f" Harga Satuan     : Rp {harga_satuan:,}")
        print(f" Subtotal         : Rp {subtotal:,}")
        print(f" Keterangan       : {status_diskon}")
        if diskon > 0:
            print(f" Jumlah Diskon    : Rp {diskon:,.0f}")
        print(f" Total Pembayaran : Rp {total_pembayaran:,.0f}")
        print("------------------------------------------")

# Menjalankan program
if __name__ == "__main__":
    program_tiket_bioskop()