#!/usr/bin/env python3

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
print("iter 1")
# calls A's test()
print(b.test())
# single _ can be called.
print(b._ff())
# thunder __ appended; private; can't be called
# b.__test()
print

class B(A):
    def __init__(self):
        self.test = '123'
    def __test(self):
        return "B test"

print("iter 2")
b = B()
# B's test var is now a constant with '123'; A's test attrib has been over ridden
# this gives error
# b.test()
# print(test's value then)
print(b.test)
print

class B(A):
    def __init__(self):
        self.test = '123'
    def __test(self):
        return "B test"
    def cc(self):
        self.test = '245'

print("iter 3")
b = B()
# change test value
b.cc()
# print(new test value)
print(b.test)
# reset test value with B's __init__
b.__init__()
# print(new test value)
print(b.test)
print

class B(A):
    def __test(self):
        return "B test"
    def cc(self):
        return self.__test()

print("iter 4")
b = B()
# return B's __test value
print(b.cc())
# return A's __test value
print(b.test())


### below is py2 incompatible

class A():
    def __init__(self):
        pass
    def hello(self, h):
        return self.ball(h)

class B(A):
    def __init__(self, g):
        super(B, self).__init__()
        self.g = g
    def ball(self, h):
        return h*2

b = B('4') # inherits A's methods
print(b.hello('2')) # calls B.ball although that's not defined in A


########

print("iter 5")

class A():
    def __init__(self, x=2):
        self.foo = x
    def hello(self, h):
        return self.ball(h)

class B(A):
    def __init__(self, g=None):
        if g:
            super(B, self).__init__(g)
        else:
            super(B, self).__init__()
        
    def ball(self, h):
        return h*2
b = B()
print(b.foo)
b = B(5)
print(b.foo)

# =================

# multiple inheritence
# also look at http://scottlobdell.me/2015/06/multiple-inheritance-python/
# and at https://stackoverflow.com/questions/34884567/python-multiple-inheritance-passing-arguments-to-constructors-using-super

class A(object):
    def __init__(self, a):
        self.a = a
        print("called A")
        
    def aa(self):
        print("aa ", self.a)
        
class B(A):
    def __init__(self, b, z):
        self.b = b*2
        self.z = z
        print("called B")
        super(B, self).__init__(30, 3,4)
        print("x,y: ", self.x, self.y)
        
    def bb(self):
        print("bb ", self.a, self.b)
    
        
class C(A):
    def __init__(self, c, x, y):
        self.c = c*3
        self.x = x
        self.y = y
        print("called C")
        super(C, self).__init__(20)
        # super(C).__init__(c)
        
    def cc(self):
        print("cc ", self.a, self.b, self.c)
        
        
class D(B, C):
    def __init__(self, d):
        self.d = d*4
        print("called D")
        super(D, self).__init__(d, 1)
        
    def dd(self):        
        print("dd ", self.a, self.b, self.c, self.d)        

    def all(self):
        self.dd()
        self.cc()
        self.bb()
        self.aa()

print("--------------")
x = D(2)
x.all()
print(D.mro())
# import pdb; pdb.set_trace()

# called D
# called B
# called C
# called A
# x,y:  3 4
# dd  20 4 90 8
# cc  20 4 90
# bb  20 4
# aa  20
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

