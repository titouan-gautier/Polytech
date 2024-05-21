#include "network.h"
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

void send_packet(int sockfd, struct sockaddr_in *addr, Packet *packet) {
    sendto(sockfd, packet, sizeof(Packet), 0, (struct sockaddr *)addr, sizeof(*addr));
}

void receive_packet(int sockfd, Packet *packet) {
    recvfrom(sockfd, packet, sizeof(Packet), 0, NULL, NULL);
}
