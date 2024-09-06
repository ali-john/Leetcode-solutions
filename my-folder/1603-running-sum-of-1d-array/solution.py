class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        prev = 0 
        for i in range(n):
            prev+=nums[i]
            prefix[i] = prev
        return prefix
