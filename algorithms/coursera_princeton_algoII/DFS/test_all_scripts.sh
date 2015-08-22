#!/bin/bash

python client_Graph_API.py data/tinyG.txt
echo -e "\n==============================\n"
python proceessing_Graph_API.py data/tinyG.txt
