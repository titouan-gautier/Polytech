#include "client.c"
#include <stdio.h>

int main(int argc, char * argv[])
{

    printf("%s \n", "Start");

    char *ip = "127.0.0.1";

    printf("%i %i %s %i \n", atoi(argv[1]), atoi(argv[2]), ip, atoi(argv[3]));

    createSocket(atoi(argv[1]), atoi(argv[2]), ip, atoi(argv[3]));

    return 0;
}

