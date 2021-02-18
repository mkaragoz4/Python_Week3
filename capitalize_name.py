def name(y):
    x=y.lower()
    word_list=x.split()
    new_word_list=[]
    for i in word_list:
        j=list(i)
        j[0]=j[0].upper()
        str=""
        for k in j:
            str+=k
        new_word_list.append(str)

    names=" ".join(new_word_list)
    return names

txt=input("Please enter your name:\n")
print(name(txt))