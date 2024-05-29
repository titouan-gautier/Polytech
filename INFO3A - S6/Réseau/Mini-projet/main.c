#include "network.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <host_id> <local_port> <next_port>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int host_id = atoi(argv[1]);
    int local_port = atoi(argv[2]);
    int next_port = atoi(argv[3]);
    int nb_machine = atoi(argv[4]);


    printf("Démarrage de la machine %d sur le port %d\n", host_id, local_port);
    srand(getpid());
    host_loop(host_id, local_port, next_port,nb_machine);

    return 0;
}
