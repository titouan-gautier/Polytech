#ifndef TRI_H
#define TRI_H

int recursion(int *tab, int index_debut, int index_fin, int (*ordre) (int,int));
int quicksort(int *tab, int taille, int (*ordre) (int,int));
int bubblesort(int *tab, int taille, int (*ordre) (int,int));
int swap(int *tab, int index_pivot, int index_courant);

#endif