add1 = lambda x: x + 1

def compose(f, g):
    return lambda x: f(g(x))

def repeated(f, n):
    if n == 0:
        return lambda x: x
    else:
        return compose(f, repeated(f, n - 1))

def plus(x, y):
    #implement plus using repeated and add1
    return repeated(add1,y)(x)
