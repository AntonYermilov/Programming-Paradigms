all: simple from_c

simple: simple.c
	gcc simple.c -o simple

from_c: from_c.c strcpy.s strcat.s
	nasm -f elf64 strcpy.s -o strcpy.o
	nasm -f elf64 strcat.s -o strcat.o
	gcc from_c.c -c -o from_c.o
	gcc from_c.o strcpy.o strcat.o -o from_c

clean:
	rm -f simple from_c *.o

.PHONY: clean
