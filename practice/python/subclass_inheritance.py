#!/usr/bin/env python2

class A():
    def __test(self):
        return "A test"
    def test(self):
        return self.__test()

########################################
class B(A):
    def __test(self):
        return "B test"
    def _ff(self):
        return '654'
    
b = B()
print "iter 1"
# calls A's test()
print b.test() 
# single _ can be called.
print b._ff()
# thunder __ appended; private; can't be called
# b.__test()
print

class B(A):
    def __init__(self):
        self.test = '123'
    def __test(self):
        return "B test"

print "iter 2"
b = B()
# B's test var is now a constant with '123'; A's test attrib has been over ridden
# this gives error
# b.test()
# print test's value then
print b.test
print

class B(A):
    def __init__(self):
        self.test = '123'
    def __test(self):
        return "B test"
    def cc(self):
        self.test = '245'

print "iter 3"
b = B()
# change test value
b.cc()
# print new test value
print b.test
# reset test value with B's __init__
b.__init__()
# print new test value
print b.test
print

class B(A):
    def __test(self):
        return "B test"
    def cc(self):
        return self.__test()

print "iter 4"
b = B()
# return B's __test value
print b.cc()
# return A's __test value
print b.test()
