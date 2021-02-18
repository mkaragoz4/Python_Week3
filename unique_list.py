def unique_list(x):
    y=set(x)
    unic_lst=list(y)
    unic_lst.sort()
    return unic_lst

raw_list=[1,2,3,3,3,3,3,4,7,8,5,4,9,11,21,34,12]

print("Repeted List",raw_list)

print("Unrepeted List",unique_list(raw_list))
