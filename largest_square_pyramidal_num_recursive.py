from math import *

def largest_square_pyramidal_num_rec(n) :
    if test_square_pyramidal(n):
        return n
    else:
        return largest_square_pyramidal_num_rec(n-1)


def test_square_pyramidal(n) :
    k=1
    while (2*k**3+3*k**2+k)/6<=n:
        if (2*k**3+3*k**2+k)/6==n:
            return True 
        k+=1
    return False


print(largest_square_pyramidal_num_rec(100))
