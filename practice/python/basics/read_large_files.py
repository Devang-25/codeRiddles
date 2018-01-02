# 1 GB RAM, but 4 GB file size.
# https://en.wikipedia.org/wiki/External_sorting

# https://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python
# https://stackoverflow.com/a/519653/1332401
# https://stackoverflow.com/questions/1661986/why-doesnt-pythons-mmap-work-with-large-files

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

# read files N lines at a time
f = open('file_age.txt')

from itertools import islice

N = 10

while True:
    data = islice(f, N)
    if not data:
        break

# bash
# split -C 20m --numeric-suffixes input_filename output_prefix
