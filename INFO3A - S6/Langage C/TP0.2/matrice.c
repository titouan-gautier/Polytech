//
// Created by titoug on 02/02/24.
//

#include <stdio.h>

void display_matrice(const int l1,const int l2, int m[][l1]) {

    printf("\n");

    for (int i=0 ; i<l1 ; i++) {

        printf("| ");

        for (int k=0 ; k<l2 ; k++) {

            printf("%d ",m[i][k]);

        }

        printf("| ");
        printf("\n");


    }

    printf("\n");

}

int main() {

    int m[5][5] = {

        {1,2,3,8,8},
        {4,5,6,9,9},
        {6,7,8,7,7},
        {1,2,3,8,8},
        {4,5,6,9,9}

    };

    const int length1 = sizeof(m) / sizeof(m[0]);
    const int lenght2 = sizeof(m[0]) / sizeof(m[0][0]);

    display_matrice(length1, lenght2, m);

    return 0;

}
