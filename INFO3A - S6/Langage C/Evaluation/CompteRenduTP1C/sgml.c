#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include "sgml.h"
#include "pile.h"


enum Etats{
	SEtatDebut, /*On n'est pas encore dans une tag*/
	SEtatTag, /*On est dans une tag */
	SEtatTagO, /*SEtatTagOpen*/ /*On est dans une tag ouvrante */
	SEtatTagFDeb, /* On est dans le debut d'une tag fermante (juste apres le / )*/
	SEtatTagF, /*On est dans une tag fermante */
	SEtatFin, /*La tag est termin�e */
	SEtatAttribut, /*Pour �crire le nom d'un attribut */
	SEtatVal, /*Pour �crire la valeur d'un attribut*/
	SEtatValD, /*Le debut de la valeur*/
	SEtatValF /*La fin de la valeur*/
};



int VerifImbrication(char *tg,enum ETagEtat *tgE, struct SPile *p)
{
	if(*tgE == Opening)
	{
		PilePush(p,tg);
	}
	else if(*tgE == Closing)
	{
		char *top;
		top = PileTop(p);
		PilePop(p);
		if(strcmp(top,tg) == 0)
		{
			return 0;
		}
		else
		{
			return 2;
		}
	}
	
	return 0;
}



int TagSGML(FILE *fp){
	
	char c;
	enum Etats current; /* current : Contiendra l'etat actuel de l'automate  */
	int nb = 0;
	int erreur =0; /* Prend 1 s''il y a une erreur */
	char *tag; /* Contiendra le nom de la tag actuellement parcourue */
	enum ETagEtat *tagEtat = malloc(sizeof(enum ETagEtat));  /* Indiquera dans quel type de tag on est actuellement (ouvrante/fermante/on n'est pas dans une tag) */
	struct SPile pile;

	tag = (char*) malloc(20 * sizeof(char));
	*tagEtat = NoTag;
	current = SEtatDebut;
	PileInit(&pile);
	

	while (erreur == 0 && !feof(fp))
	{
		c = fgetc(fp);

		printf("%c",c);

		switch(current)
		{
			case SEtatDebut:
				if(c == '<'){ 
					nb = 0;
					free(tag); /* On libere l'espace occup� par le nom du tag precedent */
					tag = (char*) malloc(20 * sizeof(char)); /* On alloue de l'espace pour le nom du nouveau tag */ /*On suppose que le nom est de 20 caracteres maximum */
					current = SEtatTag;
				}
				break;
			case SEtatTag:
				if(c == '/'){
					*tagEtat = Closing;
					current = SEtatTagFDeb;
				}
				else if(isalpha(c)){
					*tagEtat = Opening;
					current = SEtatTagO;
					tag[nb] = c;
					nb++;
				}
				else{
					erreur = 1;
				}
				break;
			case SEtatTagO:
				if(isalnum(c) || c == '_' || c =='-'){
					tag[nb] = c;
					nb++;
				}
				else if(c == '>'){
					current = SEtatFin;
					erreur = VerifImbrication(tag,tagEtat,&pile); /*Cette fonction va verifier si l'imbrication des tags est valide , lorsqu'il s'agit d'une tag ouvrante elle va juste empiler le nom du tag et retourner 0 */
					*tagEtat = NoTag;
					current = SEtatDebut; /* Il faut prevoir le cas o� deux balises sont consecutives <B><C> */
				}
				else if(c == ' '){
					current = SEtatAttribut;
				}
				else{
					erreur = 1;
				}
				break;
			case SEtatTagFDeb:
				if(isalpha(c)){
					current = SEtatTagF;
					tag[nb] = c;
					nb++;
				}
				else{
					erreur = 1;
				}
				break;
			case SEtatTagF:
				if(isalnum(c) || c == '_' || c =='-'){
					tag[nb] = c;
					nb++;
				}
				else if(c == '>'){
					current = SEtatFin;
					erreur = VerifImbrication(tag,tagEtat,&pile); /*Cette fonction va verifier si l'imbrication des tags est valide et retourne 0 si correcte et 2 sinon */
					*tagEtat = NoTag;
					current = SEtatDebut; /* Il faut prevoir le cas o� deux balises sont consecutives <B><C> */
				}
				else{
					erreur = 1;
				}
				break;
			case SEtatAttribut:
				if(!isalnum(c) && c != '_' && c !='-' && c!= '='){
					erreur = 1;
				}
				else if(c == '='){
					current = SEtatValD;
				}
				break;
			case SEtatValD:
				if(c == '\"' || c == '\'' || isalpha(c)){
					current = SEtatVal;
				}
				else{
					erreur = 1;
				}
				break;
			case SEtatVal:
				if(!isalnum(c) && c != '_' && c !='-' && c != '\"' && c != '\'' && c != ' '){
					erreur = 1;
				}
				else if (c == '\"' || c == '\'' || c == ' '){
					current = SEtatValF;
				}
				break;
			case SEtatValF:
				if(c == ' '){
					current = SEtatAttribut;
				}
				else if(c == '>'){
					current = SEtatFin;
				}
				else{
					erreur = 1;
				}
				break;

			default:
				break;
				
		}

	}
	free(tag);
	free(tagEtat);

	/* Il faut tester aussi si taille de la pile est = 0 � la fin du fichier (toute balise ouvrante est ferm�e)*/
	if(PileSize(&pile) != 0){
		erreur = 2;
	}

	return erreur;
	
}




int main()
{
	int res;
	FILE *pFile;
	
	if(pFile=fopen("./fichier.html","rt")){

		res = TagSGML(pFile);  /*retourne 0 si valide / 1 si erreur lexicale / 2 si erreur d'imbrication */

		fclose (pFile);

		if (res==0)
		{
			printf("Fichier HTML valide");
		}
		else if (res == 1)
		{
			printf("Fichier HTML invalide , erreur lexicale");
		}
		else if (res == 2)
		{
			printf("Fichier HTML invalide , erreur d'imbrication");
		}
	}
	else printf("erreur d'ouverture du fichier\n");

	return 0;
}
/*S'il y a une faute elle provient probablement de la partie de traitement des attributs des balises */
