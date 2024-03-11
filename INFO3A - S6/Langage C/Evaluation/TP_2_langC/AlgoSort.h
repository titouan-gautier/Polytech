#pragma once

#include <stdio.h>


// Inclusion du fichier d'en-tête contenant la définition de fxnCmp
#include "MyBubbleSort.h"

// Définition de la structure pour représenter un algorithme de tri
struct SAlgo
{
	char *Nom;
	void (*Fonction)(fxnCmp, int*, unsigned int);
};

// Déclaration du tableau des algorithmes de tri
extern struct SAlgo Algos[];
