def fibo(a=0,b=1,upto=4000000):
    while b<upto:
        yield b
        print b
        a,b = b,a+b

x = sum(i for i in fibo() if not i%2)
print '\n',"sum = %d" %(x)
