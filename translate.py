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
