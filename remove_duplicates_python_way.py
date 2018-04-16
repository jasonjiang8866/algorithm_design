def remove_duplicates_python_way(lst):
    db=tuple(lst)
    for item in db:
        while lst.count(item)!=1:
            lst.remove(item)
    print("happyhappy",lst)
    return lst
