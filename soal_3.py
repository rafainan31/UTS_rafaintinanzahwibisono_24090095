jumlah_barang = int(input("Masukan Jumlah Barang : "))

total_harga = 0
for a in range(jumlah_barang):
    harga = int(input(f'Masukan harga barang ke- {a+1}: '))
    total_harga += harga
if jumlah_barang>0:
    rata_rata = jumlah_barang + total_harga
    print(f'Total Belanjaan dari {jumlah_barang} adalah {rata_rata : .2f}')