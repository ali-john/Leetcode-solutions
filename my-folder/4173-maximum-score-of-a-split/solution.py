class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return nums[0] - nums[1]
        
        pre = [0]*n
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        
        suff = [0]*n
        suff[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suff[i] = min( suff[i+1],  nums[i] )
        
        ans = float('-inf')
        for i in range(n-1):
            ans = max(ans, pre[i] - suff[i+1])
        return ans
