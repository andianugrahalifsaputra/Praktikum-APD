def buat_biodata():
    
    nama = input("Masukkan nama Anda: ")
    usia = int(input("Masukkan usia Anda: "))
    tinggi_badan = float(input("Masukkan tinggi badan Anda: "))
    berat_badan = float(input("Masukkan berat badan Anda: "))
    status_pernikahan = input("Apakah Anda sudah menikah? (ya/tidak): ")
    total = usia + tinggi_badan + berat_badan
    
    if status_pernikahan == 'ya':
        status_pernikahan = True
    elif status_pernikahan == 'tidak':
        status_pernikahan = False
    else:
        print("Input tidak valid untuk status pernikahan. Harap masukkan 'ya' atau 'tidak'.")
        return
    
    print("="*50)
    print(" " * 20 + "Bio Data Anda")
    print("="*50)
    print(f"Nama                            : {nama}")
    print(f"Usia                            : {usia} tahun")
    print(f"Tinggi Badan                    : {tinggi_badan}")
    print(f"Berat Badan                     : {berat_badan}")
    print(f"Status Pernikahan               : {'Sudah menikah' if status_pernikahan else 'Belum menikah'}")
    print(f"Total (usia + tb + bb)          : {total}")
    print("=" * 50)
buat_biodata()
