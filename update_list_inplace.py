def at_least_n(lst, n):
    for item in lst[:]: #slicing will produce a new list
        if item<n:
            lst.remove(item)
    return lst
    
lst=[1,2,3,4,5]
at_least_n(lst,2)


def at_least_n_new_list(lst, n):
    result=[]
    for item in lst:
        if item>=n:
            result.append(item)
    return result
