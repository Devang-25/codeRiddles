# http://www.pythonchallenge.com/pc/def/channel.html

from urllib.request import urlopen

# url = 'http://www.pythonchallenge.com/pc/def/zip.html'
# print(urlopen(url).read().decode())

# url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
# data = urlopen(url).read()
# with open('channel.zip', 'wb') as f:
#     f.write(data)
    
from zipfile import ZipFile

zf = ZipFile('channel.zip')

print("sample contents of zip")
print(zf.infolist()[-3:])

filenames = zf.namelist()

readme = filenames.pop(-1)

print(zf.read(readme).decode())

comments = []

def traverse(q='90052', _prev=None):
    text = zf.read('%s.txt' % q).decode()
    comments.append(zf.getinfo('%s.txt' % q).comment.decode())
    _prev = q
    _next = text.split()[-1]
    # print("reading Next - %s :: Previous - %s" % (_next, _prev))
    if 'nothing is' in text:
        return traverse(_next, _prev)
    elif 'Divide by two' in text:
        _next = int(_prev) // 2
        print("_next is ", _next)
        return traverse(_next, _prev)
    else:
        return "Final: %s" % text

print(traverse())
print(''.join(comments))
zf.close()

# hockey.html -> look up in the air
# oxygen.html (formed from chars in the ASCII art of output)
