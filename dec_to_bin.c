// find the binary equivalent of a an integer number entered from user also count the number of 1’s and number of 0’s in the resultant binary number
#include <stdio.h>
#include <string.h>
int main() {
    int number;
    printf("Enter the number: ");
    scanf("%d", &number);
    int varnumb = number;
    char str[50] = ""; 
    int i = 0;
    while (varnumb > 0) { 
        if (varnumb % 2 == 0) {
            strcat(str, "0");
        } else {
            strcat(str, "1");
        }
        varnumb = varnumb / 2;
    }
    if (number == 0) {
        strcat(str, "0");
    }
    strrev(str);
    printf("Binary equivalent: %s\n", str);
    int num0=0,num1=0;
    for (int i=0; i<strlen(str);i++){
        if (str[i]=='0') {
            num0++; }
        else {
            num1++;
        }
    }
    printf("Number of 0 is %d\nNumber of 1 is %d",num0,num1);
    return 0;
}
