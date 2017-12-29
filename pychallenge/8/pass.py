import re
import ast
import bz2
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'

html = urlopen(url).read()

# print(html.decode())

# search in bytes with regex b'' format
# but this brings the format: b"'<escaped encoded text>'"
# which is difficult to deal with, especially
# since we're automating this retrieval of user/pass from html source code

# data = re.findall(b'\'BZ.*\'', res)
# # [b"'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084'",
# #  b"'BZh91AY&SY\\x94$|\\x0e\\x00\\x00\\x00\\x81\\x00\\x03$ \\x00!\\x9ah3M\\x13<]\\xc9\\x14\\xe1BBP\\x91\\xf08'"]

html = html.decode()
data = re.findall(r'\'BZ.*\'', html)
# ["'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084'",
#  "'BZh91AY&SY\\x94$|\\x0e\\x00\\x00\\x00\\x81\\x00\\x03$ \\x00!\\x9ah3M\\x13<]\\xc9\\x14\\xe1BBP\\x91\\xf08'"]

# we'd like to bring the format "'<escaped encoded text>'"
# to the format "b'<escaped encoded text>'" for passing it as input for decompression
user = ast.literal_eval('b%s' % data[0])
pwd =  ast.literal_eval('b%s' % data[1])

# both strings starting with BZ. Meaning it's a hashed / compressed form of some kind
# a but of googling reveals bzip2 format. https://en.wikipedia.org/wiki/Bzip2#File_format
# Also, http://wiki.pythonchallenge.com/index.php?title=Level8:Main_Page
user = bz2.decompress(user).decode()
pwd = bz2.decompress(pwd).decode()

print("User: ", user)
print("Password: ", pwd)

# next url > hyper link to bee's image
# curl http://huge:file@www.pythonchallenge.com/pc/return/good.html
# http://www.voidspace.org.uk/python/articles/urllib2.shtml#id6

# _next = re.search('href=".*.html"', res).group()
# _next = _next.split("=")[-1]
# _next = ast.literal_eval(_next)

_next = re.search('href="(.*.html)"', html).groups()[0]

from posixpath import dirname, join

_next = join(dirname(url), _next)

from urllib.request import HTTPPasswordMgrWithDefaultRealm, \
    HTTPBasicAuthHandler, \
    build_opener, \
    HTTPHandler, \
    Request

password_mgr = HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/"
password_mgr.add_password(None, top_level_url, user, pwd)
handler = HTTPBasicAuthHandler(password_mgr)
opener = build_opener(HTTPHandler, handler)
# request = Request(url)
# urlopen(request)
res = opener.open(_next).read()
with open('next.html', 'wb') as f:
    f.write(res)
print(res.decode())
