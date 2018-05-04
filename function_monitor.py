
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
