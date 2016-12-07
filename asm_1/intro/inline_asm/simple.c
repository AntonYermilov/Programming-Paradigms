#include <stdio.h>


int main(void)
{
  int foo = 10, bar = 15, rem = 0;
  asm volatile("div %%rbx"
               :"=d"(rem), "=a"(bar)
               :"a"(bar), "b"(foo), "d"(rem));
  printf("bar / foo, bar %% foo = %d, %d\n", bar, rem);
  return 0;
}
