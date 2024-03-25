#pragma once

struct SNoeud;

struct SNoeud* CreerFeuille(unsigned char lettre, unsigned int valeur);
struct SNoeud* AssocierNoeud(struct SNoeud* filsG, struct SNoeud* filsD);
int EtapeGlouton(struct SNoeud** tab, unsigned int nb);
struct SNoeud* CreerForet(struct SNoeud** tab, unsigned int nb);
void AfficherNoeud(struct SNoeud* n);
void LibererNoeud(struct SNoeud* n);
