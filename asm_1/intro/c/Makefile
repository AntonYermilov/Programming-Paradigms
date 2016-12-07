SRCS=$(wildcard *.s)
OBJS=$(SRCS:.s=.o)
EXECS=$(OBJS:.o=.exe)

all: $(EXECS)

%.o : %.s
	nasm -f elf64 $< -o $@

%.exe: %.o
	gcc $< -o $@

#	ld -dynamic-linker /lib/ld-linux.so.2 \
#	/usr/lib/crt1.o \
#	/usr/lib/crti.o \
#	-lc hello3.o -o hello3.exe \
#	/usr/lib/crtn.o

clean:
	rm -f *.exe

.PHONY: clean
