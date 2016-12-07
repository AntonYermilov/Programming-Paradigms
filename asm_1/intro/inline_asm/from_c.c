#include <stdio.h>

char* strcpy_asm(char* dst, char* src);
char* strcat_asm(char* dst, char* src);

int main(void)
{
  char src[] = "hello, calling asm from c!";
  char dst[sizeof(src)] = {0};
  strcpy_asm(dst, src);
  printf("%s\n", dst);


  char dst2[100] = {0};
  strcat_asm(dst2, "hello, ");
  strcat_asm(dst2, "concatenation!");
  printf("%s\n", dst2);

  return 0;
}
