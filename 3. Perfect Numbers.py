#===========================PERFECT_NUMBER===================================
# Developer: Cemil Tepecik
# Date:18.02.2021
#Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
#The smallest perfect number is 6, which is the sum of 1, 2, and 3.
#Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
#Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 and 1000
# and find the sum of the perfect numbers using reduce and filter functions.
#------------------function----------------------------------
def perfect_numbers(x):

    divider=[]
    x_list = list(range(1,x)) #temporary list to check all numbers
    for y in x_list:
        if x%y==0:
            divider.append(y)  #add all dividers of the current number

    if sum(divider)==x:
        return x

#..................call function .......................................
number=1000
pnl=list(filter(lambda x:perfect_numbers(x),list(range(1,number))))
print(pnl) #perfect number list
print(f"List of perfect numbers till {number} is: {pnl}")

from functools import reduce
pen = reduce(lambda x,y: x + y, pnl)
print(f"Sum of the perfect numbers is: {pen}")

#==============OUTPUT=========================
#List of perfect numbers till 1000 is: [6, 28, 496]
#Sum of the perfect numbers is: 530