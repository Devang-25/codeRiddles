#!/bin/bash

egrep '^[a-z][a-z][a-z][a-z]$' /usr/share/dict/words > wordlists_large.txt
python generate_words.py
rm wordlists_large.txt
