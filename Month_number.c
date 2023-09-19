// Write a program to print the month name corresponding to the digit enter from the user using switch statement. For example if user enter 1 then print “January” on 2 print “February”…..
#include <stdio.h>
#include <conio.h>
int main() {
    int month;
    printf("Enter Month number: ");
    scanf("%d", &month);
    switch (month){
        case 1:
            printf("Month is January");
            break;
        case 2:
            printf("Month is February");
            break;
        case 3:
            printf("Month is March");
            break;
        case 4:
            printf("Month is April");
            break;
        case 5:
            printf("Month is May");
            break;
        case 6:
            printf("Month is June");
            break;
        case 7:
            printf("Month is July");
            break;
        case 8:
            printf("Month is August");
            break;
        case 9:
            printf("Month is September");
            break;
        case 10:
            printf("Month is October");
            break;
        case 11:
            printf("Month is November");
            break;
        case 12:
            printf("Month is December");
            break;
        default:
            printf("Invalid Number entered");
    }
    return 0;
}