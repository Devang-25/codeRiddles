#!/bin/bash

# Sort the content of the a file based on second field, e.g.

# Jervie,12,M
# Jaimy,11,F
# Tony,23,M
# Janey,11,F
# Output file:
# Jaimy,11,F
# Janey,11,F
# Jervie,12,M
# Tony,23,M

# 1 GB RAM, but 4 GB file size.
# https://en.wikipedia.org/wiki/External_sorting

# https://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python
# https://stackoverflow.com/a/519653/1332401
# https://stackoverflow.com/questions/1661986/why-doesnt-pythons-mmap-work-with-large-files


#################

# this method would end up using thrice the size of file on external storage
# it would produce new chunks which in turn would require space to be stored and processed and combined into a third sorted file

fpath=data/age_data_remodelled

rm -f data/age_chunked*

split -C 1m --numeric-suffixes $fpath data/age_chunked

for chunk in `ls data/age_chunked*`; do
    sort -k2 -n -t, $chunk > "$chunk"_sorted
    mv "$chunk"_sorted $chunk
done

python3 ./2_sort_file_contents_second_field.py

echo "verifying results...."
total_results=`awk -F',' '{print $2}' data/age_sorted_large.txt  | uniq | wc -l`
if [[ $total_results -eq 91 ]]; then
	echo "Results OK"
else
	echo "Unexpected results"
fi


# TODO: merge back chunked sorts
# keep N file pointers open


#############

### inline sorting with storage constraint

#############

# f = open('really_big_file.dat')
# def read1k():
#     return f.read(1024)

# for piece in iter(read1k, ''):
#     process_data(piece)

###########

# for line in open('really_big_file.dat'):
#     process_data(line)
########

# def read_in_chunks(file_object, chunk_size=1024):
#     """Lazy function (generator) to read a file piece by piece.
#     Default chunk size: 1k."""
#     while True:
#         data = file_object.read(chunk_size)
#         if not data:
#             break
#         yield data


# for piece in read_in_chunks(f):
#     process_data(piece)
################

