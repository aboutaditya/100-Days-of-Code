#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        ##Your code here
        l_min,r_max=[a[0]]*n,[a[-1]]*n
        for i in range(1,n):
            l_min[i]=min(l_min[i-1],a[i])
            r_max[-i-1]=max(r_max[-i],a[-i-1])
        l,r,ans=0,0,0
        while l<n and r<n:
            if l_min[l]<=r_max[r]:
                ans=max(ans,r-l)
                r+=1
            else:
                l+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends