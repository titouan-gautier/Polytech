#include <stdio.h>
#include <stdbool.h>
#include "myQuickSort.h"

// Fonction d'échange de deux éléments dans un tableau
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Fonction de comparaison pour vérifier si le premier élément est supérieur au deuxième
bool estSup(int a, int b) {
    return (a > b);
}

// Fonction de comparaison pour vérifier si le premier élément est inférieur au deuxième
bool estInf(int a, int b) {
    return (a < b);
}
// Fonction de comparaison pour vérifier si le nombre est pair
bool estPaire(int a, int b) {
    return (a % 2 == 0 && b % 2 != 0); // Si a est pair et b est impair, a est considéré comme inférieur à b
}

// Fonction de comparaison pour vérifier si le nombre est impair
bool estImpaire(int a, int b) {
    return (a % 2 != 0 && b % 2 == 0); // Si a est impair et b est pair, a est considéré comme supérieur à b
}

// Fonction partition pour QuickSort
int partition(int array[], int debut, int fin, fxnCmp comparer) {
    int pivot = array[debut]; // Choix du pivot (premier élément du tableau)
    int i = debut + 1;
    int j = fin;

    // Boucle pour partitionner le tableau autour du pivot
    while (i <= j) {
        // Trouver un élément plus grand que le pivot à gauche du tableau
        while (i <= fin && comparer(array[i] , pivot)) {
            i++;
        }
        // Trouver un élément plus petit que le pivot à droite du tableau
        while (j >= debut && comparer(pivot,array[j])) {
            j--;
        }
        // Si les indices ne se sont pas croisés, échanger les éléments
        if (i <= j) {
            swap(&array[i], &array[j]);
            i++;
            j--;
        }
    }

    // Placement du pivot à sa position finale
    swap(&array[debut], &array[j]);
    // Retourner la position du pivot
    return j;
}


// Fonction QuickSort
void quicksort(fxnCmp comparer,int array[],unsigned int size) {
    quicksortRecursive(array, 0, size - 1, comparer);
}

void quicksortRecursive(int array[], int debut, int fin, fxnCmp comparer) {
    if (debut < fin) {
        int pi = partition(array, debut, fin, comparer);
        quicksortRecursive(array, debut, pi - 1, comparer);
        quicksortRecursive(array, pi + 1, fin, comparer);
    }
}


// Fonction d'affichage d'un tableau
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

