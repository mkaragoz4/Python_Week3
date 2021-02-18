def sort_words(y):
    x=y.lower()
    word_list=x.split("-")
    word_list.sort()
    str=""
    for i in range(len(word_list)):
        if i==0:
            str += word_list[i]
        else:
            str+=("-"+word_list[i])
    return str

txt=input("Please enter the text with hypent(-):\n")
print(sort_words(txt))