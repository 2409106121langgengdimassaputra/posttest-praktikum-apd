import os
data_volume =   ["One Piece Vol 1: Romance Dawn","One Piece Vol 2: Buggy the Clown","One Piece Vol 3: The Pirate Hunter","One Piece Vol 4: The New World",
"One Piece Vol 5: The Dueling Vanities","One Piece Vol 6: The Oath","One Piece Vol 7: The Hottest Day","One Piece Vol 8: I’m Not a Hero",
"One Piece Vol 9: The Goat of a Thousand Yards","One Piece Vol 10: The Legend Begins","One Piece Vol 11: The Path to Victory","One Piece Vol 12: The Battle of the Brothers",
"One Piece Vol 13: The Eternal Youth","One Piece Vol 14: The Song of the Sea","One Piece Vol 15: The Island of the Sun","One Piece Vol 16: The Path of the Gods",
"One Piece Vol 17: The Ruler of the Sea","One Piece Vol 18: The Great Pirate Era","One Piece Vol 19: The Phoenix","One Piece Vol 20: The Winter’s War",
"One Piece Vol 21: The Quest for Gold","One Piece Vol 22: The Road to Raftel","One Piece Vol 23: The Last Stand","One Piece Vol 24: The Return of the Captain",
"One Piece Vol 25: The New Era","One Piece Vol 26: The Great Expedition","One Piece Vol 27: The Pirate Alliance","One Piece Vol 28: The Lost Treasure",
"One Piece Vol 29: The Heart of the Sea","One Piece Vol 30: The Pirate's Dream","One Piece Vol 31: The Battle at the Summit","One Piece Vol 32: The Forgotten Island",
"One Piece Vol 33: The Hidden Fortress","One Piece Vol 34: The Warrior's Code","One Piece Vol 35: The Age of Pirates","One Piece Vol 36: The Straw Hat Pirates",
"One Piece Vol 37: The Search for the One Piece","One Piece Vol 38: The Rebellion","One Piece Vol 39: The Path of the Pirate King","One Piece Vol 40: The Clashing Ideals",
"One Piece Vol 41: The New World","One Piece Vol 42: The Return of the King","One Piece Vol 43: The Final Chapter","One Piece Vol 44: The Battle for the Future",
"One Piece Vol 45: The Rise of the Empires","One Piece Vol 46: The Quest for Freedom","One Piece Vol 47: The Last Adventure","One Piece Vol 48: The Shining Star",
"One Piece Vol 49: The Legacy","One Piece Vol 50: The New Generation","One Piece Vol 51: The Power of Friendship","One Piece Vol 52: The Heart of the Crew",
"One Piece Vol 53: The Road to Freedom","One Piece Vol 54: The Fire Within","One Piece Vol 55: The Will to Fight","One Piece Vol 56: The Guardian of the Sea",
"One Piece Vol 57: The Journey Ahead","One Piece Vol 58: The Curse of the Sea","One Piece Vol 59: The Soul of the Sea","One Piece Vol 60: The Bonds of Loyalty",
"One Piece Vol 61: The Flame of Hope","One Piece Vol 62: The Tides of Fate","One Piece Vol 63: The Awakening","One Piece Vol 64: The Storm Ahead",
"One Piece Vol 65: The Path to Victory","One Piece Vol 66: The Battle of the Sea","One Piece Vol 67: The Rise of the Pirates","One Piece Vol 68: The Heart of the Crew",
"One Piece Vol 69: The Legend Continues","One Piece Vol 70: The Fall of the Empire","One Piece Vol 71: The New Hope","One Piece Vol 72: The Strength of the Crew",
"One Piece Vol 73: The Clash of Titans","One Piece Vol 74: The End of the World","One Piece Vol 75: The New Dawn","One Piece Vol 76: The Ultimate Challenge",
"One Piece Vol 77: The Legacy of Dreams","One Piece Vol 78: The Heart of the Sea","One Piece Vol 79: The Final Journey","One Piece Vol 80: The Call to Adventure",
"One Piece Vol 81: The Road to Glory","One Piece Vol 82: The Strength of Bonds","One Piece Vol 83: The Bonds of Destiny","One Piece Vol 84: The Last Adventure",
"One Piece Vol 85: The Echo of the Past","One Piece Vol 86: The Search for Truth","One Piece Vol 87: The Path of the Heroes","One Piece Vol 88: The Edge of the World",
"One Piece Vol 89: The Depths of the Sea","One Piece Vol 90: The Rise of Legends","One Piece Vol 91: The Spirit of Adventure","One Piece Vol 92: The Battle for Tomorrow",
"One Piece Vol 93: The Winds of Change","One Piece Vol 94: The Power of Unity","One Piece Vol 95: The Hope of the Future","One Piece Vol 96: The Last Stand",
"One Piece Vol 97: The End of an Era","One Piece Vol 98: The New World Order","One Piece Vol 99: The Final Battle","One Piece Vol 100: The New Frontier",
"One Piece Vol 101: The Journey Continues","One Piece Vol 102: The Unbreakable Bonds","One Piece Vol 103: The Spirit of the Sea","One Piece Vol 104: The Destiny of Pirates",
"One Piece Vol 105: The Legend Lives On","One Piece Vol 106: The Heart of the World","One Piece Vol 107: The Call of the Ocean","One Piece Vol 108: The Rise of Heroes",
"One Piece Vol 109: The Final Journey"
]


usn = "dimas"
pw = "121"
role = ["admin","user"]
salah = 0
batas_salah = 3

while salah < batas_salah:
    ussername = input("masukkan ussername anda: ")
    password = input("masukkan password anda: ")
    role = input("masukkan role : ")
    if usn == ussername and pw == password and role == "admin":
        print("""
    Menu
Daftar Akun  >> 1
Login >> 2
Keluar   >> 3
""")
        print("berhasil login sebagai admin")
    elif role == "user":
        print("berhasil login sebagai user")
        break
    else:
        salah +=1
        print(f"login gagal,sisa kesempatan anda {batas_salah - salah}")
    if salah == batas_salah:
        print("login gagal ! ")
        exit()


os.system('cls || clear')
while True:
    print("""
    Menu
Lihat Data  >> 1
Tambah Data >> 2
Edit Data   >> 3
Hapus Data  >> 4
Keluar      >> 5
""")
    pilih = input("Masukan Pilihan menu >> ")
    os.system('cls || clear')
    match(pilih):
        case "1":
            print("===Lihat Data===")
            for i in range(len(data_volume)):
                print(f"Data Ke {i+1}")
                print(f"{data_volume[i]}")
                print("="*10)
            input("Enter.....")
            os.system('cls || clear')
        case "2":
            print("Menu tambah data")
            print("=" * 10)
            inputUser = input("Volume one piece yang mau ditambahkan : ")
            data_volume.append(inputUser)
            print(f"{inputUser} telah ditambahkan")
            input("Enter....")
            os.system('cls || clear')
        case "3":
            print("Menu ubah data")
            for i in range(len(data_volume)):
                print(f"data ke {i+1}")
                print(f"Nama : {data_volume[i]}")
                print("="*10)
            index= int(input("masukkan data yang mau diedit : "))
            data_baru =input("masukkan volume yang anda inginkan :")
            data_volume[index-1]=data_baru
            print("data berhasil diubah")
            input("Enter.....")
            os.system('cls || clear')
        case "4":
            print("Menu Hapus Data")
            for i in range(len(data_volume)):
                print(f"data ke {i+1}")
                print(f"Nama : {data_volume[i]}")
                print("="*10)
            index_user = int(input("masukkan volume yang ingin dihapus: "))
            del_user = data_volume.pop(index_user-1)
            print(f"{del_user} telah dihapus")
            input("Enter......")
            os.system('cls || clear')
        case "5":
            print("Anda keluar..")
            exit()
        case _:
            print(f"Menu {pilih} tidak tersedia")
            input("Enter.....")
            os.system('cls || clear')