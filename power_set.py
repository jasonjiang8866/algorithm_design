def power_set(lst):
    if lst==[]:
        return [[]]
    else:
        item=lst[0]
        return power_set(lst[1:])+[[item]+x for x in power_set(lst[1:])]


def power_set_check(lst):
    max_lst=[]
    for item in lst:
        if len(item)>len(max_lst):
            max_lst=item
    powerset=power_set(max_lst)
    for item in powerset:
        if item not in lst:
            print(item)
            return False
    return True

print(
power_set_check([[1,2,3],[1,2],[1,3],[2,3],[1],[2],[3],[]])
    )
            
