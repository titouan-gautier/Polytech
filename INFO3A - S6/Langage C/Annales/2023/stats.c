//
// Created by titoug on 18/03/24.
//

#include "stats.h"

#include <stdio.h>
#include <stdlib.h>

struct Stats {

    unsigned char *nbOccurence ;

};

Stats* CreateStats() {

    Stats *stats = malloc(sizeof(Stats));
    stats -> nbOccurence = malloc(sizeof(char) * 255);

    return stats;

}

int GetOccurence(Stats *stats, char c) {

    return stats->nbOccurence[(int)c];

}

Stats* StatistiquesFichiers(const char *nameFile) {

    FILE *pFile = fopen(nameFile,"rt");

    if (pFile == NULL) {
        fprintf(stderr, "Erreur d'ouverture du fichier\n");
        return NULL;
    }

    char c;

    Stats *stats = CreateStats();


    while (!feof(pFile)) {

        c = fgetc(pFile);

        stats -> nbOccurence[(int)c] += 1;

    }


    fclose(pFile);

    return stats;

}

