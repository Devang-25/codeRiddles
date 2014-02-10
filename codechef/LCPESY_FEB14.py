if __name__ == '__main__': 
    try:
        t = int(raw_input())
        assert 1<=t<=100        
        ans = []
        for i in xrange(t):
            A, B = raw_input(), raw_input()
            #check on A,B
            assert 1<=len(A)<=10000 and 1<=len(B)<=10000
            valid_ord = range(48,58) + range(65,91) + range(97,123)
            z = lambda x: x.replace(x,str(ord(x)))
            A_ord, B_ord = map(int, map(z,A)), map(int, map(z,B))
            for element in A_ord:
                assert element in valid_ord
            for element in B_ord:
                assert element in valid_ord
                            
            A, B = list(A), list(B)
            c = 0
            for i in A:
                if i in B:
                    B.remove(i)
                    c+=1
            ans.append(c)
        for i in ans: print i
    except:
        quit()
