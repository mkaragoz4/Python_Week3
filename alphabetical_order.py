def alfabe (x):
    ayır=x.split("-")
    ayır.sort()
    birleştir="-".join(ayır)
    print(birleştir)
x="mehmet-ali-yellow-black-white"
alfabe(x)