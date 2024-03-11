//
// Created by titoug on 30/01/24.
//

#include <stdio.h>

int main() {

    int x;
    int y;

    scanf("%d",&x);
    scanf("%d",&y);

    int reste = x % y;
    int quotient = x / y;
    int quotientr = (x/y) + reste;

    printf("Reste : %d \n", reste);
    printf("Quotient : %d \n", quotient);
    printf("Quotient rationnel : %d \n", quotientr);

}
