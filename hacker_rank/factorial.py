def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
t=int(raw_input())
r=[]
if 1<=t<=100:
    for i in range(t):
        p=int(raw_input())
        r.append(factorial(p))
    for i in range(t):
        print r[i]