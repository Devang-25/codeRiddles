package main

import (
        "fmt"
        "log"
	"io/ioutil"

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
        A string
	BottleNeck `yaml:"bot"`
	E int
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

	// err := yaml.Unmarshal([]byte(data), &t)
	datafile, err := ioutil.ReadFile("./example.yaml")
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

	/*
        m := make(map[interface{}]interface{})
    
        //err = yaml.Unmarshal(datafile, &m)
	err = yaml.Unmarshal([]byte(data), &m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m:\n%v\n\n", m)
	f := m["b"]
	fmap := convertInterface(f)
	//fmap := f.(map[interface{}]interface{})
	fmt.Println(fmap["d"])
	
        d, err = yaml.Marshal(&m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m dump:\n%s\n\n", string(d))
	*/
}
