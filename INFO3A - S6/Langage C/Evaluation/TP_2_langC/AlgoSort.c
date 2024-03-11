#include "AlgoSort.h"
#include "myQuickSort.h"
//#include "MyBubbleSort.h"
#include <stdlib.h>

#define ALGO(nom) {#nom, nom},
#define ALGOTERM() {NULL, NULL},

struct SAlgo Algos[]={
	ALGO(BubbleSort)
	ALGO(quicksort)
	ALGOTERM()
	};
