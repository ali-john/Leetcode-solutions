class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        max_ones = ones_count = 0
        left = 0
        for right in range(2*n):
            if nums[right % n]:
                ones_count+=1
            
            if right-left+1>total_ones:
                ones_count-=nums[left%n]
                left+=1
            
            max_ones = max(max_ones,ones_count)
        return total_ones - max_ones
            
