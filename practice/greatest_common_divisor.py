def euclid_GCD(m,n):
    """
    Euclid's algorithm to find GCD 
    # 1000000 loops, best of 3: 518 ns per loop
    """
    count = 0
    while n%m!=0:
        r = n%m
        n = m
        m = r
        count+=1
    return m, count

'''
def gcd(x,y):
    """
    By Recursion
    # 1000000 loops, best of 3: 922 ns per loop
    """
    if y==0:
        return x
    else:
        return gcd(y,x%y)
'''

if __name__ == '__main__': 
    try:
        # input comma-separated elements into array
        cnt = raw_input("Enter 2 comma separated integers: ").split(',')
        # checks and converts list of strings into integers 
        cnt = map(int, cnt)
    except:
        quit('Constraint: Only integer / no space input allowed')

    if len(cnt)==2:
        gcd, iterations = euclid_GCD(min(cnt), max(cnt))
        print "GCD: ", gcd, " || iterations: ",iterations
    else:
        quit("\nOnly 2 integes allowed.. Exiting!\n")
