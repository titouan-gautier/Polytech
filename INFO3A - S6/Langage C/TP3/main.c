#include <stdlib.h>
#include <stdio.h>
#include "listeBlocMemoire.h"

void PrintList(SList *list);

int main() {

	SList *list;
	SCell *cell;

	list=CreateList();

	printf("Ajoute au début 5, 3, 1\n");
	AddElementBegin(list,5);
	cell=AddElementBegin(list,3);
	AddElementBegin(list,1);
	PrintList(list);
	printf("\n");


	printf("Supprime le 0\n");
	DeleteCell(list,GetLastElement(list));
	PrintList(list);
	printf("\n");

	printf("Ajoute à la fin 6, 8\n");
	AddElementEnd(list,6);
	AddElementEnd(list,8);
	PrintList(list);
	printf("\n");

	printf("Ajoute 4 après 3\n");
	AddElementAfter(list,cell,4);
	PrintList(list);
	printf("\n");

	printf("Ajoute 2 après le premier élément\n");
	AddElementAfter(list,GetFirstElement(list),2);
	PrintList(list);
	printf("\n");

	printf("Add 7\n");
	AddElementAfter(list,GetPrevElement(GetLastElement(list)),7);
	PrintList(list);
	printf("\n");

	printf("Add 9, 10 \n");

	AddElementEnd(list,9);
	AddElementEnd(list,10);

	PrintList(list);
	printf("\n");

	DeleteList(list);

	return 0;
}

void PrintList(SList *list)
{
	if (list)
	{
		SCell *cell=GetFirstElement(list);
		while (cell!=NULL)
		{
			printf("[%d] -> ",GetData(cell));
			cell=GetNextElement(cell);
		}
		printf("NULL\n");
	}
}
