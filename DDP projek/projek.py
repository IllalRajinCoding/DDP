import pyfiglet
judul = pyfiglet.figlet_format("Selamat Datang di JUNKFOOD")
print(judul)

menu = {
    'burger':12000,
    'Coca-cola':9000,
    'kentang goreng':10000,
    'nasi':2000,
    'matcha':15000,
    'chiken':18000,
}

print('======================== daftar menu =======================')
for i in menu:
    print('Daftar menu :', i, 'harga:', menu[i])
print('Anda akan mendapatkan diskon 10% jika membeli lebih dari 2 item')
print('============================================================')
beli = input('pilih menu :')
jumlah = int(input('Jumlah pesanan :'))
bayar = jumlah * menu[beli]

if jumlah > 2:
    diskon = bayar * 10/100
    total = bayar - diskon

else:
    total = bayar

print('========================== Detail Pembayaran ==========================')
print('Menu yang dibeli         :', beli,)
print('jumlah                   :', jumlah)
print('Total biaya              :' , bayar)
print('Total yang harus dibayar :' ,total)
print('=======================================================================')
print('                             ilal                                      ')
