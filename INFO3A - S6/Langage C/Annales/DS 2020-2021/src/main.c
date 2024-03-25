#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void conjugue(const char *verbe)
{
	int len=strlen(verbe);
	char *pronom[]={"je", "tu", "il", "nous", "vous", "ils"};
	char *term[]={"e", "es", "e", "ons", "ez", "ent"};
	if (len<3 || verbe[len-2]!='e' || verbe[len-1]!='r')
	{
		printf("'%s' n'est pas un verbe correct\n", verbe);
		return;
	}
	for (unsigned int i=0;i<6;++i)
	{
		printf("%s ",pronom[i]);
		for (unsigned int j=0;j<len-2;++j) putchar(verbe[j]);
		printf("%s\n",term[i]);
	}
}

char* concat(const char *c1, const char *c2)
{
	int limit1=strlen(c1)/2;
	int c2Len=strlen(c2);
	int limit2=c2Len/2;
	int i,ic3;

	char *c3=(char*)malloc(sizeof(limit1+(c2Len-limit2)+1));

	for (i=0, ic3=0; i<limit1; ++i, ++ic3) c3[ic3]=c1[i];
	for (i=limit2; i<c2Len; ++i, ++ic3) c3[ic3]=c2[i];
	c3[ic3]='\0';

	return(c3);
}

void trim(char *chaine)
{
	unsigned int deb=0;
	while (chaine[deb]!='\0' && (chaine[deb]==' ' || chaine[deb]=='\t' || chaine[deb]=='\n' || chaine[deb]=='\r')) ++deb;
	unsigned int fin=strlen(chaine);
	while (fin>0 && (chaine[fin-1]==' ' || chaine[fin-1]=='\t' || chaine[fin-1]=='\n' || chaine[fin-1]=='\r')) --fin;
	unsigned int i;
	for (i=0; deb<fin; ++i,++deb)
	{
		chaine[i]=chaine[deb];
	}
	chaine[i]='\0';
}

int exists(const char *str, const char *search)
{
	unsigned int iStr,iSearch,pos;
	iStr=0;
	iSearch=0;
	while (str[iStr]!='\0')
	{
		if (str[iStr]==search[iSearch])
		{
			if (iSearch==0) pos=iStr;
			iSearch++;
			if (search[iSearch]=='\0') return(pos);
		}
		else if (iSearch!=0)
		{
			iStr-=iSearch;
			iSearch=0;
		}
		iStr++;
	}
	return(-1);
}

int main()
{
	printf("-----------------------\n--- conjugue\n");
	conjugue("finir");
	conjugue("chanter");

	printf("\n-----------------------\n--- concat\n");
	char *c1=concat("jeu de vilain!", "lendemain.");
	printf("%s\n", c1);
	free(c1);

	printf("\n-----------------------\n--- trim\n");
	char ch_trim[]="  \t\r chaine de caractere   \t\n ";
	trim(ch_trim);
	printf("#%s#\n", ch_trim);

	printf("\n-----------------------\n--- exists\n");
	printf("1- %d\n", exists("Chaine dans le texte", "dans"));
	printf("2- %d\n", exists("Chaine xt dans le texte", "xte"));
	printf("3- %d\n", exists("beaucoup ppplus dur", "pplus"));
	printf("4- %d\n", exists("encore un test", "langage"));

	return(0);
}
