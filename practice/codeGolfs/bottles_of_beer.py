for bottle_count in xrange(99,1,-1):
    if bottle_count > 1:
        print "%s bottles of beer on the wall, %s bottles of beer."%(bottle_count, bottle_count)
        if bottle_count == 2:
            print "Take one down and pass it around, %s bottle of beer on the wall.\n"%(bottle_count-1)
        else:
            print "Take one down and pass it around, %s bottles of beer on the wall.\n"%(bottle_count-1)
        continue    
    print "1 bottle of beer on the wall, 1 bottle of beer."
    print "Go to the store and buy some more, 99 bottles of beer on the wall."
