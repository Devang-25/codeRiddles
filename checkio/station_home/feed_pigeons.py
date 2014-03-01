def checkio(number):
    if number<1:
        quit()    
    c = 0
    pigns = [1]
    rem = number - 1
    #print rem

    while rem > 0:
        if pigns[-1]==1:
            c+=1
            for i in xrange(c+1):
                pigns.append(0)
            #print pigns
            j = 0
        pigns[j]+=1
        #print pigns
        j+=1
        rem -=1

    while 0 in pigns:
        pigns.remove(0)

    return len(pigns)


if __name__ == '__main__':
        print checkio(int(raw_input()))

#pigns = map(lambda x:x+1, pigns[:rem]) + pigns[rem:]
