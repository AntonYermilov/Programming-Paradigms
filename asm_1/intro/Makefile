SRCS=$(wildcard *.s)
OBJS=$(SRCS:.s=.o)
EXECS=$(OBJS:.o=.exe)

all: $(EXECS)

%.o : %.s
	nasm -f elf64 $< -o $@

%.exe: %.o
	ld $< -o $@

clean:
	rm -f *.exe

.PHONY: clean
