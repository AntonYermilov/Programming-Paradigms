#include <stdio.h>
bool flag;

int f(int n) {
    int retVal;
    if flag then retVal = 2 * n;
            else retVal = n;
    flag = !flag;
    return retVal;
}

void test(){
    flag = true;
    
    printf("f(1) + f(2) = %d\n", f(1) + f(2));
    printf("f(2) + f(1) = %d\n", f(2) + f(1));

    return 0;
}

void main(void) {
    return test();
}

// Каков будет вывод при вызове test?
