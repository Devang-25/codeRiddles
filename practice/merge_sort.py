def merge(a, i = 0, j = 0, l = []):
    l1 = sorted(a[:len(a)/2])
    l2 = sorted(a[len(a)/2:])
    for k in xrange(len(a)):
        # check for list out of range
        if  i == len(l1):
            l.extend(l2[j:]); return l
        elif  j == len(l2):
            l.extend(l1[i:]); return l
        # compare
        if l1[i] < l2[j]:
            l.append(l1[i])
            i+=1
        elif l2[j] < l1[i]:
            l.append(l2[j])
            j+=1
        elif l1[i]==l2[j]:
            l.append(l1[i])
            l.append(l2[j])
            i+= 1; j+= 1
    # return final list
    return l


x = raw_input("Enter space separated list of integers: ").split()
print merge(map(int, x))
