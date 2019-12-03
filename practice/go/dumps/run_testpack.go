package main

import "./testpack"
import "./testpack/nested"
import "fmt"

func main() {
	arcops.TestDirOps()
	// arcops.test_dir_ops() or arcops.testDirOps() won't run and error out w/:
	// ./run_testpack.go:8:2: cannot refer to unexported name arcops.test_dir_ops
	// ./run_testpack.go:8:2: undefined: arcops.test_dir_ops
	fmt.Println("CWD: ", arcops.GetCWD())
	nesty.GetNesty()
}
