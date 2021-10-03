#include <stdio.h>

int main(void) {
    int t;  // test cases
    printf("Enter number of lines: ");
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        printf("Enter line %d (End with -1): ", i + 1);

        int sum = 0;
        int num = 0;
        int counter = 0;
        while (num != -1) {
            sum += num;
            counter++;
            scanf("%d", &num);
        }

        double average = (double)sum / --counter;
        printf("Average = %.2f\n", average);
    }

    return 0;
}