#!/bin/env python3

import timeit
popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

# pop(0) - O(n)
# x = list(range(2000000))
# print("%.10f" % popzero.timeit(number=1000))
# # 4.8213560581207275
# # my laptop - 1.5628500970

# pop() - O(1)
# x = list(range(2000000))
# print("%.10f" % popend.timeit(number=1000))
# # 0.0003161430358886719
# # my laptop - 0.0001083990


print("\tpop(0)\t\tpop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))

#       pop(0)		       pop()
#################################
#       0.63203,         0.00007
#       1.54482,         0.00008
#       2.51172,         0.00008
#       3.47731,         0.00008
#       4.26797,         0.00008
#       5.33547,         0.00008
