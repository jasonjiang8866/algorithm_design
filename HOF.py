from math import *

def exception_function(f, rejected_input, new_output):
    def g(x):
        return new_output if x==rejected_input else f(x)
    return g



new_sqrt = exception_function(sqrt, 7, 2)


def usually_double(x):
    """Your code here"""
    return 2*x

def new_double(x):
    """Your code here"""
    if x in [4,7,11]:
        return exception_function(usually_double, x, 0)(x)
    else:
        return usually_double(x)


def make_generator(op):
    """Your code here"""
    def g(y):
        def h(x):
            return op(x,y)
        return h
    return g
        
    


def mul(x,y):
    return x*y

def pow(x,y):
    return x**y

make_multiplier = make_generator(mul)
make_exponentiator = make_generator(pow)

print(make_exponentiator(3)(2))
