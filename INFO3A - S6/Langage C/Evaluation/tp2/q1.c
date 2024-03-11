#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "tri.h"
#include "tab.h"
#include "ordre.h"
#include "temps.h"

int main() {
  int taille = 30000; //on initialise la taille du tableau
  int tab[taille];  //on initialise un tableau de taille taille
  int tabtest[10] = {5,7,2,6,9,4,1,10,3,8}; //tableau test pour mieux voir si la fonction marche bien dans les cas où on a des nombres randoms très élevés

  char fonc[20][20] = {"quicksort","bubblesort"}; //on fait un tableau de chaînes de caractère de nos fonctions de tri
  int (*point_fonc[]) (int* ,int,int (int, int)) = {quicksort,bubblesort};  //on fait un tableau qui pointe vers nos fonctions, qui doivent toutes avoir le même format

  rand_tab(tab, taille);  //on initialise un tableau de valeurs au hasard, on a besoin du tableau et de sa taille
  bubblesort(tabtest, 10, croissant); //exemple d'utilisation d'une fonction de tri du tableau test, on a besoin d'un tableau, de sa taille et de l'ordre parmi les différentes fonction d'ordre
  print_tab(tabtest, 10); //on affiche le tableau

  for (int n = 0 ; n < 2; n++) {
  printf("La fonction de tri %s a mis %f ms\n", fonc[n], time_taken(tab, taille, croissant, point_fonc[n]) );
  }
  return 0; //ici on affiche le temps d'execution de chaque commande avec la fonction time_taken
}
