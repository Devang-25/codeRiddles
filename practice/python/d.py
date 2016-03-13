for i in xrange(1,101):
    print lambda i: i%3==0 & i%5 == 0,i
