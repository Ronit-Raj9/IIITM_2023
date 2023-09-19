// check whether the entered integer number is palindrome or not
#include <stdio.h>
#include <conio.h>
int main() {
    int numb, reversed = 0, original, remainder;
    printf("Enter number: ");
    scanf("%d", &numb);
    original=numb;
    while (numb>0) {
        remainder=numb%10;
        reversed=reversed*10+remainder;
        numb=numb/10;
    }
    if (original == reversed) {
        printf("Number is palindrome\n");
    } else {
        printf("Number is not palindrome\n");
    }
}
