def mode_score(students):
    scores=[]
    frequency=[]
    for item in students:
        if item[2] not in scores:
            scores.append(item[2])
            frequency.append(1)
        else:
            frequency[scores.index(item[2])]+=1
    max_frequency=max(frequency)
    index=[]
    for i in range(len(frequency)):
        if frequency[i]==max_frequency:
            index.append(i)
    result=[]
    for i in range(len(frequency)):
        if i in index:
            result.append(scores[i])
    print(result)
    return result



students = [('tiffany', 'A', 15), 
            ('jane', 'B', 10),
            ('ben', 'C', 8), 
            ('simon', 'A', 21), 
            ('eugene', 'A', 21), 
            ('john', 'A', 15), 
            ('jimmy', 'F', 1), 
            ('charles', 'C', 9), 
            ('freddy', 'D', 4), 
            ('dave', 'B', 12)]
mode_score(students)
