def col_sum(matrix):
    col_count=len(matrix[0])
    result=[0]*col_count
    for item in matrix:
        for i in range(col_count):
            result[i]+=item[i]
    print(result)
    return result



col_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


def row_sum(matrix):
    row_count=len(matrix)
    result=[]
    for item in matrix:
        result.append(sum(item))
    print(result)
    return result

row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
