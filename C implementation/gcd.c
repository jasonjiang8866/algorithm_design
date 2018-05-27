int gcd(int x,int y){
 
int temp;
while (y!=0){
    temp=x;
    x=y;
    y=temp%y;
}
return x;
}

/*
Python:  Greatest Common Divisor
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
*/