def increase_by_one(d):
    if d=={}:
        return d
    else:
        for key, value in d.items():
            if type(value) is dict:
                #print(key,value)
                increase_by_one(value)
            else:
                #print(key,value)
                d[key]=value+1
        return d
