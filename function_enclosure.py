def make_accumulator():
    result=[0]# stateful variable
    def helper(item):
        result[0]+=item
        return result[0]
    return helper
    
 
A = make_accumulator()
A(10)
A(5)
