//
// Created by titoug on 30/01/24.
//

#include <stdio.h>

int main() {

    int A;
    int B;
    int C;

    int temp;

    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);

    printf("A: %d, B: %d, C: %d \n", A,B,C);

    temp = A;
    A = B;
    B = C;
    C = temp;

    printf("A: %d, B: %d, C: %d \n", A,B,C);

}