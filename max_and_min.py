def max_and_min(values):
    # Write your code here
    max_i,min_i=0,999999999999
    for item in values:
        if item>max_i:
            max_i=item
        if item<min_i:
            min_i=item
    return max_i,min_i


print(max_and_min((5, -2, -3, 4, -1)))
