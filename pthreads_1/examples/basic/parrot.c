#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>

static void *stupid_parrot(void *dummy)
{
	#define SECRET "stop it, please"
	char buffer[1024];

	(void) dummy;

	while (1) {
		printf("You: ");
		fgets(buffer, sizeof(buffer), stdin);
		if (!strncmp(SECRET, buffer, sizeof(SECRET) - 1))
			break;
		printf("Parrot: %s", buffer);
	}

	return NULL;
}

int main(void)
{
	pthread_t th;
	pthread_attr_t attr;
	int rc;

	/*
	Or just call pthread_detach(th); There are plenty bunch of another
	attributes (stack address, stack size, scheduling priority ...).

	For every attribute there is pair of functions (setter and getter),
	that usually looks like:
		pthread_attr_set*(&attr, value);
		pthread_attr_get*(&attr, &value);
	where * is one of:
		detachstate
		stacksize
		stackaddr
		...
	*/
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);

	rc = pthread_create(&th, &attr, stupid_parrot, NULL);
	if (rc) {
		perror("main");
		exit(1);
	}

	pthread_attr_destroy(&attr);

	/*
	We still need pthread_exit even for detached threads
	*/
	pthread_exit(NULL);

	return 0;
}
