//
// Created by titoug on 19/03/24.
//

#ifndef DAMES_H
#define DAMES_H

typedef struct SGrid SGrid;
enum StateGrid;

SGrid* CreateGrid();
void DestroyGrid();
SGrid* InitGrid(SGrid *grid);
int DrawGrid(SGrid *grid);

int Num2GridCoord(SGrid *grid, int num);
int Grid2NumCoord(SGrid *grid, int x, int y);
int User2GridCoord(SGrid *grid, int x, int y);
int Grid2UserCoord(SGrid *grid, int x, int y);

#endif //DAMES_H
