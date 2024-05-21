#include "network.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

void process_token(int sockfd, struct sockaddr_in *next_addr, int current_host) {
    decision(sockfd, next_addr, current_host, "token");
}

void process_message(int sockfd, struct sockaddr_in *next_addr, int current_host, Packet *packet) {
    if (packet->destination == current_host) {
        decision(sockfd, next_addr, current_host, "message");
    } else {
        send_packet(sockfd, next_addr, packet);
    }
}

void decision(int sockfd, struct sockaddr_in *next_addr, int current_host, char *type) {
    printf("Machine %d à reçu un %s, voulez vous envoyer un message ? (y/n)\n", current_host, type);

    char send_message = getchar();
    while (getchar() != '\n');

    if (send_message == 'y') {

        printf("A quel Machine voulez vous envoyer le message ?\n");
        int destination;
        scanf("%d", &destination);

        printf("Quel message voulez vous envoyer ?\n");
        char message[MAX_MESSAGE_LENGTH];
        scanf("%s", message);

        Packet packet;
        packet.type = MESSAGE;
        packet.source = current_host;
        packet.destination = destination;
        snprintf(packet.message, MAX_MESSAGE_LENGTH, message, current_host);
        send_packet(sockfd, next_addr, &packet);
    } else {
        Packet token = { .type = TOKEN };
        send_packet(sockfd, next_addr, &token);
    }
}

void host_loop(int host_id, int local_port, int next_port) {
    int sockfd;
    struct sockaddr_in addr, next_addr;
    Packet packet;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(local_port);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("bind failed");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    memset(&next_addr, 0, sizeof(next_addr));
    next_addr.sin_family = AF_INET;
    next_addr.sin_port = htons(next_port);
    next_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (host_id == 0) {
        Packet token = { .type = TOKEN };
        send_packet(sockfd, &next_addr, &token);
    }

    while (1) {
        printf("Machine %d en attente d'un paquet...\n", host_id);
        receive_packet(sockfd, &packet);
        switch (packet.type) {
            case TOKEN:
                process_token(sockfd, &next_addr, host_id);
                break;
            case MESSAGE:
                process_message(sockfd, &next_addr, host_id, &packet);
                break;
            default:
                printf("Unknown packet type\n");
                break;
        }
    }

    close(sockfd);
}
