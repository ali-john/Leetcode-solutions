class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1 if len(nums)>0 else 0
        n = len(nums)
        # increasing sequence
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]>nums[j-1]:
                    ans = max(ans,j-i+1)
                else: break
        
        # decreasing sequence
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]<nums[j-1]:
                    ans = max(ans,j-i+1)
                else: break
        return ans
