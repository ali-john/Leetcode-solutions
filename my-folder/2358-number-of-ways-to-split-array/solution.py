class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        #print(prefix)
        ans = 0
        for i in range(n - 1):
            s1 = prefix[i]
            s2 = prefix[-1] - prefix[i]
            if s1>=s2: ans+=1
        return ans
