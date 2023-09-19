// Multiplication Table
#include <stdio.h>
#include <conio.h>
int main() {
    int numb,mul;
    printf("Number for multiplication table: ");
    scanf("%d",&numb);    // Taking input for showing multiplication table
    int i=1;
    int m=1;
    while (m==1) {  // running while loop 
        if (i<=10){
            mul=numb*i;
            printf("%dx%d=%d\n",numb,i,mul); //output
            i+=1; //i+1=1
        if (i>10){
            break; // To break loop after 10 numbers
        }
        }
    }
    return 0;
}

