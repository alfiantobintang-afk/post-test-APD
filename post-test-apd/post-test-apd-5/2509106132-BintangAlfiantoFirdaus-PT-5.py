import os


users = [
    [1, "admin", "123", "admin"],
    [2, "user", "123", "user"]
]


midlaners = [
    [1, "Lunox", "Burst", ["Genius Wand", "Glowing Wand", "Arcane Boots", "Lightning Truncheon", "Holy Crystal", "Blood Wings"]],
    [2, "Yve", "Poke", ["Enchanted Talisman", "Glowing Wand", "Demon Shoes", "Feather of Heaven", "Divine Glaive", "Blood Wings"]],
    [3, "Kagura", "Burst", ["Genius Wand", "Glowing Wand", "Arcane Boots", "Lightning Truncheon", "Holy Crystal", "Blood Wings"]],
]
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== LIST ITEM MIDLANER MOBILE LEGENDS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        user = None
        for u in users:
            if u[1] == username and u[2] == password:
                user = u
                break

        if user is None:
            print("Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue

        print(f"Login berhasil! Selamat datang, {user[3]}!")
        input("Tekan Enter untuk melanjutkan...")

        
        if user[3] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. Lihat Hero Midlaner")
                print("2. Tambah Hero Baru")
                print("3. Update Hero")
                print("4. Hapus Hero")
                print("5. Logout")

                pilihan = input("Pilih menu: ")

                
                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR HERO MIDLANER ===")
                    print("ID\tNama\t\tTipe\t\tItem")
                    print("-" * 60)
                    for m in midlaners:
                        print(f"{m[0]}\t{m[1]:10}\t{m[2]:10}\t{', '.join(m[3])}")
                    print("-" * 60)
                    input("Tekan Enter untuk kembali...")

        
                elif pilihan == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH HERO BARU ===")
                    nama = input("Nama hero: ")
                    tipe = input("Tipe hero (Burst/Poke): ")

                    if nama == "" or tipe == "":
                        print("Nama dan tipe tidak boleh kosong!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    items = []
                    print("Masukkan 6 item (ketik '-' jika ingin berhenti):")
                    while len(items) < 6:
                        item = input(f"Item {len(items)+1}: ")
                        if item == "-":
                            break
                        if item != "":
                            items.append(item)
                        else:
                            print("Nama item tidak boleh kosong!")

                    new_id = midlaners[-1][0] + 1 if midlaners else 1
                    midlaners.append([new_id, nama, tipe, items])
                    print("Hero berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali...")

                
                elif pilihan == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UPDATE HERO ===")
                    id_hero = input("Masukkan ID Hero: ")

                    if not id_hero.isdigit():
                        print("ID harus berupa angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_hero = int(id_hero)
                    ditemukan = False
                    for m in midlaners:
                        if m[0] == id_hero:
                            ditemukan = True
                            print(f"Update hero: {m[1]}")
                            nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
                            tipe_baru = input("Tipe baru (kosongkan jika tidak diubah): ")

                            if nama_baru != "":
                                m[1] = nama_baru
                            if tipe_baru != "":
                                m[2] = tipe_baru

                            ubah_item = input("Ingin ubah item? (y/n): ")
                            if ubah_item.lower() == "y":
                                items_baru = []
                                print("Masukkan item baru (maks 6, ketik '-' untuk berhenti):")
                                while len(items_baru) < 6:
                                    item = input(f"Item {len(items_baru)+1}: ")
                                    if item == "-":
                                        break
                                    if item != "":
                                        items_baru.append(item)
                                if items_baru:
                                    m[3] = items_baru
                            print("Data hero berhasil diperbarui!")
                            break

                    if not ditemukan:
                        print("ID Hero tidak ditemukan!")
                    input("Tekan Enter untuk kembali...")

                
                elif pilihan == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS HERO ===")
                    id_hero = input("Masukkan ID Hero yang ingin dihapus: ")

                    if not id_hero.isdigit():
                        print("ID harus berupa angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_hero = int(id_hero)
                    ditemukan = False
                    for m in midlaners:
                        if m[0] == id_hero:
                            ditemukan = True
                            midlaners.remove(m)
                            print("Hero berhasil dihapus!")
                            break
                    if not ditemukan:
                        print("ID Hero tidak ditemukan!")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

       
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU USER ===")
                print("1. Lihat Hero Midlaner")
                print("2. Logout")

                pilih = input("Pilih menu: ")

                if pilih == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR HERO MIDLANER ===")
                    print("ID\tNama\t\tTipe\t\tItem")
                    print("-" * 60)
                    for m in midlaners:
                        print(f"{m[0]}\t{m[1]:10}\t{m[2]:10}\t{', '.join(m[3])}")
                    print("-" * 60)
                    input("Tekan Enter untuk kembali...")
                elif pilih == "2":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            continue

        sudah_ada = False
        for u in users:
            if u[1] == username:
                sudah_ada = True
                break

        if sudah_ada:
            print("Username sudah digunakan!")
        else:
            new_id = users[-1][0] + 1 if users else 1
            users.append([new_id, username, password, "user"])
            print("Akun berhasil dibuat!")

        input("Tekan Enter untuk kembali...")

    elif menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program List Item Midlaner ML!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")