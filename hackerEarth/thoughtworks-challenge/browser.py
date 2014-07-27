# The Best Internet Browser
"""
Sample Input:

2
www.google.com
www.hackerearth.com
"""

import sys


class CheckChar:
    """ Predicts # of chars to be entered """

    def __init__(self, url):
        self.link = url
        
    def predict(self):        
        return 4 + len(''.join([x for x in \
                                url.lstrip('www.').rstrip('.com') \
                                if x not in 'aeiou']))

if __name__=='__main__':
    try:
        N = int(raw_input())
        assert 1 <= N <= 100
        ans = []
        for i in xrange(N):
            url = raw_input()
            assert 1 <= len(url) <= 100
            CC = CheckChar(url.lower())
            ans.append((CC.predict(),len(url)))

        for i in ans:
            sys.stdout.write('{0}/{1}\n'.format(i[0],i[1]))
            #print "%d/%d"%i
    except:
        quit()
