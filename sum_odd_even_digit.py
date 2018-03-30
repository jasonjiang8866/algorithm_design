'''
def divisible_by_11(num):
    #your code here
    digit=count_digit(num)
    even=0
    odd=0
    for i in range(1 ,digit+1):
        if i%2==0:
            even+=num//10**(digit-1)
        else:
            odd+=num//10**(digit-1)
        num%=10**(digit-1)
        digit-=1
        print(even,odd)
    return (even-odd)%11==0


def count_digit(num):
    remain=num
    digit=0
    while remain>0:
        remain//=10
        digit+=1
    return digit

'''
def count_digit(num):
    remain=num
    digit=0
    while remain>0:
        remain//=10
        digit+=1
    return digit

def odd_even_difference(num):
    digit=count_digit(num)
    if digit==1:
        return num
    elif digit==2:
        return (num//10-num%10)
    else:
        return num//10**(digit-1)-odd_even_difference(num-num//10**(digit-1)*10**(digit-1))


def divisible_by_11(num):
    return odd_even_difference(num)%11==0


print(divisible_by_11(121))
