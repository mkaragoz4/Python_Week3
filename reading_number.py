def transcript(x):

    lst = [i for i in x]
    if lst[0]=='1':
        if lst[1]=='0':
            return 'Ten'
        elif lst[1]=='1':
            return 'Eleven'
        elif lst[1]=='2':
            return 'Twelve'
        elif lst[1]=='3':
            return 'Thirteen'
        elif lst[1]=='4':
            return 'Fourteen'
        elif lst[1]=='5':
            return 'Fifteen'
        elif lst[1]=='6':
            return 'Sixteen'
        elif lst[1]=='7':
            return 'Seventeen'
        elif lst[1]=='8':
            return 'Eighteen'
        else:
            return 'Nineteen'
    elif lst[0]=='2':
        return 'Twenty '+number(lst[1])
    elif lst[0]=='3':
        return 'Thirty '+number(lst[1])
    elif lst[0]=='4':
        return 'Fourty '+number(lst[1])
    elif lst[0]=='5':
        return 'Fifty '+number(lst[1])
    elif lst[0]=='6':
        return 'Sixty '+number(lst[1])
    elif lst[0]=='7':
        return 'Seventy '+number(lst[1])
    elif lst[0]=='8':
        return 'Eighty '+number(lst[1])
    else:
        return 'Ninety '+number(lst[1])

def number(y):

    if y == '0':
        return ''
    elif y == '1':
        return 'one'
    elif y == '2':
        return 'two'
    elif y == '3':
        return 'three'
    elif y == '4':
        return 'four'
    elif y == '5':
        return 'five'
    elif y == '6':
        return 'six'
    elif y == '7':
        return 'seven'
    elif y == '8':
        return 'eight'
    else:
        return 'nine'

a=input('Please insert the two digit numbers:')
print(a," -------------------> ",transcript(a))
