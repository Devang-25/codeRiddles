package main

import "fmt"
import (
	"crypto/rand"
	"crypto/ecdsa"
	"crypto/elliptic"
)

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

//https://splice.com/blog/iota-elegant-constants-golang/
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
	GB = 1 << (iota * 10) // 1 << (3 * 10)
	TB = 1 << (iota * 10) // 1 << (3 * 10)
)

func zero(x int) {
	fmt.Printf("%p \n", &x) // address in func zero
	fmt.Println(&x) // address in func zero
	x = 0
}

func zerofoo(z *int) {
	fmt.Printf("%p \n", z) // address in func zero
	fmt.Println(z) // address in func zero
	*z = 0
}

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
	fmt.Printf("%b\t%d -- thousand\n", KB, KB)
	fmt.Printf("%b\t%d -- million\n", MB, MB)
	fmt.Printf("%b\t%d -- billion\n", GB, GB)
	fmt.Printf("%b\t%d -- trillion\n", TB, TB)

	a = 43
	fmt.Println(a)
	fmt.Println(&a)

	// can't use the colloquial a,b reference,
	// can'r redeclare b here. .can't do var b *int = &a since "b" was used abve.
	// can't re-assign b to a different type (ptr here, it was int earlier)
	// so we use a new var z
	var z *int = &a
	fmt.Println(z)
	fmt.Println(*z)

	*z = 42
	/**
         multi line comment!!
         **/

	// pass by value. pass a mem addr is pass by value.
	// everything in Go is PBV
	fmt.Println(a)

	x := 5
	fmt.Println(x) // x is 5
	fmt.Printf("%p\n", &x) // address in main
	fmt.Println(&x) // address in main
	zero(x) // we tried to demean x
	fmt.Println(x) // x is still 5.
	// this means, x still standing strong. great dude!
	// be the X you're meant to be. huhuhuh
	// sorry. Life, pffft ! ^_^

	fmt.Printf("\n%d\n",x) // x is 0. wohhhh
	fmt.Printf("%p\n", &x) // address in main
	fmt.Println(&x) // address in main
	zerofoo(&x) // we tried to demean x again, with more foo
	fmt.Println(x) // x is 0. wohhhh. for the better?
	// what's X's bar with foo applied now?
	// Ren.ovated? 0'ed! noo o_O ..ya!?
	fmt.Println(rand.Reader)
	fmt.Println(ecdsa.GenerateKey(elliptic.P256(), rand.Reader))
}
