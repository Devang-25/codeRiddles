def fibonacci(n):
    i = 0
    start = 1
    start_1 = 1
    while i < n:
        if i in (0,1):
            print 1
        else:
            temporary = start + start_1
            print temporary
            start_1 = start
            start = temporary
        i = i + 1
            
fibonacci(19)
