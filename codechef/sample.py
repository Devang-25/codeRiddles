a=[]
from collections import Counter
i=int(raw_input('No. of test cases? : '))
# OUT: No. of test cases? : 42
if(1<=i<=100):
    for k in xrange(i):
        a.append(raw_input("Enter test case %s: "% (k+1)))
        c=Counter(a[k].strip())
        print c[0]
        
    

# OUT: Enter test case 1: asd
# OUT: 0
# OUT: Enter test case 2: sffasf
# OUT: 0

c
# OUT: Counter({'f': 3, 's': 2, 'a': 1})
c.values
# OUT: <built-in method values of Counter object at 0x9f855cc>
c[2]
# OUT: 0
c.view
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: AttributeError: 'Counter' object has no attribute 'view'
c.viewkeys
# OUT: <built-in method viewkeys of Counter object at 0x9f855cc>
c.elements
# OUT: <bound method Counter.elements of Counter({'f': 3, 's': 2, 'a': 1})>
c.pop
# OUT: <built-in method pop of Counter object at 0x9f855cc>
c
# OUT: Counter({'f': 3, 's': 2, 'a': 1})
c.pop(a)
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: unhashable type: 'list'
c.pop('a')
# OUT: 1
c
# OUT: Counter({'f': 3, 's': 2})
c.viewvalues('s')
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: viewvalues() takes no arguments (1 given)
c.viewvalues(s)
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 's' is not defined
c.viewvalues()
# OUT: dict_values([2, 3])
