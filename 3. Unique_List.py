#=============UNIQUE LIST FUNCTION========
# Developer: Cemil Tepecik
# Date:16.02.2021
#Write a function that filters all the unique(unrepeated) elements of a given list.
# Example:Function call: unique_list([1,2,3,3,3,3,4,5,5]), Output : [1, 2, 3, 4, 5]
def unique_list(number_list):

    print('all list',number_list)
    number_list.sort()
    number_set=set(number_list)
    number_list=list(number_set)
    print('unique list',number_list)

#..................call function equal_reverse
number_list=[1,5,3,3,1,3,4,5,2]
unique_list(number_list)
#==============END============================