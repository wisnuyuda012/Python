import random
from libs import welcome_message

welcome_message("Selamat Datang di Tutorial Python")


# print(', '.join(map(str,name)))


# print(kotak_harta_kosong)
# print(kotak_harta)


nama_user = input("Silakan masukan nama anda : ")
while nama_user=="":
    nama_user = input("Masukkan nama kamu terlebih dahulu : ")

while True:    
    HartaKarun_Posisi = random.randint(1, 4)
    kotak= "[_]"
    kotak_harta_kosong = [kotak] * 4

    kotak_harta = kotak_harta_kosong.copy()
    kotak_harta[HartaKarun_Posisi -1]  = "[=|==>]"

    kotak_harta_kosong = '  '.join(kotak_harta_kosong)
    kotak_harta =  '  '.join(kotak_harta)
    
    print(f'''Halo {nama_user} ! Coba perhatikan Kotak dibawah ini :
    {kotak_harta_kosong}''')

    # number_range = range()
    pilihan_user = int(input("Menurut kamu ada di kotak nomor berapa harta karunnya [1 / 2 / 3 / 4 ]?  "))
    while pilihan_user >= 5 or pilihan_user <= 0:
        pilihan_user = int(input("Masukkan nomor 1-4 : "))  
            
    konfirmasi_user = input(f"Apakah kamu yakin jawabannya adalah {pilihan_user} ? [y/n] : ")

    if konfirmasi_user == "n":
        print("Program dihentikan!")
        exit()
    elif konfirmasi_user == "y":
        if pilihan_user == HartaKarun_Posisi:
            print(f'''
Selamat {nama_user} anda menemukan harta posisi karunnya ! 
{kotak_harta}''')
        else:
            print(f'''
Maaf {nama_user}, anda belum menemukan posisi harta karunnya. 
{kotak_harta}''')
    else:
        print("Silahkan ulangi program kembali!")
        exit()

    play_again = input("\n\nApakah anda ingin melanjutkan game ? [y/n]")
    if play_again == "n":
        break

print("Program Selesai")
