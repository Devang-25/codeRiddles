import sys

cache = {0:0}

def change(num):
    if num in cache:
        return cache[num]
    else:
        cache[num] = max(num, change(num / 4) + change(num / 3) + change(num / 2))
        return cache[num]

#For codechef to test
if __name__ == "__main__":
    while True:
        try:
            num = int(raw_input())
            sys.stdout.write("%dn" % change(num))
        except:
            break

'''
import sys
t=int(raw_input())
a=[]
b=[]
c=[]
if 1<=t<=10:
    n=int(raw_input())
    if 1<=n<=1000000000:
        def divi(n):
            if n>0:
                a.append(n/2)
                b.append(n/3)
                c.append(n/4)
def tree_divi(x):
    if x==0:
        return 1
    else 
'''        