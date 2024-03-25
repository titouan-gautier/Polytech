#pragma once
#define _CRT_SECURE_NO_WARNINGS

typedef struct
{
	unsigned int nbT;
	unsigned int nbF;
	double ratioTF;
	unsigned int *nbTcol;
	unsigned int *nbFcol;
	double *ratioTFcol;
	unsigned int *nbTlig;
	unsigned int *nbFlig;
	double *ratioTFlig;
	char isSym;
	char isTriSup;
	char isTriInf;
} SStatResult;

typedef struct
{
	char *file;
	unsigned int size;
	char *matrix;
	SStatResult stats;
} SMatrixFile;

SMatrixFile* MatrixFileInit(const char *file);
void MatrixFileUninit(SMatrixFile *matrixfile);
void MatrixFileStats(SMatrixFile *matrixfile);
