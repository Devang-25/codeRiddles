# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
import functools
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

# char_map = pickle.loads(urlopen(url).read())
char_map = pickle.load(open('banner.p', 'rb'))

z = lambda x,y: x*y

def process(line):
    """
    returns single string combined from reduction of a character multipled by number
    provided in list of lists
    """
    return ''.join(functools.reduce(z, pair) for pair in line)

data = '\n'.join([process(line) for line in char_map])

print(data)
