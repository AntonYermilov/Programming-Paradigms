SRC=main.c atomic_int.c atomic_int.h
LIBS=pthread
OUT=./pth_demo

build: $(SRC)
	gcc -Wall -std=gnu99 -o $(OUT) $(SRC) $(addprefix -l, $(LIBS))

check_mem: build
	valgrind --leak-check=yes $(OUT)
