//Write a C program to find maximum and minimum number among three numbers with or without using ternary operators
#include <stdio.h>
#include <conio.h>
int main() {
    int num1,num2,num3;
    printf("Enter Number 1: ");
    scanf("%d", &num1);
    printf("Enter Number 2: ");
    scanf("%d", &num2);
    printf("Enter Number 3: ");
    scanf("%d", &num3);
    int max,min;
    max = num1;
    min = num2;
    (num1>num2) ? (max = num1) : (max = num2);
    (max>num3) ? (max = max) : (max = num3);
    (num1<num2) ? (min = num1) : (min = num2);
    (min<num3) ? (min = min) : (min = num3);
    printf("Max is %d\n", max);
    printf("Min is %d", min);
    return 0;
}