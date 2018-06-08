def make_stack():
    stack=[]
    _table={
        'push':lambda x: stack.append(x),
        'peek': lambda x: stack[-1],
        'pop': lambda x: stack.pop(),
        'size':lambda x:len(stack)
            }
    def helper(op,*args):
        return _table[op](args[0]) if args!=() else _table[op](0)
    return helper

ops=['+','-','*','/']
my_stack=make_stack()
def prefix_infix(lst):
    if type(lst) is not list:
        return lst
    for item in lst[::-1]:
        if item not in ops:
            my_stack('push',prefix_infix(item))
        else:
            a=my_stack('pop',prefix_infix(item))
            b=my_stack('pop',prefix_infix(item))
            return '('+str(a)+' '+item+' '+str(b)+')'
    
   
#print(
#prefix_infix (['+', ['*', 5, 4], ['-', 2, 1]])
#)



print(
prefix_infix(['-',['*',5,4],['-',['/',1,45],['+',1,1]]])=='((5 * 4) - ((1 / 45) - (1 + 1)))'
    )

