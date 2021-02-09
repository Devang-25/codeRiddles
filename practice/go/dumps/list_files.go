package main

import (
    "fmt"
    "path/filepath"
)

func main() {
    matches, _ := filepath.Glob("./data/*.jsonl")
    for _, match := range matches {
        fmt.Println(match)
    }
}
