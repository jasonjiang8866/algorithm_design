from math import *

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def test_even_num(n):
    return n % 2 == 0

def test_prime_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def combine_num(op, n, test_func) :
    # Fill your code here
    if op(0,1)==0:
        result=1
    else:
        result=0
    for i in range(1,n+1):
        if test_func(i):
            result=op(i,result)
    return result


print(combine_num(add, 5, test_even_num))
