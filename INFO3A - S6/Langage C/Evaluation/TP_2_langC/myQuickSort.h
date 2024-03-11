#ifndef QUICKSORT_H
#define QUICKSORT_H
#include <stdbool.h>


// Définition du type de fonction de comparaison
typedef bool (*fxnCmp)(int, int);

bool estSup(int a, int b);
bool estInf(int a, int b);
bool estPaire(int a, int b) ;
bool estImpaire(int a, int b);


//void MyQuickSort(int (*fnCmp)(int,int), int *tab, unsigned int size);


// Fonction d'affichage d'un tableau
void printArray(int array[], int size);

int partition(int array[], int debut, int fin, fxnCmp comparer);

// Fonction QuickSort
void quicksort(fxnCmp comparer,int array[],unsigned int size);
void quicksortRecursive(int array[], int debut, int fin, fxnCmp comparer);

#endif