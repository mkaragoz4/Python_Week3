def msbul(sayi):
    toplam=0
    for x in range(1,sayi):
        if sayi%x==0:
            toplam+=x
    return sayi==toplam
lst=list(range(1,1001))
a=list(filter(msbul,lst))
print("Mukemmel sayilar:",a)
from functools import reduce
print('Mukemmel sayilarin toplami:',reduce(lambda x,y:x+y,a))
