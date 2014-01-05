import sys

def enemy_state(loc):
    e_loc = loc[-2:]
    x = loc[:-2][::2]
    y = loc[:-2][1::2]
    if e_loc[0] <= max(x) and e_loc[0] >= min(x)\
       and e_loc[1] <= max(y) and e_loc[0] >= min(y):
        return 'INSIDE'
    else:
        return 'OUTSIDE'

if __name__ == '__main__': 
    try:
        T = int(raw_input())
        if 1<=T<=1000:
            pass
        else:
            quit()
        r = []
        for i in xrange(T):
            tri = raw_input().split()
            # checks and converts list of strings into integers 
            tri = map(int, tri)
            if len(tri)==8:
                pass
            else:
                quit()
            r.append(enemy_state(tri))
        
        for i in r:
            print i
    except:
        print "Unexpected error:", sys.exc_info()[0]  # >>sys.exc_info()<< whole exception 
        raise
