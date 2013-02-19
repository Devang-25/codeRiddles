f = open(raw_input("Enter the file name in the present directory you'd like this program to run upon: ")).read()
fq={}
c=0
w=0
d=0
print f
for line in f:
#    print line,
    for char in line:
#        print char,
        if char in fq:
            fq[char]+=1
        else:
            fq[char]=1
        if char=="\n":
            print "1 new line found.."
            c+=1
        if char==" " or char=="\n":
            w+=1
#        if fq['''"''']%2==1:
#            print char,


print fq
print "\n%d lines exist in the given file"%c
print "\nThe characters(including special ones) used in the file are: "
for i in fq:
    if i=="\n":
        print "\\n",
    else:
        print i,

print "\nNo of characters%d"%sum(fq.values())

print "\nno. of words found = %d"%w
