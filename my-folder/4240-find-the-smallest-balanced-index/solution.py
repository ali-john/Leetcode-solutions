class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)

        lsum = sum(nums)
        rprod = 1

        for i in reversed(range(n)):
            lsum-=nums[i]
            if lsum == rprod:
                return i
            if lsum < rprod:
                break
            
            rprod = rprod * nums[i]
        return -1
            

