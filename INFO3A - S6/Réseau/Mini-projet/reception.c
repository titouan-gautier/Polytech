//
// Created by titoug on 17/05/24.
//

#include "network.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int priseReception(int port) {
    int			sock;
    struct sockaddr_in	address;

    if ((sock = socket (PF_INET, SOCK_DGRAM, 0)) == -1) {
        perror ("creerPriseReception");
        exit (1);
    }

    memset (&address, 0, sizeof (address));
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons (port);

    if (bind (sock,
          (struct sockaddr*) &address,
          sizeof (address)) == -1)
    {
        perror ("creerPriseReception");
        exit (1);
    }

    return sock;
}
