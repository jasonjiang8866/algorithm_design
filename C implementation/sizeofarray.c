#include <stdio.h>
int nth_sum_of_num_array(int);
int num_array[10] = {3, 4, 6, 1, 0, 9, 8, 6, 2, 5};
int main()
{
    /*
    int a[] = {1, 2, 3, 4, 5};
    int i, j, result;
    i = a[0]++;
    printf("i=%d\n", i);
    j = a[i++];
    printf("j=%d\n", j);
    printf("i=%d\n", i);
    result = i + j;
    printf("%d\n", result);
    printf("%d\n", a[0]);
    */
    int result;
    result=nth_sum_of_num_array(10);
    return result;
}

int nth_sum_of_num_array(int n) {
   
    int size;
	int sum=0;
    size=sizeof(num_array)/sizeof(num_array[0]);
    if (n<=0||n>size){
		return -1;
	} else {
		for (int i=0;i<n;i++){
			sum+=nth_sum_of_num_array[i];
		}
	}
	return sum;
}
