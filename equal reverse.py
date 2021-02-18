def e_r(xklm):
     a=xklm==xklm[::-1]
     return a

print("Sirayla 3 kelime giriniz.")
klm=input("1. kelime:")
klm2=input("2. kelime:")
klm3=input("3. kelime:")

print("\n",e_r(klm),e_r(klm2),e_r(klm3))