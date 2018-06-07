#include <stdio.h>
#define NUM 7
char get_check_code(int []);

int main(void){
	int nric;
	int digits[7];
	char outcome;
	printf("Enter your 7-digit NRIC number:\n");
	scanf("%d", &nric);
	for (int i=0; i<NUM;++i){
		digits[NUM-1-i]=nric%10;
		nric/=10;
	}
	/* for (int i=0;i<NUM;++i){
	    printf("%d",digits[i]);
	} */
	outcome=get_check_code(digits);
	printf("%c\n",outcome);
	return 0;
}

char get_check_code(int digits[]) {
	int result=0;
	int weight[]={2,7,6,5,4,3,2};
	char lookup[]={'A','B','C','D','E','F','G','H','I','Z','J'};
	char outcome;
	for (int i=0;i<NUM;++i){
		result+=digits[i]*weight[i];
	}
	result=11-result%11;
	outcome=lookup[result-1];
	return outcome;
}