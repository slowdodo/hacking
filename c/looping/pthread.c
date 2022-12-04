#include <stdio.h>
#include <pthread.h>

// number of threads to create
#define NUM_THREADS 4

// thread function that consumes CPU resources
void *thread_func(void *arg) {
    int x = 0;
    for (int i = 0; i < 100000000; i++) {
        x += i;
    }
    return NULL;
}

int main() {
    // create an array of threads
    pthread_t threads[NUM_THREADS];

    // create the threads
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, thread_func, NULL);
    }

    // wait for the threads to finish
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
