#include <stdio.h>
#include "automate.h"

int main() {

    FILE *pFile = fopen("fichier.html","rt");

    if (pFile == NULL) {
        fprintf(stderr, "Erreur d'ouverture du fichier\n");
        return 1; // Quitte le programme avec un code d'erreur
    }

    automate(pFile);

    return 0;
}
