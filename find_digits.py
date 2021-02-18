def find_digit(x):
    digits = [i for i in x]
    number_of_digits=0
    for i in digits:
        if int(i)!=0 and int(x)%int(i)==0:
            number_of_digits+=1
    return number_of_digits

number=input("Please enter the number to fined divisor digits:\n")
print(find_digit(number))

