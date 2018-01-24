class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		n = len(A)
		c = []
		for i in range(n):
			c.append([0])
		for i in range(n-1,-1,-1):
			if A[i]==-1: continue
			c[A[i]][len(c[A[i]])-1] = 1 + max(c[i])
			c[A[i]].append(0)
		print(c)
		count = 0
		for i in range(n):
			if(len(c[i])==1):
				if c[i][0]>count:count=c[i][0]
			else:
				c[i].sort()
				temp = c[i][len(c[i])-1] + c[i][len(c[i])-2]
				if temp>count: count = temp
		return count


if __name__ == '__main__':
	max_depth = 0
	A = [-1,0,0,0,3]
	S = Solution()
	print(S.solve(A))
