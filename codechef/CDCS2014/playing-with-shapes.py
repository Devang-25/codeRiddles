class Shapes:
    ''' Check the moves'''
    def __init__(self, L):
        self.L = L
        self.A = [1]*L #the extra case
        self.B = [[1,1,1,0], [1,1,0,0],[1,0,0,0]]
        self.C = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
        self.basic = 3 # \ / =
    '''
    def sum_m(X,Y,length):
        Z = []
        for i in xrange(length):
            Z.append(X[i]+Y[i])
        return Z
    '''
    def play_with_shapes(self):
        try:
            #m_join = [[x+y for x,y in zip(B[i], C[i])] for i in xrange(3)]
            
        except:
            return 0
            
if __name__ == '__main__': 
    try:
        T = int(raw_input())
        assert 1<=T<=30
        ans = []
        for i in xrange(T):
            # input values
            L = int(raw_input())
            #check on L
            assert 2<=L<=100
            Sh = Shapes(L)
            ans.append(Sh.play_with_shapes())
        for i in ans: print i
    except:
        quit()
