# data_mhs = {
#     "nama" : "ucup",
#     "nim" : 1,
#     "dosen" : {
#     "nama": "Pak Awang",
#     "matkul": "APD"
#     }

# print(data_mhs['nama'])
# print(data_mhs['nim'])
# print(data_mhs.get('mapel', 'gak ada'))

# for data in data_mhs:
#     print(data)

# for key_data, value_data in data_mhs.items():
#     print(f"Nama : {key_data}\nValue : {value_data}\n")

#Menghapus Data
# del data_mhs["nim"]

# cache = data_mhs.pop('nim')
# print(data_mhs, "Dictionary")
# print(cache, "cache")
# data_mhs["id"] = cache
# print(data_mhs)

# print(len(data_mhs))

# for value in data_mhs.values:
#     print(data_mhs)

data_mhs = [
    {"nama" : "ucup",
     "role" : "admin",
    #  "username" : "ucup12",
    #  "password" : "ucup93823",
    },

    {"nama" : "michael",
     "role" : "user"
    #  "username" : "michael121",
    #  "password" : "michaelll923",
     }
]
print(data_mhs[0]['nama'])
print(data_mhs[1]['nama'])

# data_mhs2 = [
#     ["ucup", "admin"],
#     ["michael", "user"]
# ]
# print(data_mhs2[0][1])