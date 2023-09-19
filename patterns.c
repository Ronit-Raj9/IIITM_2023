// patterns
#include <stdio.h>
#include <conio.h>
int main() {
    int choice,star;
    printf("1. Inverted star\n");
    printf("2. Equivalent star\n");
    printf("3. Right angled star\n");
    printf("Enter your choice sr. no. : ");
    scanf("%d", &choice);
    switch (choice) {
        case 1:
            printf("Upto number of stars (odd number only): ");
            scanf("%d", &star);
            for (int i=0; i<star; i++){
                for (int j=0; j<(star-i-3);j++){
                    printf(" *");
                }
         //       for (int j=0; j<=i; j++){
          //          printf("*");
           //     }
                printf("\n");
            }
            break;

        case 3:
            printf("Upto number of stars: ");
            scanf("%d", &star);
            for (int i=0; i<star; i++){
                for (int j=0; j<=i; j++){
                printf("*");
                }
            printf("\n");
            }
            break;
    }
    return 0;
}