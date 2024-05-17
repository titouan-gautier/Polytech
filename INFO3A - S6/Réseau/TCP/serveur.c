/* Socket - Serveur - Mode Datagramme */

#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <strings.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#define UDP_port_S 8000
#define BACKLOG 5



int main() {

	int sock_S, conn_S;
	
	char message[10];
	struct sockaddr_in sa_S, sa_C;

	unsigned int taille_sa_C;
	
	/* creation socket Serveur*/
	sock_S = socket(PF_INET, SOCK_DGRAM, 0);
	perror("socket ");
	
	/* @IP et n° port Serveur */
	bzero((char*) &sa_S, sizeof(struct sockaddr));
	sa_S.sin_family      = AF_INET;
	sa_S.sin_addr.s_addr = htonl( INADDR_ANY );
	sa_S.sin_port        = htons( UDP_port_S );

	/* Attachement */
	bind(sock_S, (struct sockaddr *) &sa_S, sizeof(struct sockaddr));
	perror("bind ");

	taille_sa_C = sizeof( struct sockaddr );

	listen(sock_S,BACKLOG);
	perror("listen");

	conn_S = accept(sock_S, (struct sockaddr *) &sa_C,&taille_sa_C);
	perror("accept");

	while(1) {
		bzero(message,10);

		read(conn_S,message,10);
		printf("Message du client: %s",message);

		if (strcmp(message,"exit")) {
			break;
		}

	}

	close(sock_S);

}