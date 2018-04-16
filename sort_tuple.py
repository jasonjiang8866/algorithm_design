def sort_tuple(lst):
    sorted_lst=[]
    while lst:
        biggest=0
        temp=0
        for item in lst:
            if item[1]>biggest:
                biggest=item[1]
                temp=item
        sorted_lst.append(temp)
        lst.remove(temp)
    return sorted_lst


sort_tuple([("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)])
