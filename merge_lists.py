def merge_lists(list1, list2):
    merged_list=[]
    while list1 and list2:
        if list1[0]>list2[0]:
            merged_list.append(list1[0])
            list1.remove(list1[0])
        else:
            merged_list.append(list2[0])
            list2.remove(list2[0])
    merged_list+=list1
    merged_list+=list2
    return merged_list
