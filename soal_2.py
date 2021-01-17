print("Buatlah program untuk penambahan bonus dan diskon belanja")
print('============================================================')
totalBelanja = float(input("Masukan total belanja anda: "))
if totalBelanja >= 200000:
    diskon = 0.15
    totalDiskon = diskon * totalBelanja
    print('==========================================')
    print('== Anda mendapatkan Diskon dan Bonus    ==')
    print('== Diskon 15% dan Bonus Makanan/Minuman ==')
    print('==========================================')
    print('Total benlanja anda adalah: ',totalBelanja)
    print('Kamu dpt potongan',totalDiskon)
    print('Harga yang harus dibayar: ',totalBelanja - totalDiskon)
else:
    print('=========================================================')
    print('Total belanja anda adalah: ',totalBelanja)
    print('Harga yang harus dibayar: ',totalBelanja)
    