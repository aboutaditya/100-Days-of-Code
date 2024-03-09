#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        for i in range(r):
            s1=''
            for j in range(n+1):
                if s[j]=="0":
                    s1=s1+"01"
                else:
                    s1=s1+"10"
            s=s1
        return s1[n]
     

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends