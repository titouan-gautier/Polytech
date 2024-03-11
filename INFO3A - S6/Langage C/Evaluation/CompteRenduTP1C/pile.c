#include <string.h>
#include "pile.h"

void PileInit(struct SPile *pile)
{
	pile->Index = 0;
}

unsigned int PileSize(struct SPile *pile)
{
	return(pile->Index);
}

char* PileTop(struct SPile *pile)
{
	return(pile->Tableau[pile->Index-1]);
}

void PilePush(struct SPile *pile, char *elmt)
{
	if(pile->Index < 30)
	{
		strcpy(pile->Tableau[pile->Index],elmt);
		pile->Index++;
	}
}

void PilePop(struct SPile *pile)
{
	pile->Index--;
}

