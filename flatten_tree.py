def flatten(matrix):
    if matrix==():
        return ()
    elif type(matrix) is not tuple:
        return (matrix,)
    else:
        return (flatten(matrix[0]))+(flatten(matrix[1:]))
