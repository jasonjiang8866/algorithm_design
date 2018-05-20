table = {}  # table to memoize computed values
counter=0
def num_of_paths(n, m):
    global counter
    counter+=1
    if (n,m) in table:
        return table[(n,m)]
    if n==1 or m==1:
        result=1
    else:
        result=num_of_paths(n-1, m)+num_of_paths(n, m-1)
    table[(n,m)]=result
    return result

print(
num_of_paths(10, 10),
counter
    )
