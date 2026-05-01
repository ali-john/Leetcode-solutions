class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                ans+= (max(0, nums[i - 1] - nums[i]))
        return ans
    
        



            




