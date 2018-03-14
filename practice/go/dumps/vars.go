package main

import "fmt"

var g string = "cool guy"
var x int = 4

func increment() int {
	x++
	return x
}

func multiple(mul int) func() int {
	// x := 2
	return func() int {
		x = x * mul
		return x
	}
}

const (
	Pi = 3.14
	Language = "Go"
	A = iota
	B = iota
	C = iota

	D
	E
	F
)

const (	
	_ = iota // 0
	KB = 1 << (iota * 10) // 1 << (1 * 10) -- shifted 10 times to left
	MB = 1 << (iota * 10) // 1 << (2 * 10) (because it was iota and already shifted by 10)
)

func main() {
	a := 10
	b := "golang"
	c := 4.17
	d := true

	fmt.Printf("%v \n", a)
	fmt.Printf("%v \n", b)
	fmt.Printf("%v \n", c)
	fmt.Printf("%v \n", d)

	fmt.Printf("%v \n", g)
	g = "cowboy"
	fmt.Printf("%v \n", g)	

	a = 43

	fmt.Println("a - ", a)
	fmt.Println("a's memory address - ", &a)
	fmt.Printf("%d \n", &a)

	fmt.Println(increment())
	fmt.Println(increment())

	decrease := func () int {
		x--
		return x
	}

	fmt.Println(decrease())
	v := multiple(4)
	fmt.Println(v) // returns a function
	// https://github.com/GoesToEleven/GolangTraining/blob/master/07_memory-address/01_showing-address/main.go
	fmt.Println(&v)
	fmt.Println(multiple(4)()) // returned value (a func) is called again here
	fmt.Println(multiple(5)()) // returned value (a func) is called again here

	fmt.Println(Pi)
	fmt.Println(Language)
	fmt.Printf("%d %d %d -- %d %d %d \n",
		A, B, C, D, E*10, F) //iota(s) self increment.
	fmt.Printf("%b\t%d\n", KB, KB)
	fmt.Printf("%b\t%d\n", MB, MB)
}
