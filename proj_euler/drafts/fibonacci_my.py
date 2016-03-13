def fibo(a=-1,b=1,upto=raw_input("Enter upper limit: ")):
    while a+b<upto:
        a,b = b,a+b
        yield b

x = sum(i for i in fibo() if not i%2)
print '\n',"sum = %d" %(x)
