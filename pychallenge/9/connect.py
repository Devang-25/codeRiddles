# http://www.pythonchallenge.com/pc/return/good.html

from PIL import Image

img = Image.open('good.png')

all_blacks = {}
for w in range(width):
    for h in range(height):
        if pix[w,h] == (0,0,0):
            all_blacks['%s_%s' % (w,h)] = pix[w,h]

{k:v for k,v in all_blacks.items() if int(k.split('_')[0]) < w//2}

