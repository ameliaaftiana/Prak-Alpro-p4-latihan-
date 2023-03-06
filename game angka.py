#program tebak angka yang diberi hint dan batas percobaan 
import random
def generate(bawah,atas):
    angkakomp = random.randrange(bawah,atas)
    return angkakomp

#level
level=int(input("Masukkan level anda anda (1-3) = "))
if level == 1:
    print("Level Easy [0...100]")
    angkakomp=generate(0,100)
    langkah = 3
elif level == 2:
    print("Level Medium [0...1000]")
    angkakomp = generate(0,1000)
    langkah = 5
else:
    print("Level Hard [0...1000000]")
    angkakomp = generate(0,1000000)
    langkah = 7

#program utama
tebakan = False 
hasil = False #kalah
while tebakan == False: #selama tebakan masih salah maka akan berulang 
    if langkah == 0:
        break
    tebakanuser = int(input("Masukkan tebakan anda = "))
    langkah = langkah - 1
    if tebakanuser == angkakomp :
        tebakan = True
        hasil = True
        break
    else:
        if tebakanuser > angkakomp:
           print("Tebakkan anda terlalu besar")
        else:
           print("Tebakkan anda terlalu kecil")
        print ("Tebakkan anda salah! Silahkan coba lagi")
if hasil==True:
    print ("Selamat tebakkan anda benar. Sisa tebakan anda",langkah)
else: 
    print ("Anda kalah dan kehabisan langkah")