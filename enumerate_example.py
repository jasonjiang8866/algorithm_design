def even_rank(tup):
    result=()
    for item in enumerate(tup):
        if (item[0]+1)%2==0:
            result+=(item[1],)
    return result


print(even_rank((3, 1, 4, 3, 2, 3, 19, 7, -90)))
            
