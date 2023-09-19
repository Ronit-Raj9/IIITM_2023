//Swapping value of 2 variables using xor
#include <stdio.h>

int main() {
    int a,b;
    printf("Number a: ");
    scanf("%d",&a);
    printf("\nNumber b: ");
    scanf("%d",&b);
    printf("\nBefore swapping: a = %d, b = %d\n", a, b);
    // Swap the values of a and b using XOR
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    printf("After swapping: a = %d, b = %d\n", a, b);
    return 0;
}
/* Eg:   for XOR FUNCTION                                       OPERATION
      a=5 & b=7                                              0     0  ---  0
      a=000000101 & b=00000111                               0     1  ---  1
      a^b=(a U b) ∩ (a' U b')                                1     1  ---  0
      a^b=00000010                                           1     0  ---  1
      ...
*/
