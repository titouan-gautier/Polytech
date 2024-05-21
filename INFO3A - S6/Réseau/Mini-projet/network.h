#ifndef NETWORK_H
#define NETWORK_H

#include <netinet/in.h>

#define MAX_MESSAGE_LENGTH 256

typedef enum { TOKEN, MESSAGE } PacketType;

typedef struct {
    PacketType type;
    int source;
    int destination;
    char message[MAX_MESSAGE_LENGTH];
} Packet;

void send_packet(int sockfd, struct sockaddr_in *addr, Packet *packet);
void receive_packet(int sockfd, Packet *packet);
void process_token(int sockfd, struct sockaddr_in *next_addr, int current_host);
void process_message(int sockfd, struct sockaddr_in *next_addr, int current_host, Packet *packet);
void host_loop(int host_id, int local_port, int next_port);
void decision(int sockfd, struct sockaddr_in *next_addr, int current_host, char *type);

#endif // NETWORK_H
