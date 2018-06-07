def power_set(lst):
    if lst==[]:
        return [[]]
    else:
        item=lst.pop()
        return power_set(lst[:])+[[item]+x for x in power_set(lst[:])]




print(
    (power_set([1,2,3]))
      )
