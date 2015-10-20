include ../Makefile.inc
all: hello echo parrot

hello: hello.c
	$(CC) hello.c $(CFLAGS) $(LDFLAGS) -o hello

echo: echo.c
	$(CC) echo.c $(CFLAGS) $(LDFLAGS) -o echo

parrot: parrot.c
	$(CC) parrot.c $(CFLAGS) $(LDFLAGS) -o parrot

clean:
	rm hello echo parrot

.PHONY: clean
