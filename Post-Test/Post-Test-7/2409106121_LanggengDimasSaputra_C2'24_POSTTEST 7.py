import os

data_volume = {
    1: "One Piece Vol 1: Romance Dawn",
    2: "One Piece Vol 2: Buggy the Clown",
    3: "One Piece Vol 3: The Pirate Hunter",
    4: "One Piece Vol 4: The New World",
    5: "One Piece Vol 5: The Duel of Giants",
    6: "One Piece Vol 6: The Oath",
    7: "One Piece Vol 7: The Hottest Day",
    8: "One Piece Vol 8: It’s Not a Hero!",
    9: "One Piece Vol 9: The Dueling Warriors",
    10: "One Piece Vol 10: The Legend Begins",
    11: "One Piece Vol 11: The Battle of the Brothers",
    12: "One Piece Vol 12: The Song of the Sea",
    13: "One Piece Vol 13: The Island of the Gods",
    14: "One Piece Vol 14: The Birth of Legends",
    15: "One Piece Vol 15: Impel Down",
    16: "One Piece Vol 16: The Path of Gods",
    17: "One Piece Vol 17: The Land of Gold",
    18: "One Piece Vol 18: The Lost Soul",
    19: "One Piece Vol 19: The Road to Pirate",
    20: "One Piece Vol 20: The Pirate’s Dream",
    21: "One Piece Vol 21: The Last Stand",
    22: "One Piece Vol 22: The Return of the Captain",
    23: "One Piece Vol 23: The Battle of the Summit",
    24: "One Piece Vol 24: The Treasure’s Light",
    25: "One Piece Vol 25: The Forgotten Island",
    26: "One Piece Vol 26: The Pirate’s Heart",
    27: "One Piece Vol 27: The Unbroken Dream",
    28: "One Piece Vol 28: The New Frontier",
    29: "One Piece Vol 29: The Warrior’s Code",
    30: "One Piece Vol 30: The Age of Pirates",
    31: "One Piece Vol 31: The Straw Hat Pirates",
    32: "One Piece Vol 32: The Shining Star",
    33: "One Piece Vol 33: The Storm Ahead",
    34: "One Piece Vol 34: The Flashing Blades",
    35: "One Piece Vol 35: The Golden Road",
    36: "One Piece Vol 36: The Path to Power",
    37: "One Piece Vol 37: The King of the Seas",
    38: "One Piece Vol 38: The Final Chapter",
    39: "One Piece Vol 39: The Heart of the Future",
    40: "One Piece Vol 40: The Battle of the New World",
    41: "One Piece Vol 41: A New Era",
    42: "One Piece Vol 42: The Will of the King",
    43: "One Piece Vol 43: The Shining Star",
    44: "One Piece Vol 44: The Path of the Warrior",
    45: "One Piece Vol 45: The Rise of the Empires",
    46: "One Piece Vol 46: The Quest for Freedom",
    47: "One Piece Vol 47: The Last Adventure",
    48: "One Piece Vol 48: The Shining Star",
    49: "One Piece Vol 49: Freedom Awaits",
    50: "One Piece Vol 50: New Generations",
    51: "One Piece Vol 51: The Fall of the Emperor",
    52: "One Piece Vol 52: The Heart of the Crew",
    53: "One Piece Vol 53: The Final Frontier",
    54: "One Piece Vol 54: The Journey Ahead",
    55: "One Piece Vol 55: The Soul of the Sea",
    56: "One Piece Vol 56: Bonds of Loyalty",
    57: "One Piece Vol 57: The Fame of Heroes",
    58: "One Piece Vol 58: The Tides of Fate",
    59: "One Piece Vol 59: The Awakening",
    60: "One Piece Vol 60: The Storm Ahead",
    61: "One Piece Vol 61: The New World Order",
    62: "One Piece Vol 62: The Thunderous Echo",
    63: "One Piece Vol 63: The Heart of the Crew",
    64: "One Piece Vol 64: Bonds of Strength",
    65: "One Piece Vol 65: Tides of War",
    66: "One Piece Vol 66: The Winds of Fate",
    67: "One Piece Vol 67: The Leaps of Fate",
    68: "One Piece Vol 68: The Final Battle",
    69: "One Piece Vol 69: The Darkened Future",
    70: "One Piece Vol 70: New Frontiers",
    71: "One Piece Vol 71: The Journey Continues",
    72: "One Piece Vol 72: The Heart of the Sea",
    73: "One Piece Vol 73: The Leap of Titans",
    74: "One Piece Vol 74: The End of the World",
    75: "One Piece Vol 75: The New Dawn",
    76: "One Piece Vol 76: The Ultimate Challenge",
    77: "One Piece Vol 77: The Return to Power",
    78: "One Piece Vol 78: The Awakening",
    79: "One Piece Vol 79: The Battle of Legends",
    80: "One Piece Vol 80: The Final Stand",
    81: "One Piece Vol 81: Echoes of the Past",
    82: "One Piece Vol 82: The Heart of the East",
    83: "One Piece Vol 83: The New Age",
    84: "One Piece Vol 84: The Rise of the East",
    85: "One Piece Vol 85: The Search for Truth",
    86: "One Piece Vol 86: The Path of Heroes",
    87: "One Piece Vol 87: The Edge of the World",
    88: "One Piece Vol 88: New Horizons",
    89: "One Piece Vol 89: The Heart of Legends",
    90: "One Piece Vol 90: The Age of Empires",
    91: "One Piece Vol 91: A New Dawn",
    92: "One Piece Vol 92: The Shining Light",
    93: "One Piece Vol 93: The Final Journey",
    94: "One Piece Vol 94: Echoes of Time",
    95: "One Piece Vol 95: The Path of Destiny",
    96: "One Piece Vol 96: The New World Order",
    97: "One Piece Vol 97: Rise of the Empire",
    98: "One Piece Vol 98: The Final Battle",
    99: "One Piece Vol 99: The Destiny of Pirates",
    100: "One Piece Vol 100: The Endless Seas",
    101: "One Piece Vol 101: A New Era",
    102: "One Piece Vol 102: The Shining Star",
    103: "One Piece Vol 103: The Heart of the World",
    104: "One Piece Vol 104: The Call of the Ocean",
    105: "One Piece Vol 105: The Rise of Heroes",
    106: "One Piece Vol 106: The Final Journey",
    107: "One Piece Vol 107: The Soul of the Sea",
    108: "One Piece Vol 108: The Final World"
}

def clear_screen():
    os.system('cls || clear')

def tampilkan_menu():
    print("""
    Menu
    1. Lihat Data
    2. Tambah Data
    3. Edit Data
    4. Hapus Data
    5. Keluar
    """)

def lihat_data():
    clear_screen()
    print("=== Lihat Data ===")
    if data_volume:
        for i in data_volume:
            print(f"Data Ke-{i}: {data_volume[i]}")
    else:
        print("Tidak ada data yang tersedia.")
    input("Tekan Enter untuk kembali ke menu...")

def tambah_data():
    clear_screen()
    print("=== Tambah Data ===")
    inputuser = input("Masukkan judul Volume One Piece yang mau ditambahkan: ")
    if inputuser:
        new_index = len(data_volume) + 1
        data_volume[new_index] = inputuser
        print("Data berhasil ditambahkan.")
    else:
        print("Data tidak boleh kosong.")
    input("Tekan Enter untuk kembali ke menu...")

def edit_data():
    clear_screen()
    print("=== Edit Data ===")
    if data_volume:
        for i in data_volume:
            print(f"{i}. {data_volume[i]}")
        try:
            index = int(input("Masukkan nomor volume yang mau diedit: "))
            if index in data_volume:
                data_volume[index] = input("Masukkan judul volume baru: ")
                print("Data berhasil diedit.")
            else:
                print("Nomor volume tidak ditemukan.")
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")
    else:
        print("Tidak ada data yang bisa diedit.")
    input("Tekan Enter untuk kembali ke menu...")

def hapus_data():
    clear_screen()
    print("=== Hapus Data ===")
    if data_volume:
        for i in data_volume:
            print(f"{i}. {data_volume[i]}")
        try:
            index = int(input("Masukkan nomor volume yang ingin dihapus: "))
            if index in data_volume:
                data_volume.pop(index)
                print("Data berhasil dihapus.")
            else:
                print("Nomor volume tidak ditemukan.")
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")
    else:
        print("Tidak ada data yang bisa dihapus.")
    input("Tekan Enter untuk kembali ke menu...")

def main():
    while True:
        clear_screen()
        tampilkan_menu()
        pilih = input("Masukkan pilihan menu >> ")
        clear_screen()
        
        if pilih == '1':
            lihat_data()
        elif pilih == '2':
            tambah_data()
        elif pilih == '3':
            edit_data()
        elif pilih == '4':
            hapus_data()
        elif pilih == '5':
            print("Anda keluar dari program.")
            break
        else:
            print("Menu pilihan tidak tersedia!")
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
