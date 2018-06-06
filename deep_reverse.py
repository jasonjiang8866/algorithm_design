def deep_reverse(lst):
    if lst==[]:
        return []
    elif type(lst) is not list:
        return lst
    else:
        return deep_reverse(lst[1:])+[deep_reverse(lst[0]),]
