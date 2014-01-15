def russian(a,b):
    """
    Wikipedia: Ancient Egyptian Multiplication"""
    x = a; y = b
    z = 0
    while x > 0:
        print "x, y, z : ", x,y,z
        if x % 2 == 1: z += y 
        y <<= 1 # double y
        x >>= 1 # halve x
    print
    return z

ip = map(int, raw_input().split())
ans = reduce(lambda x,y: russian(x,y), ip)
print "Multiplication: ", ans

'''
# What reduce() does.. 
for i in xrange(1,len(ip)):
    x = russian(x, ip[i])
'''
