def safe_normalize(lst):
    # handle the error
    try:
        return normalize(lst)
    except ZeroDivisionError:
        return lst


def normalize(lst):
    s = sum(lst)
    return list(map(lambda v: v / s, lst))

print(
safe_normalize([1, 2, 2, 3])
    )
