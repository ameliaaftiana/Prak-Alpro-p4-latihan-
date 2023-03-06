bawah=int(input("Masukkan batas bawah = "))
atas=int(input("Masukkan batas atas = "))

def cetak(bawah, atas):
    if bawah > atas:
        for i in (bawah, atas+1, -1):
            print (i)
    else:
        for i in (bawah,0,atas+1):
            print (i)

cetak(bawah,atas)