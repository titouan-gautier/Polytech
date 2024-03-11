#include "tri.h"


int swap(int *tab, int index_pivot, int index_courant) {  //on prend un tableau et deux index
  for (int i = index_courant ; i > index_pivot; i--) {    //s'ils sont succesifs : échange les deux valeurs
    int temp = tab[i-1];                                  //s'ils ne le sont pas : décale les valeurs pour que l'index courant se retrouve juste avant l'index_pivot
    tab[i-1] = tab[i];
    tab[i] = temp;
  }
  return 0;
}

int recursion(int *tab, int index_debut, int index_fin, int (*ordre) (int,int)) { //la fonction récursive de notre quicksort qui prend un tableau, deux index et une fonction d'ordre
  if ((index_debut != index_fin) && (index_debut < index_fin)) {  //condition d'arrêt : les deux index se croisent
    int pivot = tab[index_debut];
    int index_pivot = index_debut;
    for (int i = index_debut + 1 ; i < index_fin+1; i++) {  //on boucle pour placer toutes les valeurs inférieures au pivot avant celui dans le tableau
      if (ordre(tab[i], pivot) == 1) {
        swap(tab, index_pivot, i);
        index_pivot ++;
      }
    }
    recursion(tab, index_debut, index_pivot, ordre);  //on refait la même chose sur la partie avant et après le pivot
    recursion(tab, index_pivot+1, index_fin, ordre);
  }
  return 0;
}

int quicksort(int *tab, int taille, int (*ordre) (int,int)) { //on prend en entrée un tableau, sa taille et une fonction d'ordre et on exécute la récursion du premier au dernier élément du tableau
  recursion(tab, 0, taille -1, ordre);
  return 0;
}

int bubblesort(int *tab, int taille, int (*ordre) (int,int)) {
  for (int i = 0 ; i < taille; i++) {
    for (int j = 0 ; j < taille - i - 1; j++) { //on boucle pour comparer chaque éléments
      if (ordre(tab[j+1], tab[j]) == 1) { //on échange selon l'ordre choisi
        swap(tab, j, j+1);
      }
    }
  }
  return 0;
}