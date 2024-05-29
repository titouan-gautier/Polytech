/* Socket - Client - Mode Datagramme */

#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <strings.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int createSocket(int port_A, int port_B, char *ip, int first)
{
	int sock_S, sock_C;

    /* creation socket Client */
	sock_S = socket(PF_INET, SOCK_DGRAM, 0);
	perror("socket");

	sock_C = socket(PF_INET, SOCK_DGRAM, 0);
	perror("socket");
	
	struct sockaddr_in sa_S, sa_C, sa_R;
	
	unsigned int taille_sa_S, taille_sa_C;
	
	char message[10];

	/* @IP et n� port Server */
	bzero((char*) &sa_S, sizeof(sa_S));
	sa_S.sin_family      = AF_INET;
	sa_S.sin_addr.s_addr = inet_addr( ip );
	sa_S.sin_port        = htons( port_A );

    /* @IP et n� port Client */
	bzero((char*) &sa_C, sizeof(sa_C));
	sa_C.sin_family      = AF_INET;
	sa_C.sin_addr.s_addr = inet_addr( ip );
	sa_C.sin_port        = htons( port_B );

	bind(sock_S, (struct sockaddr *) &sa_S, sizeof(struct sockaddr));
	perror("bind ");

	/* emission vers le serveur (a partir du client) */
	taille_sa_S = sizeof( struct sockaddr );
    taille_sa_C = sizeof( struct sockaddr );
	
    while (1) {
        if (first) {
            sendto(sock_C, "Salut", 10 * sizeof(char), 0, (struct sockaddr*) &sa_C, taille_sa_C);
            first = 0;
        }

        recvfrom(sock_S, message, 10 * sizeof(char), 0, (struct sockaddr *) &sa_R, &taille_sa_S);

        printf("%s \n", message);

		char res[10];
    	int num = atoi(message) + 1;
    	sprintf(res, "%d", num);

        sendto(sock_C, message, 10 * sizeof(char), 0, (struct sockaddr*) &sa_C, taille_sa_C);
    }

	close(sock_S);
	close(sock_C);
	exit(EXIT_SUCCESS);	
}

