#include <ctype.h>
#include <string.h>
#include "automate.h"


enum Etats_automate automate(FILE *file, char *balise, int *OuvertFerme)
{
	enum Etats
	{
		SDebut0,
		SFindBra1,
		SSlash10,
		SBaliseFermante11,
		SBaliseOuvrante2,
		SSpace4,
		Sarg5,
		Segal6,
		SQuoteOpen9,
		SQuoteClose8,
		SDQuoteOpen7,
		SDQoteClose8,
		Svalue70,
		SFindKet3,
		SError
	};

	enum Etats curEtat = SDebut0;  //Etat courant de l'automate
	char c; //caractère courant analysé

//jcomprends pas l'erreur pourtant j'me suis bien fait aidé.

	curEtat = SDebut0;
	balise[0] = '\0';

	while (curEtat != SFindKet3)
	{
		c=fgetc(file); // Récupérer un caractère
		switch(curEtat) // Calcul des transitions
		{
			case SDebut0: //Automate dans l'état initial
				if (c == '<') curEtat = SFindBra1; //Première transition
				break;

			case SFindBra1: //Automate dans l'état Bra trouvé
				if (c=='/') curEtat = SSlash10;
				else if  (isalpha(c))
				{
					curEtat = SBaliseOuvrante2;
					strncat(balise, &c, 1);
				}
				else curEtat = SError;
				break;

			case SSlash10:
				strncat(balise, &c,1);
				if (isalpha(c)) curEtat = SBaliseFermante11;
                else curEtat = SError;
                break;
				
			case SBaliseFermante11:
				if (c == '>') curEtat = SFindKet3;
                else if (!(isalnum(c) || c == '-')) curEtat = SError;
                else strncat(balise, &c, 1);
                break;
			
			case SBaliseOuvrante2:
				if (c == '>') curEtat = SFindKet3;
				else if (!(isalnum(c) || c == '-')) curEtat = SError;
                else if (c == ' ') curEtat = SSpace4;

                else strncat(balise, &c, 1);
                break;

			case SSpace4:
				if (c == '>') curEtat = SFindKet3;
                else if (isalpha(c)) curEtat = Sarg5;
                else if(c != ' ') curEtat = SError;
                break;

			case Sarg5:
				if (c == '=') curEtat = Segal6;
                else if (!(isalnum(c) || c == '-')) curEtat = Sarg5;
                break;

			case Segal6:
				if (c == '"') curEtat = SDQuoteOpen7;
                else if (c == '\'') curEtat = SQuoteOpen9;
                else if (isalnum(c)) curEtat = Svalue70;
                else curEtat = SError;
                break;
			
			case SDQuoteOpen7:
				if (c == '"') curEtat = SDQoteClose8;
                break;
			
			case SQuoteOpen9:
				if (c == '\'') curEtat = SDQoteClose8;
                break;
			
			case SDQoteClose8:
				if (c == '>') curEtat = SFindKet3;
                else if (c == ' ') curEtat = SSpace4;
                else curEtat = SError;
                break;

			case Svalue70:
				if (c == '>') curEtat = SFindKet3;
                else if (c == ' ') curEtat = SSpace4;
                else if (!(isalnum(c) || c == '-')) curEtat = SError;
                break;
			
		}
	}
	if (curEtat == SFindKet3){
        *OuvertFerme = 0;
        return ESOK;
    }else if (curEtat == SFindKet3){
        *OuvertFerme = 1;
        return ESOK;
    }else if(feof(file)) return ESEND;
    else return ESKO;
}