class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        output = nums[0]
        for i in range(1,len(nums)):
            output^=nums[i]
        return output


        
