def top_k(students, k):
    result=[]
    studentscopy=students[:]
    while studentscopy:
        biggest=0
        temp=()
        for entry in studentscopy:
            if entry[2]>biggest:
                biggest=entry[2]
                temp=entry
        result.append(temp)
        studentscopy.remove(temp)
        remain_scores=[x[2] for x in studentscopy]
        #print(biggest,max(remain_scores))
        if len(result)>=k and biggest>max(remain_scores):
            break
    #print(result)
    unique_score=[]
    for item in result:
        if item[2] not in unique_score:
            unique_score.append(item[2])
    final=[]
    for item in unique_score:
        partition=list(filter(lambda x: x[2]==item,result))
        sorted_partition=[]
        while partition:
            smallest='zzzzzzzzzzzzzzzz'
            temp=()
            for item in partition:
                #print(item[0])
                if item[0]<smallest:
                    smallest=item[0]
                    temp=item
            
            sorted_partition.append(temp)
            partition.remove(temp)
        final+=sorted_partition
    return final

students = [('tiffany', 'A', 15), 
            ('jane', 'B', 10),
            ('ben', 'C', 8), 
            ('eugene', 'A', 21),
            ('simon', 'A', 21), 
            ('john', 'A', 15), 
            ('jimmy', 'F', 1), 
            ('charles', 'C', 9), 
            ('freddy', 'D', 4), 
            ('dave', 'B', 12)]

print(top_k(students, 3))
print(top_k(students, 5))
