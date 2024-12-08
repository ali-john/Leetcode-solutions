class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i,num in enumerate(nums):
            if nums[i]>0 or nums[i]<0:
                idx = (i+nums[i])%n
                value = nums[idx]
                res[i] = value
            else:
                res[i] = num
        return res
            
            
