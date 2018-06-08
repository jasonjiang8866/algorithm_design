def bubble_sort(lst):
    flag=1
    length=len(lst)
    while flag:
        flag=0
        i=0
        while i<length-1:
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                flag=1
            i+=1
    return lst


print(bubble_sort([3,4,5,-1,-7,0,3,4]))
