package main

import (
    "fmt"
    "runtime"
    "sync"
)

// number of threads to create
const numThreads = 4

// thread function that consumes CPU resources
func threadFunc() {
    x := 0
    for i := 0; i < 100000000; i++ {
        x += i
    }
}

func main() {
    // set the number of CPUs to use
    runtime.GOMAXPROCS(numThreads)

    // create a wait group to wait for the threads to finish
    var wg sync.WaitGroup
    wg.Add(numThreads)

    // create the threads
    for i := 0; i < numThreads; i++ {
        go func() {
            // call the thread function
            threadFunc()

            // mark the thread as done
            wg.Done()
        }()
    }

    // wait for the threads to finish
    wg.Wait()
}
