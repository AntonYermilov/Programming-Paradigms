#include "atomic_int.h"

#include <pthread.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

struct AtomicInt {
  int value;
  pthread_mutex_t value_mutex;
  pthread_cond_t value_cv;
  int limit;
};

struct AtomicInt* AtomicInt_init(int init_value) {
  AtomicInt* new_ai = malloc(sizeof(*new_ai));
  assert(new_ai && "Mem alloc for Atomic int failed");
  memset(new_ai, 0, sizeof(*new_ai));

  new_ai->value = init_value;

  // init recursive mutex
  pthread_mutexattr_t value_mutex_attrs;
  pthread_mutexattr_init(&value_mutex_attrs);
  pthread_mutexattr_settype(&value_mutex_attrs, PTHREAD_MUTEX_RECURSIVE);
  pthread_mutex_init(&new_ai->value_mutex, &value_mutex_attrs);
  pthread_mutexattr_destroy(&value_mutex_attrs);

  // init conditional variable
  pthread_cond_init(&new_ai->value_cv, NULL);

  return new_ai;
}

int AtomicInt_get(AtomicInt* atomic_int) {
  assert(atomic_int);
  return atomic_int->value;
}

void AtomicInt_add(AtomicInt* atomic_int, int delta) {
  assert(atomic_int);

  pthread_mutex_lock(&atomic_int->value_mutex);
  if (atomic_int->limit == 0) {
    goto out;
  }
  atomic_int->value += delta;
  if (atomic_int->value >= atomic_int->limit) {
    pthread_cond_signal(&atomic_int->value_cv);
  }

out:
  pthread_mutex_unlock(&atomic_int->value_mutex);
}

int AtomicInt_wait(AtomicInt* atomic_int, int limit) {
  int result = 0;

  pthread_mutex_lock(&atomic_int->value_mutex);
  atomic_int->limit = limit;
  while (atomic_int->value < atomic_int->limit) {
    pthread_cond_wait(&atomic_int->value_cv, &atomic_int->value_mutex);
  }
  result = atomic_int->value;
  pthread_mutex_unlock(&atomic_int->value_mutex);

  return result;
}

void AtomicInt_destroy(AtomicInt** atomic_int) {
  assert(atomic_int && *atomic_int);

  pthread_cond_destroy(&(*atomic_int)->value_cv);
  pthread_mutex_destroy(&(*atomic_int)->value_mutex);
  free(*atomic_int);

  *atomic_int = NULL;
}
