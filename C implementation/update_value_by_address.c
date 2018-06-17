#include <stdio.h>

int main()
{
    int a,*b;
    a=10;
    b=&a;
    *b+=2;
    printf("a=%d and b=%d\n",a,*b);
    printf("%c\n",'C' + ('a' - 'A')+1 );\\bonus...character arithmetics
    return 0;
}
