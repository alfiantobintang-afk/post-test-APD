nim = input("Masukkan NIM kalian: ")
stamina = int(nim[-3:])
chakra = 0

print("\n=== Misi 1: Menyempurnakan Rasengan ===")
while stamina > 0 and chakra < 200:
    chakra += 5       
    stamina -= 3      

print(f"Chakra yang dikumpulkan: {chakra}")
print(f"Sisa stamina: {stamina}")

if chakra >= 200:
    print("Naruto berhasil mencapai 200 chakra dan menyempurnakan Rasengan!")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra...")

tinggi_menara = int(nim[-2:])
gulungan = 0

print("\n=== Misi 2: Infiltrasi Menara ===")
for meter in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print(f"Tinggi menara: {tinggi_menara} meter")
print(f"Gulungan informasi yang ditemukan: {gulungan}")

jumlah_koridor = int(nim[-2])
intelijen = 0
perangkap = 0

print("\n=== Misi 3: Penyelidikan Markas Rahasia ===")
for koridor in range(1, jumlah_koridor + 1):
    print(f"\nKoridor {koridor}:")
    for ruangan in range(1, 4):  
        if ruangan % 2 != 0:
            print(f"  Ruangan {ruangan}: Data Intelijen ditemukan")
            intelijen += 1
        else:
            print(f"  Ruangan {ruangan}: Perangkap Peledak dijinakkan")
            perangkap += 1

print("\n=== Hasil Penyelidikan ===")
print(f"Total Data Intelijen: {intelijen}")
print(f"Total Perangkap Peledak: {perangkap}")
print("\n Semua misi berhasil dijalankan oleh Naruto!")