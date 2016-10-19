include ../Makefile.inc
LDFLAGS ?=

all: volatile nonvolatile

volatile: volatile.c
	$(CC) volatile.c -O3 $(CFLAGS) $(LDFLAGS) -o volatile

nonvolatile: nonvolatile.c
	$(CC) nonvolatile.c -O3 $(CFLAGS) $(LDFALGS) -o nonvolatile

clean:
	rm volatile nonvolatile

.PHONY: clean
