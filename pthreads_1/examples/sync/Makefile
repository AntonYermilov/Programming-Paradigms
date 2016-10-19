CC      ?= gcc
CFLAGS  ?= -Wall -Wextra -Werror -ansi -pedantic
LDFLAGS ?= -lpthread

all: msgqueue

msgqueue: msgqueue.o linkedlist.o queue.o squeue.o wsqueue.o
	$(CC) msgqueue.o linkedlist.o queue.o squeue.o wsqueue.o \
		$(LDFLAGS) -o msgqueue

msgqueue.o: msgqueue.c
	$(CC) -c msgqueue.c $(CFLAGS) -o msgqueue.o

linkedlist.o: linkedlist.c
	$(CC) -c linkedlist.c $(CFLAGS) -o linkedlist.o

queue.o: queue.c
	$(CC) -c queue.c $(CFLAGS) -o queue.o

squeue.o: squeue.c
	$(CC) -c squeue.c $(CFLAGS) -o squeue.o

wsqueue.o: wsqueue.c
	$(CC) -c wsqueue.c $(CFLAGS) -o wsqueue.o

clean:
	rm *.o msgqueue

.PHONY: clean
