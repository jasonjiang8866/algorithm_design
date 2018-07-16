def combinations(lst,n):  # combinations of n elements
        if n==1:
            return list(map(lambda x: [x],lst))
        elif len(lst)==n:
            return [list(lst)]
        else:
            first = lst[0]
            rest = lst[1:]
            return list(map(lambda x: [first]+x, combinations(rest,n-1))) + combinations(rest,n)


def combination_alter(lst, n):
    if len(lst)<=n:
        return [lst]
    elif n<=0:
        return [[]]
    else:
        element=lst[0]
        return combination(lst[1:],n)+ [[element]+x for x in combination(lst[1:],n-1)]
