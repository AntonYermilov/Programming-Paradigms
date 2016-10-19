#include "barrier.h"

#include <pthread.h>
#include <stdlib.h>
#include <assert.h>


struct barrier {
	atomicint_t    atomic_int;
	int            limit;
	pthread_cond_t limit_reached;
};

barrier_t* barrier_make(int limit) {
	barrier_t* b = malloc(sizeof(*b));
	assert(b);

	atomicint_init(&b->atomic_int, 0);
	b->limit = limit;
	pthread_cond_init(&b->limit_reached, NULL);

	return b;
}

int  barrier_get(barrier_t* b) {
	assert(b);

	return atomicint_get(&b->atomic_int);
}

void barrier_add(barrier_t* b, int value) {
	assert(b);

	pthread_mutex_lock(&b->atomic_int.value_mutex);

	b->atomic_int.value += value;
	if (b->atomic_int.value >= b->limit)
		pthread_cond_broadcast(&b->limit_reached);

	pthread_mutex_unlock(&b->atomic_int.value_mutex);
}

int  barrier_wait(barrier_t* b) {
	int result;

	assert(b);

	pthread_mutex_lock(&b->atomic_int.value_mutex);

	while (b->atomic_int.value < b->limit) /* spurious wakeups */
		pthread_cond_wait(&b->limit_reached, &b->atomic_int.value_mutex);
	result = b->atomic_int.value;

	pthread_mutex_unlock(&b->atomic_int.value_mutex);

	return result;
}

void barrier_free(barrier_t* b) {
	assert(b);

	atomicint_destroy(&b->atomic_int);
	pthread_cond_destroy(&b->limit_reached);
	free(b);
}
