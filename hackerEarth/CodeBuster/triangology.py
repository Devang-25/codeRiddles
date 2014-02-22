class TriangleCheck:
    ''' Check triangle inequality'''
    def __init__(self, sides):
        self.sides = sides

    def check_triangle(self):
        smallest,medium,biggest = sorted(self.sides)
        return smallest+medium>biggest and all(s>0 for s in self.sides)

if __name__ == '__main__': 
    try:
        T = int(raw_input())
        ans = []
        for i in xrange(T):
            # input values
            sides = map(int, raw_input().split())
            #check on input
            assert len(sides)==3
            # intiate class object
            TC = TriangleCheck(sides)
            # append result to an answers list, to be printed later
            ans.append(TC.check_triangle().real)
        for i in ans: print i
    except:
        raise
