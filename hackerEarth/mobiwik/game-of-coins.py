class GameOfCoins:
    '''Find the prized door'''
    def __init__(self, N):
        self.coins = '1'*N #a long string of 1's

    def move1(self): #in string form with 1's and 0's
        # CASE 1: To modify odd lengthed str
        if filter(lambda x: len(x)%2!=0, self.coins): #odd length elem found
            for i,e in enumerate(self.coins):
                temp = list(e) #convert single string to list of strings
                # first modify odd lengths with >3 characters
                if len(e)%2!=0:
                    if len(e)>=3: #if odd and len(e) is not 1
                        temp[(len(e)+1)/2-1] = '0' #remove the coin; 1 -> 0
                        self.coins[i]=''.join(temp) #modify original list of str
                        return self.coins #return; so that move is made only once
                    else:
                        ###################
                        # edit here #######
                        ###################
                else:
                    pass
        #CASE 2: To modify 1st even length str found
        else:
            ###################
            # edit here #######
            ###################
            
    def move2(m):
        ###################
        # edit here #######
        ###################
            
    def find_winner(self):
        self.coins = self.coins.split('0') #convert str to list of str

if __name__ == '__main__': 
    try:
        T = int(raw_input())
        assert 1<=T<=100
        ans = []
        for i in xrange(T):
            # input values
            N = int(raw_input())
            #check on input
            assert 1<=N<=10**9
            # intiate class object
            GC = GameOfCoins(N)
            # append result to an answers list, to be printed later
            ans.append(CH.find_winner())
        for i in ans: print i
    except:
        raise
