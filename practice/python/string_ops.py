from operator import itemgetter
from itertools import combinations
from itertools import product

list(combinations(['af','1d',4], 2))
# [('af', '1d'), ('af', 4), ('1d', 4)]

list(product(*['af','1d']))
# [('a', '1'), ('a', 'd'), ('f', '1'), ('f', 'd')]

a = {'a':4, 'b':2}
sorted(a.items(), key=itemgetter(1))
# [('b', 2), ('a', 4)]
sorted(a.items(), key=itemgetter(1), reverse=True)
# [('a', 4), ('b', 2)]
