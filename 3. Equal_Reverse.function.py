#=============EQUAL REVERSE FUNCTION========
# Developer: Cemil Tepecik
# Date:16.02.2021
# Write a function that controls the given inputs
# whether they are equal to their reversed order or not.
#-------------function-------------------
def equal_reverse():
    print('Enter a word to check its reverse is equal to itself:')
    word=input().lower()  #make all lower words
    word_orjinal=[i for i in word]  #conver to string into a list
    leng=len(word_orjinal)
    word_reversed=word_orjinal[leng-1::-1] #reversing
    print('reverse of the word:',str(word[leng-1::-1])) #see the reversed version

    if word_orjinal==word_reversed:
        return  True
    else:
        return False

#..................call function equal_reverse
a=equal_reverse()
print(a)
#==============END============================

#===========OUTPUT==============================
#Enter a word to check its reverse is equal to itself:
#radar
#reverse of the word: radar
#True

#Enter a word to check its reverse is equal to itself:
#termal
#reverse of the word: lamret
#False