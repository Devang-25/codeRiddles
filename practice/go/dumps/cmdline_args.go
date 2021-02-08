package main

import (
  "flag"
  "os"
  "fmt"
)

func doLint(cmdline []string){
  flag.CommandLine.Parse(cmdline)

	packages := []string{"./..."}
  fmt.Println(packages)
	if len(flag.CommandLine.Args()) > 0 {
		packages = flag.CommandLine.Args()
	}
  fmt.Println(packages)
}

func main(){
  doLint(os.Args[1:])
}
