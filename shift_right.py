def shift_right(num, n):
    if n==0:
        return num
    elif n==1:
        remain=num
        digit=0
        while remain>10:
            remain//=10
            digit+=1
        return num%10*10**digit+num//10
    else:
        return shift_right(shift_right(num, n-1), 1)
    
def shift_right_alt(num, n):
    remain=num
    digit=0
    while remain>10**n:
        remain//=10
        digit+=1
    return num%(10**n)*10**digit+num//10**n

print(shift_right_alt(12345, 1))
