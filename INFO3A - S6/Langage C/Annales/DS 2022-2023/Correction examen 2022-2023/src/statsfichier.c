#include "statsfichier.h"
#include <stdio.h>

struct SStat StatistiqueFichier(const char* path)
{
	FILE* fp;
	struct SStat stats;

	for (unsigned int i = 0; i < 256; ++i) stats.Stat[i] = 0;

	if ((fp = fopen(path, "r")) != NULL)
	{
		int c;
		while ((c = fgetc(fp)) && !feof(fp))
		{
			stats.Stat[c]++;
		}
		fclose(fp);
	}

	return(stats);
}
