def shift_one_left(num):
    remain=num
    digit=0
    while remain>10:
        remain//=10
        digit+=1
    return remain+(num-remain*10**digit)*10
    
    
def shift_left(num, n):
    remain=num
    digit=0
    while remain>10**n:
        remain//=10
        digit+=1
    return remain+(num-remain*10**digit)*10**n
    
def shift_left_alt(num, n):
    #your code here
    if n==0:
        return num
    elif n==1:
        return shift_one_left(num)
    else:
        return shift_left_alt(shift_left_alt(num, n-1), 1)


print(shift_left_alt(12345,2))
