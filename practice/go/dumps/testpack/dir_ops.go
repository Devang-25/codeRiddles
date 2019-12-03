package arcops

import (
	"fmt"
	//"strconv"
	"os"
	"path"
	"reflect"
	"io/ioutil"
	"strings"
)

const PORT_NUMBER = 40623
const MAX_FAIL = 1
const N = 2
const OUTPUT_THRESHOLD = 0

func TestDirOps(){
	msg := []string{" Foo <->", "Bar", "\n"}
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

	// myPrintStrLst(2, 4)

	// also, just in case:
	// https://golang.org/doc/faq#convert_slice_of_interface

	//filename :=  ""
	write_new_keys(2)
	read_keys_test(2)

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
	fmt.Println(peersList[1])
	//myPrintInterface(2, peersList)
}
