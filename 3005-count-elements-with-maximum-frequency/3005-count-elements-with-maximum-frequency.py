class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m={}
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        return max(m.values())*(list(m.values()).count(max(m.values())))