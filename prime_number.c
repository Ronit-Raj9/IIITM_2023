//  Write a program whether the enter number is prime or not
#include <stdio.h>
#include <conio.h>
int main() {
    int num, c = 0;
    printf("Enter number: ");
    scanf("%d", &num);
    if (num == 2)
        printf("\nprime");
    else {
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                c++;
                break; }}
        if (c != 0)
            printf("\nnot a prime");
        else
            printf("\nprime"); }
    return 0; }
