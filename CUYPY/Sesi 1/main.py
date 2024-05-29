import random
from libs import welcome

welcome_message = "WELCOME TO CUYPY GAMES!"

welcome("SELAMAT DATANG DI CUYPY")

nama_user = input("Masukan Nama Kamu: ")

while nama_user == "":
    nama_user = input("isi dulu nama kamu: ")

while True:
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 #INI GOA HARUS KOSONG

    cuy_position = random.randint(1, 4)

    goa = goa_kosong.copy() #INI GOA MODIFIKASI TEMPAT CUYPY BERADA
    goa[cuy_position - 1] = "|0_0|"

    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)
    
    print(f'''
    Halo {nama_user}! Coba perhatikan Goa dibawah ini!
    {goa_kosong}
    ''')

    pilihan_user = int(input("menurut kamu di Goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] "))

    while pilihan_user > 4:
        pilihan_user = int(input("pilihannya cuman 4 bro mau yang mana? [1 / 2 / 3 / 4]"))

    confirm_pilihan_user = input("apakah kamu yakin dengan pilihanmu? [y/n]")

    if confirm_pilihan_user == "n":
        exit()
    elif confirm_pilihan_user == "y":
        if pilihan_user == cuy_position:
            print(f"\n {goa} \n Selamat kamu menang CUYPY berada di goa nomor {cuy_position} dan pilihanmu adalah goa nomor {pilihan_user}")
        else:
            print(f"\n {goa} \n Kamu kalah CUYPY berada di goa nomor {cuy_position} sedangkan pilihanmu adalah goa nomor {pilihan_user}")
    else:
        print("silahkan ulangi programmnya")
        exit()
        
    play_again = input("\n apakah kamu ingin melanjutkan gamenya? [y/n] ")
    if play_again == "n":
        break
    
print("program selesai!")