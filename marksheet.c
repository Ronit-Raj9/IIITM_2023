// Write a C program to input marks of five subjects and calculate the percentage
#include <stdio.h>
#include <conio.h>
int main() {
    float pcp,fee,ep,maths,spe;
    printf("Enter Marks of PCP: ");
    scanf("%f", &pcp);
    printf("Enter Marks of FEE: ");
    scanf("%f", &fee);
    printf("Enter Marks of EP: ");
    scanf("%f", &ep);
    printf("Enter Marks of MATHS: ");
    scanf("%f", &maths);
    printf("Enter Marks of SPE: ");
    scanf("%f", &spe);
    float marks=(pcp+fee+ep+maths+spe); float per=(marks/5.0);
    printf("Total Marks out of 500 is %f and total Percentage is %f %%\n",marks,per);
    if (per>=90.0F){
        printf("A grade");
    }
    else if (per>=80.0F) {
        printf("B grade");
    }
    else if (per>=70.0F) {
        printf("C grade");
    }
    else if (per>=60.0F) {
        printf("D grade");
    }
    else if (per>=40.0F) {
        printf("E grade");
    }
    else{
        printf("Fail");
    }
    return 0;
}