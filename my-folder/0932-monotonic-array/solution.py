class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n= len(nums)
        if n==1:
            return True
        
        increasing = True
        decreasing = True

        for i in range(1,n):
            if nums[i-1]>nums[i]:
                increasing = False
                break


        for i in range(1,n):
            if nums[i-1]<nums[i]:
                decreasing = False
                break
        
        if increasing or decreasing:
            return True
        else:
            return False

