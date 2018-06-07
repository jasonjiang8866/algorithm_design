#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define DST_SIZE 100

void copy_odd(char *dst, char *src, int *count) {
    /*
     Parameters:
        dst   - Pointer to a char array
        src   - Pointer to a char array (with a valid string in it)
        count - Count of characters copied
     
     Copy all ODD characters from the source to the destination char array and
     return the number of characters copied through the "count" pointer.
    
    
	*count=0;
	dst[0]=0;
	while (src[*count]!=0){
	    if ((*count%2) == 0)
	    {
	    dst[*count/2]=src[*count];
	    dst[*count/2+1]=0;
	    }
	    *count=*count+1;
	}
	*count=(*count+1)/2;
}
*/

*count=0;
while (*src!=0){
        *dst++=*src;
        (*count)++;
        src++;
        if(*src==0){
            break;
        } else {
        src++;
        }
}
*dst=0;
}

void test_copy_odd(char *input) {
    char output[DST_SIZE];
    int count;
    memset(output, '*', DST_SIZE);
    output[DST_SIZE - 1] = 0;
    copy_odd(output, input, &count);
    printf("\"%s\" --(copied %d)--> \"%s\"\n", input, count, output);
}

int main(void) {
    test_copy_odd("");
    test_copy_odd("C");
    test_copy_odd("123");
    test_copy_odd("hello world");
    return 0;
}

/*
 EXPECTED OUTPUT:
 
    "" --(copied 0)--> ""
    "C" --(copied 1)--> "C"
    "123" --(copied 2)--> "13"
    "hello world" --(copied 6)--> "hlowrd"
*/
