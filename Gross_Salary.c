//Gross Salary
#include <stdio.h>
#include <conio.h>
int main(){
    float sal,all,exp;
    printf(" Enter Salary: ");
    scanf("%f", &sal);
    printf("\n Allowance: ");
    scanf("%f", &all);
    printf("\n Expenditure: ");
    scanf("%f", &exp);
    printf("\n Annual Gross salary: %f", sal+all-exp);
    return 0;
}