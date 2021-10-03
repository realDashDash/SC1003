#include <stdio.h>

int main(void) {
    int studentID;
    int mark;
    char grade;

    printf("Enter Student ID: ");
    scanf("%d", &studentID);
    printf("Enter Mark: ");
    scanf("%d", &mark);

    if (studentID != -1) {
        if (mark >= 75 && mark <= 100) {
            grade = 'A';
        } else if (mark >= 65 && mark <= 74) {
            grade = 'B';
        } else if (mark >= 55 && mark <= 64) {
            grade = 'C';
        } else if (mark >= 45 && mark <= 54) {
            grade = 'D';
        } else {
            grade = 'E';
        }
    }

    return 0;
}