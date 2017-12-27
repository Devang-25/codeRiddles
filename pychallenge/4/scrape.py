import urllib.request

# http://www.pythonchallenge.com/pc/def/linkedlist.php

def fetch(q='12345', _prev=None):
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % q) as response:
        html = response.read().decode()
    print(html)
    _prev = q
    _next = html.split()[-1]
    if 'next nothing' in html:
        return fetch(_next, _prev)
    elif 'Divide by two' in html:
        _next = int(_prev) // 2
        print("_next is ", _next)
        return fetch(_next, _prev)
    else:
        return html

print("Final: ", fetch())

# peak.html
