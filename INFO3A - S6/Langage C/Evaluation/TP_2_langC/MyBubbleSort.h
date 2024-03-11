#pragma once
#include <stdbool.h>
#include "myQuickSort.h"


// Définition du type de fonction de comparaison
//typedef int (*fxnCmp)(int, int);

void BubbleSort(fxnCmp comparer, int *tab, unsigned int n);
