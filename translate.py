'''
A Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
'''
def translate(source,destination,string):
    if not all ((source,destination)):
        return string
    else:
        dictionary=dict(zip(source,destination))
        result=''
        for char in string:
            if char in dictionary:
                result+=dictionary[char]
            else:
                result+=char
        return result

def caesar_cipher(shift,string):
    shift=shift%26
    original=dict(zip(range(24),[]))
    list1=[chr(x) for x in range(97,123)]
    list2=[chr(x) for x in range(65,91)]
    list1new=shift_list(shift, list1)
    list2new=shift_list(shift, list2)
    
    return translate(list1+list2,list1new+list2new,string)
def shift_list(shift, lst):
    length=len(lst)
    dictionary=dict(zip(range(length),lst))
    new_dictionary={}
    for key, value in dictionary.items():
        new_key=key-shift
        if new_key>=0:
            new_dictionary[new_key]=value
        else:
            new_dictionary[new_key+length]=value
    print(new_dictionary)
    temp=[0]*26
    for key,value in new_dictionary.items():
        temp[key]=value
    result=''
    for item in temp:
        result+=item
    return result
