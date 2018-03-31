package main

import (
	"fmt"
	//"strconv"
	"log"
	"path/filepath"
	"os"
	"github.com/fatih/color"
	"path"
	"strings"
	"reflect"
	"io/ioutil"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"bufio"
)

const PORT_NUMBER = 40623
const MAX_FAIL = 1
const N = 2
const OUTPUT_THRESHOLD = 0

//func myPrintInterface(t int, args ...interface{}) {
func myPrintInterface(t int, format string, args ...interface{}) {
	// t: log level
	// 		0: information
	//		1: emphasis
	//		2: warning
	//		3: error
	blue := color.New(color.FgBlue).SprintFunc()
	yellow := color.New(color.FgYellow).SprintFunc()
	red := color.New(color.FgRed).SprintFunc()

	if t >= OUTPUT_THRESHOLD {
		
		switch t {
		case 0:  // info
			//fmt.Print("[ ]", strings.Join(args... , " "))
			fmt.Printf("[ ]" + format, args ... )
			break
		case 1: // emphasized
			//fmt.Print(blue("[.]"), strings.Join(args... , " "))
			fmt.Printf(blue("[.]") + format, args ... )
			break
		case 2: // warning
			//fmt.Print(yellow("[!]"), strings.Join(args... , " "))
			fmt.Printf(yellow("[!]") + format, args ... )
			break
		case 3:  // error
			//fmt.Print(red("[x]"), strings.Join(args... , " "))
			fmt.Printf(red("[x]") + format, args ... )
		}	
	}
}

func myPrintStrLst(t int, args ...string) {
	// t: log level
	// 		0: information
	//		1: emphasis
	//		2: warning
	//		3: error
	blue := color.New(color.FgBlue).SprintFunc()
	yellow := color.New(color.FgYellow).SprintFunc()
	red := color.New(color.FgRed).SprintFunc()

	if t >= OUTPUT_THRESHOLD {
		
		switch t {
		case 0:  // info
			fmt.Print("[ ]", strings.Join(args, " "))
			break
		case 1: // emphasized
			fmt.Print(blue("[.]"), strings.Join(args, " "))
			break
		case 2: // warning
			fmt.Print(yellow("[!]"), strings.Join(args, " "))
			break
		case 3:  // error
			fmt.Print(red("[x]"), strings.Join(args, " "))
		}	
	}
}


// func write_new_keys(kcount int) {
// 	// KD, err := filepath.Abs(filepath.Dir(os.Args[0]))
// 	// if err != nil {
// 	// 	log.Fatal(err)
// 	// }
// 	// //fmt.Println(KD)

// 	sk := []byte("test")
// 	for k:= 0; k < kcount; k++ {
// 		sk = ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
// 		filename := fmt.Sprintf("sign%v.dat", 2)
// 		err := ioutil.WriteFile(path.Join(GetCWD(), filename), sk, 0644)
// 	}
// }


func GetCWD() string {
	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		log.Fatal(err)
	}
	return dir
}

type Node struct {
	ecdsaKeyMap       map[string]*ecdsa.PublicKey
	ecdsaPriKey    *ecdsa.PrivateKey
	ecdsaKeyPubKey    *ecdsa.PublicKey
}

func check(e error, t int) {
	// t = 1 => panic
	// t = 0 => log.Fatal
        if e != nil{
		if t == 1 {
			panic(e)
		} else {
			log.Fatal(e)
		}
        }
}


func readLines(path string) ([]string, error) {
  file, err := os.Open(path)
  if err != nil {
    return nil, err
  }
  defer file.Close()

  var lines []string
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    lines = append(lines, scanner.Text())
  }
  return lines, scanner.Err()
}

func main(){
	KD, _ := filepath.Abs(filepath.Dir(os.Args[0]))
	msg := []string{"\tCWD:", KD, "\n"}
	//fmt.Print(0, strings.Join(msg, " "))
	// fmt.Print(0, msg ...)
	// fmt.Print(msg ...)
	// fmt.Print(0, "\tchosen Key Dir as ", KD, "\n")

	// // myPrintInterface(0, msg)
	// // myPrintInterface(1, msg)
	// // myPrintInterface(2, msg)
	// // myPrintInterface(3, msg)

	
	myPrintInterface(0, strings.Join(msg, " "))
	myPrintInterface(1, strings.Join(msg, " "))
	myPrintInterface(2, strings.Join(msg, " "))
	myPrintInterface(3, strings.Join(msg, " "))
	
	myPrintStrLst(0, msg...)
	myPrintStrLst(1, msg...)
	myPrintStrLst(2, msg...)
	myPrintStrLst(3, msg...)

	cwd := GetCWD()
	fmt.Println("CWD:", cwd)
	//filename :=  ""
	for k:= 0; k < 2; k++ {
		filename := fmt.Sprintf("key%v.dat", k)
		//fmt.Println(path.Join("./", filename))	
		sk, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
		fmt.Println(reflect.TypeOf(sk))
		fmt.Println(k, sk)
		//key_dat := fmt.Sprintf("%b", sk)
		//err := ioutil.WriteFile(path.Join(GetCWD(), filename), key_dat , 0644)
		err := ioutil.WriteFile(path.Join(cwd, filename), sk.D.Bytes() , 0644)
		check(err, 1)
	}
	
	hosts_filep := path.Join(os.Getenv("HOME"), "hosts")
	peers, err := ioutil.ReadFile(hosts_filep)
	//fmt.Println(peers)
	//check(err, 1)
	check(err, 0)
	fmt.Println(string(peers))

	peersList, err := readLines(hosts_filep)
	check(err, 0)
	fmt.Println(peersList)
	fmt.Println(reflect.TypeOf(peersList))
	fmt.Println(peersList[2])
	//myPrintInterface(2, peersList)
}
