def hexadecimal_to_decimal(hex_number):
    # return the decimal number that hex_number represents
    hex_str=hex_number
    result=0
    while hex_str!='':
        result+=int(digit_decoder(hex_str[0]))*16**(len(hex_str)-1)
        hex_str=hex_str[1:]
    return result

def digit_decoder(x):
    lookup=['A','B','C','D','E','F']
    if x in lookup:
        return str(lookup.index(x)+10)
    else:
        return x
        
print(hexadecimal_to_decimal('DEADBEEF'))
