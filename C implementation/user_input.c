#include <stdio.h> // For scanf and printf

double area_of_circle(int radius) {
    
    double result;
    result=3.14159265358979323846*radius*radius;
    return result;
}

int main(void) {
    int radius;
    scanf("%d", &radius); // Get user input for radius
    double area = area_of_circle(radius); // Store value of area
    printf("Area of circle with radius %d: %lf\n", radius, area);
    return 0;
}
