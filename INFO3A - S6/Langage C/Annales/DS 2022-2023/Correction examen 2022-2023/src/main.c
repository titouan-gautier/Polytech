#include <stdio.h>
#include <stdlib.h>
#include "statsfichier.h"
#include "agglobin.h"
#include "deserialisation.h"

void AfficherStats(struct SStat* stats)
{
	if (stats == NULL) return;

	for (unsigned int i = 0; i < 256; ++i)
	{
		printf("%d (%c):\t%d\n", i, i>32 ? i : ' ', stats->Stat[i]);
	}
}

int main()
{
	// Statistiques de fichier
	struct SStat stats = StatistiqueFichier("src/main.c");
	AfficherStats(&stats);

	// Agglomération d'arbres binaires
	struct SNoeud* tab[6];

	tab[0]=CreerFeuille('F', 5);
	tab[1]=CreerFeuille('A', 10);
	tab[2]=CreerFeuille('B', 10);
	tab[3]=CreerFeuille('D', 15);
	tab[4]=CreerFeuille('C', 25);
	tab[5]=CreerFeuille('E', 35);

	struct SNoeud* n = CreerForet(tab, 6);
	AfficherNoeud(n);
	printf("\n");

	for (unsigned int i = 0; i < 6; ++i) LibererNoeud(tab[i]);

	// Question bonus
	const char* str = "(100,(40,(15,68),(25,(10,66),(15,(5,70),(10,65)))),(60,(25,67),(35,69)))";
	struct SNoeud* n2 = GenererForet(str);
	AfficherNoeud(n2);
	printf("\n");
	LibererNoeud(n2);

	return(0);
}
