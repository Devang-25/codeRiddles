T=int(raw_input()) #test cases
a=[]
#a=[[raw_input() for i in xrange(4)] for i in xrange(2)]
for i in xrange(T):
    a.append([raw_input() for i in xrange(4)])
    print
for k in xrange(len(a)):
    count=0
    O=0
    X=0
    for i in xrange(len(a[k])): 
        print a[k][i]
        if a[k][i]=='XXXX' or a[k][i]=='XXXT' or a[k][i]=='XXTX' or a[k][i]=='XTXX' or a[k][i]=='TXXX':
#            if a[k][i]!='OOOO' and a[k][i]!='OOOT' and a[k][i]!='OOTO' and a[k][i]!='OTOO' and a[k][i]!='TOOO':
            X+=1
        elif a[k][i]=='OOOO' or a[k][i]=='OOOT' or a[k][i]=='OOTO' or a[k][i]=='OTOO' or a[k][i]=='TOOO':
#            if a[k][i]!='XXXX' and a[k][i]!='XXXT' and a[k][i]!='XXTX' and a[k][i]!='XTXX' and a[k][i]!='TXXX':
            O+=1
        if '.' in a[k][i]:
            count+=1 
    
    print "X=",X," O=",O
    
    if O==1 and X==0:
        print "O won"
    elif X==1 and O==0:
        print "X won"
    elif X==0 and O==0 and count>0:
        print "Game not completed yet"
    elif X==0 and O==0 and count==0:
        print "Draw"
    else:
        print "invalid board"

    print
