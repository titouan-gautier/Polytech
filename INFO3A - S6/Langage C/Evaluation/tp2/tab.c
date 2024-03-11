#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "tab.h"


int rand_tab(int *tab, int taille) { //on initialise chaque case du tableau par une valeur aléatoire
  srand( time( NULL ) );
  for(int i=0; i < taille; i++) {
    tab[i]=rand();
  }
  return 0;
}

int print_tab(int *tab, int taille) { //on affiche chaque case du tableau avec sa valeur
  for(int i=0; i < taille; i++) {
    printf("[%d] = %d\n", i, tab[i]);
  }
  return 0;
}

int is_sorted(int *tab, int taille, int (*ordre) (int,int)) { //on vérifie que le tableau est bien trié selon l'ordre qu'on a défini
  for(int i=0; i < taille-1; i++) {
    if (ordre(tab[i+1], tab[i]) == 1) {
      printf("Tableau non trié\n");
      return 0;
    }
  }
  printf("Tableau trié\n");
  return 0;
}

int sort(int *tab, int taille) {
  return 0;
}
