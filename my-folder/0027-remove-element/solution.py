class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        nextPtr = 0
        prevPtr = 0

        while nextPtr < len(nums):
            if nums[nextPtr]!=val:
                nums[prevPtr] = nums[nextPtr]
                prevPtr+=1
            nextPtr+=1
        return prevPtr


        
