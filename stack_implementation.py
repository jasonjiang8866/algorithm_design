def make_stack(seq):
    return list(seq)

def make_empty_stack():
    return []

def is_empty_stack(stack):
    return True if stack==[] else False

def push_stack(stack, item):
    # pushes an item onto the stack, returns the stack
    return stack.append(item)

def pop_stack(stack):
    # removes the top item of the stack, returns that item. If the stack is empty, it should return None.
    if stack==[]:
        return None
    else:
        return stack.pop(-1)

    def peek_stack(stack):
    # returns but does not remove the top element of the stack. If the stack is empty, it should return None.
        return stack[-1] if not is_empty_stack(stack) else None
    
def clear_stack(stack):
    # modifies the stack to be empty and returns the stack
    stack.clear()
    return stack

#an application of stack
def calculate(inputs):
    buffer=make_empty_stack()
    if len(inputs)==0:
        return None
    elif len(inputs)==1:
        return inputs[0]
    else:
        for item in inputs:
            if type(item) is str:
                A=pop_stack(buffer)
                B=pop_stack(buffer)
                print(str(B)+item+str(A))
                result=eval(str(B)+item+str(A))
                push_stack(buffer,result)
            elif type(item) is not str:
                push_stack(buffer,item)
        return buffer[0]
            


print(calculate((5, 2, '/', 4, '*')))

'''
You can calculate the expression using the following algorithm:
If the expression only contains an integer, return that integer. Otherwise, maintain a stack.
Loop through the tuple and push every element to the stack, unless the element is an operator. If the element is an operator,
pop the first two elements out of the stack (the first and second elements popped will be the right and left operands respectively),
calculate the result and push the result into the stack.

To illustrate, we take the example (1, 2, '+', 3, '*') below (the stack is initially empty):
  a. take 1, push 1                                         # stack is [1]
  b. take 2, push 2                                         # stack is [1, 2]
  c. take '+', pop 2, pop 1, calculate 1 + 2 = 3, push 3    # stack is [3]
  d. take 3, push 3                                         # stack is [3, 3]
  e. take '*', pop 3, pop 3, calculate 3 * 3 = 9, push 9    # stack is [9]
  f. input empty, pop 9, return 9
'''

                
                
