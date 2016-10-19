#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>


void *say_hello(void *dummy)
{
	(void) dummy;
	puts("Hello, World!");

	return NULL; /* or pthread_exit(NULL); */
}

int main(void)
{
	pthread_t th;
	int rc;

	/*
	pthread_create starts thread th with function say_hello.
	*/
	rc = pthread_create(&th, NULL, say_hello, NULL);
	if (rc) {
		perror("main");
		exit(1);
	}

	/*
	if main finishes without calling pthread_exit, all created
	threads will terminate.
	*/
	pthread_exit(NULL);

	return 0;
}
