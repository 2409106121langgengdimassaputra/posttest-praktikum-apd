usn = "dimas"
pw = "121"
salah = 0
batas_salah = 3

while salah < batas_salah:
    ussername = input("masukkan ussername anda: ")
    password = input("masukkan password anda: ")
    if usn == ussername and pw == password:
        print("login berhasil")
        break
    else:
        salah +=1
        print(f"login gagal,sisa kesempatan anda {batas_salah - salah}")
    if salah == batas_salah:
        print("login gagal ! ")
        exit()
        
mobil = input("masukkan merek mobil yang ingin dibeli : ")

harga = float(input("masukkan harga mobil : ") )

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

hitung = 1
while True:
    ulang = input("mobil apa lagi yang ingin anda beli ? ")
    if ulang == "toyota":
        print(f"mobil toyota seharga {harga} diskon 21% menjadi {harga_mobil_toyota_setelah_diskon}")
    elif ulang == "tesla:":
        print(f"mobil tesla seharga {harga} diskon 17% menjadi {harga_mobil_tesla_setelah_diskon}")
    elif ulang == "hyundai":
        print(f"mobil hyundai seharga {harga} diskon 23% menjadi {harga_mobil_hyundai_setelah_diskon}")
    else:
        print(f"selamat berbelanja")
        break 
    hitung +=1