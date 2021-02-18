#=================READING_NUMBER============================
# Developer: Cemil Tepecik
# Date:16.02.2021
#Write a function that outputs the transcription of an input number with two digits.
#Example:
#28---------------->Twenty Eight

def reading_number(number):
    ones_digit=['Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ','Seventy ','Eighty ', 'Ninety ']
    decimal_digit=['One','Two','Three','Four','Five','Six','Seven', 'Eight','Nine','Ten',
                   'Eleven','Twelf','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']


    number_listform=int(number[0]),int(number[1])
    number_list=list(number_listform)

    counter_decimal=[2,3,4,5,6,7,8,9]
    counter_digit=[1,2,3,4,5,6,7,8,9]
# Decimal-------------------------------------------------------------
    if int(number[0])>1:
        for x in counter_decimal:
            if x==number_list[0]:
                transcription=ones_digit[x-2]
# Digit-------------------------------------------------------------
        for y in counter_digit:
            if y==number_list[1]:
                transcription+=decimal_digit[y-1]
# 10 to 19-------------------------------------------------------------
    else:
        if int(number[1])==0:
            transcription=decimal_digit[9]
        elif int(number[1])==1:
            transcription = decimal_digit[10]
        elif int(number[1])==2:
            transcription = decimal_digit[11]
        elif int(number[1])==3:
            transcription = decimal_digit[12]
        elif int(number[1])==4:
            transcription = decimal_digit[13]
        elif int(number[1])==5:
            transcription = decimal_digit[14]
        elif int(number[1])==6:
            transcription = decimal_digit[15]
        elif int(number[1])==7:
            transcription = decimal_digit[16]
        elif int(number[1])==8:
            transcription = decimal_digit[17]
        elif int(number[1])==9:
            transcription = decimal_digit[18]
    return transcription

#..................call function equal_reverse
number=input('Enter the number from 10 to 99:')
tr=reading_number(number)
stre=str(number)
print(stre,'---------------->',tr)
#==============END============================

#==============OUTPUT=========================
#Enter the number from 10 to 99:82
#82 ----------------> Eighty Two