def even_fibs(n):
    return accumulate(lambda x,y:(x,)+y,(), tuple(
        filter(
            is_even,map(
                fib,enumerate_interval(
                    1, n)))))

is_even=lambda x: x%2==0

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def accumulate(fn, initial,seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0],accumulate(fn, initial, seq[1:]))
def enumerate_interval(low,high):
    return tuple(range(low,high+1))

print(even_fibs(30))
