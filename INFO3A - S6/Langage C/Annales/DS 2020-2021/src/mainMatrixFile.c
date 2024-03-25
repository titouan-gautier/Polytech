#include "MatrixFile.h"
#include <stdio.h>

int main()
{
	SMatrixFile *matrixfile=MatrixFileInit("links.txt");
	if (matrixfile)
	{
		MatrixFileStats(matrixfile);
		printf("Nb vrai : %d\n", matrixfile->stats.nbT);
		printf("Nb faux : %d\n", matrixfile->stats.nbF);
		printf("Ratio T/F : %f\n", matrixfile->stats.ratioTF);

		printf("Nb vrai / ligne :\n\t");
		for (unsigned int i = 0; i < matrixfile->size; ++i) printf("%d ", matrixfile->stats.nbTlig[i]);
		printf("\n");
		printf("Nb faux / ligne :\n\t");
		for (unsigned int i = 0; i < matrixfile->size; ++i) printf("%d ", matrixfile->stats.nbFlig[i]);
		printf("\n");
		printf("Ratio T/F / ligne :\n\t");
		for (unsigned int i = 0; i < matrixfile->size; ++i) printf("%f ", matrixfile->stats.ratioTFlig[i]);
		printf("\n");

		printf("Nb vrai / colonne :\n\t");
		for (unsigned int i = 0; i < matrixfile->size; ++i) printf("%d ", matrixfile->stats.nbTcol[i]);
		printf("\n");
		printf("Nb faux / colonne :\n\t");
		for (unsigned int i = 0; i < matrixfile->size; ++i) printf("%d ", matrixfile->stats.nbFcol[i]);
		printf("\n");
		printf("Ratio T/F / colonne :\n\t");
		for (unsigned int i = 0; i < matrixfile->size; ++i) printf("%f ", matrixfile->stats.ratioTFcol[i]);
		printf("\n");

		printf("La matrice ");
		if (matrixfile->stats.isSym) printf("est");
		else printf("n'est pas");
		printf(" symetrique\n");

		printf("La matrice ");
		if (matrixfile->stats.isTriInf) printf("est");
		else printf("n'est pas");
		printf(" triangulaire inferieure\n");

		printf("La matrice ");
		if (matrixfile->stats.isTriSup) printf("est");
		else printf("n'est pas");
		printf(" triangulaire superieure\n");

		MatrixFileUninit(matrixfile);
	}
	else printf("Le fichier n'a pas pu etre analyse\n");

	return 0;
}
