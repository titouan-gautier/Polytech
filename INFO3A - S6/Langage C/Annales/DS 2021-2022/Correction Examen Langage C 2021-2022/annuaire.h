#pragma once

typedef struct SAnnuaire SAnnuaire;

SAnnuaire* GenererAnnuaire();
void SupprimerAnnuaire(SAnnuaire *annuaire);

void SaisirAnnuaire(SAnnuaire *annuaire);
void AfficheAnnuaire(SAnnuaire *annuaire);

void EnregistrerAnnuaire(SAnnuaire *annuaire, const char *fichier);
SAnnuaire* LireAnnuaire(const char *fichier);

void RechercheNomAnnuaire(SAnnuaire *annuaire, const char *nom);
void RecherchePrenomAnnuaire(SAnnuaire *annuaire, const char *prenom);
void RechercheAgeAnnuaire(SAnnuaire *annuaire, unsigned int age);
