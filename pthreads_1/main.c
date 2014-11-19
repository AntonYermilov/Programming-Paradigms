// Task: several threads update counter, want to stop as soon as counter reachs some limit.
// E.g. dice, forward random walk.

#include <stdio.h>
#include <pthread.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

#include "atomic_int.h"

#define WALKERS_NM 2
#define LIMIT 100

void* walk(void *);

int main(int argc, char **argv) {
  srand(time(NULL));
  AtomicInt *counter = AtomicInt_init(0);

  pthread_t walkers[WALKERS_NM];
  for (unsigned i = 0; i < WALKERS_NM; ++i) {
    int create_status = pthread_create(walkers + i, NULL /* attrs */, walk, (void*) counter);
    assert(!create_status && "Unable to create thread");
  }

/* Bad approach
while (AtomicInt_get(counter) < LIMIT) {
    sleep(2);
  }
*/
  printf("Counter value: %d\n", AtomicInt_wait(counter, LIMIT));
  for (unsigned i = 0; i < WALKERS_NM; ++i) {
    int cancel_status = pthread_cancel(walkers[i]); // TODO: cancelation point?
    assert(!cancel_status && "Unable to cancel thread");
    pthread_join(walkers[i], NULL);
  }
  
  AtomicInt_destroy(&counter);
  pthread_exit(NULL); // waits till all child threads are done
}

void* walk(void *arg) {
  AtomicInt *counter = (AtomicInt*)arg;
  while (1) {
    AtomicInt_add(counter, rand() % 20);
    printf("%d\n", AtomicInt_get(counter));
    // Q: u prefix in function name
    usleep(10000); // explain "man" utility & chapters
  }
}
