class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)
        sum_ = sum(nums)
        curr = nums[0]
        max_element = -1
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                max_element = nums[i-1]
                break
            else:
                curr+=nums[i]
        other = sum_ - curr + max_element
        
        if curr > other:
            return 0
        elif other > curr:
            return 1
        else:
            return -1
        
