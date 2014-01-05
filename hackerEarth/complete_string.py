def check_complete(ip_str):
    if len(ip_str)<=100:
        pass
    else:
        quit()
    unique_input = set(list(ip_str))    
    range_check = [ord(i) for i in unique_input]
    #print "\nRange: ",sorted(range_check),"\n"
    if ((max(range_check)< 123) and (min(range_check)>=97)):
        if (len(range_check)==26):
            return 'YES'
        else:
            return 'NO'
    else:
        quit()
        #quit('\n>> alphabets not integer.. quit')

try:
    N = int(raw_input())
    if 1<=N<=10:        
        #alphas = list(map(chr, range(97, 123)))
        check = []
        for i in xrange(N):
            check.append(check_complete(raw_input()))
        for i in xrange(N):
            print check[i]
    else:
        quit()
        #quit('\n>> not in range.. quit')
except:
    quit()
    #quit('\n>> not integer.. quit')
    
