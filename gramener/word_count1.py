f = open('gr.txt').read()
fq={}
c=0
words=0
lines=0
for char in f:
    if char in fq:
        fq[char]+=1
    else:
        fq[char]=1
    if char=="\n":
        lines+=1
    if char==" " or char=="\n":
        words+=1
print lines,words,sum(fq.values())
