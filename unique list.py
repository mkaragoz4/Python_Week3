from collections import Counter

def unique(xlst):

	print(*Counter(sorted(xlst)))

lst=[6,6,5,88,5,7,1,2,9]
print(lst)
print("""
duzenli hali:
""")
unique(lst)

