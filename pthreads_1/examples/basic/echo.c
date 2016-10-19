#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>


static void *echo(void *data)
{
	/*
	Cast back, because all the data passed as void *, it's a bit sad
	*/
	const char *message = data;
	puts(message);

	/*
	Similary, we return everything as void *
	*/
	return NULL;
}

int main(int argc, char **argv)
{
	pthread_t *ths;
	int rc, i;

	ths = malloc((argc - 1) * sizeof(pthread_t));
	if (!ths) {
		perror("main");
		exit(1);
	}

	for (i = 0; i < argc - 1; ++i) {
		/*
		Fourth argument is a data that will be passed to
		*/
		rc = pthread_create(ths + i, NULL, echo, argv[i + 1]);
		if (rc) {
			perror("main");
			exit(2);
		}
	}

	/*
	pthread_join waits until specified thread terminated, because
	we cannot free ths while someone uses it
	*/
	for (i = 0; i < argc - 1; ++i)
		pthread_join(*(ths + i), NULL);
	free(ths);

	return 0;
}
