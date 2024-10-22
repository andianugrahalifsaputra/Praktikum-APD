import os

users = {}
admin_users = {}
default_saham = {
    "INDF": {"jumlah": 0, "harga_per_saham": 0, "total_investasi": 0},
    "INTP": {"jumlah": 0, "harga_per_saham": 0, "total_investasi": 0},
    "BREN": {"jumlah": 0, "harga_per_saham": 0, "total_investasi": 0},
    "BRPT": {"jumlah": 0, "harga_per_saham": 0, "total_investasi": 0},
    "ASII": {"jumlah": 0, "harga_per_saham": 0, "total_investasi": 0},
    "AUTO": {"jumlah": 0, "harga_per_saham": 0, "total_investasi": 0},
    "ANTR": {"jumlah": 0, "harga_per_saham": 0, "total_investasi": 0}
}

def clear_console():
    os.system('cls || clear')

def register_admin():
    username = input("Masukkan username Admin: ")
    password = input("Masukkan password: ")
    if username in admin_users:
        print(f"Username admin '{username}' sudah ada. Pilih username lain.")
    else:
        admin_users[username] = {'password': password}
        print(f"Admin '{username}' berhasil didaftarkan.")
    input("Tekan Enter untuk melanjutkan...")
    clear_console()

def register_user():
    username = input("Masukkan username User: ")
    password = input("Masukkan password: ")
    if username in users:
        print(f"Username user '{username}' sudah ada. Pilih username lain.")
    else:
        users[username] = {
            'password': password,
            'saham_list': default_saham.copy()
        }
        print(f"User '{username}' berhasil didaftarkan dengan saham awal.")
    input("Tekan Enter untuk melanju tkan...")
    clear_console()

def add_user_stock(username_user):
    nama_saham = input("Masukkan nama saham: ")
    if nama_saham in users[username_user]['saham_list']:
        jumlah_saham = int(input("Masukkan jumlah saham: "))
        harga_per_saham = float(input("Masukkan harga per saham: "))
        users[username_user]['saham_list'][nama_saham]['jumlah'] += jumlah_saham
        users[username_user]['saham_list'][nama_saham]['harga_per_saham'] = harga_per_saham
        users[username_user]['saham_list'][nama_saham]['total_investasi'] = users[username_user]['saham_list'][nama_saham]['jumlah'] * harga_per_saham
        print(f"Investasi '{nama_saham}' berhasil ditambahkan untuk user '{username_user}'.")
    else:
        print(f"Saham '{nama_saham}' tidak ditemukan.")
    input("Tekan Enter untuk melanjutkan...")
    clear_console()

def print_user_stock_list(username_user):
    if not users[username_user]['saham_list']:
        print(f"Tidak ada investasi saham yang terdaftar untuk user '{username_user}'.")
    else:
        print(f"Daftar Investasi Saham untuk user '{username_user}':")
        for nama_saham, data in users[username_user]['saham_list'].items():
            print(f"Nama Saham: {nama_saham}, Jumlah: {data['jumlah']}, "
                  f"Harga per Saham: {data['harga_per_saham']}, "
                  f"Total Investasi: {data['total_investasi']}")

def update_user_stock(username_user):
    print(f"Daftar Saham untuk {username_user}:")
    for nama_saham, data in users[username_user]['saham_list'].items():
        print(f"Nama Saham: {nama_saham}, Jumlah: {data['jumlah']}, Harga per Saham: {data['harga_per_saham']}")
    
    nama_saham = input("Masukkan nama saham yang ingin diperbarui: ")
    if nama_saham in users[username_user]['saham_list']:
        jumlah_baru = int(input("Masukkan jumlah saham baru: "))
        harga_baru = float(input("Masukkan harga per saham baru: "))
        users[username_user]['saham_list'][nama_saham]['jumlah'] = jumlah_baru
        users[username_user]['saham_list'][nama_saham]['harga_per_saham'] = harga_baru
        users[username_user]['saham_list'][nama_saham]['total_investasi'] = jumlah_baru * harga_baru
        print(f"Investasi '{nama_saham}' berhasil diperbarui untuk user '{username_user}'.")
    else:
        print("Saham tidak ditemukan.")
    input("Tekan Enter untuk melanjutkan...")
    clear_console()

def delete_user_stock(username_user):
    print(f"Daftar Saham untuk {username_user}:")
    for nama_saham, data in users[username_user]['saham_list'].items():
        print(f"Nama Saham: {nama_saham}, Jumlah: {data['jumlah']}, Harga per Saham: {data['harga_per_saham']}")
    
    nama_saham = input("Masukkan nama saham yang ingin dihapus: ")
    if nama_saham in users[username_user]['saham_list']:
        del users[username_user]['saham_list'][nama_saham]
        print(f"Investasi saham '{nama_saham}' berhasil dihapus untuk user '{username_user}'.")
    else:
        print("Saham tidak ditemukan.")
    input("Tekan Enter untuk melanjutkan...")
    clear_console()

def list_registered_users():
    if users:
        print("Daftar User Terdaftar:")
        for user in users:
            print(f"- {user}")
    else:
        print("Belum ada user yang terdaftar.")
    input("Tekan Enter untuk melanjutkan...")
    clear_console()

def main_menu():
    clear_console()
    print("""
    Menu Utama
1. Register Admin
2. Register User
3. Login Admin
4. Login User
5. Keluar
""")
    return input("Masukkan Pilihan menu >> ")

def admin_menu():
    clear_console()
    print("""
    Menu Admin
1. Tambah Investasi Saham untuk User
2. Baca Daftar Investasi Saham untuk User
3. Perbarui Investasi Saham untuk User
4. Hapus Investasi Saham untuk User
5. Tampilkan List User
6. Logout
""")
    return input("Masukkan Pilihan menu >> ")

def user_menu(username):
    clear_console()
    print(f"""
    Menu User ({username})
1. Tambah Investasi Saham
2. Baca Daftar Investasi Saham
3. Perbarui Investasi Saham
4. Hapus Investasi Saham
5. Logout
""")
    return input("Masukkan Pilihan menu >> ")

def admin_login():
    username = input("Masukkan username Admin: ")
    password = input("Masukkan password: ")
    if username in admin_users and admin_users[username]['password'] == password:
        while True:
            pilihan_admin = admin_menu()
            clear_console()
            if pilihan_admin == "1":  
                username_user = input("Masukkan username User: ")
                if username_user in users:
                    add_user_stock(username_user)
                else:
                    print(f"User '{username_user}' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                clear_console()

            elif pilihan_admin == "2":  
                username_user = input("Masukkan username User: ")
                if username_user in users:
                    print_user_stock_list(username_user)
                else:
                    print(f"User '{username_user}' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                clear_console()

            elif pilihan_admin == "3":  
                username_user = input("Masukkan username User: ")
                if username_user in users:
                    update_user_stock(username_user)
                else:
                    print(f"User '{username_user}' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                clear_console()

            elif pilihan_admin == "4":  
                username_user = input("Masukkan username User: ")
                if username_user in users:
                    delete_user_stock(username_user)
                else:
                    print(f"User '{username_user}' tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan...")
                clear_console()

            elif pilihan_admin == "5":  
                list_registered_users()

            elif pilihan_admin == "6":  
                break

def user_login():
    username = input("Masukkan username User: ")
    password = input("Masukkan password: ")
    if username in users and users[username]['password'] == password:
        while True:
            pilihan_user = user_menu(username)
            clear_console()
            if pilihan_user == "1":  
                add_user_stock(username)

            elif pilihan_user == "2":  
                print_user_stock_list(username)
                input("Tekan Enter untuk melanjutkan...")
                clear_console()

            elif pilihan_user == "3":  
                update_user_stock(username)
                input("Tekan Enter untuk melanjutkan...")
                clear_console()

            elif pilihan_user == "4":  
                delete_user_stock(username)

            elif pilihan_user == "5":  
                break

while True:
    pilihan = main_menu()
    if pilihan == "1":
        register_admin()

    elif pilihan == "2":
        register_user()

    elif pilihan == "3":
        admin_login()

    elif pilihan == "4":
        user_login()

    elif pilihan == "5":
        break
