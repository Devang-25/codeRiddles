#!/bin/env python3

######### kwargs

def bar(**ab):
    return ab

def foo(**kwargs):
    return bar(**kwargs)

print("\n\t**kwargs usage in nested methods")
print(foo(a=2,b=55))
# Out[34]: {'a': 2, 'b': 55}
print(foo(**{'a':2, 'b':55}))
# Out[35]: {'a': 2, 'b': 55}

######### __repr__

class Point:
  def __init__(self, x, y):
    self.x, self.y = x, y

p = Point(1, 2)
# In [127]: p
# Out[127]: Point(x=1, y=2)

######### __str__ | __contains__ | __iter__

class GraphVertexMixed(object):

    def __init__(self, key):
        self._id = key
        self.vertList = {}
        self.inward_count = 0
        self.connectedTo = {}
        self.props = {}
        
    def __contains__(self, k):                                                    
        return k in self.vertList                                                 

    def __iter__(self):                                                           
        return iter(self.vertList.values())      

    def __str__(self):
        return "Graph's ID is: %s" % self._id
    
    def __repr__(self):
        return """
        GraphVertexMixed( 
        \t _id=%s, 
        \t vertList=%s, 
        \t inward_count=%s, 
        \t connectedTo=%s, 
        \t props=%s
        )
        """ % \
            (                                                                                                                                                   
                str(self._id),
                str(self.vertList),
                str(len(self.getConnections())),                                                                                                   
                self.inward_count,
                str(self.props)                                                                                                                           
            )                                                                                                                                    
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def setProperties(self, **kwargs):
        self.props.update(kwargs)

G = GraphVertexMixed(10)

G.vertList = {1: 20, 'b': 40}
G.inward_count = 10
G.connectedTo = {2:4}
G.props = { "name" : "bumblebee"}

print("\n\t __str__ usage")
print("-- ", G)

print("\n\t __repr__ usage\n")
# __repr__ is overridden by _str__
# __repr__ is of use in interpreter, or for developers mostly. 
# To prevent this, comment out __str__() definition in class GraphVertexMixed
# and then uncomment below to see new results:
# print("-- ", G)
print("-- ", G.__repr__)
# print("-- ", G.__repr__())

print("\n\t__contains__ usage")
print("-- ", 1 in G)

print("\n\t__iter__ usage")
for v in G:
    print("-- ", v)
