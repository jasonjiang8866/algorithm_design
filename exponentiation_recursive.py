def exponentiation_recursive(x, e):
    """Calculates x^e using recursion"""
    if e==0:
        return 1
    else:
        return x*exponentiation_recursive(x,e-1)

print(exponentiation_recursive(4,2))

def exponentiation_iteration(x, e):
    """Calculates x^e iteratively"""
    result=1
    for i in range(1,e+1):
        result*=x
    return result
print(exponentiation_iteration(4,2))
