import pyfiglet
import json

#import json
file_json = open("sembako.json")

daftar_sembako = json.loads(file_json.read())


# Menampilkan judul
judul = pyfiglet.figlet_format('Toko Indo NF')
print(judul)

# Bagian header
print('====== SELAMAT DATANG DI TOKO KAMI ======'.center(80))
print('=Kami akan memenuhi kebutuhan pokok anda='.center(80))
print('========================================='.center(80))

def print_sembako(data):
    print(f"{'ID':<5} {'Nama':<25} {'Jenis':<15} {'Harga':<15} {'Stok':<10} {'Satuan'}")
    print("=" * 80)
    
    for item in data['sembako']:
        # Nentuin harga satuan
        harga = (
            item.get('harga_per_kg') or
            item.get('harga_per_liter') or
            item.get('harga_per_butir') or
            item.get('harga_per_100g') or
            item.get('harga_per_karton') or
            item.get('harga_per_paket') or
            0  # Default jika tidak ada harga
        )

        print(f"{item['id']:<5} {item['nama']:<25} {item['jenis']:<15} {harga:<15} {item['stok']:<10} {item['satuan']}")

# Memanggil fungsi untuk mencetak data
print_sembako(daftar_sembako)
print("="*80)

# Daftar belanja
belanja = []

# Meminta input nama barang dan jumlah barang
while True:
    print("="*80)
    nama_barang = input('Masukkan nama barang: ')
    jumlah_barang = int(input('Masukkan jumlah barang: '))
    print("="*80)

    # Mencari harga barang dari daftar sembako
    harga_barang = None
    for item in daftar_sembako['sembako']:
        if item['nama'].lower() == nama_barang.lower():
            harga_barang = (
                item.get('harga_per_kg') or
                item.get('harga_per_liter') or
                item.get('harga_per_butir') or
                item.get('harga_per_100g') or
                item.get('harga_per_karton') or
                item.get('harga_per_paket') or
                0
            )
            break
    
    if harga_barang is None:
        print("Barang tidak ditemukan. Silakan coba lagi.")
        continue

    # Menambahkan barang ke dalam belanja
    belanja.append({
        'nama': nama_barang,
        'harga': harga_barang,
        'jumlah': jumlah_barang
    })
    print(f"{jumlah_barang} {nama_barang} telah ditambahkan ke dalam belanja.")

    # fungsi buat nanya item 'nambah/ga'
    tambah = input('Apakah Anda ingin menambahkan barang lain? (ya/tidak) : ').strip().lower()
    if tambah != 'ya':
        break

# Proses pembelian (contoh)
total_harga = sum(item['harga'] * item['jumlah'] for item in belanja)
print(f"Total harga belanja Anda adalah: Rp {total_harga:.2f}")