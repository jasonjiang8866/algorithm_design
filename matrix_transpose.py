def transpose(matrix):
    col_count=len(matrix[0])
    result=[]
    for i in range(col_count):
        result+=[[],] #do not use [[],]*col_count
    print(result)
    for row in matrix:
        for i in range(col_count):
            #print(i,result[i],result)
            result[i].append(row[i])
            #print(i,result[i],result)
    print(result)
    return result

transpose([[ 1, 2, 3], [4, 5, 6], [7, 8, 9]])
