#!/bin/bash

echo '127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1' > ~/hosts

go build run_testpack.go && ./run_testpack
