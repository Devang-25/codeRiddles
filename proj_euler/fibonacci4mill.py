a =[1,1]
def fib(self):
    if self<3:
        return a[self-1]
    else:
        for i in range(2,self):
            a.append(a[i-1]+a[i-2])
        return a[self-1]

def final():
#    a=[1,1]
    x = int(raw_input("Enter fibonacci series term no.: "))
    print "\n","resultant: ",fib(x),"\n"

    y = raw_input('want to print the fibonacci series till %d ? (y/n)' % (x))
    if y=='y':
        for i in range(0,x):
            print a[i]
        else:
            print 'thank you!'
final()


'''
    z = raw_input('wish to print some other resultant? (y/n)')
    if z=='y':
#        a=[1,1]
        x = int(raw_input("Enter fibonacci series term no.: "))
        print "\n","resultant: ",fib(x)
    else:
         print 'next...'

#    print a,x,'test',"\n\n"
'''
