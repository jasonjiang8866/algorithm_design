def replace_digit(n, d, r):
    if n<10:
        return n if n!=d else r
    else:
        num_digit=count_digit(n)
        first_digit=n//10**(num_digit-1)
        #print(num_digit,first_digit)
        if first_digit==d:
            result=r*10**(num_digit-1)+replace_digit(n%10**(num_digit-1), d, r)
        else:
            result=first_digit*10**(num_digit-1)+replace_digit(n%10**(num_digit-1), d, r)
        return result
        


def count_digit(x):
    if x<10:
        return 1
    else:
        return 1+count_digit(x//10)

print(replace_digit(31242154125, 1, 0))
