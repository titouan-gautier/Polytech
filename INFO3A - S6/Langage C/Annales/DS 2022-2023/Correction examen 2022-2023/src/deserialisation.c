#include "deserialisation.h"
#include <stdlib.h>

enum EEtat
{
	EEdebut,
	EEvaleur,
	EElettreOuNoeud,
	EElettre,
	EESousNoeud1,
	EESousNoeudInter,
	EESousNoeud2,
	EEfin,
	EEerreur
};

struct SNoeud* GenererForetRec(const char** str)
{
	struct SNoeud* pNoeud = NULL;
	enum EEtat etat = EEdebut;
	int valeur, ascii;
	struct SNoeud* n1 = NULL, * n2 = NULL;

	while ((etat != EEfin) && (**str != '\0'))
	{
		char c = **str;
		switch (etat)
		{
		case EEdebut:
			if (c == '(')
			{
				etat = EEvaleur;
				valeur = 0;
			}
			else etat = EEerreur;
			break;

		case EEvaleur:
			if (c == ',')
			{
				etat = EElettreOuNoeud;
				ascii = 0;
			}
			else if (c >= '0' && c <= '9') valeur = valeur * 10 + c - '0';
			else etat = EEerreur;
			break;

		case EElettreOuNoeud:
			if (c == '(')
			{
				if ((n1 = GenererForetRec(str)) == NULL) etat = EEerreur;
				else etat = EESousNoeud1;
			}
			else if (c >= '0' && c <= '9')
			{
				etat = EElettre;
				ascii = c - '0';
			}
			else etat = EEerreur;
			break;

		case EElettre:
			if (c == ')')
			{
				etat = EEfin;
				pNoeud = CreerFeuille(ascii, valeur);
			}
			else if (c >= '0' && c <= '9') ascii = ascii * 10 + c - '0';
			else etat = EEerreur;
			break;

		case EESousNoeud1:
			if (c == ',') etat = EESousNoeudInter;
			else etat = EEerreur;
			break;

		case EESousNoeudInter:
			if ((n2 = GenererForetRec(str)) == NULL) etat = EEerreur;
			else etat = EESousNoeud2;
			break;

		case EESousNoeud2:
			if (c == ')')
			{
				etat = EEfin;
				pNoeud = AssocierNoeud(n1, n2);
			}
			else etat = EEerreur;
			break;
		}

		if (etat != EEfin) (*str)++;
	}

	if (etat == EEerreur)
	{
		if (n1) LibererNoeud(n1);
		if (n2) LibererNoeud(n2);
	}

	return(pNoeud);
}

struct SNoeud* GenererForet(const char* str)
{
	const char* s = str;
	return(GenererForetRec(&s));
}
