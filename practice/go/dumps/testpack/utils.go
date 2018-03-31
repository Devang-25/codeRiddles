package arcops

import (
	"os"
	// "io"
	"fmt"
	"bufio"
	"bytes"
	"path"
	"reflect"
	"io/ioutil"
	"strings"
	"github.com/fatih/color"
	"path/filepath"
	"encoding/gob"
	"log"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	// "crypto/x509"
)

type config struct {
	N 		int
	IPList	[]string
	Ports  	[]int
}

type Node struct {
	ecdsaKeyMap       map[string]*ecdsa.PublicKey
	ecdsaPriKey    *ecdsa.PrivateKey
	ecdsaKeyPubKey    *ecdsa.PublicKey
}

// c := elliptic.P256()
// params := c.Params()
// // k, err := ecdsa.randFieldElement(, rand.Reader)
// b := make([]byte, params.BitSize/8+8)
// tst, err_tst := io.ReadFull(rand.Reader, b)
// fmt.Println(tst)
// check(err_tst, 1)

func read_keys_test(kcount int) {
	cwd := GetCWD()
	for k:= 0; k < kcount; k++ {
		// err := ioutil.WriteFile(path.Join(cwd, filename), sk.D.Bytes() , 0644)
		filename := fmt.Sprintf("key%v.dat", k)
		kfpath := path.Join(cwd, filename)
		fmt.Printf("Reading key from: " + kfpath + "\n")
		b, err := ioutil.ReadFile(kfpath)
		if err != nil {
			fmt.Printf("Error reading keys: " + kfpath + "\n")
			// return err
		}
		// fmt.Println(b)
		bufm := bytes.Buffer{}
		bufm.Write(b)
		gob.Register(&ecdsa.PrivateKey{})
		d := gob.NewDecoder(&bufm)
		sk := ecdsa.PrivateKey{}
		d.Decode(&sk)
		// fmt.Println(d.Decode(&sk))
		fmt.Println(d)
		fmt.Println(k, " ====== ", sk)
	}
}

func write_new_keys(kcount int) {
	// KD, err := filepath.Abs(filepath.Dir(os.Args[0]))
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// //fmt.Println(KD)
	cwd := GetCWD()
	// sk := []byte("test")
	for k:= 0; k < kcount; k++ {
		filename := fmt.Sprintf("key%v.dat", k)
		//fmt.Println(path.Join("./", filename))
		sk, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)

		fmt.Println(reflect.TypeOf(sk))
		fmt.Println(k, " ====== ", sk)
		// //key_dat := fmt.Sprintf("%b", sk)
		// //err := ioutil.WriteFile(path.Join(GetCWD(), filename), key_dat , 0644)

		// err := ioutil.WriteFile(path.Join(cwd, filename), sk.D.Bytes() , 0644)

		buf := bytes.Buffer{}
		e := gob.NewEncoder(&buf)
		e.Encode(sk)
		err := ioutil.WriteFile(path.Join(cwd, filename), buf.Bytes(), 0644)
		check(err, 1)
	}
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

func GetCWD() string {
	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		log.Fatal(err)
	}
	return dir
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
