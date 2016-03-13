import numpy
import csv,operator,numpy
a={}
rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
for i in xrange(len(rows)):
    sa
    
as
# OUT:   File "<input>", line 4
# OUT:     as
# OUT:      ^
# OUT: SyntaxError: invalid syntax
rows
# OUT: [{'Salary': '500', 'City': 'Delhi', 'Job': 'Doctors'}, {'Salary': '400', 'City': 'Delhi', 'Job': 'Lawyers'}, {'Salary': '300', 'City': 'Delhi', 'Job': 'Plumbers'}, {'Salary': '1000', 'City': 'Hong Kong', 'Job': 'Doctors'}, {'Salary': '1200', 'City': 'Hong Kong', 'Job': 'Lawyers'}, {'Salary': '900', 'City': 'Hong Kong', 'Job': 'Plumbers'}, {'Salary': '800', 'City': 'London', 'Job': 'Doctors'}, {'Salary': '700', 'City': 'London', 'Job': 'Lawyers'}, {'Salary': '100', 'City': 'London', 'Job': 'Plumbers'}, {'Salary': '900', 'City': 'Tokyo', 'Job': 'Doctors'}, {'Salary': '800', 'City': 'Tokyo', 'Job': 'Lawyers'}, {'Salary': '400', 'City': 'Tokyo', 'Job': 'Plumbers'}]
rows[0]
# OUT: {'Salary': '500', 'City': 'Delhi', 'Job': 'Doctors'}
rows[][0]
# OUT:   File "<input>", line 1
# OUT:     rows[][0]
# OUT:          ^
# OUT: SyntaxError: invalid syntax
for i in xrange(len(rows)):
    print rows[i].values()
    

# OUT: ['500', 'Delhi', 'Doctors']
# OUT: ['400', 'Delhi', 'Lawyers']
# OUT: ['300', 'Delhi', 'Plumbers']
# OUT: ['1000', 'Hong Kong', 'Doctors']
# OUT: ['1200', 'Hong Kong', 'Lawyers']
# OUT: ['900', 'Hong Kong', 'Plumbers']
# OUT: ['800', 'London', 'Doctors']
# OUT: ['700', 'London', 'Lawyers']
# OUT: ['100', 'London', 'Plumbers']
# OUT: ['900', 'Tokyo', 'Doctors']
# OUT: ['800', 'Tokyo', 'Lawyers']
# OUT: ['400', 'Tokyo', 'Plumbers']
for i in xrange(len(rows)):
    print rows[i].values()[0]
    

# OUT: 500
# OUT: 400
# OUT: 300
# OUT: 1000
# OUT: 1200
# OUT: 900
# OUT: 800
# OUT: 700
# OUT: 100
# OUT: 900
# OUT: 800
# OUT: 400
p=[]
for i in xrange(len(rows)):
    p.append(rows[i].values()[0])
    

p
# OUT: ['500', '400', '300', '1000', '1200', '900', '800', '700', '100', '900', '800', '400']
p[0]
# OUT: '500'
for i in xrange(len(rows)):
    print rows[i].values()[0]
    

# OUT: 500
# OUT: 400
# OUT: 300
# OUT: 1000
# OUT: 1200
# OUT: 900
# OUT: 800
# OUT: 700
# OUT: 100
# OUT: 900
# OUT: 800
# OUT: 400
rows
# OUT: [{'Salary': '500', 'City': 'Delhi', 'Job': 'Doctors'}, {'Salary': '400', 'City': 'Delhi', 'Job': 'Lawyers'}, {'Salary': '300', 'City': 'Delhi', 'Job': 'Plumbers'}, {'Salary': '1000', 'City': 'Hong Kong', 'Job': 'Doctors'}, {'Salary': '1200', 'City': 'Hong Kong', 'Job': 'Lawyers'}, {'Salary': '900', 'City': 'Hong Kong', 'Job': 'Plumbers'}, {'Salary': '800', 'City': 'London', 'Job': 'Doctors'}, {'Salary': '700', 'City': 'London', 'Job': 'Lawyers'}, {'Salary': '100', 'City': 'London', 'Job': 'Plumbers'}, {'Salary': '900', 'City': 'Tokyo', 'Job': 'Doctors'}, {'Salary': '800', 'City': 'Tokyo', 'Job': 'Lawyers'}, {'Salary': '400', 'City': 'Tokyo', 'Job': 'Plumbers'}]
for i in xrange(len(rows)):
    print rows[i].values()
    

# OUT: ['500', 'Delhi', 'Doctors']
# OUT: ['400', 'Delhi', 'Lawyers']
# OUT: ['300', 'Delhi', 'Plumbers']
# OUT: ['1000', 'Hong Kong', 'Doctors']
# OUT: ['1200', 'Hong Kong', 'Lawyers']
# OUT: ['900', 'Hong Kong', 'Plumbers']
# OUT: ['800', 'London', 'Doctors']
# OUT: ['700', 'London', 'Lawyers']
# OUT: ['100', 'London', 'Plumbers']
# OUT: ['900', 'Tokyo', 'Doctors']
# OUT: ['800', 'Tokyo', 'Lawyers']
# OUT: ['400', 'Tokyo', 'Plumbers']
import csv,numpy
a=dict()
rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
for i in xrange(len(rows)):
    if rows[i].values()[2] in a:
        a[rows[i].values()[2]].append(int(rows[i].values()[0]))
    else:
        a[rows[i].values()[2]]=[int(rows[i].values()[0])]


z
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 'z' is not defined
a
# OUT: {'Plumbers': [300, 900, 100, 400], 'Lawyers': [400, 1200, 700, 800], 'Doctors': [500, 1000, 800, 900]}
a[0]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: KeyError: 0
from collections import defaultdict
for i in xrange(len(rows)):
    print rows[i]
    

# OUT: {'Salary': '500', 'City': 'Delhi', 'Job': 'Doctors'}
# OUT: {'Salary': '400', 'City': 'Delhi', 'Job': 'Lawyers'}
# OUT: {'Salary': '300', 'City': 'Delhi', 'Job': 'Plumbers'}
# OUT: {'Salary': '1000', 'City': 'Hong Kong', 'Job': 'Doctors'}
# OUT: {'Salary': '1200', 'City': 'Hong Kong', 'Job': 'Lawyers'}
# OUT: {'Salary': '900', 'City': 'Hong Kong', 'Job': 'Plumbers'}
# OUT: {'Salary': '800', 'City': 'London', 'Job': 'Doctors'}
# OUT: {'Salary': '700', 'City': 'London', 'Job': 'Lawyers'}
# OUT: {'Salary': '100', 'City': 'London', 'Job': 'Plumbers'}
# OUT: {'Salary': '900', 'City': 'Tokyo', 'Job': 'Doctors'}
# OUT: {'Salary': '800', 'City': 'Tokyo', 'Job': 'Lawyers'}
# OUT: {'Salary': '400', 'City': 'Tokyo', 'Job': 'Plumbers'}
d = defaultdict(list)
d
# OUT: defaultdict(<type 'list'>, {})
for i in xrange(len(rows)):
    d[rows[i].values()[2]].append(int(rows[i].values()[0]))
    

d
# OUT: defaultdict(<type 'list'>, {'Plumbers': [300, 900, 100, 400], 'Lawyers': [400, 1200, 700, 800], 'Doctors': [500, 1000, 800, 900]})
d
# OUT: defaultdict(<type 'list'>, {'Plumbers': [300, 900, 100, 400], 'Lawyers': [400, 1200, 700, 800], 'Doctors': [500, 1000, 800, 900]})
d[0]
# OUT: []
d[1]
# OUT: []
d[2]
# OUT: []
d
# OUT: defaultdict(<type 'list'>, {0: [], 1: [], 2: [], 'Lawyers': [400, 1200, 700, 800], 'Plumbers': [300, 900, 100, 400], 'Doctors': [500, 1000, 800, 900]})
d
# OUT: defaultdict(<type 'list'>, {0: [], 1: [], 2: [], 'Lawyers': [400, 1200, 700, 800], 'Plumbers': [300, 900, 100, 400], 'Doctors': [500, 1000, 800, 900]})
d.pop[0]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
d.pop(0)
# OUT: []
d.pop(1)
# OUT: []
d.pop(0)
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: KeyError: 0
d
# OUT: defaultdict(<type 'list'>, {2: [], 'Lawyers': [400, 1200, 700, 800], 'Plumbers': [300, 900, 100, 400], 'Doctors': [500, 1000, 800, 900]})
d.pop(2)
# OUT: []
d
# OUT: defaultdict(<type 'list'>, {'Lawyers': [400, 1200, 700, 800], 'Plumbers': [300, 900, 100, 400], 'Doctors': [500, 1000, 800, 900]})
d.values()
# OUT: [[400, 1200, 700, 800], [300, 900, 100, 400], [500, 1000, 800, 900]]
d.keys()
# OUT: ['Lawyers', 'Plumbers', 'Doctors']
d.values()[0]
# OUT: [400, 1200, 700, 800]
d.values()[0][0]
# OUT: 400
d.values()[0]
# OUT: [400, 1200, 700, 800]
d.values()[01
]
# OUT: [300, 900, 100, 400]
d.values()[2]
# OUT: [500, 1000, 800, 900]
d.values()[0]
# OUT: [400, 1200, 700, 800]
d.values()[1]
# OUT: [300, 900, 100, 400]
d.values()[2]
# OUT: [500, 1000, 800, 900]
d.keys()
# OUT: ['Lawyers', 'Plumbers', 'Doctors']
d.keys()[0]
# OUT: 'Lawyers'
d.keys()[1]
# OUT: 'Plumbers'
d.keys()[2]
# OUT: 'Doctors'
d.values()
# OUT: [[400, 1200, 700, 800], [300, 900, 100, 400], [500, 1000, 800, 900]]
d
# OUT: defaultdict(<type 'list'>, {'Lawyers': [400, 1200, 700, 800], 'Plumbers': [300, 900, 100, 400], 'Doctors': [500, 1000, 800, 900]})
len(d)
# OUT: 3
for i in xrange(len(d)):
sd 
# OUT:   File "<input>", line 3
# OUT:     sd
# OUT:      ^
# OUT: IndentationError: expected an indented block
import numpy
for i in xrange(len(d)):
    numpy.median(d.values()[0])
    

# OUT: 750.0
# OUT: 750.0
# OUT: 750.0
for i in xrange(len(d)):
    numpy.median(d.values()[i])
    

# OUT: 750.0
# OUT: 350.0
# OUT: 850.0
for i in xrange(len(d)):
    int(numpy.median(d.values()[i]))
    

# OUT: 750
# OUT: 350
# OUT: 850
for i in xrange(len(d)):
    print d.keys()[i]+","+int(numpy.median(d.values()[i]))
    

# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 2, in <module>
# OUT: TypeError: cannot concatenate 'str' and 'int' objects
for i in xrange(len(d)):
    print d.keys()[i]+","+str(numpy.median(d.values()[i]))
    

# OUT: Lawyers,750.0
# OUT: Plumbers,350.0
# OUT: Doctors,850.0
d.values()
# OUT: [[400, 1200, 700, 800], [300, 900, 100, 400], [500, 1000, 800, 900]]
d.keys()
# OUT: ['Lawyers', 'Plumbers', 'Doctors']
d
# OUT: defaultdict(<type 'list'>, {'Lawyers': [400, 1200, 700, 800], 'Plumbers': [300, 900, 100, 400], 'Doctors': [500, 1000, 800, 900]})
rows
# OUT: [{'Salary': '500', 'City': 'Delhi', 'Job': 'Doctors'}, {'Salary': '400', 'City': 'Delhi', 'Job': 'Lawyers'}, {'Salary': '300', 'City': 'Delhi', 'Job': 'Plumbers'}, {'Salary': '1000', 'City': 'Hong Kong', 'Job': 'Doctors'}, {'Salary': '1200', 'City': 'Hong Kong', 'Job': 'Lawyers'}, {'Salary': '900', 'City': 'Hong Kong', 'Job': 'Plumbers'}, {'Salary': '800', 'City': 'London', 'Job': 'Doctors'}, {'Salary': '700', 'City': 'London', 'Job': 'Lawyers'}, {'Salary': '100', 'City': 'London', 'Job': 'Plumbers'}, {'Salary': '900', 'City': 'Tokyo', 'Job': 'Doctors'}, {'Salary': '800', 'City': 'Tokyo', 'Job': 'Lawyers'}, {'Salary': '400', 'City': 'Tokyo', 'Job': 'Plumbers'}]
sorted(a.iteritems(),key=operator.itemgetter(1)))
# OUT:   File "<input>", line 1
# OUT:     sorted(a.iteritems(),key=operator.itemgetter(1)))
# OUT:                                                     ^
# OUT: SyntaxError: invalid syntax
import operator
sorted(d.iteritems(),key=operator.itemgetter(1))
# OUT: [('Plumbers', [300, 900, 100, 400]), ('Lawyers', [400, 1200, 700, 800]), ('Doctors', [500, 1000, 800, 900])]
sorted(d.iteritems(),key=operator.itemgetter(0))
# OUT: [('Doctors', [500, 1000, 800, 900]), ('Lawyers', [400, 1200, 700, 800]), ('Plumbers', [300, 900, 100, 400])]
sorted(d.iteritems(),key=operator.itemgetter(2))
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: IndexError: tuple index out of range
sorted(d.iteritems(),key=operator.itemgetter(1))
# OUT: [('Plumbers', [300, 900, 100, 400]), ('Lawyers', [400, 1200, 700, 800]), ('Doctors', [500, 1000, 800, 900])]
d.items()
# OUT: [('Lawyers', [400, 1200, 700, 800]), ('Plumbers', [300, 900, 100, 400]), ('Doctors', [500, 1000, 800, 900])]
d.items()[0]
# OUT: ('Lawyers', [400, 1200, 700, 800])
d.items()[0][1]
# OUT: [400, 1200, 700, 800]
d.itervalues()
# OUT: <dictionary-valueiterator object at 0xab0b3ec>
d.iterkeys
# OUT: <built-in method iterkeys of collections.defaultdict object at 0xab2eadc>
d.iterkeys()
# OUT: <dictionary-keyiterator object at 0xab0b0cc>
d.iteritems()
# OUT: <dictionary-itemiterator object at 0xab0b4dc>
d.iteritems()[0]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'dictionary-itemiterator' object has no attribute '__getitem__'
d.iteritems()()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'dictionary-itemiterator' object is not callable
d.iteritems(
)
# OUT: <dictionary-itemiterator object at 0xab0beb4>
a
# OUT: {'Plumbers': [300, 900, 100, 400], 'Lawyers': [400, 1200, 700, 800], 'Doctors': [500, 1000, 800, 900]}
d
# OUT: defaultdict(<type 'list'>, {'Lawyers': [400, 1200, 700, 800], 'Plumbers': [300, 900, 100, 400], 'Doctors': [500, 1000, 800, 900]})
for i in xrange(len(d)):
    print d.keys()[i]+","+str(numpy.median(d.values()[i]))
    

# OUT: Lawyers,750.0
# OUT: Plumbers,350.0
# OUT: Doctors,850.0
d.items()[p][1].sort()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: list indices must be integers, not list
int(d.items()[p][1]).sort()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: list indices must be integers, not list
d.items()[p][1]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: list indices must be integers, not list
d.items()[0][1]
# OUT: [400, 1200, 700, 800]
d.items()[0][1].sort()
d.items()[0][1]
# OUT: [400, 700, 800, 1200]
d.items()[1][1]
# OUT: [300, 900, 100, 400]
d.items()[1][0]
# OUT: 'Plumbers'
d.items()[1][1].sort()
d.items()[2][1].sort()
d.items()[2][1]
# OUT: [500, 800, 900, 1000]
d.items()[1][1]
# OUT: [100, 300, 400, 900]
for i in xrange(len(d)):
    print d.keys()[i]+","+str(numpy.median(d.values()[i]))
    

# OUT: Lawyers,750.0
# OUT: Plumbers,350.0
# OUT: Doctors,850.0
d
# OUT: defaultdict(<type 'list'>, {'Lawyers': [400, 700, 800, 1200], 'Plumbers': [100, 300, 400, 900], 'Doctors': [500, 800, 900, 1000]})
