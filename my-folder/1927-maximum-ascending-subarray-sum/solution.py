class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        if n==1: return nums[0]
        
        curr = nums[0]
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                curr+=nums[i]
                ans = max(ans,curr)
            else:
                ans = max(ans,curr)
                curr = 0
                curr+=nums[i]
        return ans


