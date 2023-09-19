// find sum of even numbers which are divisible by 2,3 and 5 up to ‘n’ numbers where n is entered from user
#include <stdio.h>
#include <conio.h>
int main() {
    int numb, add=0;
    printf("Enter the number: ");
    scanf("%d", &numb);
    for (int i=2; i<=numb ;i=i+2) {
        if (i%15==0) {
        add=add+i; }
    }
    printf("Summation is: %d", add);
    return 0;
}