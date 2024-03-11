#include <stdio.h>
#include "sort.h"
#include "test.h"
#include "comparator.h"

#define TAILLE_TAB 100000 // Taile du tableau
#define MIN_RAND 0 // Valeur min pour le random
#define MAX_RAND TAILLE_TAB // Valeur max pour le random

int main() {

    int tab[TAILLE_TAB]; // Déclarartion du tableau

    // Création d'un tableau de n case avec des nombres aléatoire entre min et max
    createTableau(tab, TAILLE_TAB,MIN_RAND,MAX_RAND);

    printf("Tableau de base : \n");
    printTableau(tab, TAILLE_TAB);
    printf("\n");

    // Fonction de tri quicksort avec en parametre le tableau, la fonction de comparaison, la première case, la dernière case
    quicksort(tab,sortCroissant,0,TAILLE_TAB - 1);
    //quicksort(tab,sortDecroissant,0,TAILLE_TAB - 1);

    printf("Tableau trié : \n");
    printTableau(tab, TAILLE_TAB);
    printf("\n");

    // On test si le tableau est trié dans l'ordre croissant
    if (testTableauCroissant(tab,TAILLE_TAB) == 1) {

        printf("Le tableau est trié dans l'ordre croissant \n");

    // On test si le tableau est trié dans l'ordre décroissant
    } else if (testTableauDecroissant(tab,TAILLE_TAB) == 1) {

        printf("Le tableau est trié dans l'ordre decroissant \n");

    } else {

        printf("Le tableau n'est pas trié \n");

    }

    printf("\n");

    // On déclare le tableau de fonction
    void (*sortFunction[])() = {quicksort, tri_a_bulles};
    // On test les fonction de tri
    testPerfSort(sortFunction, sortCroissant, 0, TAILLE_TAB - 1);

    return 0;
}
