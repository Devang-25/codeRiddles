steps = 0

def negative(n):
    return n-1

def posdiv(n):
    if not n%2:
        return n/2
    else:
        return n
    
def primdiv(n):
    if not n%3:
        return n/3
    else:
        return n
    
def main(n):
    if n>1:
        global steps
        steps+=1
        print negative(n), posdiv(n),primdiv(n)
        return (1 + min(negative(n), posdiv(n), primdiv(n)))
    else:
        return 0

if __name__ == '__main__':
    print main(int(raw_input())), steps
