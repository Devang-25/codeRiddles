def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

import itertools
upto_4000000 = itertools.takewhile(lambda x: x <= 4000000, fibonacci())
print(sum(x for x in upto_4000000 if x % 2 == 0))
