T=int(raw_input())
a=[]
D={}
for i in xrange(T):
    a.append([raw_input() for i in xrange(4)])
    print
for k in xrange(len(a)):
    count=0
    O=0
    X=0
    for i in xrange(len(a[k])): 
        if a[k][i]=='XXXX' or a[k][i]=='XXXT' or a[k][i]=='XXTX' or a[k][i]=='XTXX' or a[k][i]=='TXXX':
            X+=1
        elif a[k][i]=='OOOO' or a[k][i]=='OOOT' or a[k][i]=='OOTO' or a[k][i]=='OTOO' or a[k][i]=='TOOO':
            O+=1
        if '.' in a[k][i]:
            count+=1
#        if 

    if O==1 and X==0:
        D[k+1]="O won"
    elif X==1 and O==0:
         D[k+1]="X won"
    elif X==0 and O==0 and count>0:
         D[k+1]="Game has not completed"
    elif X==0 and O==0 and count==0:
         D[k+1]="Draw"
    else:
        quit()
    
for i in xrange(len(D.keys())):
    print "Case #%d: %s"%(i+1,D[i+1])
