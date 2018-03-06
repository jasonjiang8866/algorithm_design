def change_value_at_index(tpl, index, value):
    length=len(tpl)
    p1=tpl[-length:index]
    p2=tpl[index+1:length]
    return p1+(value,)+p2 if (index>=0 and index<length) or (index<0 and -index<=length) else  tpl

print(change_value_at_index((1, 2, 3), 10, -1))
