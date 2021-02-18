def sayi_yazdir(xsayi):

    birler={0:"",1:"bir",2:"iki",3:"uc",4:"dort",5:"bes",6:"alti",7:"yedi",8:"sekiz",9:"dokuz"}
    onlar={1:"on",2:"yirmi",3:"otuz",4:"kirk",5:"elli",6:"altmis",7:"yetmis",8:"seksen",9:"doksan"}
    a=str(xsayi)
    b=list(a)
    print(onlar[int(b[0])]+" "+birler[int(b[1])])

while True:
    sayi = int(input("iki basamakli sayi girin:"))
    if 9<sayi<100:
        sayi_yazdir(sayi)
        break
    else:
        print('Tekrar deneyin:')
