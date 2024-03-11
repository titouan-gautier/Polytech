//
// Created by titoug on 14/02/24.
//

#ifndef SORT_H
#define SORT_H

// Definition d'un type de fonction pour réaliser un tableau de pointeurs de fonctions
typedef void (*sortFunction)(int tab[],int (*comparator)(int,int), int low, int high);

void quicksort(int tab[],int (*comparator)(int,int), int low, int high);
int partition(int tab[], int (*comparator)(int,int), int low, int high);

void tri_a_bulles(int tab[],int (*comparator)(int,int), int low, int high);

#endif //SORT_H
