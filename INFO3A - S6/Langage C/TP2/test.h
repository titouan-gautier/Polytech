//
// Created by titoug on 14/02/24.
//

#ifndef TEST_H
#define TEST_H
#include "sort.h"

int randMinMax(int min, int max);

int createTableau(int tab[], int len, int min, int max);

int testTableauCroissant(int t[], int len);

int testTableauDecroissant(int t[], int len);

void printTableau(int t[], int len);

void testPerfSort(sortFunction sort[], int (*comparator)(int,int), const int low, const int high);

#endif //TEST_H
