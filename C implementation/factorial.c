int factorial(int n) {
/*  a for-loop */
    int result=1;
    int i=1;
    for(int i=1;i<=n;i++){
        result*=i;
    }
    return result;
}


int factorial(int n) {
/*  a recursive function */
if (n==1||n==0){
    return 1;
} else {
    return factorial(n-1)*n;
}
}

