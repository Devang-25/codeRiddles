// http://www.golangpatterns.info/concurrency/coroutines

package main

import (
    "fmt"
)

type ByteSize float64

const (
	_           = iota // ignore first value by assigning to blank identifier
	KB  = 1 << (10 * iota)
	// KB ByteSize = 1 << (10 * iota)	
	MB
	GB
	TB
	PB
	EB
	ZB
	YB
)

func integers () chan int {
    yield := make (chan int);
    count := 0;
    go func () {
        for {
            yield <- count;
            count++;
        }
    } ();
    return yield
}

func main() {
    resume := integers();
    generateInteger := func () int {
        return <-resume
    }    
    fmt.Println(generateInteger())
    fmt.Println(generateInteger())
    fmt.Println(generateInteger())
    fmt.Println(generateInteger())
    fmt.Println(generateInteger())
    fmt.Println(generateInteger())

    fmt.Println(KB, MB, GB)
}
