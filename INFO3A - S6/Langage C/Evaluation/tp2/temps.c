#include <stdlib.h>
#include <time.h>
#include "temps.h"


double time_taken(int *tab, int taille, int (*ordre) (int,int), int (*fonction) (int* ,int,int (int, int))) {   //on prend un tableau, sa taille, une fonction d'ordre et une fonction de tri
  double time;
  clock_t begin = clock();  //temps avant tri

  fonction(tab, taille, ordre); //on effectue le tri

  clock_t end = clock();    //temps après tri
  time = ((end - begin)*1000) / CLOCKS_PER_SEC;
  return time;  //on retourne le temps en milliseconde
}