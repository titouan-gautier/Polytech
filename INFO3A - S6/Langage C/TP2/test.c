//
// Created by titoug on 14/02/24.
//

#include "test.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int createTableau(int tab[], const int len, const int min, const int max) {
    srand( time( NULL ) ); // initialise le random

    for (int i = 0; i < len; i++) {
        tab[i] = randMinMax(min,max); // Ajoiute une valeur randome entre min et max à la case i du tableau
    }

    return *tab;
}

int randMinMax(const int min, const int max) {

    return rand() % (max - min + 1) + min; // Renvoie un nombre random entre min et max

}

// Test si un tableau est croissant
int testTableauCroissant(int t[], const int len) {

    for (int i = 1; i < len; i++) {
        if (t[i] < t[i-1]) {
            return 0;
        }
    }

    return 1;

}

// Test si un tableau est décroissant
int testTableauDecroissant(int t[], const int len) {

    for (int i = 1; i < len ; i++) {
        if (t[i] > t[i-1]) {
            return 0;
        }
    }

    return 1;

}

// Affiche un tableau
void printTableau(int t[], const int len) {

    printf("[");

    int c = 0;

    for (int i = 0; i < len ; i++) {
        printf("%d, ",t[i]);
        c++;
    }

    printf("%d] \n",t[len - 1]);

}

// Test les performances des fonctions de tri
void testPerfSort(void (*sortFunction[])(int tab[], int (*comparator)(int,int), int low, int high),int (*comparator)(int,int), int low, int high ) {

    // Création d'un tableau de n case avec des nombres aléatoire entre min et max
    int tab[high + 1];
    createTableau(tab,high + 1,0,high + 1);

    for (int i = 0; i < 2; i++) {

        const double debut = clock();

        sortFunction[i](tab, comparator, low, high);

        const double fin = clock();

        // Calcul du temps d'execution en millisecondes
        const double temps = ((fin - debut) / CLOCKS_PER_SEC) * 1000;

        printf("Temps d'execution de la focntion %d: %f millisecondes \n",i + 1,temps);

    }

}


