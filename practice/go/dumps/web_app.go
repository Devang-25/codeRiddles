package main

import (
"fmt"
"net/http"
"os/exec"
)

func CheckErr(e error) {
	if e != nil {
		panic(e)
	}
}

func handler(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path[1:])
}

func query(w http.ResponseWriter, r *http.Request) {
  // cmd := exec.Command("/bin/basg", mongoToCsvSH)
  // cmd := "ls"
  shpath := "/Users/arcolife/workspace/projects/Personal/codeRiddles/practice/go/dumps/test_script.sh"
  out, err := exec.Command("/bin/bash", shpath).Output()
  // out, err := exec.Command("/bin/bash", "-c", "ls").Output()
  CheckErr(err)
  fmt.Println("nxhjd")
  fmt.Fprintf(w, string(out))

}

func main() {
  http.HandleFunc("/", handler)
  http.HandleFunc("/query", query)
  http.ListenAndServe(":8080", nil)
}

// http://localhost:8080/shrooms
