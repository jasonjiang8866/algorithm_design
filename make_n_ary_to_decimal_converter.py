def make_n_ary_to_decimal_converter(n):
    # return a number converter that takes a string representation of a base n number and returns its decimal equivalent
    def hexadecimal_to_decimal(hex_number):
        # return the decimal number that hex_number represents
        hex_str=hex_number
        result=0
        while hex_str!='':
            result+=int(digit_decoder(hex_str[0]))*n**(len(hex_str)-1)
            hex_str=hex_str[1:]
        return result
    return hexadecimal_to_decimal

def digit_decoder(x):
    lookup=['A','B','C','D','E','F']
    if x in lookup:
        return str(lookup.index(x)+10)
    else:
        return x


binary_to_decimal = make_n_ary_to_decimal_converter(2)
octal_to_decimal = make_n_ary_to_decimal_converter(8)
hexadecimal_to_decimal = make_n_ary_to_decimal_converter(16)

print(make_n_ary_to_decimal_converter(14)('DABBAD00'))
