package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"gopkg.in/yaml.v2"
)

var data = `
a: Easy!
b:
  c: 2
  d: [3, 4]
`

type BottleNeck struct {
	RenamedC int `yaml:"some"`
	D        []int
}

// Note: struct fields must be public in order for unmarshal to
// correctly populate the data.
type T struct {
	A          string
	BottleNeck `yaml:"bot"`
	E          int
}

/*
// Note: struct fields must be public in order for unmarshal to
// correctly populate the data.
type T struct {
        A string
        B struct {
                RenamedC int `yaml:"some"`
                D        []int
        }
	E int
}
*/

func convertInterface(someFace interface{}) map[interface{}]interface{} {
	return someFace.(map[interface{}]interface{})
}

func main() {
	t := T{}
	//
	// // err := yaml.Unmarshal([]byte(data), &t)
	if len(os.Args) < 2 {
		fmt.Println("Missing parameter, provide file name!")
		return
	}
	datafile, err := ioutil.ReadFile(os.Args[1])

	if err != nil {
		fmt.Println("Can't read file:", os.Args[1])
		panic(err)
	}
	err = yaml.Unmarshal(datafile, &t)

	if err != nil {
		log.Fatalf("error: %v", err)
	}
	fmt.Printf("---> t:\n%v\n\n", t)
	fmt.Println(t.BottleNeck)

	d, err := yaml.Marshal(&t)
	if err != nil {
		log.Fatalf("error: %v", err)
	}
	fmt.Printf("--- t dump:\n%s\n\n", string(d))

	m := make(map[interface{}]interface{})

	// err = yaml.Unmarshal([]byte(data), &m)
	err = yaml.Unmarshal([]byte(datafile), &m)
	if err != nil {
		log.Fatalf("error: %v", err)
	}
	fmt.Printf("--- m:\n%v\n\n", m)

	fmt.Printf("type(m): %T\n", m)

	// fmt.Printf("bot.d: %T\n", m["bot"]["d"])
	// ^ This can't run yet. We get following error on trial:
	// ./config.go:88:37: invalid operation: m["bot"]["d"] (type interface {} does not support indexing)
	// https://stackoverflow.com/questions/25214036/getting-invalid-operation-mymaptitle-type-interface-does-not-support-in

	f := m["bot"]
	fmt.Printf("type(f): %T\n", f)

	fmap := convertInterface(f)
	//fmap := f.(map[interface{}]interface{})
	fmt.Println(fmap["d"])

	// var d
	d, error := yaml.Marshal(&m)
	fmt.Printf("type(d): %T\n", d)

	if error != nil {
		log.Fatalf("error: %v", err)
	}
	fmt.Printf("--- m dump:\n%s\n\n", string(d))
}
