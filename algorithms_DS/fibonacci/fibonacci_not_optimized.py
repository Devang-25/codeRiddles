#!/usr/bin/env python2
#!/usr/bin/python2.7

def fib(n):
    a = 0
    b = 1
    for i in xrange(n):
        a,b = b, a+b
        return a

print fib(10 ** 7)
