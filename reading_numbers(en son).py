x=int(input('Sayıyı gır ıkı hanaelı; '))
birler=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
onlar=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
yirmi_sonrası=["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
def reading_number(x):
    if  20 > x > 9:
        return print(x, "------>", onlar[x%10])
    elif 100 > x > 19:
        return print(x, "------>", yirmi_sonrası[(int(x/10))-2], birler[x%10])
reading_number(x)




