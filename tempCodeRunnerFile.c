// print number in words
#include <stdio.h>
#include <string.h>
#include <conio.h>
int main() {
    char strg[50]="";
    int numb=0;
    printf("Enter word: ");
    scanf("%s",strg);
    for (int i=0; i<strlen(strg);i++ ){
        if ((strg[i]=='0') || (strg[i]=='1') || (strg[i]=='2') || (strg[i]=='3') || (strg[i]=='4') || (strg[i]=='5' || strg[i]=='6') || (strg[i]=='7') || (strg[i]=='8') || (strg[i]=='9')){
           numb++; 
        }
    }
    printf("Numbers in word are: %d",numb);
    return 0;
}