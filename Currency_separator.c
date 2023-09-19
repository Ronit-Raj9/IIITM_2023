// currency notes of each denomination the cashier will have to give to the withdrawer
#include <stdio.h>
int main() {
    int amount;  // enter the amount to be withdrawn
    printf("input the amount to be withdrawn: ");
    scanf("%d", &amount);
    int hundreds = amount / 100; // calculate the number of 100's notes
    amount = amount % 100;
    int fifties = amount / 50; // calculate the number of 50's notes
    amount = amount % 50; // calculate the number of 10's notes
    int tens = amount / 10; // calculate the number of 1's notes
    int ones = amount % 10;
    printf("Number of 100's notes = %d\n", hundreds);
    printf("Number of 50's notes = %d\n", fifties);
    printf("Number of 10's notes = %d\n", tens);
    printf("Number of 1's notes = %d\n", ones);
    return 0;
}