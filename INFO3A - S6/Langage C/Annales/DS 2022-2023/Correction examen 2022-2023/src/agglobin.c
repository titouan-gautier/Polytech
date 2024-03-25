#include "agglobin.h"
#include <stdlib.h>
#include <stdio.h>

struct SFilsNoeud
{
	struct SNoeud* FilsG;
	struct SNoeud* FilsD;
};

enum ETypeNoeud
{
	ETNfeuille,
	ETNinter
};

struct SNoeud
{
	int Valeur;
	enum ETypeNoeud Type;
	union
	{
		unsigned int Lettre;
		struct SFilsNoeud Fils;
	};
};


struct SNoeud* CreerFeuille(unsigned char lettre, unsigned int valeur)
{
	struct SNoeud* pNoeud = (struct SNoeud*)malloc(sizeof(struct SNoeud));

	if (pNoeud)
	{
		pNoeud->Valeur = valeur;
		pNoeud->Type = ETNfeuille;
		pNoeud->Lettre = lettre;
	}

	return(pNoeud);
}

struct SNoeud* AssocierNoeud(struct SNoeud* filsG, struct SNoeud* filsD)
{
	struct SNoeud* pNoeud = (struct SNoeud*)malloc(sizeof(struct SNoeud));

	if (pNoeud)
	{
		pNoeud->Valeur = filsG->Valeur + filsD->Valeur;
		pNoeud->Type = ETNinter;
		pNoeud->Fils.FilsG = filsG;
		pNoeud->Fils.FilsD = filsD;
	}

	return(pNoeud);
}

int EtapeGlouton(struct SNoeud** tab, unsigned int nb)
{
	unsigned int iMin1, iMin2;
	unsigned int nbValue = 0;

	// Recherche des deux plus petites valeurs
	for (unsigned int i = 0; i < nb; ++i)
	{
		if (tab[i] != NULL)
		{
			if (nbValue == 0) iMin1 = i;
			else
			{
				if (tab[i]->Valeur < tab[iMin1]->Valeur)
				{
					iMin2 = iMin1;
					iMin1 = i;
				}
				else if (nbValue == 1 || tab[i]->Valeur < tab[iMin2]->Valeur) iMin2 = i;
			}
			nbValue++;
		}
	}

	// Association des deux plus petites valeurs
	if (nbValue >= 2)
	{
		tab[iMin1] = AssocierNoeud(tab[iMin1], tab[iMin2]);
		tab[iMin2] = NULL;
	}
	if (nbValue == 1) return(iMin1);
	return(-1);
}

struct SNoeud* CreerForet(struct SNoeud** tab, unsigned int nb)
{
	int pos;
	while ((pos = EtapeGlouton(tab, nb)) == -1);

	return(tab[pos]);
}

void AfficherNoeud(struct SNoeud* n)
{
	if (n != NULL)
	{
		printf("(%d,", n->Valeur);
		if (n->Type == ETNfeuille) printf("%d", n->Lettre);
		else
		{
			AfficherNoeud(n->Fils.FilsG);
			printf(",");
			AfficherNoeud(n->Fils.FilsD);
		}
		printf(")");
	}
}

void LibererNoeud(struct SNoeud* n)
{
	if (n != NULL)
	{
		if (n->Type == ETNinter)
		{
			LibererNoeud(n->Fils.FilsG);
			LibererNoeud(n->Fils.FilsD);
		}
		free(n);
	}
}
