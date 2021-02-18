def sirala(xlst):
    a =sorted(xlst)
    b ="\n"+a[0]+"-"+a[1]+"-"+a[2]+"-"+a[3]+"-"+a[4]
    print(b)

print("Sirayla 5 kelime giriniz:")
klm=input("1. kelime:")
klm2=input("2. kelime:")
klm3=input("3. kelime:")
klm4=input("4. kelime:")
klm5=input("5. kelime:")
lst=[klm,klm2,klm3,klm4,klm5]

sirala(lst)