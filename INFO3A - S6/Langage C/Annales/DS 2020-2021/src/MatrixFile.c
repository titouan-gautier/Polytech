#include "MatrixFile.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

enum EState
{
	ESinit,
	ESnumber,
	ESfirstline,
	ESmatrix,
	ESnextline,
	ESline,
	ESprebool,
	ESbool,
	ESblanck,
	ESend
};

void InitStats(SStatResult *stats, unsigned int nbElmt)
{
	stats->nbTcol = nbElmt ? (unsigned int*)malloc(nbElmt*sizeof(unsigned int)) : NULL;
	stats->nbFcol = nbElmt ? (unsigned int*)malloc(nbElmt * sizeof(unsigned int)) : NULL;
	stats->ratioTFcol = nbElmt ? (double*)malloc(nbElmt * sizeof(double)) : NULL;
	stats->nbTlig = nbElmt ? (unsigned int*)malloc(nbElmt * sizeof(unsigned int)) : NULL;
	stats->nbFlig = nbElmt ? (unsigned int*)malloc(nbElmt * sizeof(unsigned int)) : NULL;
	stats->ratioTFlig = nbElmt ? (double*)malloc(nbElmt * sizeof(double)) : NULL;
}

void UninitStats(SStatResult* stats)
{
	if (stats)
	{
		free(stats->nbTcol);
		free(stats->nbFcol);
		free(stats->ratioTFcol);
		free(stats->nbTlig);
		free(stats->nbFlig);
		free(stats->ratioTFlig);
	}
}

SMatrixFile* MatrixFileInit(const char *file)
{
	FILE *fp;
	char c;
	
	if ((fp=fopen(file,"rt"))!=NULL)
	{
		SMatrixFile *matrixfile=NULL;

		char end=0;
		char error=0;
		enum EState state=ESinit;
		unsigned int line,col;
		while (!end && !error)
		{
			c=fgetc(fp);

			switch(state)
			{
			case ESinit:
				matrixfile=(SMatrixFile*)malloc(sizeof(SMatrixFile));
				matrixfile->file=(char*)malloc(sizeof(char)*strlen(file)+1);
				strcpy(matrixfile->file,file);
				matrixfile->size=0;
				matrixfile->matrix=NULL;
				InitStats(&matrixfile->stats,0);
				state=ESnumber;
			case ESnumber:
				if (isdigit(c)) matrixfile->size=matrixfile->size*10+(c-'0');
				else if (isblank(c)) state= ESfirstline;
				else if (c=='\n') state= ESmatrix;
				else error=1;
				break;

			case ESfirstline:
				if (c == '\n') state = ESmatrix;
				else if (!isblank(c)) error = 1;
				break;

			case ESnextline:
				if (c == '\n') state = ESline;
				else if (!isblank(c)) error = 1;
				break;

			case ESmatrix:
				matrixfile->matrix=(char*)malloc(matrixfile->size*matrixfile->size*sizeof(char));
				InitStats(&matrixfile->stats, matrixfile->size);
				state=ESline;
				line=0;
			case ESline:
				col=0;
				state=ESprebool;
			case ESprebool:
				if (isblank(c)) break;
				state=ESbool;
			case ESbool:
				if (c=='0' || c=='1')
				{
					matrixfile->matrix[col+line*matrixfile->size]=c-'0';
					col++;
					if (col<matrixfile->size) state=ESblanck;
					else
					{
						col=0;
						line++;
						if (line<matrixfile->size) state=ESnextline;
						else state=ESend;
					}
				}
				else error=1;
				break;

			case ESblanck:
				if (!isblank(c)) error=1;
				else state=ESprebool;
				break;

			case ESend:
				if (!isblank(c) && c!='\n' && c!=EOF) error=1;
			}

			if (c==EOF) end=1;
		}

		if (error || state!=ESend)
		{
			MatrixFileUninit(matrixfile);
			return(NULL);
		}
		return(matrixfile);
	}
	return(NULL);
}

void MatrixFileUninit(SMatrixFile *matrixfile)
{
	if (matrixfile)
	{
		UninitStats(&matrixfile->stats);
		free(matrixfile->file);
		free(matrixfile->matrix);
		free(matrixfile);
	}
}

char MatrixFileStatsSym(SMatrixFile* matrixfile)
{
	for (unsigned int j = 0; j < matrixfile->size; ++j)
	{
		for (unsigned int i = j + 1; i < matrixfile->size; ++i)
		{
			if (matrixfile->matrix[i + j * matrixfile->size] != matrixfile->matrix[j + i * matrixfile->size]) return(0);
		}
	}
	return(1);
}

void MatrixFileStatsTri(SMatrixFile* matrixfile)
{
	int tri;

	// Test sup
	tri = 1;
	for (unsigned int j = 0; tri && j < matrixfile->size; ++j)
	{
		for (unsigned int i = j + 1; tri && i < matrixfile->size; ++i)
		{
			if (matrixfile->matrix[j + i * matrixfile->size] != 0) tri = 0;
		}
	}
	matrixfile->stats.isTriSup = tri;

	// Test inf
	tri = 1;
	for (unsigned int j = 0; tri && j < matrixfile->size; ++j)
	{
		for (unsigned int i = j + 1; tri && i < matrixfile->size; ++i)
		{
			if (matrixfile->matrix[i + j * matrixfile->size] != 0) tri = 0;
		}
	}
	matrixfile->stats.isTriInf = tri;
}

void MatrixFileStats(SMatrixFile *matrixfile)
{
	// Global
	matrixfile->stats.nbT = 0;
	for (unsigned int i = 0; i < matrixfile->size * matrixfile->size; ++i)
	{
		if (matrixfile->matrix[i]) matrixfile->stats.nbT++;
	}
	matrixfile->stats.nbF= matrixfile->size * matrixfile->size - matrixfile->stats.nbT;
	matrixfile->stats.ratioTF = matrixfile->stats.nbT / ((double)matrixfile->size * matrixfile->size);

	// Lignes et Colonnes
	for (unsigned int j = 0; j < matrixfile->size; ++j)
	{
		matrixfile->stats.nbTlig[j] = 0;
		matrixfile->stats.nbTcol[j] = 0;
		for (unsigned int i = 0; i < matrixfile->size ; ++i)
		{
			if (matrixfile->matrix[i + j * matrixfile->size]) matrixfile->stats.nbTlig[j]++;
			if (matrixfile->matrix[j + i * matrixfile->size]) matrixfile->stats.nbTcol[j]++;
		}
		matrixfile->stats.nbFlig[j] = matrixfile->size - matrixfile->stats.nbTlig[j];
		matrixfile->stats.nbFcol[j] = matrixfile->size - matrixfile->stats.nbTcol[j];
		matrixfile->stats.ratioTFlig[j] = matrixfile->stats.nbTlig[j] / (double)matrixfile->size;
		matrixfile->stats.ratioTFcol[j] = matrixfile->stats.nbTcol[j] / (double)matrixfile->size;
	}

	// Symétrique
	matrixfile->stats.isSym = MatrixFileStatsSym(matrixfile);

	// Triangulaire
	MatrixFileStatsTri(matrixfile);
}
