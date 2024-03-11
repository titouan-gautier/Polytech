//
// Created by titoug on 14/02/24.
//

#include "sort.h"
#include <string.h>
#include <stdio.h>

// Echange deux entiers en place
void swap(int *a, int *b) {
    const int t = *a;
    *a = *b;
    *b = t;
}


//Partitionne le tableau en deux parties triées par rapport à un pivot
int partition(int tab[], int (*comparator)(int,int), const int low, const int high) {
    const int pivot = tab[high];

    int i = (low - 1);

    for (int j = low; j < high; j++) {

        if (comparator(tab[j],pivot) == 0) {
            i++;
            swap(&tab[i], &tab[j]);
        }

    }

    swap(&tab[i + 1], &tab[high]);

    return (i + 1);
}

// Tri rapide, tri le tableau en utilisant la fonction partition
void quicksort(int tab[],int (*comparator)(int,int), const int low, const int high) {

    if (low < high) {

        const int pivot = partition(tab, comparator, low, high);

        quicksort(tab, comparator, low, pivot - 1);

        quicksort(tab, comparator, pivot + 1, high);
    }

}

// Tri à bulles
void tri_a_bulles(int tab[],int (*comparator)(int,int), const int low, const int high) {

    for (int i = 0; i < high; i++) {
        for (int j = 0; j < i - 1; j++) {
            if (comparator(tab[j+1],tab[j]) == 0 ) {

                swap(&tab[j+1],&tab[j]);

            }
        }
    }

}
