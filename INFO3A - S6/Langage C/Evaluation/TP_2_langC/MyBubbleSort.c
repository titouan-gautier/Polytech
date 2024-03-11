#include "MyBubbleSort.h"

void SwapBubble(int *tab, int i1, int i2)
{
	int temp=tab[i1];
	tab[i1]=tab[i2];
	tab[i2]=temp;
}
  
void BubbleSort(fxnCmp comparer, int *tab, unsigned int n)
{
	unsigned int i, j;

	for (i=0; i<n-1; ++i){

		for (j=0; j<n-i-1; j++){

			if (!comparer(tab[j],tab[j+1]))
			{

				SwapBubble(tab, j, j+1);
			}
		}
	}
}
