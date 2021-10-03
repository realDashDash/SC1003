#include <stdio.h>

int main(void) {
    int height;
    printf("Enter the height: \n");
    scanf("%d", &height);
    printf("Pattern: \n");

    int num = 1;
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < i + 1; j++) {
            printf("%d", num);
        }
        printf("\n");
        if (++num == 4) {
            num = 1;
        }
    }

    return 0;
}
