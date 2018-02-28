#def maclaurin(x, n):
#    # code that approximates e^x up to the nth term
#    if n==1:
#        return 1
#    else:
#        return x**(n-1)/factorial(n-1)+maclaurin(x, n-1)

#def factorial(x):
#    if x==1:
#        return 1
#    else:
#        return x*factorial(x-1)

def factorial(x):
    result=1
    for i in range(2,x+1):
        result*=i
    return result
        
def maclaurin(x, n):
    # code that approximates e^x up to the nth term
    result=0
    for i in range(1,n+1):
        result+=x**(i-1)/factorial(i-1)
    return  round(result,3)

print(maclaurin(2, 10))
