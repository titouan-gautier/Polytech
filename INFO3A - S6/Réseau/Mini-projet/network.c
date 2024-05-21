#include "network.h"
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdio.h>

void send_packet(int sockfd, struct sockaddr_in *addr, Packet *packet) {
    sendto(sockfd, packet, sizeof(Packet), 0, (struct sockaddr *)addr, sizeof(*addr));
    printf("Paquet envoyé: type=%d, source=%d, destination=%d, message=%s\n", packet->type, packet->source, packet->destination, packet->message);
	printf("\n");
}

void receive_packet(int sockfd, Packet *packet) {
    recvfrom(sockfd, packet, sizeof(Packet), 0, NULL, NULL);
    printf("Paquet reçu: type=%d, source=%d, destination=%d, message=%s\n", packet->type, packet->source, packet->destination, packet->message);
	printf("\n");
}
