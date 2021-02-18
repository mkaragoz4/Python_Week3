#===================ALPHABETICAL_ORDER===========================0
# Developer: Cemil Tepecik
# Date:16.02.2021
#Write a function that takes an input of different words with hyphen (-) in between them and then:
#sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words. Example:
#Input >>> green-red-yellow-black-white
#Output >>> black-green-red-white-yellow
def alphebethic_order(color):
    print('Input >>>',color)
    clr=[]
    clr=color.split('-')
    clr.sort()
    color_ordered='-'.join(clr)
    print('Output >>>',color_ordered)

#..................call function equal_reverse
color='green-red-yellow-black-white'
alphebethic_order(color)
#==============END============================

#==============OUTPUT=========================
#Input >>> green-red-yellow-black-white
#Output >>> black-green-red-white-yellow