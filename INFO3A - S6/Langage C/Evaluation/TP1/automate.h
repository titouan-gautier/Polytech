#pragma once
#include <stdio.h>

enum Etats_automate
{
    ESKO,
    ESOK,
    ESEND,
};
enum Etats_automate automate(FILE *pf, char *balise, int *OuvertFerme);
