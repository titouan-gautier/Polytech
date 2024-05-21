CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = ring_network
OBJS = main.o host.o network.o

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

main.o: main.c network.h
	$(CC) $(CFLAGS) -c main.c

host.o: host.c network.h
	$(CC) $(CFLAGS) -c host.c

network.o: network.c network.h
	$(CC) $(CFLAGS) -c network.c

clean:
	rm -f $(OBJS) $(TARGET)
