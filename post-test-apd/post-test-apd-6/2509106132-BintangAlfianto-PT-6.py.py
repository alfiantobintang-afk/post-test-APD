import os

users = {
    1: {"username": "admin", "password": "123", "role": "admin"},
    2: {"username": "user", "password": "123", "role": "user"}
}

midlaners = {
    1: {"nama": "Lunox", "tipe": "Burst", "items": ["Genius Wand", "Glowing Wand", "Arcane Boots", "Lightning Truncheon", "Holy Crystal", "Blood Wings"]},
    2: {"nama": "Yve", "tipe": "Poke", "items": ["Enchanted Talisman", "Glowing Wand", "Demon Shoes", "Feather of Heaven", "Divine Glaive", "Blood Wings"]},
    3: {"nama": "Kagura", "tipe": "Burst", "items": ["Genius Wand", "Glowing Wand", "Arcane Boots", "Lightning Truncheon", "Holy Crystal", "Blood Wings"]}
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== LIST ITEM MIDLANER MOBILE LEGENDS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    # === LOGIN ===
    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        user_aktif = None
        for id_user, data in users.items():
            if data["username"] == username and data["password"] == password:
                user_aktif = {"id": id_user, **data}
                break

        if user_aktif is None:
            print("Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue

        print(f"Login berhasil! Selamat datang, {user_aktif['role'].capitalize()} {user_aktif['username']}!")
        input("Tekan Enter untuk melanjutkan...")

        # === MENU ADMIN ===
        if user_aktif["role"] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. Lihat Hero Midlaner")
                print("2. Tambah Hero Baru")
                print("3. Update Hero")
                print("4. Hapus Hero")
                print("5. Logout")

                pilihan = input("Pilih menu: ")

                # Lihat hero
                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR HERO MIDLANER ===")
                    print("ID\tNama\t\tTipe\t\tItem")
                    print("-" * 60)
                    for idh, data in midlaners.items():
                        print(f"{idh}\t{data['nama']:<10}\t{data['tipe']:<10}\t{', '.join(data['items'])}")
                    print("-" * 60)
                    input("Tekan Enter untuk kembali...")

                # Tambah hero
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
                    print("Masukkan maksimal 6 item (ketik '-' untuk berhenti):")
                    while len(items) < 6:
                        item = input(f"Item {len(items)+1}: ")
                        if item == "-":
                            break
                        if item != "":
                            items.append(item)
                        else:
                            print("Nama item tidak boleh kosong!")

                    new_id = max(midlaners.keys()) + 1 if midlaners else 1
                    midlaners[new_id] = {"nama": nama, "tipe": tipe, "items": items}
                    print("Hero berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali...")

                # Update hero
                elif pilihan == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UPDATE HERO ===")
                    print("ID\tNama\t\tTipe")
                    print("-" * 40)
                    for idh, data in midlaners.items():
                        print(f"{idh}\t{data['nama']:<10}\t{data['tipe']}")
                    print("-" * 40)

                    id_hero = input("Masukkan ID Hero yang ingin diupdate: ")
                    if not id_hero.isdigit():
                        print("ID harus berupa angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_hero = int(id_hero)
                    if id_hero not in midlaners:
                        print("ID Hero tidak ditemukan!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    data = midlaners[id_hero]
                    print(f"Update hero: {data['nama']}")
                    nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
                    tipe_baru = input("Tipe baru (kosongkan jika tidak diubah): ")

                    if nama_baru != "":
                        data["nama"] = nama_baru
                    if tipe_baru != "":
                        data["tipe"] = tipe_baru

                    ubah_item = input("Ingin ubah item? (y/n): ")
                    if ubah_item.lower() == "y":
                        items_baru = []
                        print("Masukkan item baru (maks 6, '-' untuk berhenti):")
                        while len(items_baru) < 6:
                            item = input(f"Item {len(items_baru)+1}: ")
                            if item == "-":
                                break
                            if item != "":
                                items_baru.append(item)
                        if items_baru:
                            data["items"] = items_baru

                    print("Data hero berhasil diperbarui!")
                    input("Tekan Enter untuk kembali...")

                # Hapus hero
                elif pilihan == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS HERO ===")
                    print("ID\tNama\t\tTipe")
                    print("-" * 40)
                    for idh, data in midlaners.items():
                        print(f"{idh}\t{data['nama']:<10}\t{data['tipe']}")
                    print("-" * 40)

                    id_hero = input("Masukkan ID Hero yang ingin dihapus: ")
                    if not id_hero.isdigit():
                        print("ID harus berupa angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_hero = int(id_hero)
                    if id_hero in midlaners:
                        del midlaners[id_hero]
                        print("Hero berhasil dihapus!")
                    else:
                        print("ID Hero tidak ditemukan!")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

        # === MENU USER ===
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
                    for idh, data in midlaners.items():
                        print(f"{idh}\t{data['nama']:<10}\t{data['tipe']:<10}\t{', '.join(data['items'])}")
                    print("-" * 60)
                    input("Tekan Enter untuk kembali...")
                elif pilih == "2":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

    # === REGISTER ===
    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            continue

        sudah_ada = any(data["username"] == username for data in users.values())

        if sudah_ada:
            print("Username sudah digunakan!")
        else:
            new_id = max(users.keys()) + 1 if users else 1
            users[new_id] = {"username": username, "password": password, "role": "user"}
            print("Akun berhasil dibuat!")

        input("Tekan Enter untuk kembali...")

    # === KELUAR ===
    elif menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program List Item Midlaner ML!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
