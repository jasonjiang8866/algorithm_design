def flatten(matrix):
    if matrix==():
        return ()
    elif type(matrix) is not tuple:
        return (matrix,)
    else:
        return flatten(matrix[0])+flatten(matrix[1:])

print(flatten((1,2,(3,4,(5,6)),7,8)))
