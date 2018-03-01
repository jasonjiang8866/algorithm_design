def make_decimal_to_n_ary_converter(n):
    # return a number converter that takes a decimal number and returns its string representation in base n
    def decimal_to_binary(number):
    
        check=number
        result=[]
        base=n
        position=0
        multiplier=1
        number_string=[]
        while number>0:
            remainder=0
            while remainder>=0:
                remainder=number-multiplier*base**position
                position+=1
                print('here1')
            print(remainder)
            position=position-2
            print(position)
            remainder=number-multiplier*base**position
            while remainder>=0:
                remainder=number-multiplier*base**position
                multiplier+=1
                print('here2')
                print(multiplier)
            multiplier=multiplier-2 if multiplier!=1 else 1
            if number_string==[]:
                number_string.append(digit_transformer(multiplier))
                for indexer in range(0,position):
                    number_string.append('0')
            else:
                number_string[-position-1]=str(digit_transformer(multiplier))
            number=number-multiplier*base**position
            print('number_string='+str(number_string))
            print(number)
            position=0
            multiplier=1
        return ''.join(number_string) if check>0 else '0'
    return decimal_to_binary

def digit_transformer(x):
    lookup=['A','B','C','D','E','F']
    if x>=9:
        return lookup[x-10]
    else:
        return str(x)

decimal_to_binary = make_decimal_to_n_ary_converter(2)
decimal_to_octal = make_decimal_to_n_ary_converter(8)
decimal_to_hexadecimal = make_decimal_to_n_ary_converter(16)

print(make_decimal_to_n_ary_converter(2)(213))
