// Calculator
#include <stdio.h>
#include <conio.h>
int main() {
    int opsr,tsr; // operator's Sr No.
    float fno; // first number variable
    int m =1;
    printf("Enter Number: ");
    scanf("%f",&fno);
    float add,sub,mul,div,result,num;
    result=fno;
    while (m==1) {
        printf("\nWant to enter another number\nEnter 1 for yes and 2 for no : ");
        scanf("%d",&opsr);
        if (opsr==1) {
            printf("\nEnter Number: ");
            scanf("%f",&num);
            printf("\nOperators:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n");
            printf("Enter sr no. of operator: "); //enter either 1,2,3,4
            scanf("%d",&tsr);
            if (tsr==1) {
                result=result+num;
            }
            if (tsr==2) {
                result=result-num;
            }
            if (tsr==3) {
                result=result*num;
            }
            if (tsr==4) {
                result=result/num;
            }
            printf("\nFinal Result: %f",result);
        }
        if (opsr==2) {
            printf("\nEnding Calculator Program");
            break;
        }
    }
    return 0;
}