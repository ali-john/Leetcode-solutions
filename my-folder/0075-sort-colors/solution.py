class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)-1
        i=0
        while i<=r:
            if nums[i]==0:
                temp = nums[l]
                nums[l] = 0
                nums[i] = temp
                l+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                temp = nums[r]
                nums[i] = temp
                nums[r] = 2
                r-=1
        

        
