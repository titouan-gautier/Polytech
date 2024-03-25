//
// Created by titoug on 19/03/24.
//

#include "dames.h"
#include <stdio.h>
#include <stdlib.h>

enum StateCase {
    PionNoir,
    PionBlanc,
    Vide
};

struct SGrid {

    enum StateCase grid[5][10];
    
};

SGrid* CreateGrid() {

    SGrid *sgrid = malloc(sizeof(SGrid));

    return sgrid;

}

void DestroyGrid(SGrid *sgrid) {

    free(sgrid);

}

SGrid* InitGrid(SGrid *grid) {

    int count = 0;

    for (int i=0; i < 5; i++) {
        for (int j=0; j < 10; j++) {
            if (count < 20) {
                grid->grid[i][j] = PionNoir;
            } else if (count >= 20 && count < 30) {
                grid->grid[i][j] = Vide;
            } else {
                grid->grid[i][j] = PionBlanc;
            }

            count++;
        }

        
    }

    return grid;

}

int DrawGrid(SGrid *grid) {

    printf(" 0 1 2 3 4 5 6 7 8 9 \n");

    int line = 0;

    for (int i=0; i < 5; i++) {

        printf("+-+-+-+-+-+-+-+-+-+-+\n");

        printf("%d",line);
        line++;

        for (int j=0; j < 5; j++) {

            if (grid->grid[i][j] == PionNoir) {
                printf("| |x");
            } else if (grid->grid[i][j] == Vide) {
                printf("| | ");
            } else {
                printf("| |o");
            }
            

        }

        printf("|\n");
        printf("+-+-+-+-+-+-+-+-+-+-+\n");
        printf("%d",line);
        line++;

        for (int j=5; j < 10; j++) {

            if (grid->grid[i][j] == PionNoir) {
                printf("|x| ");
            } else if (grid->grid[i][j] == Vide) {
                printf("| | ");
            } else {
                printf("|o| ");
            }        

        }

        printf("|\n");
    }

    return 0;


}

int Num2GridCoord(SGrid *grid, int num) {

    int i = 0;
    int j = 0;

    int count = 0;

    num = num - 1;

    for (int k=0; k < 5; k++) {
        for (int l=0; l < 10; l++) {
            if (count == num) {
                i = k;
                j = l;

                printf("i = %d, j = %d\n", i, j);

                return 0;
            }

            count++;
        }
    }
    
    printf("i = %d, j = %d\n", i, j);    

    return 0;

}
int Grid2NumCoord(SGrid *grid, int x, int y) {

    int count = 1;

     for (int k=0; k < 5; k++) {
        for (int l=0; l < 10; l++) {

            if (k == x && l == y) {
                printf("NumCoord : %d \n",count);
                return 0;
            }

            count++;

        }
     }

     return 0;

}

int User2GridCoord(SGrid *grid, int x, int y) {

    int countx  = 0;
    int county  = 0;


    for (int k=0; k < 5; k++) {
        for (int l=0; l < 10; l++) {

            if (countx == x && county == y) {

                printf("x: %d, y: %d",k,l);

                return 0;
            }

            if (l == 4) {
                county++;
            }

            countx++;
        }

        county++;
    }

    printf("ff");

    return 0;

}

