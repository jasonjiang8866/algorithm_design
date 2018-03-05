def exponentiation_recursive(x, e):
    """Calculates x^e using recursion"""
    if e==0:
        return 1
    else:
        return x*exponentiation_recursive(x,e-1)

print(exponentiation_recursive(4,2))
