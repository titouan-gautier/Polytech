//
// Created by titoug on 06/05/24.
//

#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <strings.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#define UDP_port_S 8000
#define IP_addr_S "127.0.0.1"
#define MESSAGE "message 2"

int main()
{
	int sock_C, conn_C, i;

	struct sockaddr_in sa_S;

	unsigned int taille_sa_S;

	char message[10];

	/* creation socket Client */
	sock_C = socket(PF_INET, SOCK_DGRAM, 0);
	perror("socket");

	/* @IP et n� port Serveur */
	bzero((char*) &sa_S, sizeof(sa_S));
	sa_S.sin_family      = AF_INET;
	sa_S.sin_addr.s_addr = inet_addr( IP_addr_S );
	sa_S.sin_port        = htons( UDP_port_S );

	/* emission vers le serveur (a partir du client) */
	taille_sa_S = sizeof( struct sockaddr );

	conn_C = connect(sock_C, (struct sockaddr *) &sa_S, sizeof(struct sockaddr));

	while(1) {
		bzero(message,10);

		scanf("%s %d", message, &i);

		write(conn_C,message,10);

	}
}