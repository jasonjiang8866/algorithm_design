def occurrence(s1, s2):
    """Counts the number of occurrences of s2 in s1"""
    length=len(s1)
    sub_length=len(s2)
    counter=0
    while length>=sub_length:
        if s1[:sub_length]==s2:
            counter+=1
            s1=s1[sub_length:]
            print(s1)
        else:
            s1=s1[1:]
            print(s1)
        length=len(s1)

    return counter

print(occurrence('101010', '10'))
