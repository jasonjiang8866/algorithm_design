#include <stdio.h>

void split(char *, char *, char *);

int main()
{
    char username[]="***********************";//alternatively use memset(*buffer,'*',50);
    char domain[]="***********************";
    char email[]="apple@pear@com";
    split(email, username, domain);
    printf("email=%s, username=%s, email=%s\n",email,username,domain);
    return 0;
}


void split(char *email, char *username, char *domain) {
    int username_flag=1;
    int first_a_flag=1;
    while(*email){
        if (*email=='@' && first_a_flag ){
            username_flag=0;
            first_a_flag=0;
            *username=0;
            email++;
        }
        if(username_flag){
            *username++=*email;
        }else{
            *domain++=*email;
        }
        email++;
    }
    *domain=0;
}
