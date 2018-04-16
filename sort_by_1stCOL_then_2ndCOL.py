def sort_by_1stCOL_then_2ndCOL(lst):
    # Fill in your code here
    unique_key=[]
    for item in lst:
        if item[0] not in unique_key:
            unique_key.append(item[0])
    sorted_key=[]
    while unique_key:
        biggest='A'
        for item in unique_key:
            if item>biggest:
                biggest=item
        sorted_key.append(biggest)
        unique_key.remove(biggest)
    sorted_lst=[]
    for item in sorted_key:
        partition=list(filter(lambda x: x[0]==item,lst))
        print(partition)
        sorted_partition=[]
        while partition:
            biggest=0
            temp=0
            for item in partition:
                if item[1]>biggest:
                    biggest=item[1]
                    temp=item
            print(temp)
            sorted_partition.append(temp)
            partition.remove(temp)
        sorted_lst+=(sorted_partition)
    return sorted_lst

sort_by_1stCOL_then_2ndCOL([("F", 9), ("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)])
