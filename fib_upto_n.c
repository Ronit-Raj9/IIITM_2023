// print fibonacci upto n
#include <stdio.h>
#include <conio.h>
int main() {
    int index;
    printf("Enter a index number: ");
    scanf("%d", &index);
    int num1=0;
    int num2=1;
    if (index==1) {
        printf("0");
    }
    else if (index==2) {
        printf("1");
    }
    else {
    printf("0\n");
    for (int i=0; i< index-1 ;i++){
        num2=num1+num2;
        num1=num2-num1;
        printf("%d\n",num1);
    }}
    return 0;
}