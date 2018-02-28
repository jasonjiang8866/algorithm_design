def decimal_to_binary(number):
    # code to convert number into its binary representation
    check=number
    result=[]
    base=2
    while number>=0:
        i=0
        remainder=0
        while remainder>=0:
           remainder=number-base**i
           i+=1
        number=number-base**(i-2)
        #print(number)
        if result==[]:
            result.append('1')
            for j in range(0,i-2):
                result.append('0')
        else:
            print(i)
            result[-i+1]='1'
    return ''.join(result) if check>0 else '0'

print(decimal_to_binary(17))
