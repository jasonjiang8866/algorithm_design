def hanoi(n, src, dsc, aux):
    if n==1:
        return ((src,dsc),)
    else:
        return hanoi(n-1, src, aux, dsc)+hanoi(1, src, dsc, aux)+hanoi(n-1, aux, dsc, src)


print(hanoi(2, 1, 3, 2))
