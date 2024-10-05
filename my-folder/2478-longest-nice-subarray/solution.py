class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 0
        max_len = 0
        curr_sum = 0
        for right in range(n):
            while curr_sum & nums[right]!=0:
                curr_sum^=nums[left]
                left+=1
            
            curr_sum|=nums[right]
            max_len = max(max_len,(right-left+1))
        return max_len





