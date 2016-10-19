CFLAGS=-fsanitize=thread -g
LDFLAGS=-lpthread
CC=clang

all: example

example: example.c
	$(CC) example.c $(CFLAGS) $(LDFLAGS) -o example

clean:
	rm example

.PHONY: clean
