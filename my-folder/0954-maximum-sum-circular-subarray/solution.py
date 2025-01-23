class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        globMax = nums[0]
        globMin = nums[0]
        currMax= 0
        currMin = 0

        total = sum(nums)
        for i in range(n):
            currMax = max(nums[i],currMax+nums[i])
            currMin = min(nums[i],currMin+nums[i])
            globMax = max(globMax,currMax)
            globMin = min(globMin,currMin)

        return max(globMax, total - globMin) if globMax>0 else globMax
       
