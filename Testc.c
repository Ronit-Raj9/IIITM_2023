#include <stdio.h>
#include <conio.h>
int main() {
    int num,add;
    printf("Sum of digits of a Number\n");
    printf("Enter the number: ");
    scanf("%d",&num);
    add=0;
    for (int i=1; num%i==0 ;i=i*10) {
        printf("%d",i);
    }
    printf("\n%d",add);
    return 0;
}