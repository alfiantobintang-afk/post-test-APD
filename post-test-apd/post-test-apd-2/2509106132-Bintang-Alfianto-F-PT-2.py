nama_pelanggan = input("Masukkan nama pelanggan: ")
jumlah_batu_bata = int(input("Masukkan jumlah batu bata yang dibeli: "))
jumlah_semen = int(input("Masukkan jumlah karung semen yang dibeli: "))

harga_bata = 100
harga_semen = 100000

total_awal = (jumlah_batu_bata * harga_bata) + (jumlah_semen * harga_semen)

is_paket_hemat = jumlah_batu_bata >= 500 and jumlah_semen >= 5
is_paket_ultra = jumlah_batu_bata >= 2000 and jumlah_semen >= 16

if is_paket_ultra:
    diskon_persen = 0.30
    ket_diskon = "Paket Ultra Mantap (30%)"
elif is_paket_hemat:
    diskon_persen = 0.15
    ket_diskon = "Paket Hemat (15%)"
else:
    diskon_persen = 0
    ket_diskon = "Tidak Ada Diskon"

jumlah_diskon = total_awal * diskon_persen
total_akhir = float(total_awal - jumlah_diskon)

print("="*42)
print("        ESTIMASI BIAYA BAHAN BANGUNAN       ")
print("="*42)
print(f"Nama Pelanggan : {nama_pelanggan}")
print("-"*57)
print("| Barang     | Jumlah     | Harga Satuan       |")
print("-"*57)
print(f"| Batu Bata  | {jumlah_batu_bata:<10} | Rp{harga_bata:<15} |")
print(f"| Semen      | {jumlah_semen:<10} | Rp{harga_semen:<15} |")
print("-"*57)
print(f"Total Biaya Awal         : Rp {total_awal:,}")
print(f"Diskon yang Didapat      : {ket_diskon}")
print(f"Jumlah Diskon            : Rp {int(jumlah_diskon):,}")
print("-"*57)
print(f"TOTAL BIAYA AKHIR        : Rp {int(total_akhir):,}")
print("="*42)
