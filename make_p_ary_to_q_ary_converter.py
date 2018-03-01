def compose(f, g):
    return lambda x: f(g(x))

def make_p_ary_to_q_ary_converter(p, q):
    # return a number converter that takes a string representation of a number in base p and returns the string representation of that number in base q
    return compose(make_decimal_to_n_ary_converter(q),make_n_ary_to_decimal_converter(p))

binary_to_octal = make_p_ary_to_q_ary_converter(2, 8)
hexadecimal_to_binary = make_p_ary_to_q_ary_converter(16, 2)
octal_to_hexadecimal = make_p_ary_to_q_ary_converter(8, 16)
octal_to_binary = make_p_ary_to_q_ary_converter(8, 2)
