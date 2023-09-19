// Swap variable's value for float
#include <stdio.h>
#include <conio.h>
int main() {
    float a,b;
    printf("Enter Value a: ");
    scanf("%f",&a);
    printf("\nEnter Value b: ");
    scanf("%f",&b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("New value of a is %f\nNew value of b is %f",a,b);
    return 0;
}