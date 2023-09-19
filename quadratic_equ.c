// Write a C program to input the coefficients of a quadratic equation and find the roots of equation
#include <stdio.h>
#include <conio.h>
#include <math.h>
int main() {
    float a,b,c;
    printf("ax^2+bx+c=0 is quadratic equation\n");
    printf("Enter coefficient of x^2: ");
    scanf("%f", &a);
    printf("Enter coefficient of x: ");
    scanf("%f", &b);
    printf("Enter constant: ");
    scanf("%f", &c);
    float root1,root2;
    float srinum=sqrt((b*b)-(4*a*c));
    root1=((-b)+(srinum))/(2*a);
    root2=((-b)-(srinum))/(2*a);
    printf("Root 1 is %f\n",root1);
    printf("Root 2 is %f\n",root2);
    return 0;
}   