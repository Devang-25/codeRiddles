#!/bin/bash

counts=$((tr ' ' '\n' | sed -r '/^\s*$/d' | sort | uniq -c | awk '{print $2" "$1}') < words_large)

echo "$counts" | awk -F' ' -v OFS=' ' '{ 
     if ($2 in a) { 
       a[$2] = a[$2]" "$1;
     } else { 
       a[$2] = $1;
     } 
  } END { for (i in a) print i, a[i] }' | sort -k1 -V
