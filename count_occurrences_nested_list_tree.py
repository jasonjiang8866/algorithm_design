def count_occurrences_nested_list_tree(lst, num):
    if lst==[]:
        return 0
    elif lst[0]==num:
        return 1+count_occurrences(lst[1:], num)
    elif type(lst[0]) is list:
        return count_occurrences(lst[0], num)+count_occurrences(lst[1:], num)
    else:
        return count_occurrences(lst[1:], num)
