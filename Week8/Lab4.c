#include <math.h>
#include <stdio.h>

int factorial(int n) {
    int sum = 1;
    if (n == 0) {
        return 1;
    } else {
        for (int i = 0; i < n; i++) {
            sum *= (i + 1);
        }
        return sum;
    }
}

int main(void) {
    float x;
    printf("Enter x: \n");
    scanf("%f", &x);

    float sum = 0;
    for (int i = 0; i < 11; i++) {
        sum += ((float)pow(x, i) / (float)factorial(i));
    }

    printf("%.2f", sum);
    return 0;
}