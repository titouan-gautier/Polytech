#include <stdio.h>
#include <string.h>
#include "annuaire.h"

int main()
{
	SAnnuaire *annuaire=GenererAnnuaire();

	SaisirAnnuaire(annuaire);
	AfficheAnnuaire(annuaire);

	printf("Enregistrement du fichier\n");
	EnregistrerAnnuaire(annuaire, "annuaire.annu");

	SupprimerAnnuaire(annuaire);

	printf("Lecture du fichier\n");
	SAnnuaire *annuaireLecture=LireAnnuaire("annuaire.annu");
	AfficheAnnuaire(annuaireLecture);
	SaisirAnnuaire(annuaireLecture);
	AfficheAnnuaire(annuaireLecture);

	char str[30],end;
	int age;

	end=0;
	while (!end)
	{
		printf("Saisir un Nom à recherche ('-' pour terminer) : ");
		scanf("%s", str);
		if (strcmp(str,"-")==0) end=1;
		else
		{
			RechercheNomAnnuaire(annuaireLecture, str);
		}
	}

	end=0;
	while (!end)
	{
		printf("Saisir un Prénom à recherche ('-' pour terminer) : ");
		scanf("%s", str);
		if (strcmp(str,"-")==0) end=1;
		else
		{
			RecherchePrenomAnnuaire(annuaireLecture, str);
		}
	}

	end=0;
	while (!end)
	{
		printf("Saisir un Age à recherche ('0' pour terminer) : ");
		scanf("%d", &age);
		if (age==0) end=1;
		else
		{
			RechercheAgeAnnuaire(annuaireLecture, age);
		}
	}

	SupprimerAnnuaire(annuaireLecture);

	return 0;
}
