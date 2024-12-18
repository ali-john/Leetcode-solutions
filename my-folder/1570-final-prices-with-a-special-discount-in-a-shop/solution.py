class Solution:
    def finalPrices(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[j]<=nums[i]:
                    nums[i] = nums[i] - nums[j]
                    break
        return nums
            
