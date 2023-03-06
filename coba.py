# for i in range (3,100,3):
#     print(i)

#program untuk menulis angka kelipatan 50 dari 1500 sampai 20001
# for i in range (1500,20001,50):
#     print(i)

#program mengurutkan dari 15 sampai1
# for i in range (15,0,-1): #-1 bertujuan untuk mengurangi tiap bilangannya sedangkan 0 betujuan untuk batasnya sehingga akan berhenti di angka 1
#     print(i)

#program urutan angka dengan jenisnya (ganjil/genap)
# for i in range (15,0,-1):
#     if i%2==0:
#         print(i,"bilangan genap")
#     else:
#         print(i, "bilangan ganjil")

#program menulis berulang
# for _ in range (1,100):
#     print("Helloo")

# #program bilangan fibonnaci
# def fibo(batas):
#     bil1=1
#     bil2=1
#     #dua suku fibonacci pertama
#     if bil1<batas:
#         print(bil1, end="\t")
#         print(bil2, end="\t") #\t dimaksudkan agar tulisan lanjut di sampingnya bukan ke bawah
#     #suku berikutnya dari bil1+bil2
#     sukubaru=bil1+bil2
#     while sukubaru<batas:
#         print(sukubaru, end="\t")
#         #geser bil1 dan bil 2
#         bil1=bil2
#         bil2=sukubaru
#         #hitung lagi suku berikutnya
#         sukubaru=bil1+bil2
# #program utama
# batas=int(input("Masukkan batas dari deret fibonacci = "))
# fibo(batas)

# #program bilangan prima
# def prima(angka):
#     pembagi=0
#     for i in range (1,angka+1):
#         if angka % i == 0:
#             pembagi += 1 #Pembagi = pembagi = 1
#     if pembagi == 2:
#         return True
#     else:
#         return False
# #program utama
# angka=int(input("Masukkan bilangan = "))
# hasil=prima(angka)
# if hasil:
#     print("Bilangan Prima")
# else:
#     print ("Bukan Prima")

# #program bilangan prima dengan batas yang ditentukan 
# atas=int(input("Masukkan batas atas = "))
# bawah=int(input("Masukkan batas bawah = "))
# for i in range (bawah, atas+1):
#     if i % i == 0 and i // i == i:
#         print (i, "Bilangan Prima")

# #program tebak angka
# import random
# def generate(bawah,atas):
#     angkakomp=random.randrange(bawah,atas)
#     return angkakomp
# #program utama
# angkakomp=generate(0,100)
# tebakan=False
# while tebakan==False: #selama tebakan masih salah maka akan berulang 
#     tebakanuser=int(input("Masukkan tebakan anda = "))
#     if tebakanuser == angkakomp :
#         tebakan==True
#     else:
#         print ("Tebakkan anda salah! Silahkan coba lagi")
# print("Selamat tebakkan anda benar")

# #program tebak angka yang diberi hint
# import random
# def generate(bawah,atas):
#     angkakomp = random.randrange(bawah,atas)
#     return angkakomp
# #program utama
# angkakomp = generate(0,100)
# tebakan = False
# while tebakan == False: #selama tebakan masih salah maka akan berulang 
#     tebakanuser = int(input("Masukkan tebakan anda = "))
#     if tebakanuser == angkakomp :
#         tebakan = True
#     else:
#         if tebakanuser > angkakomp:
#            print("Tebakkan anda terlalu besar")
#         else:
#            print("Tebakkan anda terlalu kecil")
#         print ("Tebakkan anda salah! Silahkan coba lagi")
# print("Selamat tebakkan anda benar")

#program tebak angka yang diberi hint dan batas percobaan 
import random
def generate(bawah,atas):
    angkakomp = random.randrange(bawah,atas)
    return angkakomp
#program utama
angkakomp = generate(0,100)
tebakan = False 
langkah = 8
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




    

