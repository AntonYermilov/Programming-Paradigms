// MIT license blah-blah-blah
//
// Author: Artur Huletski (hatless.fox@gmail.com)

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <stdint.h>

#define FLOAT_BITS (32)
#define FLOAT_BYTES (FLOAT_BITS >> 3)

#define FRAC_DIGITS_NUM "50"

#define SIGN_BG  "\E[41m"
#define EXP_BG   "\E[44m"
#define MANT_BG  "\E[45m"
#define RESET_BG "\E[m"

void print_float_in_bin(float printee);

int main(int argc, char **argv) {
  if (argc < 3) {
    fprintf(stderr, "Usage: fexpl cmd arg1 [arg2]\n");
    fprintf(stderr, "Params:\n\tcmd = {bin, add, sub, mul, div}\n");
    exit(-1);
  }
  assert(sizeof(float) == FLOAT_BYTES);

#define GENERATE_BIN_OP_SUPPORT(op)				\
  do {								\
    if (argc < 4) {						\
      fprintf(stderr, "Command "#op" expects to args\n");	\
      exit(-1);						\
    }								\
    float arg1 = strtof(argv[2], NULL);			\
    fprintf(stdout, "Arg1 is %."FRAC_DIGITS_NUM"f\n", arg1);	\
    print_float_in_bin(arg1);					\
								\
    float arg2 = strtof(argv[3], NULL);			\
    fprintf(stdout, "Arg2 is %."FRAC_DIGITS_NUM"f\n", arg2);	\
    print_float_in_bin(arg2);					\
    								\
    fprintf(stdout, #op" result is %."FRAC_DIGITS_NUM"f\n",	\
            arg1 op arg2);					\
    print_float_in_bin(arg1 op arg2);				\
  } while (0)

  if (strcmp(argv[1], "bin") == 0) {
      float value_to_explore = strtof(argv[2], NULL);
      fprintf(stdout, "Format: "SIGN_BG"Sign"RESET_BG", "EXP_BG"Exponent"
              RESET_BG", "MANT_BG"Mantissa"RESET_BG".\n");
      fprintf(stdout, "Binary of %."FRAC_DIGITS_NUM"f:\n", value_to_explore);
      print_float_in_bin(value_to_explore);
    } else if (strcmp(argv[1], "add") == 0) {
      GENERATE_BIN_OP_SUPPORT(+);
    } else if (strcmp(argv[1], "mul") == 0) {
      GENERATE_BIN_OP_SUPPORT(*);
    } else if (strcmp(argv[1], "sub") == 0) {
      GENERATE_BIN_OP_SUPPORT(-);
    } else if (strcmp(argv[1], "div") == 0) {
      GENERATE_BIN_OP_SUPPORT(/);
    } else {
      fprintf(stderr, "Unknown command: %s\n", argv[1]);
      exit(-1);
    }

#undef GENERATE_BIN_OP_SUPPORT

}


void print_float_in_bin(float printee) {

#define GET_BG(type) type##_BG

#define SET_BG_FOR_BIT(bit, type) \
  case bit:			  \
    color = GET_BG(type);	  \
    break;

  uint32_t exploree = *((uint32_t *)&printee);
  for (int bit = FLOAT_BITS - 1; bit >= 0; --bit) {
    // IEEE 754-related coloring
    char *color = "";
    switch (bit) {
    SET_BG_FOR_BIT(31, SIGN);
    SET_BG_FOR_BIT(30, EXP);
    SET_BG_FOR_BIT(22, MANT);
    }

    fprintf(stdout, "%s%u", color, (exploree & (1U << bit)) > 0);
  }
  fprintf(stdout, "\E[m\n");

#undef SET_BG_FOR_BIT
}
