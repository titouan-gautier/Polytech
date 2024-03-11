//
// Created by titoug on 19/02/24.
//

#include "comparator.h"

#include <stdio.h>

// Compare deux entiers et retourne 0 si a < b, 1 sinon
int sortCroissant(const int a, const int b) {
    if (a < b) {
        return 0;
    }

    return 1;
}

// Compare deux entiers et retourne 0 si a > b, 1 sinon
int sortDecroissant(const int a, const int b) {
    if (a > b) {
        return 0;
    }

    return 1;
}