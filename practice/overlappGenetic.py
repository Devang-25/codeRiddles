def LongestCommonSubstring(S1, S2):
    M = [[0]*(1+len(S2)) for i in xrange(1+len(S1))]
    longest, x_longest = 0, 0
    for x in xrange(1,1+len(S1)):
        for y in xrange(1,1+len(S2)):
            if S1[x-1] == S2[y-1]:
                M[x][y] = M[x-1][y-1] + 1
                if M[x][y]>longest:
                    longest = M[x][y]
                    x_longest  = x
            else:
                M[x][y] = 0
    return S1[x_longest-longest: x_longest]

s1="S1 = CGATTCCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTC"
s2="S2 = GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGC"
print "\n",s1,"\n",s2
print "\n\n",LongestCommonSubstring(s1,s2)
 
s3 = "S3 = ArchitSharmaisaGoodBoy"
s4 = "S4 = I know that ArchitSharmaisaGoodSon"
raw_input()
print "\n\n",LongestCommonSubstring(s3,s4)
print "\n",s3,"\n",s4

s5 = raw_input("\nEnter sentence 5 for substring matching:")
s6 = raw_input("\nEnter sentence 6 for substring matching:")
print "\n\n",LongestCommonSubstring(s5,s6)
