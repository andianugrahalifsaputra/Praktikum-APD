# 01
# print("Perulangan ke-0")
# print("Perulangan ke-1")
# print("Perulangan ke-2")
# print("Perulangan ke-3")
# print("Perulangan ke-4")
# print("Perulangan ke-5")
# print("Perulangan ke-6")
# print("Perulangan ke-7")
# print("Perulangan ke-8")
# print("Perulangan ke-9")

# batas = 20
# for i in range(10, batas, 2):
#     print (f"Perulangan ke-{i}")

#02
# buah_banyak = ["Semangka", "Mangga"]
# for buah in buah_banyak:
#     print(buah)

# Perulangan while
# lagi = "yes"
# ulang = 0
# while lagi == "yes":
#     ulang += 1
#     print ("mabar?")
#     lagi = input("Mabar lagi gak?")
# print ("Selesai mabar!")
# print(f"Perulangan terjadi sebanyak {ulang}x")

#break memberhentikan perulangan
#continue menghilangkan data
# for i in range (1, 28):
#     if i % 2 == 0:
#         continue
#     print(f"Perulangan ke-{i}")

# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# print()
# print("Segitiga Sama Kaki:")
# for i in range (1, 5):
#     print("*", i*1)

a = 5
while a>0:
    username = input("Masukkan Nama Anda:")
    password = input("Masukkan pw anda:")
    
    if username == "admin" and password == "admin#1234":
        print("Berhasi; login")
        break
    else:
        print("Username dan password salah")
        a -=1
        print(f"Kesempatan anda tinggal {a}x")
