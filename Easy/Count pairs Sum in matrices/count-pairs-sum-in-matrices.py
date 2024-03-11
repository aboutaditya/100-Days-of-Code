#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
		m1={}
		m2={}
		for i in mat1:
		    for j in i:
		        if j not in m1:
		            m1[j]=1
		        else:
		            m1[j]+=1
		for i in mat2:
		    for j in i:
		        if j not in m2:
		            m2[j]=1
		        else:
		            m2[j]+=1
		c=0
		for i in m1.keys():
		    if (x-i) in m2.keys():
		        c+=1
		return c
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends