def combinations(lst,n):  # combinations of n elements
        if n==1:
            return list(map(lambda x: [x],lst))
        elif len(lst)==n:
            return [list(lst)]
        else:
            first = lst[0]
            rest = lst[1:]
            return list(map(lambda x: [first]+x, combinations(rest,n-1))) + combinations(rest,n)
