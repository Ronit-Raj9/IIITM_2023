// Fibonacci Series
#include <stdio.h>
#include <conio.h>
int fib_rec(int index){
    if (index==1){
        return 0;
    }
    else if (index==2){
        return 1;
    }
    else if (index>2){
        return fib_rec(index-2)+fib_rec(index-1);
    }
    else {
        return 0;
    }
}
int fib_ite(int index){
    int num1=0;
    int num2=1;
    for (int i=0; i< index-1 ;i++){
        num2=num1+num2;
        num1=num2-num1;
    }
    return num1;
}
int main() {
    int choice,index;
    printf("By which method?\n");
    printf("\t1. Recurssive\n");
    printf("\t2. Iterative\n");
    printf("Enter Choice: ");
    scanf("%d", &choice);
    if (choice == 1) {
        printf("\nRecurssive method\n");
        printf("Enter a index number: ");
        scanf("%d", &index);
        printf("\nThe Number is %d\n",fib_rec(index));
    }
    else if (choice ==2){
        printf("\nIterative Method\n");
        printf("Enter a index number: ");
        scanf("%d", &index);
        printf("\nThe Number is %d\n",fib_ite(index));
    }
    return 0;
}