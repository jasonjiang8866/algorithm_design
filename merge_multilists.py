def merge_lists(all_lst):
    # Your code here
    
    sorted_lst=[]
    while any(all_lst):
        min_item=0
        min_seq=0
        firstNullFlag=True
        for seq, item in enumerate(all_lst):
            print(seq,item)
            if item!=[] and firstNullFlag==True:
                min_item=item[0]
                min_index=seq
                firstNullFlag=False
            elif item!=[] and item[0]<min_item:
                print(item,'here')
                min_item=item[0]
                min_index=seq
        all_lst[min_index].remove(min_item)
        sorted_lst.append(min_item)
    return sorted_lst


all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]
