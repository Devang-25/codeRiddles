import fileinput, operator

# testcases/*.java

prof = {}
for line in fileinput.input():
    #print line,
    if 'class ' in line:
        temp = line.split()
        name = temp[temp.index('class') + 1].split('{')[0]
        #print "if: ",name
        prof[name] = []
    elif '= new ' in line:
        temp = line.split('= new ')
        temp1 = temp[0].split()[0]
        temp2 = temp[1].split()[0].split('(')[0]
        if temp1 == temp2:
            prof[name].append(temp1)

#for i,e in prof.iteritems(): print '{} -> {}'.format(i,e)
print max(prof.iteritems(), key=operator.itemgetter(1))[0]
