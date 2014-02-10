class BotCheck:
    ''' Check the bot moves'''
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def testFinal(self):
        # for A
        a_pos_init = [i for i, x in enumerate(list(self.initial)) if x == 'A']
        a_pos_final = [i for i, x in enumerate(list(self.final)) if x == 'A']
        # for B
        b_pos_init = [i for i, x in enumerate(list(self.initial)) if x == 'B']
        b_pos_final = [i for i, x in enumerate(list(self.final)) if x == 'B']
        #check on whether A moves left and doesn't jump B
        for i in xrange(len(a_pos_init)):
            if a_pos_init[i] >= a_pos_final[i] and \
               a_pos_final[i] not in range(b_pos_init[0],b_pos_init[-1]+1):
                flag_A = True
            else:
                flag_A = False
        #check on whether B moves right and doesn't jump A
        for i in xrange(len(b_pos_init)):
            if b_pos_init[i] <= b_pos_final[i] and \
               b_pos_final[i] not in range(a_pos_init[0],a_pos_init[-1]+1):
                flag_B = True
            else:
                flag_B = False
        # return results
        if flag_A and flag_B:
            return 'Yes'
        else:
            return 'No'

if __name__ == '__main__': 
    try:
        t = int(raw_input())
        assert 1<=t<=1000
        ans = []
        for i in xrange(t):
            # input values
            bots = raw_input().split()
            #check on bots count
            assert len(bots)==2
            #check on strings
            assert len(bots[0])==len(bots[1])
            # check on bot names A/B
            b1,b2 = set(''.join(bots[0].split('#'))), set(''.join(bots[1].split('#')))
            z = lambda x: ord(x)==65 or ord(x)==66
            assert z(b1.pop()) and z(b1.pop()) and z(b2.pop()) and z(b2.pop())
            # pass the tested attributes
            Bc = BotCheck(bots[0], bots[1])
            ans.append(Bc.testFinal())
        for i in ans: print i
    except:
        quit()
