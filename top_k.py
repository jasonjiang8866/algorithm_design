def top_k(lst, k):
    top_k_list=[]
    while lst:
        if len(top_k_list)==k:
            break
        biggest=-99999
        for item in lst:
            if item>biggest:
                biggest=item
        top_k_list.append(biggest)
        print(biggest,lst)
        lst.remove(biggest)
        
    return top_k_list
