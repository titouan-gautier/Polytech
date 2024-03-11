#pragma once 

struct SPile
{
	char Tableau[30][20];
	unsigned int Index;
};

void PileInit(struct SPile *pile);
unsigned int PileSize(struct SPile *pile);
char* PileTop(struct SPile *pile);
void PilePush(struct SPile *pile, char *elmt);
void PilePop(struct SPile *pile);

