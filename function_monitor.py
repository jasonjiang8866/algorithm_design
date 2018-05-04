
def make_monitored(f):
    counter=[0]
    def helper(x):
        if x=='how-many-calls?':
            return counter[0]
        elif x=='reset-count':
            counter[0]=0
        else:
            counter[0]+=1
            return f(x)
    return helper
    
def double(x):
    return 2 * x
d = make_monitored(double)


def make_monitored_extended(f):
    counter=[0]
    def helper(*x):
        if x==():
            counter[0]+=1
            return f()
        elif x[0]=='how-many-calls?':
            return counter[0]
        elif x[0]=='reset-count':
            counter[0]=0
        else:
            counter[0]+=1
            return f(*x)
    return helper
 

def sum_numbers(*numbers):
    s = 0
    for n in numbers:
        s = s + n
    return s
monitored_sum_numbers = make_monitored_extended(sum_numbers)

