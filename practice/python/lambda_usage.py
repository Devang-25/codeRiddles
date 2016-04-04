#!/usr/bin/env python3

class A:
    def h(self, x):
        return lambda a=x: self.g(a)
    def g(self, y):
        return y*4

c = A()
print(c.h(5)())
    
class B:
    def h(self, x):
        return lambda x: self.g(x)
    def g(self, y):
        return y*4

c = B()
print(c.h(5)(4))

class C:
    def h(self, x):
        return lambda f=self.g, a=x: f(a)
    def g(self, y):
        return y*4

c = C()
print(c.h(3)())
