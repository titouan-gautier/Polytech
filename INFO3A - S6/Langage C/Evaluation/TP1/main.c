#include <stdio.h>
#include <string.h>
#include "automate.h"

#define L 20

int main()
{
    char balise[L + 1];
    FILE *file;
    int  OuvertFerme;
    enum Etats_automate etat;
    char pile[L][L+1];
    int pile_long = 0;

    if (file=fopen("fichier.html","rt"))
    {
        while((etat = automate(file, balise, &OuvertFerme)) == ESOK)
        {
            if (!OuvertFerme)
            {
                strcpy(pile[pile_long], balise);
                pile_long++;

            }
            else
            {
                if (!strcmp(balise, pile[pile_long - 1])) pile_long--;
                else{
                    break;
                    
                }
            }
        }

        if (etat == ESOK) printf("balise fermante %s identifiée n'est pas associée à la dernière vue : %s\n", balise, pile[pile_long-1]);
        else if (etat == ESEND)
        {
            if (pile_long == 0){
                printf("Enchainement des balises respecté\n");
            }
            else printf("Balise fermante %s manquante\n", pile[pile_long - 1]);
        }
        else printf("Erreur code ou html, bon courage\n");
        fclose(file);

    }
    else printf("Fichier non ouvert\n");
    return 0;
}