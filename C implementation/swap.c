#include <stdio.h> // For scanf and printf

void swap(float *a, float *b) {//Swap by reference
	float c;
	c=*a;
	*a=*b;
	*b=c;
	return;
}

int main(void) {
    float a, b;
    scanf("%f %f", &a, &b); // Get user input for floats
    printf("Before swap: a = %.2f, b = %.2f\n", a, b);
    swap(&b, &a);
    printf("After swap: a = %.2f, b = %.2f\n", a, b);
    return 0;
}