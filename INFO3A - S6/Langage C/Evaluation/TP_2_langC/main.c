#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "myQuickSort.h"
#include "MyBubbleSort.h"
#include "AlgoSort.h"
#include <time.h>

#define SIZE 10000

// Fonction pour initialiser un tableau avec des entiers aléatoires
int* initRandomArray(int size) {
    int* array = malloc(size * sizeof(int));
    if (array == NULL) {
        printf("Erreur d'allocation mémoire\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < size; i++) {
        array[i] = rand() % 100; // Nombres aléatoires entre 0 et 99
    }
    return array;
}


// Fonction pour tester si un tableau est trié
bool isSorted(int array[], int size) {
    for (int i = 1; i < size; i++) {
        if (array[i] < array[i - 1]) {
            return false; // Le tableau n'est pas trié
        }
    }
    return true; // Le tableau est trié
}

// Fonction de test des algorithmes de tri
void testSortingAlgorithms(struct SAlgo algorithms[], int array[],unsigned int size) {
    clock_t start, end;
    double cpu_time_used;

    for (int i = 0; algorithms[i].Nom != NULL; i++) {
        start = clock();
        algorithms[i].Fonction(estInf, array, size); // Appel de l'algorithme de tri i
        end = clock();

        cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("Temps d'execution pour l'algorithme %s : %f secondes\n", algorithms[i].Nom, cpu_time_used);
    }
}

int main() {
    // Taille du tableau
    int size = SIZE;

    // Initialisation du tableau avec des nombres aléatoires
    int* myArray = initRandomArray(size);

    // Affichage du tableau avant le tri
    printf("Tableau avant le tri : ");
    printArray(myArray, size);

    //Le tri en ordre croissant
    quicksort(estInf, myArray, size);
    printf("Tableau apres le tri croissant : ");
    printArray(myArray, size);

    //Le tri en ordre décroissant
    quicksort(estSup,myArray, size );
    printf("Tableau apres le tri decroissant : ");
    printArray(myArray, size);

    // Tri avec la fonction de comparaison pour les nombres pairs
    quicksort(estPaire,myArray, size );
    printf("Tableau apres le tri pairs : ");
    printArray(myArray, size);
    printf("\n");

    // Tri avec la fonction de comparaison pour les nombres impairs
    quicksort(estImpaire,myArray, size );
    printf("Tableau apres le tri impairs : ");
    printArray(myArray, size);
    printf("\n");

    // Vérification si le tableau est trié avant le tri
    if (isSorted(myArray, size)) {
        printf("Le tableau est trie de facon croissante apres le tri.\n");
    }


    // Test des algorithmes de tri
    testSortingAlgorithms(Algos, myArray, size);

    // Libération de la mémoire allouée pour le tableau
    free(myArray);

    return 0;
}