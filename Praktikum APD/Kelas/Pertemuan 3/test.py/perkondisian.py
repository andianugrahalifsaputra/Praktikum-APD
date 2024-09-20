# #IF/ELSE
# uang=0
# if uang:
#     print("Pergi ke Pasar")
# else:
#     print("Pergi ke Rumah Teman")

# nilai = -1
# if nilai < 70:
#     print("tidak lulus")
# else:
#     print("nilai lulus")

# bilangan = 5
# if bilangan < 0:
#     print("bilangan negatif")
# else:
#     print("bilangan positif")

# #ELIF
# umur=int(input("Masukkan umur anda"))
# if umur <=10:
#     print("anak-anak")
# elif umur<=18:
#     print("remaja")
# elif umur<=35:
#     print("dewasa")
# else:
#     print("lansia")

#menu
print("""
Menu :
1. film
2. ngoding
3. keluar""" )
menu = int(input("Masukkan pilihan: "))
if menu == 1:
    print("Sedang nonton film")
elif menu ==2:
    print("Sedang ngoding")
elif menu ==3:
    print("Keluar dari aplikasi")
else:
    print("Menu tidak tersedia")