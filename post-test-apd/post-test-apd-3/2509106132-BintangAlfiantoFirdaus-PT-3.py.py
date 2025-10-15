print("=== Penghitung Gaji Karyawan PT. BOM ===")

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (peracik/pengantar): ")
hari_kerja = int(input("Masukkan jumlah hari kerja: "))
jam_kerja = int(input("Masukkan jumlah jam kerja per hari: "))
jumlah_lembur = int(input("Masukkan jumlah lembur: "))

HargaPetasan = 5000
bayaran_perjam = 0
bayaran_lembur = 0

if jabatan.lower() == "peracik":
    if hari_kerja >= 24 and jam_kerja >= 8 and jumlah_lembur >= 4:
        bayaran_perjam = 25000
        bayaran_lembur = 15000
    elif hari_kerja >= 18 and jam_kerja >= 6 and jumlah_lembur >= 2:
        bayaran_perjam = 20000
        bayaran_lembur = 10000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 10000

elif jabatan.lower() == "pengantar":
    if hari_kerja >= 20 and jam_kerja >= 7 and jumlah_lembur >= 7:
        bayaran_perjam = 25000
        bayaran_lembur = 20000
    elif hari_kerja >= 16 and jam_kerja >= 5 and jumlah_lembur >= 4:
        bayaran_perjam = 20000
        bayaran_lembur = 15000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 12000
else:
    print("Jabatan tidak dikenali. Gaji tidak bisa dihitung.")

total_gaji = ((bayaran_perjam * jam_kerja) * hari_kerja) + (jumlah_lembur * bayaran_lembur)

print("\n=== Detail Gaji Karyawan ===")
print("Nama Karyawan     :", nama)
print("Jabatan           :", jabatan)
print("Hari Kerja        :", hari_kerja)
print("Jam Kerja         :", jam_kerja)
print("Jumlah Lembur     :", jumlah_lembur)
print("Bayaran per Jam   : Rp", bayaran_perjam)
print("Bayaran Lembur    : Rp", bayaran_lembur)
print("Total Gaji        : Rp", total_gaji)