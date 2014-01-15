def russian(a,b):
    """
    Wikipedia: Ancient Egyptian Multiplication"""
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z += y 
        y <<= 1
        x >>= 1
    return z

ip = map(int, raw_input().split())
print reduce(lambda x,y: russian(x,y), ip)

'''
# What reduce() does.. 
for i in xrange(1,len(ip)):
    x = russian(x, ip[i])
'''
