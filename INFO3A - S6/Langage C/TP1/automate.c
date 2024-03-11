//
// Created by titoug on 08/02/24.
//

#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include "stack.h"
#include "automate.h"

#include <stdlib.h>

int automate(FILE *pFile) {

    enum Etats {
        SEtatDebut,
        SEtatTag,
        SEtatTagOpen,
        SEtatAttrNom,
        SEtatAttrContenuOpen,
        SEtatAttrContenu,
        SEtatTagFerme,
        SEtatErreur,
        SEtatFini
    };

    enum Etats curEtat = SEtatDebut; // Etat courant de l'automate

    Stack s;
    initStack(&s);

    char c; // caractère courant analysé
    int b = 0;
    char *nomBalise = malloc(100 * sizeof(char));
    char *erreur = malloc(100 * sizeof(char));

    while (!feof(pFile)) {
        // Récupérer un caractère
        c=fgetc(pFile);
        // Calcul des transitions

        printf("%c",c);
        switch(curEtat) {

            case SEtatDebut: // Automate dans l'état initial

                if (c == '<') {
                    curEtat = SEtatTag;
                }

                break;

            case SEtatTag:

                if (isalpha(c)) {
                    curEtat = SEtatTagOpen;
                    strncat(nomBalise,&c,1);
                } else if (c == '/') {

                    curEtat = SEtatTagFerme;
                }

                break;

            case SEtatTagOpen:

                if (isalnum(c)) {

                    strncat(nomBalise, &c,1);

                } else if (isspace(c)) {

                    curEtat = SEtatAttrNom;

                } else if (c == '>') {

                    push(&s,nomBalise);

                    free(nomBalise);
                    nomBalise = malloc(100 * sizeof(char));
                    nomBalise[0] = '\0';

                    curEtat = SEtatDebut;
                } else {
                    strcat(erreur, "SEtatTagOpen");
                    curEtat = SEtatErreur;
                }

                break;

            case SEtatAttrNom:

                if (c == '=') {
                    curEtat = SEtatAttrContenuOpen;
                } else if ((isalnum(c) || c == '-') == 0) {
                    strcat(erreur,"SEtatAttrNom");
                    curEtat = SEtatErreur;
                }

                break;

            case SEtatAttrContenuOpen:

                if (c == '"') {
                    curEtat = SEtatAttrContenu;
                } else {
                    strcat(erreur,"SEtatAttrContenuOpen");
                    curEtat = SEtatErreur;
                }
                break;

            case SEtatAttrContenu:

                if (c == '"') {
                    curEtat = SEtatTagOpen;
                } else if (c == '>') {
                    strcat(erreur,"SEtatAttrContenu");
                    curEtat = SEtatErreur;
                }
                break;

            case SEtatTagFerme:

                if (isalnum(c) || c == '-' || c == '_') {
                    strncat(nomBalise,&c,1);

                } else if (c == '>') {

                    char *nom1 = pop(&s);

                    if (strcmp(nomBalise, nom1) == 0) {
                        curEtat = SEtatDebut;
                    } else {
                        strcat(erreur, "SEtatTagFerme");
                        curEtat = SEtatErreur;
                    }

                    free(nomBalise);
                    nomBalise = malloc(100 * sizeof(char));
                    nomBalise[0] = '\0';

                    free(nom1);  // Free the popped string
                    nom1 = malloc(100 * sizeof(char));
                    nom1[0] = '\0';
                } else {
                    strcat(erreur,"SEtatTagFerme");
                    curEtat = SEtatErreur;
                }

                break;

            case SEtatErreur:
                printf("%s \n",erreur);
                return 1;
                break;
        }
    }

    printf("\n");
    printf("Automate Fini");

    return 0;
}
