// Write a C program to input three sides of a triangle and check whether the triangle is valid or not.
#include <stdio.h>
#include <conio.h>
int main() {
    int side1,side2,side3;
    printf("Enter Side 1: ");
    scanf("%d", &side1);
    printf("Enter Side 2: ");
    scanf("%d", &side2);
    printf("Enter Side 3: ");
    scanf("%d", &side3);
    if (side1+side2>side3){
        if (side1+side3>side2){
            if (side2+side3>side1){
                printf("This Triangle is possible");
            }
            else{
                printf("This Triangle is not possible");}
        }
        else{
            printf("This Triangle is not possible");}
    }
    else{
        printf("This Triangle is not possible");}
    return 0;
}