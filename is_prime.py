def is_prime(x):
'''
to test whether it is a prime number
'''
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True if x!=1 else False
