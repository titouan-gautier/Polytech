#ifndef TAB_H
#define TAB_H

int rand_tab(int *tab, int taille);
int print_tab(int *tab, int taille);
int is_sorted(int *tab, int taille, int (*ordre) (int,int));
int sort(int *tab, int taille);

#endif