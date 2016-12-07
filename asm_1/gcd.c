#include <stdio.h>

int gcd(int a, int b) {
  if (b > 0) {
    int c = a % b;
    return gcd(b, c);
  } else {
    return a;
  }
}

int main() {
  int d = gcd(14, 42);
  int d2 = gcd(14, 21);
  printf("%d, %d\n", d, d2);
  return 0;
}
