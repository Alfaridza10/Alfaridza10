def tampilkan_menu():
    print("                          ")
    print("======== COFFE MENN =======")
    print("===========================")
    print("   ====MENU====   ")
    print("1. es teh                        Rp.8000")
    print("2. chocolate                     Rp.8000")
    print("3. thai tea                      Rp.12000")
    print("4. green tea                     Rp.8000")
    print("5. nasi goreng                   Rp.15000")
    print("6. roti bakar                    Rp.4000")
    print("   ====MENU====   ")

def pilihan_menu():
    while True:
        menu_pesanan = int(input("masukan menu pesanan(nomor menu): "))
        if menu_pesanan in [1, 2, 3, 4, 5, 6]:
            if menu_pesanan == 1:
                harga = 8000
            elif menu_pesanan == 2:
                harga = 8000
            elif menu_pesanan == 3:
                harga = 12000
            elif menu_pesanan == 4:
                harga = 8000
            elif menu_pesanan == 5:
                harga = 15000
            elif menu_pesanan == 6:
                harga = 4000
            break
        else:
            print("===Menu Tidak Tersedia Silahakan pilih Menu Lainnya ===")
    return harga

def tambah_pesanan(jumlah_pembelian, harga, h):
    for i in range(jumlah_pembelian):
        h.append(harga)
    return h

def kurangi_pesanan(jumlah_pembelian, kurang, h):
    for i in range(kurang):
        if kurang <= 1:
            a -= kurang
            del h[a]
            bayar = sum(h)
            break
        else:
            kurang -= a
            del h[kurang]
            if kurang < 0:
                break
    c = jumlah_pembelian - kurang
    return c, h

def tampilkan_total_pembayaran(jumlah_pembelian, h):
    c = jumlah_pembelian
    bayar = sum(h)
    print("Total pesanan : ", c)
    print("Total Pembayaran : Rp.{}".format(bayar))

while True:
    
    tampilkan_menu()

    h = []

    harga = pilihan_menu()

    jumlah_pembelian = int(input("masukan jumlah pembelian: "))
    h = tambah_pesanan(jumlah_pembelian, harga, h)

    while True:
        jawab = input("Apakah ada yang ingin ditambah? (tambah/tidak) : ")
        if jawab == 'tambah':
            tampilkan_menu()
            harga = pilihan_menu()
            jumlah_tambahan = int(input("masukan jumlah pembelian : "))
            h = tambah_pesanan(jumlah_tambahan, harga, h)
            c = jumlah_pembelian + jumlah_tambahan
            print("Total pesanan: ", c)
            bayar = sum(h)
            print("Total pembayaran : Rp.{}".format(bayar))
            break

        elif jawab == 'kurang':
            kurang = int(input("berapa jumlah yang dikurangkan ? : "))
            c, h = kurangi_pesanan(jumlah_pembelian, kurang, h)
            print("Total Pemesanan: ", c)
            bayar = sum(h)
            print("Total Pembayaran : Rp.{}".format(bayar))
            break
        if jawab == 'tidak':
            tampilkan_total_pembayaran(jumlah_pembelian, h)
        else:
            tampilkan_total_pembayaran(jumlah_pembelian, h)

        break

    konfirmasi = input("Apakah ada pesanan lain? (ya/tidak): ")
    if konfirmasi == 'tidak':
        break

print('==========================')
print('        Terima kasih      ')
print('                          ')
