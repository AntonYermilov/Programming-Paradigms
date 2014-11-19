#ifndef __ATOMIC_INT_H

// opaque pointer idiom
struct AtomicInt;
typedef struct AtomicInt AtomicInt;

#define T AtomicInt*

T AtomicInt_init(int init_value);
int AtomicInt_get(T atomic_int);
void AtomicInt_add(T atomic_int, int delta);
int AtomicInt_wait(T atomic_int, int limit);
void AtomicInt_destroy(T* atomic_int);

#undef T

#endif
