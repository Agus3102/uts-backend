pakaian = ['Kaos', 'Kemeja', 'Jaket']
kirim = ['JNE', 'JNT', 'SiCepat']
waktu = ['1 hari', '3 hari', '1 minggu']

while True:
    print('==== Toko Baju Online ====')

    for p in range(0, len(pakaian)):
        print(f'{p+1}.{pakaian[p]}')

    pilih = int(input('Silahkan Pilih Pakaian : '))
    print('==== Kirim Melalui ====')

    for k in range(0, len(kirim)):
        print(f'{k+1}.{kirim[k]}')

    tujuan = int(input('Silahkan Pilih dikirim Melalui : '))

    print('==== waktu ====')
    for w in range(0, len(waktu)):
        print(f'{w+1}.{waktu[w]}')
    tipe = int(input('Silahkan Pilih waktu kapan sampai : '))

    print('====================')
    print(f'Pakaian yang dipilih : {pakaian[pilih-1]}')
    print(f'Pengiriman melalui : {kirim[tujuan-1]}')
    print(f'Kecepatan pengiriman barang : {waktu[tipe-1]}')
    print('Sedang Di Proses')
    print('====================')
    lanjut = input('Apakah ingin memesan Lagi y/n ')
    if lanjut == 'y' or lanjut == 'Y':
        continue
    else:
        break