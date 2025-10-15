class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if all(num == 0 for num in nums):
            return 0
        
        xor = nums[0]
        for i in range(1,n):
            xor^= nums[i]

        if xor != 0:
            return n
        else:
            return n -1 
        
