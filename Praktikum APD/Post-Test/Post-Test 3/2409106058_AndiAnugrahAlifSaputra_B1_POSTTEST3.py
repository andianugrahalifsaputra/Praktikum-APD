# importing os module 
import os 

# Command to execute
# Using Windows OS command
cmd = 'date'

# Using os.system() method
os.system(cmd)

# Clearing the Screen
os.system('cls')

menu = print("""
==================================================
Menu Program Menghitung Luas/Keliling Bangun Ruang
==================================================
1. Kubus
2. Balok
3. Limas""")
menu = int(input("Masukkan pilihan anda"))
if menu == 1:
    kubus = print("""
1. Luas Kubus
2. Kelilng Kubus""")
    kubus = int(input("Masukkan pilihan anda"))
    if kubus == 1:
     sisi = float(input("Berapa sisinya?"))
     l_kubus = 6*sisi*sisi
     print(l_kubus)
    if kubus == 2:
     sisi = float(input("Berapa sisinya?"))
     k_kubus = 12*sisi
     print(k_kubus)
elif menu == 2:
    kubus = print("""
1. Luas Balok   
2. Kelilng Balok""")
    balok = int(input("Masukkan pilihan anda"))
    if balok == 1:
     panjang = float(input("Berapa panjangnya?"))
     lebar = float(input("Berapa lebarnya?"))
     tinggi = float(input("Berapa tingginya?"))
     l_balok2 = panjang*lebar+panjang*tinggi+tinggi*lebar
     l_balok = 2*l_balok2
     print(l_balok)
    if balok == 2:
     panjang = float(input("Berapa panjangnya?"))
     lebar = float(input("Berapa lebarnya?"))
     tinggi = float(input("Berapa tingginya?"))
     k_balok = panjang+lebar+tinggi
     k_balok2 = 4*k_balok
     print(k_balok2)
elif menu == 3:
    kubus = print("""
1. Luas Limas
2. Volume Limas""")
    limas = int(input("Masukkan pilihan anda"))
    if limas == 1:
     sisi = float(input("Berapa sisinya?"))
     alas = float(input("Berapa alasnya?"))
     tinggi = float(input("Berapa tingginya?"))
     l_limas = 0.5*alas*tinggi
     l_limas2 = sisi*sisi+4*l_limas
     print(l_limas2)
    if limas == 2:
     sisi = float(input("Berapa sisinya?"))
     tinggi = float(input("Berapa tingginya?"))
     v_limas = 1/3*sisi*sisi*tinggi
     print(v_limas)