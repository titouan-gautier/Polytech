#include "ordre.h"


int croissant(int a, int b){
  if (a < b) {
    return 1;
  } else {
    return 0;
  }
}

int decroissant(int a, int b){
  if (a > b) {
    return 1;
  } else {
    return 0;
  }
}

int parite(int a){
  if ((a % 2) == 0) return 1;
  return 0;
}

int pair_impair(int a, int b){
  if (parite(a) == parite(b)) return (a < b);
  if ((parite(a) == 1) && (parite(b) == 0)) {
    return 1;
  } else {
    return 0;
  }
}
//pour chaque fonction, on retourne 1 si on doit échanger les valeurs