#include <stdio.h>
#include "dames.h"

int main(void) {
    
    SGrid *grid = CreateGrid();

    InitGrid(grid);

    DrawGrid(grid);

    Num2GridCoord(grid,1);

    Grid2NumCoord(grid,1,1);

    User2GridCoord(grid,0,0);

}
