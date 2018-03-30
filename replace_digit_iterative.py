def replace_digit(n, d, r):
    num_digit=count_digit(n)
    result=0
    for i in range(num_digit)[::-1]:
        current_digit=n//10**i
        if current_digit!=d:
            result+=current_digit*10**i
        else:
            result+=r*10**i
        n%=10**i
    return result

def count_digit(x):
    counter=0
    while x>0:
        x//=10
        counter+=1
    return counter

print(replace_digit(31242154125, 1, 0))
