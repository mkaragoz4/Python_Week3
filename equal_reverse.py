def equal_rev(x):
    count=0
    mid=(len(x)//2)
    for i in range(mid):
        if x[i]==x[-(i+1)]:
            count+=1
    if mid==count:
        return True
    else:
        return False

txt=input("Please enter the text to check the symmetry:\n")
print(equal_rev(txt))