#include "annuaire.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//---------------------
// Question 1
typedef struct
{
	char Nom[30];
	char Prenom[30];
	unsigned int Age;
	unsigned int AnneeInscription;
} SEtudiant;

//---------------------
// Question 9 - part 1
typedef struct
{
	SEtudiant **Tab;
	int (*fnCmp)(const void*, const void*);
} SIndex;

int CmpNom(const void *v1, const void *v2);
int CmpPrenom(const void *v1, const void *v2);
int CmpAge(const void *v1, const void *v2);

void IndexerAnnuaire(SAnnuaire *annuaire);

//---------------------
// Question 2
struct SAnnuaire
{
	SEtudiant *Etudiants;
	unsigned int NbEtudiants;

	//---------------------
	// Question 9 - part 2
	SIndex Idx[3]; // 0: Nom ; 1: Prenom ; 2: Age
};

//---------------------
// Question 3
SAnnuaire* GenererAnnuaire()
{
	SAnnuaire *annuaire=(SAnnuaire*)malloc(sizeof(SAnnuaire));

	annuaire->Etudiants=NULL;
	annuaire->NbEtudiants=0;

	//---------------------
	// Question 9 - part 3
	for (unsigned int i=0; i<3; ++i) annuaire->Idx[i].Tab=NULL;
	annuaire->Idx[0].fnCmp=CmpNom;
	annuaire->Idx[1].fnCmp=CmpPrenom;
	annuaire->Idx[2].fnCmp=CmpAge;

	return(annuaire);
}

//---------------------
// Question 4
void SupprimerAnnuaire(SAnnuaire *annuaire)
{
	free(annuaire->Etudiants);

	//---------------------
	// Question 9 - part 4
	for (unsigned int i=0; i<3; ++i) free(annuaire->Idx[i].Tab);

	free(annuaire);
}

//---------------------
// Question 5
void SaisirAnnuaire(SAnnuaire *annuaire)
{
	char end=0;
	unsigned int oldNbEtudiants=annuaire->NbEtudiants;

	SEtudiant etudiant;
	while(!end)
	{
		printf("Saisissez le nom d'un étudiant ou '-' pour terminer : ");
		scanf("%s", etudiant.Nom);
		if (strcmp(etudiant.Nom, "-")==0) end=1;
		else
		{
			printf("Saisissez le prenom de l'étudiant : ");
			scanf("%s", etudiant.Prenom);
			printf("Saisissez l'âge de l'étudiant : ");
			scanf("%u", &etudiant.Age);
			printf("Saisissez l'année d'inscription de l'étudiant : ");
			scanf("%u", &etudiant.AnneeInscription);

			annuaire->NbEtudiants++;
			annuaire->Etudiants=(SEtudiant*)realloc(annuaire->Etudiants, annuaire->NbEtudiants*sizeof(SEtudiant));

			annuaire->Etudiants[annuaire->NbEtudiants-1]=etudiant;
			printf("Etudiant enregistré\n\n");
		}
	}

	//---------------------
	// Question 9 - part 5
	if (oldNbEtudiants!=annuaire->NbEtudiants) IndexerAnnuaire(annuaire);
}

//---------------------
// Question 6
void AfficherEtudiant(SEtudiant *etudiant)
{
	printf("%s %s ; %u ans ; inscrit en %uA\n", etudiant->Nom, etudiant->Prenom, etudiant->Age, etudiant->AnneeInscription);
}

void AfficheAnnuaire(SAnnuaire *annuaire)
{
	printf("Liste des étudiants présents dans l'annuaire :\n");
	for (unsigned int i=0; i<annuaire->NbEtudiants; ++i)
	{
		SEtudiant *etudiant=&annuaire->Etudiants[i];
		printf("%u : ", i+1);
		AfficherEtudiant(etudiant);
	}
	printf("\n");
}

//---------------------
// Question 7
void EnregistrerAnnuaire(SAnnuaire *annuaire, const char *fichier)
{
	FILE *fp;
	if ((fp=fopen(fichier, "w"))==NULL)
	{
		printf("Erreur d'ouverture du fichier \"%s\"\n", fichier);
		return;
	}

	fprintf(fp, "%u\n", annuaire->NbEtudiants);
	for (unsigned int i=0; i<annuaire->NbEtudiants; ++i)
	{
		SEtudiant *etudiant=&annuaire->Etudiants[i];
		fprintf(fp,"%s|%s|%u|%u\n", etudiant->Nom, etudiant->Prenom, etudiant->Age, etudiant->AnneeInscription);
	}

	fclose(fp);
}

//---------------------
// Question 8
SAnnuaire* LireAnnuaire(const char *fichier)
{
	SAnnuaire *annuaire=NULL;

	FILE *fp;
	if ((fp=fopen(fichier, "r"))!=NULL)
	{
		unsigned int nb;
		if (fscanf(fp, "%u\n", &nb)==1)
		{
			annuaire=GenererAnnuaire();
			annuaire->Etudiants=(SEtudiant*)realloc(annuaire->Etudiants, nb*sizeof(SEtudiant));

			SEtudiant etudiant;
			while ((annuaire->NbEtudiants<nb) && !feof(fp))
			{
				char c;
				unsigned int i;

				i=0;
				while ((c=fgetc(fp))!='|') etudiant.Nom[i++]=c;
				etudiant.Nom[i]='\0';

				i=0;
				while ((c=fgetc(fp))!='|') etudiant.Prenom[i++]=c;
				etudiant.Prenom[i]='\0';

				fscanf(fp, "%u|%u\n", &etudiant.Age, &etudiant.AnneeInscription);

				annuaire->Etudiants[annuaire->NbEtudiants]=etudiant;
				annuaire->NbEtudiants++;
			}
			fclose(fp);

			//---------------------
			// Question 9 - part 6
			IndexerAnnuaire(annuaire);
		}
	}
	else
	{
		printf("Erreur d'ouverture du fichier \"%s\"\n", fichier);
	}

	return(annuaire);
}

//---------------------
// Question 9 - part 7
int CmpNom(const void *v1, const void *v2)
{
	SEtudiant *e1=*(SEtudiant**)v1;
	SEtudiant *e2=*(SEtudiant**)v2;
	return(strcmp(e1->Nom, e2->Nom));
}

int CmpPrenom(const void *v1, const void *v2)
{
	SEtudiant *e1=*(SEtudiant**)v1;
	SEtudiant *e2=*(SEtudiant**)v2;
	return(strcmp(e1->Prenom, e2->Prenom));
}

int CmpAge(const void *v1, const void *v2)
{
	SEtudiant *e1=*(SEtudiant**)v1;
	SEtudiant *e2=*(SEtudiant**)v2;
	return(e1->Age-e2->Age);
}

void PrintIndexAnnuaire(SAnnuaire *annuaire)
{
	for (unsigned int idx=0; idx<3; ++idx)
	{
		printf("Liste des étudiants Idx[%u] :\n", idx);
		for (unsigned int i=0; i<annuaire->NbEtudiants; ++i)
		{
			SEtudiant *etudiant=annuaire->Idx[idx].Tab[i];
			printf("%u : ", i+1);
			AfficherEtudiant(etudiant);
		}
		printf("\n");
	}
}

void IndexerAnnuaire(SAnnuaire *annuaire)
{
	for (unsigned int i=0; i<3; ++i)
	{
		free(annuaire->Idx[i].Tab);
		annuaire->Idx[i].Tab=(SEtudiant**)malloc(annuaire->NbEtudiants*sizeof(SEtudiant*));
		for (unsigned int n=0; n<annuaire->NbEtudiants; ++n) annuaire->Idx[i].Tab[n]=&annuaire->Etudiants[n];
		qsort(annuaire->Idx[i].Tab, annuaire->NbEtudiants, sizeof(SEtudiant**), annuaire->Idx[i].fnCmp);
	}

	//PrintIndexAnnuaire(annuaire);
}

//---------------------
// Question 10
int RechercheIndexAnnuaireRec(SEtudiant **idx, int deb, int fin, const void *val, int (*cmp)(const void *, const void *))
{
	if (fin<=deb) return(deb);
	int i=(fin+deb)/2;
	int res=cmp(val, &idx[i]);
	if (res==0) return(i);
	if (res<1) return(RechercheIndexAnnuaireRec(idx, deb, i-1, val, cmp));
	return(RechercheIndexAnnuaireRec(idx, i+1, fin, val, cmp));
}

void RechercheIndexAnnuaire(SAnnuaire *annuaire, unsigned int idx, SEtudiant *etudiant)
{
	printf("Résultat de la recherche :\n");

	int (*cmp)(const void *, const void *)=annuaire->Idx[idx].fnCmp;
	int i=RechercheIndexAnnuaireRec(annuaire->Idx[idx].Tab, 0, annuaire->NbEtudiants-1, &etudiant, cmp);
	if (cmp(&etudiant, &annuaire->Idx[idx].Tab[i])!=0) printf("Aucun étudiant trouvé\n");
	else
	{
		i--;
		while ((i>=0) && (cmp(&etudiant, &annuaire->Idx[idx].Tab[i])==0)) i--;
		while (cmp(&etudiant, &annuaire->Idx[idx].Tab[++i])==0) AfficherEtudiant(annuaire->Idx[idx].Tab[i]);
	}

	printf("\n");
}

void RechercheNomAnnuaire(SAnnuaire *annuaire, const char *nom)
{
	SEtudiant etudiant;
	strcpy(etudiant.Nom, nom);

	RechercheIndexAnnuaire(annuaire, 0, &etudiant);
}

void RecherchePrenomAnnuaire(SAnnuaire *annuaire, const char *prenom)
{
	SEtudiant etudiant;
	strcpy(etudiant.Prenom, prenom);

	RechercheIndexAnnuaire(annuaire, 1, &etudiant);
}

void RechercheAgeAnnuaire(SAnnuaire *annuaire, unsigned int age)
{
	SEtudiant etudiant;
	etudiant.Age=age;

	RechercheIndexAnnuaire(annuaire, 2, &etudiant);
}


