# nama = input("masukkan nama anda : ")
# nim = input("masukkan nim anda : ") 

# harga_setiap_mobil = float(input("masukkan harga mobil : "))

# diskon_tesla = 0.17
# diskon_toyota = 0.21
# diskon_hyundai = 0.23

# harga_mobil_tesla_setelah_diskon =  harga_setiap_mobil * (diskon_tesla)
# harga_mobil_toyota_setelah_diskon = harga_setiap_mobil * (diskon_toyota)
# harga_mobil_hyundai_setelah_diskon = harga_setiap_mobil * (diskon_hyundai)
# modulus_7 = harga_setiap_mobil % 7

# print(
# f"mobil tesla seharga {harga_setiap_mobil},diskon 17% menjadi {harga_mobil_tesla_setelah_diskon}.\n"
# f"mobil toyota seharga {harga_setiap_mobil},diskon 21% menjadi {harga_mobil_toyota_setelah_diskon}.\n"
# f"mobil hyundai seharga {harga_setiap_mobil},diskon 23% menjadi {harga_mobil_hyundai_setelah_diskon}.\n "
# f"dan harga setiap mobil modulus 7 adalah {modulus_7}") 

nilai = int(input("masukkan nilai :"))

if nilai >= 80 and nilai <= 100:
    print("a")
elif nilai >= 70 and nilai <=79:
    print("b")
else:
    print("ga ada kocak")