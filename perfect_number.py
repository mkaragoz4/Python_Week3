from functools import reduce

def perfect(x):
    sum = 0
    div_lst = [i for i in range(1,x) if x%i==0]
    for i in div_lst:
        sum+=i
    if sum==x:
        return x

print(list(filter(lambda x: perfect(x), list(range(1,1000)))))

print(reduce(lambda x, y: x + y, list(filter(lambda x: perfect(x), list(range(1,1000))))))
