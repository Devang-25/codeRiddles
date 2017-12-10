
package main

import "fmt"

func main() {
     fmt.Println("Hello World")
     //uint8
     //uint16
     //uint32
     //uint64
     //int8
     //int16
     //int32
     //int64

     c := 10

     // Block 1
     // var a int = 40
     // var b float64 = 1.34242

     // Block 2
     var a int = 40
     // b := 2.12
     b := 2
     c += a / b
     // above op fails if there's a mismatch of any of the var's types.
     // produces -- invalid operation: a / b (mismatched types int and float64)

     // b := 1.3414  // -> can't happen after declaration, produces -- no new variables on left side of :=
     // b = "hsdjsd" // can't happen, produces -- cannot use "hsdjsd" (type string) as type int in assignment
     // Block 1 and Block 2 are mutually exclusive.
     fmt.Println(a,b,c)

     c += a /
       	  b
     fmt.Println(a,b,c)

     // c += a
     //   	  / b
     // syntax error: unexpected /, expecting }
     // line break can't happen before operator
     
     fmt.Println("'Hello'"); fmt.Println("\t- World")
     // semi colons not compulsary
     // Q: how do I achieve following python-based functionality in Go?
     //  >> print("foo,gee", sep=',', end=" ", flush=True); print("bar")
}
     
