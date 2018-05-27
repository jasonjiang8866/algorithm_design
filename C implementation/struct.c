#include <stdio.h>

typedef struct {
    float re;
    float im;
} Complex;

int print_complex(Complex x){
    if(x.im>=0){
    printf("%.2f + %.2fi", x.re, x.im);
    }else{
    printf("%.2f - %.2fi", x.re, -1*x.im);
    }return 0;
}

Complex create_complex(float, float); //Prototype

int main(){
    float real=10; //Real part of the complex number, feel free to edit
    float imaginary=20; //Imaginary part of the complex number, feel free to edit
    Complex new_complex1=create_complex(real, imaginary);
	Complex new_complex2=create_complex(-5, -10);
	Complex result=add(new_complex1,new_complex2);
	print_complex(result);
    return 0;
}


Complex create_complex(float real, float imaginary){
    Complex result={real,imaginary};
	return result;
}

Complex add(Complex x,Complex y){
	Complex result;
	result.re=x.re+y.re;
	result.im=x.im+y.im;
	return result;
}
