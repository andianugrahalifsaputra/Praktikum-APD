# importing os module 
import os 

# Using Windows OS command
cmd = 'date'

# Clearing the Screen
os.system('cls')

kesempatan = 0
autentikasi = False

while kesempatan < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username == "andi" and password == "58":
        autentikasi = True
        break
    else:
        kesempatan += 1
        print(f"Username atau password salah. Anda memiliki {3 - kesempatan} kesempatan lagi.")

if not autentikasi:
    print("Anda telah salah menginputkan username/password 3x. Program berhenti.")
else:
    while True:
        print("""
==================================================
Menu Program Menghitung Luas/Keliling Bangun Ruang
==================================================
1. Kubus
2. Balok
3. Limas
4. Keluar Program
""")
        
        menu = int(input("Masukkan pilihan anda: "))
        
        if menu == 1:
            print("""
1. Luas Kubus
2. Keliling Kubus""")
            kubus = int(input("Masukkan pilihan anda: "))
            if kubus == 1:
                sisi = float(input("Berapa sisinya? "))
                l_kubus = 6 * sisi * sisi
                print(f"Luas Kubus: {l_kubus}")
            
            elif kubus == 2:
                sisi = float(input("Berapa sisinya? "))
                k_kubus = 12 * sisi
                print(f"Keliling Kubus: {k_kubus}")
            else:
                print("Pilihan tidak valid.")
        
        elif menu == 2:
            print("""
1. Luas Balok   
2. Keliling Balok""")
            balok = int(input("Masukkan pilihan anda: "))
            if balok == 1:
                panjang = float(input("Berapa panjangnya? "))
                lebar = float(input("Berapa lebarnya? "))
                tinggi = float(input("Berapa tingginya? "))
                l_balok2 = panjang * lebar + panjang * tinggi + tinggi * lebar
                l_balok = 2 * l_balok2
                print(f"Luas Balok: {l_balok}")
            
            elif balok == 2:
                panjang = float(input("Berapa panjangnya? "))
                lebar = float(input("Berapa lebarnya? "))
                tinggi = float(input("Berapa tingginya? "))
                k_balok = panjang + lebar + tinggi
                k_balok2 = 4 * k_balok
                print(f"Keliling Balok: {k_balok2}")
            else:
                print("Pilihan tidak valid.")
        
        elif menu == 3:
            print("""
1. Luas Limas
2. Volume Limas""")
            limas = int(input("Masukkan pilihan anda: "))
            if limas == 1:
                sisi = float(input("Berapa sisinya? "))
                alas = float(input("Berapa alasnya? "))
                tinggi = float(input("Berapa tingginya? "))
                l_limas = 0.5 * alas * tinggi
                l_limas2 = sisi * sisi + 4 * l_limas
                print(f"Luas Limas: {l_limas2}")
            
            elif limas == 2:
                sisi = float(input("Berapa sisinya? "))
                tinggi = float(input("Berapa tingginya? "))
                v_limas = 1/3 * sisi * sisi * tinggi
                print(f"Volume Limas: {v_limas}")
            else:
                print("Pilihan tidak valid.")
        
        elif menu == 4:
            print("Anda telah keluar dari menu")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")
