'''
def nth_digit(n, num):
    if n==1:
        return num%10
    else:
        return nth_digit(n-1,num//10)
    

    
def mth_digit(m, num):
    if m==1:
        digit=count_digit(num)
        return num//10**digit
    else:
        digit=count_digit(num)
        return mth_digit(m-1, num-num//10**digit*10**digit)
'''
def count_digit(num):
    remain=num
    digit=0
    while remain>10:
        remain//=10
        digit+=1
    return digit




def nth_digit(n, num):
    for i in range(n-1):
        num//=10
    return num%10
    
    

    
def mth_digit(m, num):
    for i in range(m-1):
        digit=count_digit(num)
        num=num-num//10**digit*10**digit
    digit=count_digit(num)
    return num//10**digit




#print(nth_digit(2,12345))
print(mth_digit(3,15091))



