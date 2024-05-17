CC=gcc

all: client serveur clean

client: client.o
	$(CC) -Wall -o $@ $^

serveur: serveur.o
	$(CC) -Wall -o $@ $^

client.o: 
	$(CC) -Wall -c client.c

serveur.o: 
	$(CC) -Wall -c serveur.c	

clean:
	rm *.o
	rm *~



