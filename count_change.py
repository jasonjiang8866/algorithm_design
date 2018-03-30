coins=(1,5,10,20,50,100)
def count_change(amount, kinds_of_coins):
    coins_available=coins[:kinds_of_coins]
    #print(coins_available)
    if amount==0:
        return 1
    elif kinds_of_coins==0 or amount<0:
        return 0
    else:
        deno=coins_available[-1]
        #print(deno,kinds_of_coins,amount)
        #print(largest,amount-largest)
        return count_change(amount, kinds_of_coins-1)+count_change(amount-deno, kinds_of_coins)


print(count_change(20,5))
