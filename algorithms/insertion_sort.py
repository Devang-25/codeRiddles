def insert_sort():
    a=[]
    for i in xrange(5):
        a.append(int(raw_input("\nInsert No.: ")))
        print a
    raw_input('\n\t\t\t\tInsertion sort now beigns..\n')
    for j in range(1,5):
        x=a[j]
        i=j-1
        while i>0 and a[i]>x:
            a[i+1]=a[i]
            i-=1
            print '\t\t\t\tLoop Flag Test: ',a
        a[i+1]=x
        if a[0]>a[1]:
            p=a[0]
            a[0]=a[1]
            a[1]=p
    print '\nFinal Sorted Array --> ',a,'\n'

insert_sort()
while raw_input('wish to sort more? (y/n) ').upper()=='Y':
    insert_sort()
        
