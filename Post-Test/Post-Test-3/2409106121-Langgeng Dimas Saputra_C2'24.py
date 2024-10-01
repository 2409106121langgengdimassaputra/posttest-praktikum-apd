mobil = input("masukkan merek mobil yang ingin dibeli >> ")

harga = 300000000
diskon_tesla = harga * 0.17
diskon_toyota = harga * 0.21
diskon_hyundai = harga * 0.23

harga_mobil_tesla_setelah_diskon =  harga - (diskon_tesla)
harga_mobil_toyota_setelah_diskon = harga - (diskon_toyota)
harga_mobil_hyundai_setelah_diskon = harga - (diskon_hyundai)

if mobil == ("tesla"):
    print(f"mobil tesla seharga {harga} diskon 17% menjadi {harga_mobil_tesla_setelah_diskon} : ")
elif mobil == ("toyota"):
    print(f"mobil toyota seharga {harga} diskon 21% menjadi {harga_mobil_toyota_setelah_diskon} : ")
elif mobil == ("hyundai"):
    print(f"mobil hyundai seharga {harga} diskon 23% menjadi {harga_mobil_hyundai_setelah_diskon} : ")
else:
    print("tidak jadi membeli mobil")
