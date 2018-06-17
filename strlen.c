#include <stdio.h> // For scanf and printf

int len(char* );

int main(void) {
    char s[100];
    scanf("%s", &s); // Get the input string
    printf("Length is %d\n", len(s));
    return 0;
}

int len(char* string) {
    int i=0;
    while (string[i]){
    ++i;
    }
    return i;
}
