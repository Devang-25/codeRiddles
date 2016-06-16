# really really really really really really
# naive approach of display dict words
# Please don't follow this ever.

def select_w(a):
    t=[]
    f=open('/usr/share/dict/words','r')
    for i in f:
        if a in i:
            t.append(i)
    print "\n\t\tPress enter to see the matched list..\n "
    raw_input()
    if len(t)==0:
        print "No such pattern found!! "
    else:
        for x in xrange(len(t)):
            if t[x].index(a)==0:
                print t[x],            
    f.close()

a=raw_input('Enter the initial word pattern: ')
select_w(a)
