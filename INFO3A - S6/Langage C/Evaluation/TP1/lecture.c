#include <stdio.h>

int main()
{
    FILE *file;
    char c;
    if (file=fopen("fichier.html","rt"))
    {
        for (c=fgetc(file) ; !feof(file) ; c=fgetc(file))
        {
            printf("%c", c);
        }
        printf("\n");
        fclose(file);

    }
    else printf("prblm dou'verture du fichier\n");
    return 0;
}