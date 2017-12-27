#!/usr/bin/python3

# http://www.pythonchallenge.com/pc/def/oxygen.html

# Usage:
# $ python stegno.py  | tail

#######################################################################
# [OT] Side notes:

# if you use this script like this: $ python stegno.py  | head
# ..you'd get:

# ...
# ...
# 0 8 (107, 104, 51, 255)
# 0 9 (119, 120, 63, 255)
# Traceback (most recent call last):
#   File "stegno.py", line 45, in <module>
#     print(w,h,pix[w,h], flush=False)
# BrokenPipeError: [Errno 32] Broken pipe

# or if you use flush=True within your print() statements, you'd get:
# Traceback (most recent call last):
#   File "stegno.py", line 47, in <module>
#     print(w,h,pix[w,h], flush=True)
# BrokenPipeError: [Errno 32] Broken pipe
# Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
# BrokenPipeError: [Errno 32] Broken pipe

# read up on it at https://stackoverflow.com/questions/26692284/brokenpipeerror-in-python
# "trying to write on a pipe while the other end has been closed"
# This is due to the fact that the head utility reads from stdout, then promptly closes it.

# here's how to avoid it while continuing to use pip-head combo on python's outputs
# https://stackoverflow.com/a/26736013/1332401
#######################################################################

# import png

# pr  = png.Reader('oxygen.png')

# In [18]: pr.read()
# Out[18]: 
# (629,
#  95,
#  <map at 0x7fa426be9518>,
#  {'alpha': True,
#   'background': (0, 0, 0),
#   'bitdepth': 8,
#   'greyscale': False,
#   'interlace': 0,
#   'planes': 4,
#   'size': (629, 95)})

from PIL import Image

img = Image.open('oxygen.png')
pix = img.load()
# In [56]: pix
# Out[56]: <PixelAccess at 0x7fa425372eb0>

# http://pillow.readthedocs.io/en/3.4.x/reference/PixelAccess.html

# data = img.getdata()
# # In [57]: data.pixel_access()
# # Out[57]: <PixelAccess at 0x7fa426f842b0>

width, height = img.size

# In [64]: pix[4,4]
# Out[64]: (37, 20, 0, 255)

# In [66]: img.mode
# Out[66]: 'RGBA'
# https://www.w3.org/TR/PNG-DataRep.html#DR.Alpha-channel

import sys

def _void_f(*args,**kwargs):
    pass

h = height//2
for w in range(width):
    # for h in range(height//2):
    try:
        print(w,h,pix[w,h], flush=True)
    except (BrokenPipeError, IOError):
        sys.stdout.write = _void_f
        sys.stdout.flush = _void_f
        sys.exit()

# the above output shows us that the center line starts at 47th pixel (height wise)
# ..analyzing the pattern of RGBA values of pixels, we see that the first block is of size
# 5 pixels.
#
#   (apparently we are calling blocks being those huge boxes present in 50 shades of gray
#   in oxygen.png)
#
# ..while the rest of those blocks are 7 pixels each.

# i  j   R    G    B    A
# 0 47 (115, 115, 115, 255)
# 1 47 (115, 115, 115, 255)
# 2 47 (115, 115, 115, 255)
# 3 47 (115, 115, 115, 255)
# 4 47 (115, 115, 115, 255)
# 5 47 (109, 109, 109, 255)
# 6 47 (109, 109, 109, 255)
# 7 47 (109, 109, 109, 255)
# 8 47 (109, 109, 109, 255)
# 9 47 (109, 109, 109, 255)
# 10 47 (109, 109, 109, 255)
# 11 47 (109, 109, 109, 255)
# .....
# 600 47 (93, 93, 93, 255)
# 601 47 (93, 93, 93, 255)
# 602 47 (93, 93, 93, 255)
# 603 47 (93, 93, 93, 255)
# 604 47 (93, 93, 93, 255)
# 605 47 (93, 93, 93, 255)
# 606 47 (93, 93, 93, 255)
# 607 47 (93, 93, 93, 255)
# 608 47 (114, 112, 71, 255)
# 609 47 (112, 110, 69, 255)
# 610 47 (110, 108, 67, 255)
# 611 47 (103, 100, 59, 255)
# .....

# we now wish to iterate starting from 6th pixel (5, if 0 indexed)
# ending upto 608th pixel (607, 0 indexed)
# ..because rest of the output near the end contains arbitrary RGBA values
# which is obviously because those boxes in 50 shades of gray don't fully
# extend upto the end of the center line

# get first char from 1st block. Note that [0] because all RGB values are equal
blocks = [chr(pix[4,h][0])]

# get subsequent chars from 2nd block and so on

# starting from 5th and moving 7 pixels at a time
# 5 + 7 * i = 607
# solving for i, we get 86
# 
# which is the same as this:
# for i in range (5, 602, 7):
#     print(i)

blocks.extend([chr(pix[5+7*i, h][0]) for i in range(86)])

result = ''.join(blocks)

print(result)
try:
    print("Image Size: ", img.size, flush=True)
except (BrokenPipeError, IOError):
    sys.stdout.write = _void_f
    sys.stdout.flush = _void_f
    sys.exit()

import re

hint = re.search(r'\[.*\]', result).group()

import ast

print("%s.html" % ''.join([chr(i) for i in ast.literal_eval(hint)]))

# To search for Black colored pixels, search 0,0,0 from above output
# https://www.rapidtables.com/web/color/gray-color.html
