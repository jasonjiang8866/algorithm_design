'''
Legendre's conjecture (proposed by Adrien-Marie Legendre in 1912)
states that there is at least one prime number in range [n^2, (n + 1)^2]
for every positive integer n.
'''
def legendre(n):
    # code to test Legendre's conjecture over a range of numbers from 1 up to the input number n.
    flag=0
    for i in range(1,n+1):
        for j in range(i**2,(i+1)**2+1):
            if is_prime(j):
                print(j)
                flag+=1
                break
    if flag==n:
        return True
    else:
        return False


def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
